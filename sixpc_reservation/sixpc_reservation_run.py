import schedule
import time
from datetime import datetime
import sixpc_reservation
import requests

# 디스코드 웹훅 URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1354303661274173532/VHPVR-1PGceIABwWCUfGkVDhvBG-0u8lVhfHoNCSm2nkLnBYFb41GgSaNRSM9w-P1T2v"

def write_log(message):
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_filename = f"log_{date_str}.txt"
    with open(log_filename, "a", encoding="utf-8") as f:
        now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
        f.write(now + message + "\n")

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
        sixpc_reservation.main()
        write_log("예약 스크립트 정상 완료")
        send_discord("✅ [스터디실 예약] 예약 완료되었습니다!", start_time, end_time)
        print("예약 완료")
    except Exception as e:
        error_msg = f"예약 중 오류 발생: {e}"
        write_log(error_msg)
        send_discord(f"❌ [스터디실 예약] 예약 실패!\n오류: {e}", start_time, end_time)
        print(error_msg)

# 예약 시간 설정
schedule.every().monday.at("09:02").do(reserve_study_room)
schedule.every().wednesday.at("09:02").do(reserve_study_room)

# 무한 루프
while True:
    schedule.run_pending()
    time.sleep(1)