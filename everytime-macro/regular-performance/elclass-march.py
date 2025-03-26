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
targetBoard = "418754"  # 동아리·학회 # 대상 게시판 번호 (에브리타임 URL에서 얻을 수 있음)
targetNewStudnetBoard = "375122" # 새내기
targetHongboBoard = "375118" # 홍보

# =========================================== #

# 메인 코드

warnings.filterwarnings("ignore")
now = datetime.now()
url = "https://everytime.kr/" + str(targetBoard)
NewStudenturl = "https://everytime.kr/" + str(targetNewStudnetBoard)
Hongbourl = "https://everytime.kr/" + str(targetHongboBoard)


options = webdriver.FirefoxOptions()

options.add_argument("-headless")
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

count = 1
driver = webdriver.Firefox(options=options)

driver.get("https://account.everytime.kr/login")

# 로그인
driver.find_element(By.NAME, 'id').send_keys(userId)
driver.find_element(By.NAME, 'password').send_keys(userPw)
driver.find_element(By.NAME, 'password').send_keys(Keys.ENTER) # RETURN

time.sleep(1)

text = '''안녕하세요! 중앙대학교 유일무이 중앙 흑인음악동아리 𝐃𝐚 𝐂 𝐒𝐢𝐝𝐞 에서 2024년 3월 정기공연을 진행합니다!

☑️공연 일시: 04.04 (목) 19:30 - 21:00
☑️공연 장소: 극장 PLOT [서울특별시 서대분구 연세로4길 27 지하 1층]
 (2호선 신촌역 3번 출구에서 300m 도보로 4분 소요)

☑️공연 시간: 약 90분
☑️선예매 링크:https://forms.gle/T5xJB4tacgKcCmim9
 💲현장 결제 또는 선입금 가능합니다💲


⬇️ 𝐃𝐚 𝐂 𝐒𝐢𝐝𝐞가 더 궁금하다면? ⬇️ 
𝐿𝑖𝑛𝑘𝑡𝑟𝑒𝑒 : https://linktr.ee/dacside
𝑌𝑜𝑢𝑡𝑢𝑏𝑒 :  https://www.youtube.com/@dacside
𝐼𝑛𝑠𝑡𝑎𝑔𝑟𝑎𝑚 : https://www.instagram.com/da_c_side/

☑️문의:
24기 기획부장: 010-6455-2988 (김세윤)
24기 연락부장: 010-4092-9234 (이현재)
'''

#글작성 페이지 로드
driver.get(NewStudenturl)
time.sleep(3)

#글작성 구간
driver.find_element(By.LINK_TEXT, "새 글을 작성해주세요!").click()
driver.find_element(By.CSS_SELECTOR, "input.title").send_keys('💀중앙힙합동아리 𝐃𝐚𝐂𝐒𝐢𝐝𝐞 3월 정기공연💀')
driver.find_element(By.CSS_SELECTOR, "textarea.smallplaceholder").send_keys(text)

# driver.find_element(By.CSS_SELECTOR, "li.anonym").click()
driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(r"C:\Users\RTSE16\repo\everytime-macro\march-poster.png")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "li.submit").click()
time.sleep(3)
print("새내기 complete")

