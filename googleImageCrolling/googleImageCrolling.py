import shutil

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys
import os
import time
import socket
import pandas as pd
import threading
import re

from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError
from selenium.common.exceptions import ElementClickInterceptedException,NoSuchElementException,ElementNotInteractableException
from PIL import Image

from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬 드라이버 경로 설정
sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 크롬 드라이버 생성
driver = webdriver.Chrome(options=chrome_options)
getExcel = pd.read_excel('./tourist_spot.xlsx')
search_words =getExcel['name']

# 전역 변수 초기화
scraped_count = 0
filtered_count = 0
downloaded_srcs = set()
empty=[]

# Lock 객체 생성
lock = threading.Lock()

def reset_counters():
    """카운터 초기화 함수"""
    global scraped_count, filtered_count, downloaded_srcs
    with lock:
        scraped_count = 0
        filtered_count = 0
        downloaded_srcs = set()

# 이미지 다운로드를 위한 병렬 처리 함수
def parallel_download(src, dir_name):
    download_image(src, dir_name, scraped_count)

def download_image(src, dir_name, count):
    """이미지를 다운로드하고 카운트를 증가시킵니다."""
    global scraped_count
    start_time = time.time()
    with lock:
        try:
            _format = src.split('.')[-1]
            # if _format not in ['jpg', 'jpeg', 'png']:
            #     print('Unsupported format, skipping...'+ _format)
            #     return

            file_path = os.path.join(dir_name, f"{scraped_count + 1}.jpg")
            urlretrieve(src, file_path)
            print(f"Image saved: {file_path}")
            downloaded_srcs.add(src)
            scraped_count += 1
        except Exception as e:
            print(f"Error downloading {src}: {e}")
            return
        finally:
            end_time = time.time()  # 종료 시간 기록
            print(f"download_image 실행 시간: {end_time - start_time:.2f}초")

def click_and_save(dir_name, index, img, img_list_length):
    """이미지를 클릭하고 저장합니다."""
    start_time = time.time()
    try:
        img.click()
        time.sleep(1.5)

        img_element = driver.find_elements(By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div/div[2]/c-wiz/div/div[3]/div[1]/a/img')
        if img_element:
            src = img_element[0].get_attribute('src')
            if src and src not in downloaded_srcs:
                download_image(src, dir_name, scraped_count)
    except Exception as e:
        print(f"Error clicking image at index {index}: {e}")
        return
    finally:
        end_time = time.time()  # 종료 시간 기록
        print(f"click_and_save 실행 시간: {end_time - start_time:.2f}초")

def scraping(dir_name, query):
    """이미지를 스크래핑합니다."""
    global scraped_count
    reset_counters()
    start_time = time.time()

    url = f"https://www.google.com/search?q={query}&client=safari&sca_esv=f126b848cbaf5375&rls=en&udm=2&biw=1128&bih=984&sxsrf=ADLYWIIBh-fa_ZcaPLHHyguuAwP1gqYmXw%3A1731305411541&ei=w58xZ5fgIPPg1e8P5_2u2AI&ved=0ahUKEwjXzbWgz9OJAxVzcPUHHee-CysQ4dUDCBA&uact=5&oq=sea&gs_lp=EgNpbWciA3NlYTIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQMyBRAAGIAEMgUQABiABDIFEAAYgARIhQdQngNY_wVwAngAkAEAmAF6oAHSAqoBAzAuM7gBA8gBAPgBAZgCBaAC4gKoAgrCAgcQIxgnGOoCwgIEECMYJ8ICBxAAGIAEGArCAgsQABiABBixAxiDAcICBBAAGAOYAwaSBwMyLjOgB8kT&sclient=img"
    driver.get(url)
    driver.maximize_window()

    div = driver.find_element(By.XPATH, '//*[@id="rso"]/div/div/div[1]/div/div')
    img_list = div.find_elements(By.CSS_SELECTOR, ".YQ4gaf")
    end_time = time.time()
    print(f"get Url 실행 시간: {end_time - start_time:.2f}초]")

    roop_start_time = time.time()

    with ThreadPoolExecutor(max_workers=5) as executor:
        for index, img in enumerate(img_list):
            start_time = time.time()
            total_count = scraped_count - filtered_count
            if total_count >= 10:  # 10장 이상 다운로드하지 않도록 설정
                break
                # filter_and_remove(dir_name, search_word, 400, 30)
                # total_count = scraped_count - filtered_count
                # if total_count >= 10:  # 10장 이상 다운로드하지 않도록 설정
                #     break
            try:
                # click_and_save(dir_name, index, img, len(img_list))
                img.click()
                time.sleep(1.5)
                img_element = driver.find_elements(By.XPATH,'//*[@id="Sva75c"]/div[2]/div[2]/div/div[2]/c-wiz/div/div[3]/div[1]/a/img')
                if img_element:
                    src = img_element[0].get_attribute('src')
                    if src and src not in downloaded_srcs:
                        executor.submit(parallel_download, src, dir_name)
                        # download_image(src, dir_name, scraped_count)
            except (ElementClickInterceptedException, NoSuchElementException) as e:
                print(e)
                driver.execute_script("window.scrollTo(0, window.scrollY + 100)")
                time.sleep(1)
                click_and_save(dir_name, index, img, len(img_list))
            except (URLError, socket.timeout, socket.gaierror) as e:
                print(f"Network error: {e}")
                continue
            except ConnectionResetError as e:
                print(e)
                pass
            except ElementNotInteractableException as e:
                print(e)
                break
            except Exception as e:
                print(e)
                break
            finally:
                end_time = time.time()
                print(f"한 루프 실행 시간: {end_time - start_time:.2f}초]")
    roop_end_time = time.time()


    # 검색 결과가 없을 경우 empty 리스트에 추가
    if scraped_count == 0:
        empty.append(query)

    success_rate = (scraped_count / len(img_list) * 100.0) if img_list else 0
    # print(f"[스크래핑 종료 (성공률: {success_rate:.2f} %)]")
    print(f"[스크래핑 종료 (성공률: {success_rate:.2f} %), 실행 시간: {roop_end_time - roop_start_time:.2f}초]")

def filter_and_remove(dir_name, query, filter_size, min_file_size_kb):
    """조건에 맞지 않는 이미지를 필터링하고 제거합니다."""
    global filtered_count
    with lock:

        for index, file_name in enumerate(os.listdir(dir_name)):
            file_path = os.path.join(dir_name, file_name)
            try:
                img = Image.open(file_path)
                if (img.width < filter_size and img.height < filter_size) or os.path.getsize(file_path) < min_file_size_kb * 1024:
                    img.close()
                    os.remove(file_path)
                    print(f"{index} 이미지 제거")
                    filtered_count += 1
                else:
                    img.close()  # 조건을 만족하는 이미지는 닫기만 함
            except OSError as e:
                print(f"Error with file {file_name}: {e}")
                if os.path.exists(file_path):
                    os.remove(file_path)
                    filtered_count += 1

        print(f"[이미지 제거 개수: {filtered_count}/{scraped_count}]")
# 소켓 타임아웃 설정
socket.setdefaulttimeout(30)


for index, search_word in enumerate(search_words):
    start_time = time.time()
    print(f"{index} {search_word}")

    path = "../googleImageCrolling/images/"
    dir_name = os.path.join(path, search_word)

    if os.path.isdir(dir_name):
        # 디렉토리 내 이미지 개수 확인
        existing_images = len([name for name in os.listdir(dir_name) if name.endswith(('.jpg', '.jpeg', '.png'))])

        # 이미지가 10장 이상이면 스크래핑 건너뛰기
        if existing_images >= 10:
            print(f"{search_word}에 대한 이미지는 이미 {existing_images}장 존재하므로 스크래핑을 건너뜁니다.")
            continue
        else:
            shutil.rmtree(dir_name)

    os.mkdir(dir_name)
    # query = re.sub(r'\s*\(.*?\)', '', search_word)

    scraping(dir_name, search_word)
    end_time = time.time()
    print(f"**한 spot 당 실행 시간: {end_time - start_time:.2f}초")
    print(f"[스팟 : {index + 1}/{len(search_words)}]")  # 인덱스는 0부터 시작하므로 +1을 합니다.

# 파일 경로를 지정하여 파일 열기
file_path = "empty.txt"
# 파일 쓰기 모드로 열기
with open(file_path, "w") as file:
    for emptySpot in empty:
        file.write(emptySpot+'\n')

driver.quit()