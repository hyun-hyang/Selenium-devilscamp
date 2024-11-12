from re import I
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
from selenium.webdriver.common.by import By
import pandas as pd
import re
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# headless 설정
chrome_options.headless = True
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # 사용자 에이전트 추가

getExcel = pd.read_excel('C:/Users/msj/Desktop/googleImageCrawling/tourist_spot.xlsx')
empty=[]

search_words =getExcel['name'][580:]
driver = webdriver.Chrome(options=chrome_options)  #chromedriver.exe -> 가져 옴
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
# assert "Python" in driver.title
cccc=0
current_path = os.getcwd() # 저장 경로
for search_word in search_words:
    time.sleep(1)
    print(cccc,search_word)
    cccc=cccc+1
    elem = driver.find_element('name',"q")  # 검색탕의 검색엔진을 찾는 코드
    elem.clear()
    elem.send_keys(search_word)  # 해당 검색엔진에 글자를 입력
    elem.send_keys(Keys.RETURN)

    try:
        wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".YQ4gaf:not([class*=' '])")))
    except:
        print(f"Timeout or no images found for: {search_word}")
        empty.append(search_word)
        continue
    images = driver.find_elements(By.CSS_SELECTOR, ".YQ4gaf:not([class*=' '])")[0:10]
    if len(images)==0:
        empty.append(search_word)
        break
    folder_name = re.sub(r'[<>:"/\\|?*]', '_', search_word) 
    #해당 이미지 이름과 동일한 폴더 생성
    try:
        if not os.path.isdir(folder_name):  # 없으면 새로 생성하는 조건문
            os.mkdir(folder_name)
    except:
        empty.append(search_word)
        break
    count=0
    for image in images:
        try:         
            imgUrl = image.get_attribute('src')
            # driver.find_element(By.XPATH,
            #     "/html/body/div[3]/div/div[15]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[9]/div[2]/h3/a/div/div/div/g-img/img").get_attribute("src")
            urllib.request.urlretrieve(
                imgUrl,
                folder_name + "/" + search_word + "." + str(count) + ".jpg")
            count=count+1
        except:
            pass
    driver.back()
# 파일 경로를 지정하여 파일 열기
file_path = "empty.txt"
# 파일 쓰기 모드로 열기
with open(file_path, "w") as file:
    for emptypot in empty:
        file.write(asd+'\n')

driver.close()