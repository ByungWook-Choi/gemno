import sys
import os
import site

# 1. 경로 주입 (가장 먼저 실행되어야 함!)
user_site = site.getusersitepackages()
if user_site not in sys.path:
    sys.path.insert(0, user_site)

# 2. 이제 안심하고 라이브러리를 불러옵니다.
try:
    import requests
    import json
    from dotenv import load_dotenv
    from google import genai
except ImportError as e:
    print(f"❌ 라이브러리 로드 실패: {e}")
    print("💡 해결책: 터미널에 아래 명령어를 입력하세요.")
    print("pip install --user google-genai requests python-dotenv --break-system-packages")
    sys.exit()

# 이후 코드(load_dotenv, API 설정 등)는 동일하게 작성...