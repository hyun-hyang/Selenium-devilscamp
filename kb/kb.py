from selenium import webdriver
from selenium.webdriver.ie import service
import time
import pyautogui
from datetime import datetime, timedelta

ie_options = webdriver.IeOptions()
ie_options.ignore_protected_momde_settings = True

s=service.Service('../tools/IEDriverServer/IEDriverServer.exe')
driver = webdriver.Ie(service=s, options = ie_options)

driver.get(url='http://partner.kbinsure.co.kr')
driver.maximize_window()

time.sleep(20)

# PASSWORD 입력 위치로 이동 후 입력
password_field_location = pyautogui.locateOnScreen('password_field.png', confidence=0.9)  # PASSWORD 필드 이미지
if password_field_location:
    pyautogui.click(password_field_location)
    pyautogui.typewrite()  # ID 입력
    time.sleep(1)

# 로그인 버튼 클릭
login_button_location = pyautogui.locateOnScreen('login_button.png', confidence=0.8)  # 로그인 버튼 이미지
if login_button_location:
    pyautogui.click(login_button_location)
    time.sleep(3)

# 올바른 인증서 클릭
cert_button_location = pyautogui.locateOnScreen('cert.png', confidence=0.8)  # 로그인 버튼 이미지
if cert_button_location:
    pyautogui.click(cert_button_location)
    time.sleep(1)

# 인증서 비밀번호 입력
cert_password_location = pyautogui.locateOnScreen('cert_password.png', confidence=0.8)  # 로그인 버튼 이미지
if cert_password_location:
    pyautogui.click(cert_password_location)
    pyautogui.typewrite()  # ID 입력
    time.sleep(1)

# 인증서 창 확인 클릭
cert_ok_location = pyautogui.locateOnScreen('cert_ok.png', confidence=0.8)  # 로그인 버튼 이미지
if cert_ok_location:
    pyautogui.click(cert_ok_location)
    time.sleep(1)

# 인증서 창 확인 클릭
cert_finish_ok_location = pyautogui.locateOnScreen('cert_finish_ok.png', confidence=0.8)  # 로그인 버튼 이미지
if cert_finish_ok_location:
    pyautogui.click(cert_finish_ok_location)
    time.sleep(50)

tomorrow = datetime.now() + timedelta(days=1)
formatted_tomorrow = tomorrow.strftime("%Y%m%d")

# 기간 설정
period_forward_location = pyautogui.locateOnScreen('period_forward.png', confidence=0.8)  # 로그인 버튼 이미지
if period_forward_location:
    pyautogui.click(period_forward_location)
    pyautogui.typewrite(formatted_tomorrow)  # ID 입력
    time.sleep(1)
    pyautogui.typewrite(formatted_tomorrow)  # ID 입력
    time.sleep(1)

# 조회 버튼 클릭
search_button_location = pyautogui.locateOnScreen('search_button.png', confidence=0.8)  # 로그인 버튼 이미지
if search_button_location:
    pyautogui.click(search_button_location)
    time.sleep(1)

# 화면을 아래로 스크롤 (100픽셀만큼)
pyautogui.scroll(-100)