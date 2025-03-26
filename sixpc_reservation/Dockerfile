# 베이스 이미지
FROM python:3.10-slim

# 환경변수
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=Asia/Seoul

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    gnupg \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Geckodriver 설치
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz \
    && tar -xzf geckodriver-v0.33.0-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && rm geckodriver-v0.33.0-linux64.tar.gz

# 작업 디렉토리
WORKDIR /app

# 코드 복사
COPY . .

# logs 폴더 미리 생성
RUN mkdir -p logs

# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 스크립트 실행
CMD ["python", "scheduler.py"]