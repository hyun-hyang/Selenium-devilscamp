from selenium.webdriver.common.by import By
import sys
import time
import warnings
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.common.alert import Alert

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-type: text/html;charset=utf-8\r\n")

# 기본 사용자 세팅 (모두 입력하세요)
userId = ""  # 에브리타임 아이디 입력
userPw = ""  # 에브리타임 비밀번호 입력

cousrenum = "102591"
boardurl = "/modules/items/"
boardnum = "3184197"
courseurl = "?return_url=/courses/102591/external_tools/211"

# =========================================== #

# 메인 코드

warnings.filterwarnings("ignore")
now = datetime.now()
url = "https://eclass3.cau.ac.kr/courses/" + str(cousrenum) + str(boardurl) + str(boardnum) + str(courseurl)

options = webdriver.FirefoxOptions()

# options.add_argument("-headless")
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

count = 1
driver = webdriver.Firefox(options=options)

driver.get("https://eclass3.cau.ac.kr/courses/102591/modules/items/3184198?return_url=/courses/102591/external_tools/211")


# 로그인
driver.find_element(By.NAME, 'userID').send_keys(userId)
driver.find_element(By.NAME, 'password').send_keys(userPw)
driver.find_element(By.NAME, 'password').send_keys(Keys.ENTER) # RETURN

time.sleep(1)

# driver.get("https://account.everytime.kr/login")
#
#
# #글작성 페이지 로드
# driver.get(url)
# time.sleep(3)
#
# #글작성 구간
# driver.find_element(By.LINK_TEXT, "새 글을 작성해주세요!").click()
# driver.find_element(By.CSS_SELECTOR, "input.title").send_keys('🔥 중앙대학교 중앙힙합동아리 Da C Side 25기 모집 🔥')
# driver.find_element(By.CSS_SELECTOR, "textarea.smallplaceholder")
#
# # driver.find_element(By.CSS_SELECTOR, "li.anonym").click()
# driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(r"C:\Users\RTSE16\repo\everytime-macro\dacside poster-김세윤번호.png")
# time.sleep(3)
#
# driver.find_element(By.CSS_SELECTOR, "li.submit").click()
# time.sleep(3)
# print("새내기 complete")

