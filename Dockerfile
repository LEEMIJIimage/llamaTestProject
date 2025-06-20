# 1. Python 3.12 slim 이미지를 베이스로 사용 (최신 & 최소 이미지)
FROM python:3.12-slim

# 2. 작업 디렉토리를 /app으로 설정 (모든 작업은 이 디렉토리에서 수행됨)
WORKDIR /app

# 3. requirements.txt만 먼저 복사해서 의존성 설치 캐시를 최대화
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 나머지 모든 파일 복사 (Dockerfile이 있는 위치 기준)
COPY . .

# 5. 모델은 마운트할 예정이므로 CMD에는 포함하지 않음
# 앱 실행: 컨테이너 시작 시 python app.py 실행
CMD ["python", "app.py"]