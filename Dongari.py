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

# =========================================== #

# 메인 코드

warnings.filterwarnings("ignore")
now = datetime.now()
url = "https://everytime.kr/" + str(targetBoard)


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

text = '''안녕하세요❗ 저희는 중앙대학교 유일무이 중앙 흑인음악동아리 Da C Side 입니다‼️

Official Linktree : https://linktr.ee/dacside
Official Youtube : https://www.youtube.com/@dacside1524
Official Instagram : https://www.instagram.com/da_c_side/

🙋🏻 Hip Hop과 R&B에 관심이 있거나 배우고 싶은 사람 🙋🏻
🕺🏻 공연을 하고 싶은 사람 🕺🏻
🙋🏻‍♂️ 뮤직비디오나 디자인에 관심있는 사람 🙋🏻‍♂️

😈 Da C Side에서 6가지 분야의 신입부원을 모집합니다 😈

흑인음악부
🔥 Rap 🔥
💫 R&B 💫
🎹 Beat Maker 🎹
🎧 Producer 🎧

아트디렉터부
📽 Video [공연 영상 촬영 및 제작 & M/V] 📽
🎬 Design [공연 포스터 제작 & 앨범 커버 제작] 🎬

신청은 아래 구글 폼 양식에 맞게 작성해주시면 됩니다!
 -> https://forms.gle/FEmKL82NHtA5euDE6
혹은 동방에 오셔서 직접 신청하셔도 됩니다!

2023년 5월 정기공연 영상-> https://www.youtube.com/watch?v=tYwBG7pDv7g&list=PLzm8rVeHR8s7ZGVo8ro_I-_495y_3zH4P
2023년 9월 정기공연 영상-> https://www.youtube.com/watch?v=8WJ79WMtlis&list=PLzm8rVeHR8s5y9bng3kJ_5tko3eqlsJx6
2023년 11월 정기공연 영상-> https://www.youtube.com/watch?v=2-ijSzMbqX4&list=PLzm8rVeHR8s7ffuFQNM7Jn6BE9dRLMarW
2020년 중앙대X성균관대 디스전 영상 -> https://www.youtube.com/watch?v=-sYK-ubgxG8

🤔Q&A🤔
Q. 제가 신청한 분야에 대해 전문지식이 부족한데 입부 가능할까요?
👍물론입니다! 실력과 무관하게 열정이 있는 모든 분들을 환영합니다!

Q. 동아리 1년 정기계획이 어떻게 되나요? 주로 어떤 활동을 진행하나요?
🙃크게는 1년에 4번의 정기공연을 진행하고 각 공연마다 약 4-5주 연습을 진행합니다. 정해진 시간은 공연 연습 시간만 저녁 6-10시로 정해져있고 나머지 활동들은 자유롭게 하는 편입니다. 공연 이외에는 서로 자유롭게 곡을 만들고 피드백을 주고 받고 있습니다.

Q. 카톡방 초대는 언제 되나요?
🤗2월 둘째주를 기준으로 매주 금요일마다 일괄적으로 카톡방에 초대해드리고 있습니다.

Q. 상시모집인가요?
👌네 맞습니다. 현재 1학기, 2학기 두차례를 기준으로 홍보활동을 진행하고 있지만, 가입은 상시모집으로 진행되고 있습니다.


문의 사항은 아래 번호로 연락 주시면 감사하겠습니다!
동방 위치 : 중앙대학교 서울캠퍼스 학생회관 6층(107관 603호)
회장 : 박효석
문의 : 기획부장 김세윤 (010-6455-2988)

동방 문은 열려 있습니다! 부담 없이 찾아주세요 !
🤗 25기로 들어오실 여러분 모두 환영합니다 🤗
'''

#글작성 페이지 로드
driver.get(url)
time.sleep(3)

#글작성 구간
driver.find_element(By.LINK_TEXT, "새 글을 작성해주세요!").click()
driver.find_element(By.CSS_SELECTOR, "input.title").send_keys('🔥 중앙대학교 중앙힙합동아리 Da C Side 25기 모집 🔥')

driver.find_element(By.CSS_SELECTOR, "textarea.smallplaceholder").send_keys(text)

# driver.find_element(By.CSS_SELECTOR, "li.anonym").click()
driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(r"C:\Users\RTSE16\repo\everytime-macro\dacside poster-김세윤번호.png")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "li.submit").click()

# 팝업창 '확인' 클릭
da = Alert(driver)
da.accept()
print("동아리 complete")
time.sleep(3)

