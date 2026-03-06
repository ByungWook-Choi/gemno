import sys
import os
import site

# [중요] 경로 주입이 모든 import보다 먼저 와야 합니다!
user_site = site.getusersitepackages()
if user_site not in sys.path:
    sys.path.insert(0, user_site)

# 이제 라이브러리를 불러옵니다.
try:
    from dotenv import load_dotenv
    from google import genai
    import json
except ImportError as e:
    print(f"❌ 라이브러리 로드 실패: {e}")
    print("💡 해결책: 터미널에 'pip install --user python-dotenv google-genai --break-system-packages'를 입력하세요.")
    sys.exit()

# .env 로드 및 설정 시작
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

# ... 나머지 기존 코드 ...