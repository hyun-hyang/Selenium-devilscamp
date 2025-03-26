# sixpc_reservation.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from datetime import datetime
import pyautogui
import time
import warnings
from dotenv import load_dotenv
import os


def main():
    warnings.filterwarnings("ignore")

    # 사용자 정보


    load_dotenv()  # .env 파일 읽기

    userId = os.getenv("USER_ID")
    userPw = os.getenv("USER_PW")

    now = datetime.now()
    weekday = now.weekday()

    # 요일별 예약 시간 설정
    if weekday == 0:  # 월요일
        start_time = "15"
        end_time = "17"
    elif weekday == 2:  # 수요일
        start_time = "12"
        end_time = "14"
    else:
        print("예약 대상 요일이 아님. 종료.")
        return

    # 브라우저 설정 및 실행
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.get(
        "https://mportal.cau.ac.kr/common/auth/SSOlogin.do?redirectUrl=http://cse.cau.ac.kr/sub09/sub0901_pro.php")
    time.sleep(3)

    # 로그인
    driver.find_element(By.ID, 'txtUserID').send_keys(userId)
    driver.find_element(By.ID, 'txtPwd').send_keys(userPw)
    driver.find_element(By.ID, 'txtPwd').send_keys(Keys.ENTER)
    time.sleep(3)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass  # 팝업이 없으면 무시
    time.sleep(5)

    # 강의실 선택
    Select(driver.find_element(By.ID, "classRoomNo")).select_by_index(2)

    # 시간 선택
    Select(driver.find_element(By.ID, "reserveStartTimeH")).select_by_value(start_time)
    Select(driver.find_element(By.ID, "reserveEndTimeH")).select_by_value(end_time)

    # 인원, 메모 입력
    Select(driver.find_element(By.ID, "reserveMember")).select_by_value("3")
    driver.find_element(By.ID, "memo").send_keys("스터디")

    # 예약 버튼 클릭
    driver.find_element(By.XPATH, "//button[text()='예약하기']").click()
    time.sleep(3)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass  # 팝업이 없으면 무시
    time.sleep(2)

    print("예약 완료!")
    driver.quit()