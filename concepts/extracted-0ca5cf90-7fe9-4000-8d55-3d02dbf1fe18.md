# Extracted Knowledge from Conv: 0ca5cf90-7fe9-4000-8d55-3d02dbf1fe18

**Date**: 2025-12-22T07:12:22.849796Z

### Extracted Code (python)

```python
# 기본 연결 테스트
try:
    response = client.invoke([{"role": "user", "content": "안녕하세요"}])
    print("연결 성공!")
    print(f"응답: {response.content}")
    print(f"메타데이터: {response.response_metadata}")
except Exception as e:
    print(f"연결 실패: {e}")
```

### Extracted Code (python)

```python
import requests

url = "https://dev.apim.lgedx.biz/chatgpt/openai/v1/chat/completions"
headers = {
    "api-key": key,
    "Content-Type": "application/json"
}
data = {
    "model": model,
    "messages": [{"role": "user", "content": "테스트"}]
}

response = requests.post(url, headers=headers, json=data)
print(f"상태 코드: {response.status_code}")
print(f"응답: {response.json()}")
```

### Extracted Code (python)

```python
# 현재 설정된 정보 확인
print(f"엔드포인트: {endpoint}")
print(f"모델: {model}")
print(f"API 키: {key[:10]}...")  # 보안을 위해 일부만 출력
```

### Extracted Code (python)

```python
from langchain_openai import ChatOpenAI
import requests
import json
from datetime import datetime

# API 설정 정보
key = "3754bd5816fd412799f48083c01aa680"
model = "gpt-4.1-mini"
endpoint = "https://dev.apim.lgedx.biz/chatgpt/openai/v1"

print("=" * 60)
print("API 엔드포인트 정보 확인")
print("=" * 60)

# 1. 현재 설정된 엔드포인트 정보 출력
print("\n[1] 현재 설정 정보")
print(f"엔드포인트: {endpoint}")
print(f"모델: {model}")
print(f"API 키: {key[:10]}..." + "*" * 20)

# 2. LangChain 클라이언트로 연결 테스트
print("\n[2] LangChain 클라이언트 연결 테스트")
try:
    client = ChatOpenAI(
        openai_api_key=key,
        openai_api_base=endpoint,
        default_headers={"api-key": key},
        model=model
    )
    
    response = client.invoke([{"role": "user", "content": "안녕하세요"}])
    print("✓ 연결 성공!")
    print(f"응답: {response.content}")
    
    if hasattr(response, 'response_metadata'):
        print(f"메타데이터: {json.dumps(response.response_metadata, indent=2, ensure_ascii=False)}")
        
except Exception as e:
    print(f"✗ 연결 실패: {e}")

# 3. 직접 HTTP 요청으로 엔드포인트 확인
print("\n[3] 직접 HTTP 요청 테스트")
try:
    url = f"{endpoint}/chat/completions"
    headers = {
        "api-key": key,
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": "테스트"}],
        "max_tokens": 100
    }
    
    response = requests.post(url, headers=headers, json=data, timeout=30)
    print(f"상태 코드: {response.status_code}")
    
    if response.status_code == 200:
        print("✓ HTTP 요청 성공!")
        result = response.json()
        print(f"응답 미리보기: {json.dumps(result, indent=2, ensure_ascii=False)[:500]}...")
    else:
        print(f"✗ 요청 실패: {response.text}")
        
except Exception as e:
    print(f"✗ HTTP 요청 오류: {e}")

# 4. 질의 및 응답 저장 함수
def query_and_save(question, filename=None):
    """질문을 보내고 응답을 JSON 파일로 저장"""
    messages = [{"role": "user", "content": question}]
    response = client.invoke(messages)
    
    result = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "answer": response.content,
        "model": model,
        "endpoint": endpoint,
        "metadata": {
            "response_metadata": response.response_metadata if hasattr(response, 'response_metadata') else {}
        }
    }
    
    if filename is None:
        filename = f"response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ 응답 저장 완료: {filename}")
    return result

# 5. 실제 질의 테스트
print("\n[4] 실제 질의 테스트")
try:
    result = query_and_save("대한민국의 수도는 어디인가요?")
    print(f"답변: {result['answer']}")
except Exception as e:
    print(f"✗ 질의 실패: {e}")

print("\n" + "=" * 60)
print("엔드포인트 정보 확인 완료")
print("=" * 60)
```
