import schedule
import time
from datetime import datetime
import sixpc_reservation
import requests

import os
from dotenv import load_dotenv

load_dotenv()

# 디스코드 웹훅 URL
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
if not DISCORD_WEBHOOK_URL:
    print("⚠️ DISCORD_WEBHOOK_URL이 .env에 설정되어 있지 않습니다.")

def write_log(message):
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_filename = f"log_{date_str}.txt"
    with open(log_filename, "a", encoding="utf-8") as f:
        now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
        f.write(now + message + "\n")

import glob
import os
from datetime import datetime, timedelta

def clean_old_logs(days=30):
    cutoff = datetime.now() - timedelta(days=days)
    for filename in glob.glob("log_*.txt"):
        date_str = filename.replace("log_", "").replace(".txt", "")
        try:
            file_date = datetime.strptime(date_str, "%Y-%m-%d")
            if file_date < cutoff:
                os.remove(filename)
                print(f"🧹 오래된 로그 삭제: {filename}")
        except:
            continue

def send_discord(message, start_time=None, end_time=None):
    today = datetime.now().strftime("%Y-%m-%d (%a)")  # 예: 2025-03-24 (Mon)

    # 시간대 정보 추가
    time_info = ""
    if start_time and end_time:
        time_info = f"🕒 예약 시간: {start_time}:00 ~ {end_time}:00\n"

    full_message = f"📅 {today}\n{time_info}{message}"

    try:
        requests.post(DISCORD_WEBHOOK_URL, json={"content": full_message})
    except Exception as e:
        print("디스코드 알림 실패:", e)

def reserve_study_room():
    print("스터디실 예약 실행 중...")
    write_log("스터디실 예약 시작")

    now = datetime.now()
    weekday = now.weekday()

    # 시간 설정
    if weekday == 0:  # 월요일
        start_time = "15"
        end_time = "17"
    elif weekday == 2:  # 수요일
        start_time = "12"
        end_time = "14"
    else:
        write_log("예약 대상 요일 아님. 실행 중단")
        return

    send_discord("📌 [스터디실 예약] 예약 시도 중...", start_time, end_time)

    try:
        clean_old_logs()
        sixpc_reservation.main()
        write_log("예약 스크립트 정상 완료")
        send_discord("✅ [스터디실 예약] 예약 완료되었습니다!", start_time, end_time)
        print("예약 완료")
    except Exception as e:
        import traceback
        tb = traceback.format_exc()
        error_msg = f"예약 중 오류 발생:\n{tb}"
        write_log(error_msg)
        send_discord(f"❌ [스터디실 예약] 예약 실패!\n```\n{tb}\n```", start_time, end_time)

if not os.path.exists("logs"):
    os.makedirs("logs")

date_str = datetime.now().strftime("%Y-%m-%d")
log_filename = f"logs/log_{date_str}.txt"

# 예약 시간 설정
schedule.every().monday.at("09:02").do(reserve_study_room)
schedule.every().wednesday.at("09:02").do(reserve_study_room)

# 무한 루프
while True:
    schedule.run_pending()
    time.sleep(1)