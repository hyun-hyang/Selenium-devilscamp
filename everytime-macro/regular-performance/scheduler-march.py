# step1.관련 패키지 및 모듈 import
import schedule
import time


# step2.실행할 함수 선언
def message():
    print("스케쥴 실행중...")
    try:
        exec(open("eclass-march.py", 'rt', encoding='UTF8').read())
    except:
        print("eclass error")


def hongbomessage():
    print("hongbo 실행중...")
    try:
        exec(open("hongbo-march.py", 'rt', encoding='UTF8').read())
    except:
        print("hongbo error")

def dongarimessage():
    print("dongari 실행중...")
    try:
        exec(open("Dongari-march.py", 'rt', encoding='UTF8').read())
    except:
        print("dongari error")

def jayuimessage():
    print("jayu 실행중...")
    try:
        exec(open("jayu-march.py", 'rt', encoding='UTF8').read())
    except:
        print("jayu error")


# 매주 월요일 13시 30분에 함수 실행
schedule.every().monday.at("18:00").do(message)
schedule.every().tuesday.at("18:00").do(message)
schedule.every().wednesday.at("18:00").do(message)
schedule.every().thursday.at("17:00").do(message)

schedule.every().monday.at("18:00").do(hongbomessage)
schedule.every().tuesday.at("18:00").do(hongbomessage)
schedule.every().wednesday.at("18:00").do(hongbomessage)
schedule.every().thursday.at("17:00").do(hongbomessage)

schedule.every().monday.at("18:00").do(dongarimessage)
schedule.every().tuesday.at("18:00").do(dongarimessage)
schedule.every().wednesday.at("18:00").do(dongarimessage)
schedule.every().thursday.at("17:00").do(dongarimessage)

schedule.every().monday.at("18:00").do(jayuimessage)
schedule.every().tuesday.at("18:00").do(jayuimessage)
schedule.every().wednesday.at("18:00").do(jayuimessage)
schedule.every().thursday.at("17:00").do(jayuimessage)


#schedule.every().monday.at("18:00").do(message)
#schedule.every().tuesday.at("18:00").do(message)
#schedule.every().wednesday.at("18:00").do(message)
#schedule.every().thursday.at("18:00").do(message)
# schedule.every().friday.at("18:00").do(message)
# schedule.every().sunday.at("18:00").do(message)

#schedule.every().tuesday.at("18:00").do(hongbomessage)
#schedule.every().friday.at("18:00").do(hongbomessage)

#schedule.every().wednesday.at("18:00").do(dongarimessage)
#schedule.every().saturday.at("18:00").do(dongarimessage)

# step4.스캐쥴 시작
while True:
    schedule.run_pending()
    time.sleep(1)
