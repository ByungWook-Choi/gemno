import sys
import os
import site
import json
from dotenv import load_dotenv

# 1. 환경 설정 (라이브러리 경로 인식)
user_site = site.getusersitepackages()
sys.path.insert(0, user_site)

# 2. .env 파일 로드
load_dotenv()

try:
    from google import genai
except ImportError:
    print("❌ 라이브러리 부족: 'pip install --user google-genai python-dotenv --break-system-packages'")
    sys.exit()

# 3. 환경 변수에서 키 가져오기
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

def generate_trend_sniper():
    print("🔥 [GEMNO] 보안 모드로 트렌드 분석 시작...")
    
    prompt = """
    2030 타겟 '숏폼 트렌드 스나이퍼' 사업 아이템 기획안을 JSON으로 작성하세요.
    항목: brand_name, trend_vibe, pain_point, logic, money_map, one_line
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )
        
        raw_text = response.text.strip().replace('```json', '').replace('```', '')
        data = json.loads(raw_text)
        
        print(f"\n🎯 서비스명: {data['brand_name']}")
        print(f"✨ 한 줄 요약: {data['one_line']}")
        print("✅ 보안 설정으로 안전하게 분석 완료!")
        
        return data

    except Exception as e:
        print(f"❌ 에러: {e}")
        return None

if __name__ == "__main__":
    generate_trend_sniper()