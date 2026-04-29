# Extracted Knowledge from Conv: c8d1192b-a854-431b-895c-b2c0fe5da667

**Date**: 2025-11-12T00:39:08.135533Z

### Extracted Code (python)

```python
# Python에서 환경 변수 불러오기
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로드
api_key = os.getenv('OPENAI_API_KEY')
```

### Extracted Code (plaintext)

```plaintext
# OpenAI API 설정
OPENAI_API_KEY=sk-your-actual-api-key-here

# 선택적 설정
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.7
OPENAI_MAX_TOKENS=1000
```

### Extracted Code (bash)

```bash
# 1. OpenAI API 서버 연결 확인
curl -I https://api.openai.com

# 2. 더 상세한 테스트
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Extracted Code (python)

```python
import requests

try:
    response = requests.get('https://api.openai.com', timeout=5)
    print(f"✅ 연결 성공: {response.status_code}")
except requests.exceptions.ConnectionError:
    print("❌ 연결 실패: 네트워크 차단 가능성")
except requests.exceptions.Timeout:
    print("❌ 타임아웃: 방화벽 차단 가능성")
except Exception as e:
    print(f"❌ 오류: {e}")
```

### Extracted Code (plaintext)

```plaintext
# .env 파일
OPENAI_API_KEY=sk-proj-xxxxx

# 프록시 설정 (회사 프록시 주소)
HTTP_PROXY=http://proxy.company.com:8080
HTTPS_PROXY=http://proxy.company.com:8080
```

### Extracted Code (python)

```python
import openai
import os

# 프록시 설정
os.environ['HTTP_PROXY'] = 'http://proxy.company.com:8080'
os.environ['HTTPS_PROXY'] = 'http://proxy.company.com:8080'

# OpenAI 클라이언트
client = openai.OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    http_client=openai.DefaultHttpxClient(
        proxies={
            "http://": "http://proxy.company.com:8080",
            "https://": "http://proxy.company.com:8080"
        }
    )
)
```

### Extracted Code (bash)

```bash
# 모바일 핫스팟 연결 후 테스트
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer sk-proj-xxxxx"
```

### Extracted Code (python)

```python
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def diagnose_connection():
    api_key = os.getenv('OPENAI_API_KEY')
    
    print("=== OpenAI API 연결 진단 ===\n")
    
    # 1. API 키 존재 확인
    if not api_key:
        print("❌ API 키가 .env 파일에 없습니다.")
        return
    print(f"✅ API 키 확인: {api_key[:20]}...{api_key[-4:]}")
    
    # 2. 네트워크 연결 확인
    print("\n[네트워크 테스트]")
    try:
        response = requests.get('https://api.openai.com', timeout=5)
        print(f"✅ OpenAI 서버 연결: {response.status_code}")
    except Exception as e:
        print(f"❌ 네트워크 오류: {e}")
        return
    
    # 3. API 인증 테스트
    print("\n[API 인증 테스트]")
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get(
            'https://api.openai.com/v1/models',
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            print("✅ API 키 유효함!")
        else:
            print(f"❌ API 오류: {response.status_code}")
            print(f"상세: {response.json()}")
    except Exception as e:
        print(f"❌ 요청 실패: {e}")

if __name__ == "__main__":
    diagnose_connection()
```

### Extracted Code (text)

```text
HTTP/2 421  ← 응답을 받았음 (연결 성공)
server: cloudflare  ← Cloudflare CDN 통과
cf-ray: 99d27f170a06eab5-ICN  ← 인천(ICN)에서 응답
```

### Extracted Code (plaintext)

```plaintext
OPENAI_API_KEY= sk-proj-xxxxxxxxxxxxx$  ← 앞에 공백
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx $  ← 뒤에 공백
OPENAI_API_KEY='sk-proj-xxxxxxxxxxxxx'$  ← 따옴표
```

### Extracted Code (bash)

```bash
# 실제 API 키로 테스트 (.env에서 키 가져오기)
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $(grep OPENAI_API_KEY .env | cut -d '=' -f 2)" \
  | python -m json.tool
```

### Extracted Code (python)

```python
import os
from dotenv import load_dotenv
import openai

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

print("=== API 키 진단 ===")
print(f"키 길이: {len(api_key) if api_key else 0}")
print(f"시작: {api_key[:15] if api_key else 'None'}...")
print(f"끝: ...{api_key[-10:] if api_key else 'None'}")
print(f"공백 포함: {' ' in api_key if api_key else 'N/A'}")
print(f"줄바꿈 포함: {'\\n' in api_key if api_key else 'N/A'}")

# 실제 API 호출 테스트
try:
    client = openai.OpenAI(api_key=api_key)
    models = client.models.list()
    print("\n✅ API 키 정상 작동!")
    print(f"사용 가능 모델 수: {len(models.data)}")
except openai.AuthenticationError as e:
    print(f"\n❌ 인증 오류: {e}")
except Exception as e:
    print(f"\n❌ 기타 오류: {e}")
```

### Extracted Code (bash)

```bash
# 1. 새 .env 파일 생성
rm .env
nano .env

# 2. 아래 형식으로 입력 (따옴표 없이!)
# OPENAI_API_KEY=sk-proj-여기에전체키붙여넣기

# 3. 저장 후 확인
cat .env

# 4. Python 스크립트 재실행
```
