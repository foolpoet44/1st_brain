# Extracted Knowledge from Conv: 0fda45cf-9336-41be-9fc4-fb77c85689b4

**Date**: 2025-12-03T23:29:33.715426Z

### Extracted Code (text)

```text
[Day 1-3] 연봉 데이터 수집
- 타겟: 500개 이상 데이터 포인트
- 소스: 잡코리아, 사람인, 원티드, 로켓펀치, 크레딧잡 등
- 분류: 직군 10개 × 경력 10단계 = 100개 셀

[Day 4-7] 면접 질문 데이터 수집
- 타겟: 직군별 100개씩 (총 500개)
- 소스: 실제 면접 후기, HR 커뮤니티, 링커리어, 블라인드
- 분류: 기본/역량/상황/가치관/직무 5개 카테고리

[Day 8-10] HR 문서 표준 양식 조사
- 타겟: 노무법인 5곳 + 고용노동부 양식
- 수집: 취업규칙, 근로계약서, 평가표 각 10종씩
- 벤치마크: Best Practice 추출

[Day 11-14] 데이터 정제 및 검증
- 파이썬으로 데이터 클리닝
- 아웃라이어 제거
- 통계 검증 (평균, 중위값, 표준편차)
```

### Extracted Code (text)

```text
[Product 1] 연봉 벤치마크 가이드북 v1.0
- 구성: 
  • 50페이지 PDF
  • 10개 직군 × 10개 경력 단계
  • 직군별 연봉 분포 그래프 (파이썬 matplotlib)
  • 지역별 보정 계수
  • 실제 적용 예시 5개
- 제작 도구: 파이썬(데이터 처리) + MS Word/Canva(디자인)
- 가격: 79,000원

[Product 2] 면접 질문 템플릿 세트 v1.0
- 구성:
  • Excel 파일 3종 (개발자/마케터/영업)
  • 각 50개 질문 + STAR 평가 가이드
  • 점수 자동 계산 수식
  • 사용 매뉴얼 10페이지
- 가격: 49,000원/직군

[Product 3] HR 문서 스타터팩 v1.0
- 구성:
  • 7대 필수 문서 (Word 수정 가능)
  • 작성 가이드 20페이지
  • 실제 사례 3개
  • 법적 체크리스트
- 가격: 99,000원
```

### Extracted Code (text)

```text
[통합 상품 설계]
- 제품명: "HR Starter Kit - 완전판"
- 구성: Product 1+2+3 통합
- 추가 제공: 30분 온라인 컨설팅 1회
- 가격: 179,000원 (개별 구매 대비 30% 할인)

[마케팅 자산 제작]
- 크몽 판매 페이지 4개 (개별 3개 + 통합 1개)
- LinkedIn 소개 포스트 5개 사전 작성
- 샘플 페이지 무료 배포용 (리드 획득)
- 유튜브 소개 영상 1개 (3분)
```

### Extracted Code (text)

```text
[판매 채널 오픈]
✅ 크몽: 4개 상품 등록
  - 초기 가격: 정상가의 70% (얼리버드)
  - 목표: 첫 2주 내 10건 판매

✅ 탈잉: 1:1 컨설팅 상품 등록
  - 가격: 10만원/1시간
  - 목표: 첫 달 3건

✅ 자체 랜딩페이지 제작 (노션 or Wix)
  - 무료 샘플 다운로드 → 이메일 수집
  - 목표: 100명 이메일 리스트

[콘텐츠 마케팅 시작]
✅ LinkedIn 활동 (주 5회)
  - 포스팅 주제:
    • "스타트업 연봉 책정 실수 Top 5"
    • "면접관이 하면 안 되는 질문 10가지"
    • "취업규칙 작성 시 놓치기 쉬운 함정"
  - 목표: 팔로워 200명

✅ 블로그 시작 (티스토리 or 브런치)
  - 주 3회 포스팅 (2,000자 이상)
  - SEO 키워드:
    • "중소기업 연봉 책정"
    • "스타트업 면접 질문"
    • "취업규칙 작성"
```

### Extracted Code (text)

```text
[고객 리뷰 확보]
- 목표: 5점 리뷰 20개 이상
- 방법:
  • 구매 후 3일 이내 리뷰 요청 메시지
  • 리뷰 작성자에게 추가 템플릿 1종 무료 제공
  • 우수 리뷰는 마케팅 자료로 활용

[제품 개선]
- 고객 피드백 반영해서 v1.1 업데이트
- 가장 많이 받은 질문 → FAQ 페이지 제작
- 불만 사항 → 즉시 개선

[가격 정상화]
- Week 8부터 정상가로 전환
- 통계 확인: 전환율, 객단가, 리텐션
```

### Extracted Code (text)

```text
[AI 면접 질문 생성기 MVP]
- 기술 스택: 
  • 프론트: React (바이브 코딩으로 생성)
  • 백엔드: Claude API
  • 호스팅: Vercel (무료)
  
- 기능:
  1. 직무/경력/회사문화 입력 폼
  2. AI가 맞춤형 면접 질문 30개 생성
  3. 질문별 평가 기준 자동 생성
  4. PDF 다운로드
  
- 가격 모델:
  • 무료: 월 3회 생성
  • Pro: 월 49,000원 (무제한)
  • 기업: 월 99,000원 (팀 5명)

[연봉 계산기 웹 앱]
- 기술 스택: 
  • Streamlit (파이썬)
  • 데이터: 수집한 500개 연봉 데이터
  
- 기능:
  1. 직군/경력/지역/회사규모 선택
  2. 추천 연봉 범위 실시간 계산
  3. 동종업계 비교 그래프
  4. 인상률 시뮬레이터
  
- 가격: 무료 (리드 획득용)
```

### Extracted Code (text)

```text
[기업 맞춤형 컨설팅 패키지]

Package A: "연봉 테이블 구축" (2-3일, 300만원)
- Day 1: 회사 현황 분석 (매출, 인원, 업종)
- Day 2: 직군별 연봉 테이블 설계
- Day 3: 엑셀 툴 제작 + 설명회

Package B: "채용 프로세스 구축" (3일, 400만원)
- Day 1: 직무 분석 워크숍
- Day 2: 면접 질문 & 평가표 커스터마이징
- Day 3: 면접관 트레이닝

Package C: "HR 기초 세팅 올인원" (5일, 800만원)
- Package A + B + 취업규칙 작성
- HR 담당자 1:1 코칭 3시간
- 3개월 이메일 지원

[첫 B2B 고객 확보 전략]
- 타겟: 투자 받은 시리즈 A 스타트업
- 접근: 
  • 크레딧잡에서 투자 뉴스 모니터링
  • 투자 받은 지 1개월 이내 회사에 콜드메일
  • 무료 진단 1회 제공 → 컨설팅 전환
- 목표: 첫 3개월 내 B2B 1건 수주
```

### Extracted Code (python)

```python
# 크롤링 대상 사이트
sources = {
    "잡코리아": "https://www.jobkorea.co.kr/salary/",
    "사람인": "https://www.saramin.co.kr/zf_user/salaryinfo/",
    "원티드": "https://www.wanted.co.kr/salary",
    "로켓펀치": "https://www.rocketpunch.com/jobs",
    "크레딧잡": "https://www.creditjob.com/",
}

# 수집 데이터 구조
data_schema = {
    "직군": ["개발", "마케팅", "영업", "디자인", "HR", "재무", "CS", "기획", "법무", "물류"],
    "세부직무": ["백엔드", "프론트엔드", "데이터", ...],
    "경력": ["신입", "1년", "2년", ..., "10년+"],
    "회사규모": ["10인 미만", "10-50인", "50-100인", "100-300인"],
    "지역": ["서울", "경기", "부산", ...],
    "연봉_최소": int,
    "연봉_최대": int,
    "연봉_평균": int,
}
```

### Extracted Code (text)

```text
---

#### **문서 목록 & 제작 계획**

**필수 7대 문서:**

| 문서명 | 참고 소스 | 제작 시간 | 특이사항 |
|--------|----------|----------|----------|
| 1. 취업규칙 | 고용노동부 표준안 | 2일 | **법적 검토 필수** |
| 2. 근로계약서 (정규직) | 고용노동부 표준 | 4시간 | 변형근로제 옵션 추가 |
| 3. 근로계약서 (계약직) | 고용노동부 표준 | 4시간 | 계약 갱신 조항 명시 |
| 4. 인사평가표 | 대기업 사례 3개 | 1일 | 역량/성과 5:5 비율 |
| 5. 연차 관리 대장 | 엑셀 자체 제작 | 4시간 | 자동 계산 수식 |
| 6. 급여명세서 | 플렉스 참고 | 4시간 | 4대보험 자동 계산 |
| 7. 경조사 규정 | 노무법인 샘플 | 2시간 | - |

**추가 제공 문서 (차별화):**
- 직무기술서 (JD) 템플릿
- 온보딩 체크리스트
- 1:1 면담 기록지
- 징계 절차 가이드

---

### **D. 데이터 법적 이슈 & 대응**

#### **개인정보 보호**
```

### Extracted Code (text)

```text
---

### **E. 데이터 업데이트 계획**

#### **주기별 업데이트 전략**

**분기별 (3개월):**
- 연봉 데이터 재수집 (시장 변화 반영)
- 신규 채용공고 100개 분석
- 상승률 계산 및 그래프 업데이트

**반기별 (6개월):**
- 면접 질문 트렌드 분석
- 고객 피드백 반영하여 질문 20% 교체
- 신규 직군 추가 (예: AI 엔지니어)

**연 1회:**
- 전체 가이드북 개정판 출시
- 법률 개정사항 반영 (근로기준법 등)
- 주요 개선사항 반영

#### **버전 관리**
```

### Extracted Code (text)

```text
[실행 단계]
1. 잡코리아 접속 → 상단 메뉴 "연봉" 클릭
2. 좌측 "기업별 연봉" 선택
3. 업종 필터: IT/인터넷 선택
4. 100개 기업 리스트 확인

[수집 정보]
- 기업명, 평균연봉, 직군별 연봉 범위
- 예: 네이버 / 개발 / 5년차 / 5,500만원

[복사 방법]
→ Ctrl+C로 표 복사 → 엑셀에 Ctrl+V
→ 또는 마우스 드래그로 선택 후 복사
```

### Extracted Code (text)

```text
[실행 단계]
1. "직무별 연봉" 탭 클릭
2. 직군 선택: 개발, 마케팅, 영업, 디자인 등
3. 경력별 필터: 신입, 1-3년, 4-6년, 7-9년, 10년+

[수집 정보 예시]
직군: 백엔드 개발자
- 신입: 3,000-3,800만원
- 1-3년: 3,800-5,000만원
- 4-6년: 5,000-6,500만원
- 7-9년: 6,500-8,500만원
- 10년+: 8,500만원~

[엑셀 입력]
1 | 2025-01-10 | 잡코리아 | 개발 | 백엔드 | 신입 | 50-100인 | 서울 | 3000 | 3800
2 | 2025-01-10 | 잡코리아 | 개발 | 백엔드 | 1-3년 | 50-100인 | 서울 | 3800 | 5000
...
```

### Extracted Code (python)

```python
# 잡코리아_크롤러.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_jobkorea_salary(job_category):
    """
    잡코리아 연봉 정보 크롤링
    주의: 실제 사용 전 robots.txt 확인 필요
    """
    base_url = "https://www.jobkorea.co.kr/salary/"
    
    # 실제 구현은 사이트 구조에 따라 달라짐
    # 여기서는 개념만 제시
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    data = []
    
    try:
        response = requests.get(base_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 실제 HTML 구조 분석 후 수정 필요
        # salary_items = soup.find_all('div', class_='salary-item')
        
        # for item in salary_items:
        #     job_title = item.find('span', class_='job').text
        #     salary = item.find('span', class_='salary').text
        #     data.append({'직무': job_title, '연봉': salary})
        
        time.sleep(1)  # 서버 부하 방지
        
    except Exception as e:
        print(f"오류 발생: {e}")
    
    return data

# 실행 예시
# data = scrape_jobkorea_salary("개발")
# df = pd.DataFrame(data)
# df.to_excel("잡코리아_연봉데이터.xlsx", index=False)
```

### Extracted Code (text)

```text
[실행 단계]
1. 검색창에 직무 입력 (예: "백엔드 개발자")
2. 필터 설정:
   - 경력: 신입, 경력 1년, 경력 3년 등 개별 선택
   - 지역: 서울
   - 기업형태: 중소기업, 스타트업

3. 채용공고 100개 오픈
4. 각 공고에서 연봉 정보 확인

[수집 정보]
- "급여: 회사내규에 따름" → SKIP
- "급여: 연봉 3,500만원 이상" → 3500, 3500 입력
- "급여: 연봉 3,000~4,500만원" → 3000, 4500 입력

[팁: 크롬 확장 프로그램]
"Web Scraper" 확장 프로그램 사용하면 반자동 수집 가능
→ Chrome 웹 스토어에서 "Web Scraper" 검색 설치
```

### Extracted Code (text)

```text
공고 제목: [네이버] 백엔드 개발자 경력직 채용
급여: 연봉 5,000만원~7,000만원
경력: 3년 이상
→ 엑셀 입력: 
   직군=개발, 세부직무=백엔드, 경력=3년, 최소=5000, 최대=7000
```

### Extracted Code (text)

```text
[실행 단계]
1. 사람인 접속 → 상단 "연봉정보" 클릭
2. "직종별 평균연봉" 선택
3. 직종 대분류 선택 (IT·인터넷)
4. 중분류 선택 (웹개발, 앱개발, 데이터 등)

[화면 구성]
- 그래프로 경력별 연봉 표시
- 마우스 호버 시 정확한 수치 확인 가능

[수집 팁]
→ 스크린샷 찍어서 나중에 참고
→ 또는 개발자도구(F12) → Network 탭에서 JSON 데이터 확인
```

### Extracted Code (text)

```text
[방법]
1. F12 눌러서 개발자도구 오픈
2. Network 탭 선택
3. 페이지 새로고침 (F5)
4. XHR 필터 선택
5. "salary" 관련 요청 찾기
6. Response 탭에서 JSON 데이터 복사

[JSON 데이터 예시]
{
  "jobCategory": "백엔드개발",
  "careerLevel": "3년",
  "avgSalary": 4800,
  "minSalary": 3500,
  "maxSalary": 6500
}

→ 이걸 파이썬으로 파싱하면 빠름
```

### Extracted Code (text)

```text
[실행 단계]
1. 원티드 접속
2. 직군 선택 (예: 개발)
3. 포지션 검색 (예: "백엔드 개발자")
4. 필터:
   - 경력: 1년, 3년, 5년 등
   - 지역: 서울, 경기

[특징]
- 스타트업 연봉 데이터가 풍부
- 대부분 연봉 범위 명시됨
- "연봉 정보 없음" 공고는 SKIP

[수집 예시]
채용공고: 백엔드 개발자 (Python)
회사: 토스
연봉: 5,000만원 - 8,000만원
경력: 3년 이상
→ 엑셀 입력
```

### Extracted Code (python)

```python
# 원티드_크롤러.py
import requests
import json

def get_wanted_jobs(job_category, career):
    """
    원티드 API 활용 (비공식)
    실제 사용 시 원티드 이용약관 확인 필요
    """
    # 원티드는 API가 있을 수 있으니 확인
    # 없으면 Selenium으로 브라우저 자동화
    pass
```

### Extracted Code (text)

```text
[실행 단계]
1. 로켓펀치 접속 → "채용공고" 메뉴
2. 직군 필터 선택
3. 회사 규모: 시리즈A, 시리즈B, 시리즈C

[특징]
- 스타트업 연봉 정보 정확함
- 투자 단계별 연봉 차이 확인 가능
- 스톡옵션 정보도 있음 (선택적 수집)

[스타트업 특화 데이터]
시리즈A 스타트업:
- 개발자 3년차: 4,000-5,500만원
- 마케터 3년차: 3,500-4,500만원

시리즈B 스타트업:
- 개발자 3년차: 5,000-7,000만원
- 마케터 3년차: 4,000-5,500만원
```

### Extracted Code (text)

```text
[엑셀에서 실행]
1. 중복 데이터 제거
   → 데이터 탭 → "중복된 항목 제거"

2. 결측치 확인
   → 빈 셀이 있으면 "N/A" 입력

3. 이상치 확인
   → 신입 연봉이 1억? → 오타, 삭제
   → 10년차 연봉이 2천만원? → 오타, 삭제

4. 단위 통일
   → 모두 "만원" 단위로 통일
   → 5,000만원 → 5000
   → 5천만원 → 5000
```

### Extracted Code (python)

```python
# 데이터정제.py
import pandas as pd
import numpy as np

# 1. 데이터 로드
df = pd.read_excel("연봉데이터_수집.xlsx")

print(f"총 데이터 개수: {len(df)}")
print(f"컬럼: {df.columns.tolist()}")

# 2. 기본 정보 확인
print("\n=== 데이터 미리보기 ===")
print(df.head())
print("\n=== 결측치 확인 ===")
print(df.isnull().sum())

# 3. 중복 제거
df_clean = df.drop_duplicates()
print(f"중복 제거 후: {len(df_clean)}개")

# 4. 이상치 제거 (IQR 방법)
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    return df[
        (df[column] >= lower_bound) & 
        (df[column] <= upper_bound)
    ]

df_clean = remove_outliers(df_clean, "최소연봉")
df_clean = remove_outliers(df_clean, "최대연봉")
print(f"이상치 제거 후: {len(df_clean)}개")

# 5. 평균 연봉 계산
df_clean['평균연봉'] = (
    df_clean['최소연봉'] + df_clean['최대연봉']
) / 2

# 6. 경력을 숫자로 변환
career_map = {
    '신입': 0,
    '1년': 1,
    '2년': 2,
    '3년': 3,
    '4년': 4,
    '5년': 5,
    '6년': 6,
    '7년': 7,
    '8년': 8,
    '9년': 9,
    '10년+': 10
}
df_clean['경력_숫자'] = df_clean['경력'].map(career_map)

# 7. 직군별 통계
stats = df_clean.groupby(['직군', '경력']).agg({
    '평균연봉': ['mean', 'median', 'std', 'count']
}).round(0)

print("\n=== 직군별 통계 ===")
print(stats)

# 8. 저장
df_clean.to_excel("연봉데이터_정제완료.xlsx", index=False)
stats.to_excel("연봉통계_요약.xlsx")

print("\n✅ 정제 완료!")
print(f"최종 데이터: {len(df_clean)}개")
```

### Extracted Code (python)

```python
# 시각화.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 로드
df = pd.read_excel("연봉데이터_정제완료.xlsx")

# 1. 직군별 평균 연봉 비교
plt.figure(figsize=(12, 6))
job_avg = df.groupby('직군')['평균연봉'].mean().sort_values(ascending=False)
job_avg.plot(kind='bar', color='skyblue')
plt.title('직군별 평균 연봉', fontsize=16, fontweight='bold')
plt.xlabel('직군')
plt.ylabel('평균 연봉 (만원)')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('그래프1_직군별평균연봉.png', dpi=300)
plt.close()

# 2. 경력별 연봉 추이 (개발자 예시)
plt.figure(figsize=(12, 6))
dev_data = df[df['직군'] == '개발']
dev_career = dev_data.groupby('경력_숫자')['평균연봉'].mean()
plt.plot(dev_career.index, dev_career.values, marker='o', linewidth=2, markersize=8)
plt.title('개발자 경력별 평균 연봉 추이', fontsize=16, fontweight='bold')
plt.xlabel('경력 (년)')
plt.ylabel('평균 연봉 (만원)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('그래프2_개발자경력별연봉.png', dpi=300)
plt.close()

# 3. 회사 규모별 연봉 비교
plt.figure(figsize=(10, 6))
company_size = df.groupby('회사규모')['평균연봉'].mean().sort_values()
company_size.plot(kind='barh', color='coral')
plt.title('회사 규모별 평균 연봉', fontsize=16, fontweight='bold')
plt.xlabel('평균 연봉 (만원)')
plt.ylabel('회사 규모')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('그래프3_회사규모별연봉.png', dpi=300)
plt.close()

# 4. 히트맵 (직군 × 경력)
plt.figure(figsize=(14, 8))
pivot = df.pivot_table(
    values='평균연봉', 
    index='직군', 
    columns='경력_숫자',
    aggfunc='mean'
)
sns.heatmap(pivot, annot=True, fmt='.0f', cmap='YlOrRd', cbar_kws={'label': '평균 연봉 (만원)'})
plt.title('직군 × 경력별 평균 연봉 히트맵', fontsize=16, fontweight='bold')
plt.xlabel('경력 (년)')
plt.ylabel('직군')
plt.tight_layout()
plt.savefig('그래프4_히트맵.png', dpi=300)
plt.close()

print("✅ 그래프 4개 생성 완료!")
```

### Extracted Code (text)

```text
[실행 단계]
1. 자소설닷컴 접속 → "합격자소서" 메뉴
2. 기업 선택 (예: 네이버, 카카오, 쿠팡 등)
3. "면접후기" 탭 클릭
4. "기억에 남는 면접 질문" 섹션 확인

[실제 예시]
기업: 네이버
직무: 백엔드 개발
질문1: "동시성 이슈를 경험한 적이 있나요? 어떻게 해결했나요?"
질문2: "대용량 트래픽을 처리하기 위한 아키텍처 설계 경험은?"
질문3: "가장 어려웠던 버그는 무엇이었고, 어떻게 해결했나요?"

[엑셀 입력]
Q001 | 개발 | 백엔드 | 동시성 이슈를 경험한 적이 있나요? | 역량 | 중급 | 문제해결, 기술이해도 | 자소설닷컴

[수집 팁]
→ 기업 50개 × 질문 4개 = 200개
→ 대기업/중견/스타트업 골고루 수집
```

### Extracted Code (text)

```text
[실행 단계]
1. 링커리어 커뮤니티 접속
2. 검색: "면접 질문"
3. 인기 게시물 확인:
   - "면접 예상 질문 50개 모음"
   - "직군별 면접 질문 리스트"
   
[게시물 예시]
제목: "💯면접 예상질문 리스트 50개"
내용에서 질문 복사:
1. 간단하게 자기소개 해주세요
2. 우리 회사에 지원한 이유는?
3. 본인의 강점과 약점은?
...

[엑셀 입력]
Q051 | 공통 | - | 간단하게 자기소개 해주세요 | 기본 | 신입 | 커뮤니케이션 | 링커리어
Q052 | 공통 | - | 우리 회사에 지원한 이유는? | 기본 | 신입 | 지원동기 | 링커리어
```

### Extracted Code (text)

```text
[실행 단계]
1. 네이버에서 "[기업명] 면접 후기" 검색
2. 블로그 글 10-20개 읽기
3. 실제 받은 질문 복사

[예시 블로그 글]
"토스 백엔드 면접 후기"
1차 기술면접:
- Redis와 Memcached 차이점은?
- RESTful API 설계 원칙은?
- DB 인덱스 동작 원리는?

2차 컬처핏 면접:
- 토스에서 이루고 싶은 것은?
- 팀원과 갈등이 생기면 어떻게 해결하나요?

[엑셀 입력]
Q101 | 개발 | 백엔드 | Redis와 Memcached 차이점은? | 직무 | 주니어 | 기술지식 | 토스 면접후기 블로그
```

### Extracted Code (text)

```text
[실행 단계]
1. LinkedIn 접속
2. 검색: "HR Manager" + "Seoul"
3. 2촌 이내 찾기
4. 메시지 발송:

"안녕하세요, [이름]님.
저는 HR 컨설팅 서비스를 준비 중인 [본인이름]입니다.
면접 질문 설계에 대한 인사이트를 얻고자 
30분 정도 커피챗이 가능하실까요?
소정의 사례비(스타벅스 쿠폰)를 드립니다."
```

### Extracted Code (text)

```text
1. [직군]을 채용할 때 가장 중요하게 보는 역량은?
2. 실제 면접에서 자주 사용하는 질문 5가지는?
3. 좋은 답변과 나쁜 답변의 차이는?
4. STAR 기법을 실제로 어떻게 활용하나요?
5. 면접관들이 자주 하는 실수는?
6. 최근 면접 트렌드 변화는?
7. 스타트업 vs 대기업 면접 질문 차이는?
8. 컬처핏 평가 시 어떤 질문을 하나요?
9. 개발자 채용 시 기술 질문 난이도는?
10. 비추천하는 면접 질문이 있나요? (차별적 질문 등)
```

### Extracted Code (text)

```text
인터뷰이: 김OO (10년차 HR 매니저, 테크 스타트업)
날짜: 2025.01.15
주요 인사이트:
- "프로젝트에서 가장 어려웠던 점은?"보다
  "프로젝트에서 예상하지 못한 문제가 생겼을 때 어떻게 대응했나요?"가 더 효과적
- 이유: 구체적인 상황과 대응을 들을 수 있음

추출된 질문:
Q201 | 개발 | - | 프로젝트에서 예상치 못한 문제 발생 시 대응 방법은? | 상황 | 주니어 | 문제해결 | HR 인터뷰_김OO
```

### Extracted Code (text)

```text
제목: "Structured Interviews for Personnel Selection: A Practical Guide"
저자: Michael A. Campion et al.

주요 내용:
1. 역량 기반 질문 설계 방법
2. 평가 기준 (Rubric) 작성법
3. 면접관 편향 줄이는 방법

추출 가능한 질문:
- "Tell me about a time when you had to work under pressure"
- "Describe a situation where you had to resolve a conflict"
→ 한국어로 번역 및 각색

Q251 | 공통 | - | 압박 상황에서 업무를 수행한 경험을 말씀해주세요 | 역량 | 주니어 | 스트레스관리 | 학술논문_Campion
```

### Extracted Code (python)

```python
# 질문검증.py
import pandas as pd

df = pd.read_excel("면접질문_수집.xlsx")

# 1. 중복 질문 찾기
duplicates = df[df.duplicated(subset=['질문'], keep=False)]
print(f"중복 질문: {len(duplicates)}개")
print(duplicates[['질문ID', '질문']])

# 2. 카테고리별 분포 확인
category_dist = df['카테고리'].value_counts()
print("\n카테고리 분포:")
print(category_dist)

# 목표: 각 카테고리 100개씩
# 기본: 100개, 역량: 150개, 상황: 100개, 가치관: 50개, 직무: 100개

# 3. 직군별 분포 확인
job_dist = df['직군'].value_counts()
print("\n직군별 질문 수:")
print(job_dist)

# 목표: 주요 직군(개발, 마케팅, 영업, 디자인, HR)은 각 50개 이상

# 4. 부족한 셀 확인
shortage = []
for job in ['개발', '마케팅', '영업', '디자인', 'HR']:
    for cat in ['기본', '역량', '상황', '가치관', '직무']:
        count = len(df[(df['직군'] == job) & (df['카테고리'] == cat)])
        if count < 10:
            shortage.append({
                '직군': job,
                '카테고리': cat,
                '현재': count,
                '목표': 10,
                '부족': 10 - count
            })

shortage_df = pd.DataFrame(shortage)
print("\n추가 수집 필요:")
print(shortage_df)
shortage_df.to_excel("추가수집_계획.xlsx", index=False)
```

### Extracted Code (text)

```text
[개선 전]
"팀 프로젝트 경험이 있나요?"
→ 너무 막연함, Yes/No로 끝날 수 있음

[개선 후]
"팀 프로젝트에서 의견 충돌이 있었을 때, 
어떻게 해결하셨나요? 구체적인 상황과 결과를 말씀해주세요."
→ STAR 기법 유도, 구체적 답변 유도
```

### Extracted Code (text)

```text
질문: "가장 실패했던 경험과 그로부터 배운 점은?"

평가 기준:
✅ 우수 (5점):
- 구체적인 실패 상황 설명
- 실패 원인 분석
- 개선 조치 실행
- 실제 성과 향상 증명

⚠️ 보통 (3점):
- 실패 상황 설명만
- 원인 분석 부족
- 개선 의지는 있으나 실행 미흡

❌ 미흡 (1점):
- 막연한 답변
- 책임 회피 (남 탓)
- 배운 점 없음
```

### Extracted Code (text)

```text
[실행 단계]
1. 고용노동부 홈페이지 접속
2. 상단 메뉴: 민원·정보 → 서식자료
3. 검색창에 입력:

[필수 다운로드 10종]
1. "표준근로계약서" 검색 → 다운로드 (정규직용)
2. "기간제근로계약서" 검색 → 다운로드 (계약직용)
3. "취업규칙 작성 가이드" 다운로드
4. "취업규칙 예시" 다운로드
5. "연차휴가 사용촉진 양식" 다운로드
6. "근로시간 특례업종 동의서" 다운로드
7. "임금명세서 표준 양식" 다운로드
8. "직장 내 괴롭힘 신고서" 다운로드
9. "육아휴직 신청서" 다운로드
10. "경력증명서" 다운로드

[저장 폴더 구조]
HR문서_수집/
├─ 고용노동부/
│  ├─ 근로계약서/
│  ├─ 취업규칙/
│  └─ 기타서식/
```

### Extracted Code (text)

```text
파일명: "취업규칙_작성_예시.hwp"

목차 확인:
제1장 총칙
제2장 인사
제3장 복무
제4장 근로시간, 휴게, 휴일
제5장 임금
제6장 퇴직
제7장 포상 및 징계
제8장 교육훈련
제9장 안전보건 및 재해보상
제10장 부칙

→ 이 구조를 기반으로 자체 템플릿 제작
```

### Extracted Code (text)

```text
[검색 리스트]
1. "율촌 노무법인 블로그"
2. "법무법인 세종 노동팀"
3. "김앤장 고용노동"
4. "노무법인 일과사람들"
5. "노무법인 평안"

[수집 방법]
1. 각 법인 홈페이지 접속
2. "자료실" 또는 "블로그" 메뉴
3. 무료 다운로드 가능한 템플릿 확인
4. 뉴스레터 구독 신청 (월간 자료 받기)

[예시: 노무법인 일과사람들]
URL: https://www.worklaw.co.kr/
메뉴: 자료실 → 무료서식
다운로드:
- 인사평가표 샘플
- 상벌규정 예시
- 복리후생규정 예시
```

### Extracted Code (text)

```text
[무료 체험 가입]
1. 플렉스 홈페이지 접속
2. "무료로 시작하기" 클릭
3. 회사 정보 입력 (테스트용으로 입력 가능)

[벤치마킹 포인트]
- 근로계약서 작성 UI: 어떤 항목을 물어보나?
- 급여명세서 디자인: 레이아웃이 어떻게 되나?
- 연차관리 기능: 자동 계산 로직은?

[스크린샷 찍기]
→ 템플릿 제작 시 참고용
→ 단, 그대로 복사는 안 됨 (저작권)
```

### Extracted Code (text)

```text
[무료 기능 활용]
1. 리멤버 명함 관리 앱 다운로드
2. HR 기능 탐색
3. 제공되는 예시 데이터 확인

[벤치마킹 포인트]
- 조직도 구조
- 인사정보 입력 항목
- 근태관리 화면
```

### Extracted Code (text)

```text
[데모 요청]
1. 홈페이지에서 "데모 신청"
2. 영업 담당자와 미팅 (30분)
3. 실제 제품 시연 보면서 메모

[질문 리스트]
- 가장 많이 사용하는 기능은?
- 고객들이 가장 어려워하는 부분은?
- 중소기업에서 필수적인 기능은?
```

### Extracted Code (text)

```text
[근로계약서 - 정규직]

1. 기본 정보
- 회사명, 주소, 대표자
- 근로자 이름, 주민등록번호, 주소, 연락처

2. 필수 명시 사항 (근로기준법 17조)
✅ 근무 장소 및 업무 내용
✅ 근로 계약 기간 (정규직은 "정함이 없음")
✅ 근무 시간 (출퇴근 시각)
✅ 휴게시간 (점심 1시간 등)
✅ 휴일, 휴가
✅ 임금의 구성, 계산방법, 지급방법
✅ 퇴직에 관한 사항
✅ 4대 보험 가입 여부

3. 특약 사항 (선택)
- 수습기간 (3개월)
- 경업금지 (퇴사 후 경쟁사 이직 제한)
- 비밀유지 (기업 정보 보호)
- 스톡옵션 (있는 경우)

[워드 파일 작성]
→ 빈칸은 [     ] 표시로 남겨두기
→ 작성 가이드는 각주로 표시
→ 예시: [근무장소: 서울시 강남구 테헤란로 123 (본사 주소 입력)]
```

### Extracted Code (text)

```text
[중소기업용 간소화 버전]

필수 포함 내용:
1. 근무시간: 9시~6시 (예시)
2. 휴게시간: 12시~1시
3. 주휴일: 주 1회 (보통 일요일)
4. 연차휴가: 근로기준법에 따름
   - 1년 근무: 15일
   - 3년 이상: 매 2년마다 1일 가산 (최대 25일)
5. 임금: 매월 25일 지급 (예시)
6. 퇴직금: 1년 이상 근무 시 지급
7. 복리후생: 4대보험, 경조사비, 야근식대 등
8. 징계: 경고, 감봉, 정직, 해고
9. 직장 내 괴롭힘 금지
10. 성희롱 예방

[⚠️ 법적 주의사항]
→ 취업규칙은 고용노동부 신고 필수 (10인 이상)
→ 근로기준법보다 불리하게 작성하면 무효
→ 작성 후 반드시 노무사 검토 권장 (별도 비용)

[템플릿 구성]
- 기본 취업규칙 (20페이지)
- 작성 가이드 (10페이지)
- 신고 방법 안내 (5페이지)
- 체크리스트 (1페이지)
```

### Extracted Code (text)

```text
[역량 평가 50점 + 성과 평가 50점 = 총 100점]

1. 역량 평가 (50점)
- 의사소통 능력 (10점)
- 문제 해결 능력 (10점)
- 팀워크/협업 (10점)
- 전문 지식/스킬 (10점)
- 업무 태도 (10점)

2. 성과 평가 (50점)
- 목표 달성률 (30점)
  • 정량 목표 (매출, KPI 등)
  • 정성 목표 (프로젝트 완료 등)
- 업무 품질 (10점)
- 업무 속도/효율성 (10점)

[엑셀 기능]
- 자동 점수 계산
- 등급 자동 분류 (S/A/B/C/D)
- 그래프 자동 생성
```

### Extracted Code (text)

```text
[자동 계산 기능]
- 입사일 입력 → 발생 연차 자동 계산
- 사용 연차 입력 → 잔여 연차 자동 계산
- 미사용 연차 경고 (사용 촉진 대상)

[수식 예시]
발생연차 = IF(근무년수<1, ROUND(근무일수/12, 0), 15 + MIN(근무년수-1, 10))
```

### Extracted Code (text)

```text
[구성]
- 기본급
- 상여금
- 식대
- 교통비
- 4대보험 공제 (자동 계산)
- 소득세 (간이세액표 적용)
- 실수령액 (자동 계산)

[자동화]
→ 파이썬으로 대량 생성 가능 (50명 급여명세서 1분)
```

### Extracted Code (text)

```text
[자가 점검 리스트]

✅ 근로기준법 준수 확인
□ 최저임금 이상 명시
□ 주 52시간 근무 준수
□ 연차휴가 부여 명시
□ 퇴직금 지급 명시

✅ 차별 금지
□ 성별, 나이, 학력 차별 표현 없음
□ 임신, 출산 불이익 없음

✅ 개인정보 보호
□ 주민등록번호 수집 최소화
□ 개인정보 이용 동의 명시

⚠️ 최종 확인
→ 제작한 템플릿을 노무사에게 검토 의뢰 (20-50만원)
→ 또는 고용노동부 무료 상담 활용
→ "본 템플릿은 참고용이며, 실제 사용 전 전문가 검토 권장" 명시
```

### Extracted Code (text)

```text
[Hour 1] 연봉 데이터 20개 수집
- 잡코리아 접속
- 개발자 연봉 정보 10개 복사
- 마케터 연봉 정보 10개 복사
- 엑셀에 정리

[Hour 2] 면접 질문 50개 수집
- 링커리어 "면접 질문 50개" 게시물 검색
- 질문 복사 후 엑셀에 정리
- 직군/카테고리 분류

[Hour 3] HR 문서 다운로드
- 고용노동부 사이트 접속
- 표준 근로계약서 다운로드
- 취업규칙 예시 다운로드
- 폴더 정리
```

### Extracted Code (text)

```text
✅ 합법적 사용:
- 공개된 연봉 정보 수집 (OK)
- 개인 식별 정보 제외
- 상업적 용도 아닌 연구/분석 목적
- 적절한 크롤링 속도 (1-2초 대기)

❌ 위법 가능성:
- 로그인 필요한 정보 무단 수집
- 과도한 트래픽 발생 (서버 공격으로 간주)
- 저작권 있는 콘텐츠 무단 복제

⚖️ 권장사항:
- robots.txt 확인: https://www.jobkorea.co.kr/robots.txt
- 수집 속도 제한 (time.sleep 사용)
- User-Agent 명시
- 상업적 사용 전 법률 자문
```

### Extracted Code (bash)

```bash
# 터미널 또는 CMD에서 실행

# 기본 라이브러리
pip install requests beautifulsoup4 pandas openpyxl lxml

# Selenium (동적 페이지용)
pip install selenium webdriver-manager

# 추가 유틸리티
pip install fake-useragent tqdm
```

### Extracted Code (python)

```python
# setup_folders.py
import os

folders = [
    'data/raw',           # 원본 데이터
    'data/processed',     # 정제된 데이터
    'logs',              # 로그 파일
    'output',            # 최종 결과물
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"✅ {folder} 폴더 생성 완료")
```

### Extracted Code (python)

```python
# jobkorea_scraper_basic.py
"""
잡코리아 연봉 정보 스크래퍼 (기본 버전)
Author: Your Name
Date: 2025-01-10
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from datetime import datetime
from fake_useragent import UserAgent

class JobkoreaSalaryScraper:
    def __init__(self):
        self.base_url = "https://www.jobkorea.co.kr"
        self.salary_url = f"{self.base_url}/salary"
        self.ua = UserAgent()
        self.session = requests.Session()
        self.data = []
        
    def get_headers(self):
        """랜덤 User-Agent 생성"""
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://www.jobkorea.co.kr/'
        }
    
    def scrape_company_salaries(self, max_pages=5):
        """기업별 연봉 정보 수집"""
        print(f"🚀 기업별 연봉 수집 시작... (최대 {max_pages}페이지)")
        
        for page in range(1, max_pages + 1):
            try:
                # URL 구성 (실제 URL 구조에 맞게 수정 필요)
                url = f"{self.salary_url}/company?Page={page}"
                
                print(f"📄 페이지 {page} 수집 중...")
                response = self.session.get(url, headers=self.get_headers())
                
                if response.status_code != 200:
                    print(f"❌ 페이지 로드 실패: {response.status_code}")
                    continue
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # HTML 구조 분석하여 데이터 추출
                # 실제 구조에 맞게 셀렉터 수정 필요
                company_items = soup.select('.company-salary-item')
                
                if not company_items:
                    print("⚠️ 데이터를 찾을 수 없습니다. HTML 구조 확인 필요")
                    # HTML 저장해서 분석
                    with open(f'logs/page_{page}_html.html', 'w', encoding='utf-8') as f:
                        f.write(response.text)
                    print(f"💾 HTML이 logs/page_{page}_html.html에 저장됨")
                
                for item in company_items:
                    try:
                        company_name = item.select_one('.company-name').text.strip()
                        avg_salary = item.select_one('.avg-salary').text.strip()
                        industry = item.select_one('.industry').text.strip()
                        
                        self.data.append({
                            '수집일': datetime.now().strftime('%Y-%m-%d'),
                            '출처': '잡코리아-기업별',
                            '기업명': company_name,
                            '평균연봉': self._parse_salary(avg_salary),
                            '업종': industry,
                            '페이지': page
                        })
                    except Exception as e:
                        print(f"⚠️ 항목 파싱 오류: {e}")
                        continue
                
                print(f"✅ 페이지 {page} 완료: {len(company_items)}개 수집")
                
                # 서버 부하 방지 (1-3초 랜덤 대기)
                time.sleep(random.uniform(1, 3))
                
            except Exception as e:
                print(f"❌ 페이지 {page} 오류: {e}")
                continue
        
        print(f"🎉 총 {len(self.data)}개 데이터 수집 완료!")
        return self.data
    
    def scrape_job_salaries(self, job_categories):
        """직무별 연봉 정보 수집"""
        print(f"🚀 직무별 연봉 수집 시작... ({len(job_categories)}개 직군)")
        
        for job in job_categories:
            try:
                # URL 구성
                url = f"{self.salary_url}/job?jobCd={job['code']}"
                
                print(f"📊 {job['name']} 직군 수집 중...")
                response = self.session.get(url, headers=self.get_headers())
                
                if response.status_code != 200:
                    print(f"❌ 요청 실패: {response.status_code}")
                    continue
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # 경력별 연봉 데이터 추출
                career_levels = soup.select('.career-salary-item')
                
                for item in career_levels:
                    try:
                        career = item.select_one('.career-level').text.strip()
                        min_salary = item.select_one('.min-salary').text.strip()
                        max_salary = item.select_one('.max-salary').text.strip()
                        
                        self.data.append({
                            '수집일': datetime.now().strftime('%Y-%m-%d'),
                            '출처': '잡코리아-직무별',
                            '직군': job['name'],
                            '경력': career,
                            '최소연봉': self._parse_salary(min_salary),
                            '최대연봉': self._parse_salary(max_salary),
                            '평균연봉': (self._parse_salary(min_salary) + self._parse_salary(max_salary)) / 2
                        })
                    except Exception as e:
                        print(f"⚠️ 항목 파싱 오류: {e}")
                        continue
                
                print(f"✅ {job['name']} 완료")
                time.sleep(random.uniform(1, 3))
                
            except Exception as e:
                print(f"❌ {job['name']} 오류: {e}")
                continue
        
        return self.data
    
    def _parse_salary(self, salary_text):
        """연봉 텍스트를 숫자로 변환"""
        try:
            # "5,000만원", "5천만원", "50,000,000원" 등 다양한 형식 처리
            salary_text = salary_text.replace(',', '').replace(' ', '')
            
            if '만원' in salary_text:
                number = float(salary_text.replace('만원', ''))
                return int(number)
            elif '천만원' in salary_text:
                number = float(salary_text.replace('천만원', ''))
                return int(number * 1000)
            elif '원' in salary_text:
                number = float(salary_text.replace('원', ''))
                return int(number / 10000)  # 만원 단위로 변환
            else:
                return int(float(salary_text))
        except:
            return 0
    
    def save_to_excel(self, filename='data/raw/jobkorea_salary_raw.xlsx'):
        """데이터를 엑셀로 저장"""
        if not self.data:
            print("⚠️ 저장할 데이터가 없습니다.")
            return
        
        df = pd.DataFrame(self.data)
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"💾 데이터 저장 완료: {filename}")
        print(f"📊 총 {len(df)}개 행 저장됨")
        
        # 기본 통계 출력
        print("\n=== 수집 통계 ===")
        if '직군' in df.columns:
            print(df['직군'].value_counts())
        if '평균연봉' in df.columns:
            print(f"\n평균: {df['평균연봉'].mean():.0f}만원")
            print(f"최소: {df['평균연봉'].min():.0f}만원")
            print(f"최대: {df['평균연봉'].max():.0f}만원")
        
        return df


# 실행 예시
if __name__ == "__main__":
    # 스크래퍼 초기화
    scraper = JobkoreaSalaryScraper()
    
    # 방법 1: 기업별 연봉 수집
    # scraper.scrape_company_salaries(max_pages=3)
    
    # 방법 2: 직무별 연봉 수집
    job_categories = [
        {'name': '개발', 'code': '1001'},
        {'name': '마케팅', 'code': '2001'},
        {'name': '영업', 'code': '3001'},
        # 실제 잡코리아의 직무 코드로 수정 필요
    ]
    # scraper.scrape_job_salaries(job_categories)
    
    # 데이터 저장
    # scraper.save_to_excel()
    
    print("\n⚠️ 주의: 실제 실행 전 HTML 구조 분석 필요!")
    print("1. 브라우저에서 잡코리아 연봉 페이지 접속")
    print("2. F12 눌러서 개발자도구 오픈")
    print("3. Elements 탭에서 데이터 위치 확인")
    print("4. 셀렉터 수정 후 실행")
```

### Extracted Code (python)

```python
# jobkorea_scraper_selenium.py
"""
잡코리아 연봉 정보 스크래퍼 (Selenium 버전)
동적 페이지 렌더링 지원
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
import time
import random
from datetime import datetime

class JobkoreaSeleniumScraper:
    def __init__(self, headless=True):
        """
        Args:
            headless: True면 브라우저 숨김, False면 브라우저 표시
        """
        self.data = []
        self.driver = self._init_driver(headless)
        
    def _init_driver(self, headless):
        """Selenium 드라이버 초기화"""
        chrome_options = Options()
        
        if headless:
            chrome_options.add_argument('--headless')
        
        # 봇 탐지 우회 설정
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        
        # User-Agent 설정
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        # 자동 ChromeDriver 다운로드
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # 봇 탐지 우회 스크립트
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        print("✅ Selenium 드라이버 초기화 완료")
        return driver
    
    def scrape_salary_data(self, url, max_scroll=3):
        """연봉 페이지 스크래핑"""
        print(f"🌐 페이지 접속: {url}")
        
        try:
            self.driver.get(url)
            time.sleep(2)  # 페이지 로딩 대기
            
            # 무한 스크롤 처리
            for i in range(max_scroll):
                print(f"📜 스크롤 {i+1}/{max_scroll}")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.uniform(1, 2))
            
            # 데이터 추출
            # 예시: 연봉 카드 목록
            salary_cards = self.driver.find_elements(By.CSS_SELECTOR, '.salary-card')
            
            print(f"📊 찾은 항목 수: {len(salary_cards)}")
            
            for card in salary_cards:
                try:
                    # 각 항목에서 데이터 추출
                    company = card.find_element(By.CSS_SELECTOR, '.company-name').text
                    salary = card.find_element(By.CSS_SELECTOR, '.salary-amount').text
                    job_title = card.find_element(By.CSS_SELECTOR, '.job-title').text
                    
                    self.data.append({
                        '수집일': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        '출처': 'Selenium',
                        '기업명': company,
                        '직무': job_title,
                        '연봉': self._parse_salary(salary)
                    })
                    
                except NoSuchElementException as e:
                    print(f"⚠️ 요소 찾기 실패: {e}")
                    continue
            
            print(f"✅ 수집 완료: {len(self.data)}개")
            
        except TimeoutException:
            print("❌ 페이지 로딩 시간 초과")
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
    
    def scrape_job_posting_salaries(self, job_keyword, max_pages=5):
        """채용공고에서 연봉 정보 추출"""
        print(f"🔍 '{job_keyword}' 채용공고 검색 중...")
        
        base_url = "https://www.jobkorea.co.kr/Search/"
        
        for page in range(1, max_pages + 1):
            try:
                # 검색 URL
                search_url = f"{base_url}?stext={job_keyword}&Page={page}"
                self.driver.get(search_url)
                
                # 페이지 로딩 대기
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.list-default'))
                )
                
                # 채용공고 목록
                job_listings = self.driver.find_elements(By.CSS_SELECTOR, '.list-default .list-post')
                
                print(f"📄 페이지 {page}: {len(job_listings)}개 공고 발견")
                
                for listing in job_listings:
                    try:
                        # 공고 클릭
                        listing.click()
                        time.sleep(1)
                        
                        # 새 탭으로 전환
                        self.driver.switch_to.window(self.driver.window_handles[-1])
                        
                        # 연봉 정보 추출
                        try:
                            salary_element = WebDriverWait(self.driver, 5).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, '.salary-info'))
                            )
                            salary_text = salary_element.text
                            
                            # 기업명, 직무명
                            company = self.driver.find_element(By.CSS_SELECTOR, '.company-name').text
                            job_title = self.driver.find_element(By.CSS_SELECTOR, '.job-title').text
                            
                            # "회사 내규에 따름" 같은 경우 스킵
                            if "내규" not in salary_text and "협의" not in salary_text:
                                self.data.append({
                                    '수집일': datetime.now().strftime('%Y-%m-%d'),
                                    '출처': '채용공고',
                                    '기업명': company,
                                    '직무': job_title,
                                    '연봉정보': salary_text,
                                    '최소연봉': self._extract_min_salary(salary_text),
                                    '최대연봉': self._extract_max_salary(salary_text),
                                })
                        except TimeoutException:
                            pass  # 연봉 정보 없음
                        
                        # 탭 닫고 원래 탭으로
                        self.driver.close()
                        self.driver.switch_to.window(self.driver.window_handles[0])
                        
                        time.sleep(random.uniform(0.5, 1))
                        
                    except Exception as e:
                        print(f"⚠️ 공고 처리 오류: {e}")
                        # 탭 정리
                        if len(self.driver.window_handles) > 1:
                            self.driver.switch_to.window(self.driver.window_handles[-1])
                            self.driver.close()
                            self.driver.switch_to.window(self.driver.window_handles[0])
                        continue
                
                print(f"✅ 페이지 {page} 완료")
                time.sleep(random.uniform(2, 4))
                
            except Exception as e:
                print(f"❌ 페이지 {page} 오류: {e}")
                continue
        
        print(f"🎉 총 {len(self.data)}개 데이터 수집 완료")
    
    def _parse_salary(self, salary_text):
        """연봉 텍스트 파싱"""
        import re
        
        # 숫자만 추출
        numbers = re.findall(r'[\d,]+', salary_text)
        if numbers:
            # 쉼표 제거하고 첫 번째 숫자 반환
            return int(numbers[0].replace(',', ''))
        return 0
    
    def _extract_min_salary(self, text):
        """최소 연봉 추출"""
        import re
        numbers = re.findall(r'(\d+,?\d*)', text)
        if len(numbers) >= 1:
            return int(numbers[0].replace(',', ''))
        return 0
    
    def _extract_max_salary(self, text):
        """최대 연봉 추출"""
        import re
        numbers = re.findall(r'(\d+,?\d*)', text)
        if len(numbers) >= 2:
            return int(numbers[1].replace(',', ''))
        elif len(numbers) == 1:
            return int(numbers[0].replace(',', ''))
        return 0
    
    def save_to_excel(self, filename='data/raw/jobkorea_selenium.xlsx'):
        """데이터 저장"""
        if not self.data:
            print("⚠️ 저장할 데이터가 없습니다.")
            return
        
        df = pd.DataFrame(self.data)
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"💾 저장 완료: {filename}")
        print(f"📊 총 {len(df)}개 행")
        return df
    
    def close(self):
        """드라이버 종료"""
        if self.driver:
            self.driver.quit()
            print("✅ 드라이버 종료")


# 실행 예시
if __name__ == "__main__":
    # 스크래퍼 초기화 (headless=False로 하면 브라우저 보임)
    scraper = JobkoreaSeleniumScraper(headless=False)
    
    try:
        # 방법 1: 특정 URL 스크래핑
        # scraper.scrape_salary_data("https://www.jobkorea.co.kr/salary/")
        
        # 방법 2: 채용공고 검색
        scraper.scrape_job_posting_salaries("백엔드 개발자", max_pages=2)
        
        # 데이터 저장
        scraper.save_to_excel()
        
    finally:
        # 드라이버 종료
        scraper.close()
```

### Extracted Code (python)

```python
# analyze_html.py
"""
잡코리아 HTML 구조 분석 도구
실제 셀렉터를 찾기 위한 헬퍼 스크립트
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def analyze_jobkorea_page(url):
    """페이지 HTML 구조 분석"""
    print(f"🔍 페이지 분석 중: {url}")
    
    # 드라이버 초기화
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get(url)
        time.sleep(3)  # 페이지 완전 로딩 대기
        
        # HTML 소스 가져오기
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        # HTML 저장
        with open('logs/jobkorea_page_source.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
        print("💾 HTML 저장: logs/jobkorea_page_source.html")
        
        # 주요 클래스 찾기
        print("\n=== 발견된 주요 클래스 ===")
        
        # 연봉 관련 클래스
        salary_classes = soup.find_all(class_=lambda x: x and ('salary' in x.lower() or 'pay' in x.lower()))
        print(f"연봉 관련 클래스: {len(salary_classes)}개")
        for item in salary_classes[:5]:
            print(f"  - {item.get('class')}: {item.text[:50]}...")
        
        # 기업명 관련 클래스
        company_classes = soup.find_all(class_=lambda x: x and 'company' in x.lower())
        print(f"\n기업명 관련 클래스: {len(company_classes)}개")
        for item in company_classes[:5]:
            print(f"  - {item.get('class')}: {item.text[:50]}...")
        
        # 직무 관련 클래스
        job_classes = soup.find_all(class_=lambda x: x and 'job' in x.lower())
        print(f"\n직무 관련 클래스: {len(job_classes)}개")
        for item in job_classes[:5]:
            print(f"  - {item.get('class')}: {item.text[:50]}...")
        
        # 스크린샷 저장
        driver.save_screenshot('logs/jobkorea_screenshot.png')
        print("\n📸 스크린샷 저장: logs/jobkorea_screenshot.png")
        
    finally:
        driver.quit()

# 실행
if __name__ == "__main__":
    # 분석할 URL
    urls = [
        "https://www.jobkorea.co.kr/salary/",
        "https://www.jobkorea.co.kr/salary/company",
        "https://www.jobkorea.co.kr/salary/job",
    ]
    
    for url in urls:
        analyze_jobkorea_page(url)
        print("\n" + "="*50 + "\n")
```

### Extracted Code (text)

```text
[브라우저에서 직접 확인]

1. 잡코리아 연봉 페이지 접속
   https://www.jobkorea.co.kr/salary/

2. F12 눌러서 개발자도구 오픈

3. Elements 탭에서 연봉 정보가 있는 부분에 마우스 올리기
   → 해당 HTML이 하이라이트됨

4. 우클릭 → Copy → Copy selector
   → 예: #content > div > div.list-salary > div:nth-child(1)

5. 코드에 적용:
   soup.select('#content > div > div.list-salary > div')
```

### Extracted Code (python)

```python
# data_processing.py
"""
수집된 데이터 정제 및 통계 분석
"""

import pandas as pd
import numpy as np
from datetime import datetime

class SalaryDataProcessor:
    def __init__(self, input_file):
        self.df = pd.read_excel(input_file)
        print(f"📂 데이터 로드: {input_file}")
        print(f"📊 총 {len(self.df)}개 행, {len(self.df.columns)}개 열")
    
    def clean_data(self):
        """데이터 정제"""
        print("\n🧹 데이터 정제 시작...")
        
        initial_count = len(self.df)
        
        # 1. 중복 제거
        self.df = self.df.drop_duplicates()
        print(f"✅ 중복 제거: {initial_count - len(self.df)}개 삭제")
        
        # 2. 결측치 처리
        print(f"⚠️ 결측치: {self.df.isnull().sum().sum()}개")
        self.df = self.df.dropna(subset=['평균연봉'])  # 연봉 정보 없는 행 삭제
        
        # 3. 이상치 제거
        if '평균연봉' in self.df.columns:
            Q1 = self.df['평균연봉'].quantile(0.25)
            Q3 = self.df['평균연봉'].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            
            outliers = self.df[(self.df['평균연봉'] < lower) | (self.df['평균연봉'] > upper)]
            print(f"⚠️ 이상치: {len(outliers)}개 (범위: {lower:.0f} ~ {upper:.0f}만원)")
            
            self.df = self.df[(self.df['평균연봉'] >= lower) & (self.df['평균연봉'] <= upper)]
        
        print(f"✅ 정제 완료: 최종 {len(self.df)}개 행")
        
        return self.df
    
    def add_statistics(self):
        """통계 컬럼 추가"""
        print("\n📈 통계 컬럼 추가...")
        
        if '직군' in self.df.columns and '평균연봉' in self.df.columns:
            # 직군별 평균 연봉
            job_avg = self.df.groupby('직군')['평균연봉'].transform('mean')
            self.df['직군_평균연봉'] = job_avg
            
            # 편차
            self.df['평균대비_차이'] = self.df['평균연봉'] - self.df['직군_평균연봉']
            self.df['평균대비_비율'] = (self.df['평균연봉'] / self.df['직군_평균연봉'] * 100).round(1)
            
            print("✅ 통계 컬럼 추가 완료")
        
        return self.df
    
    def generate_summary(self):
        """요약 통계 생성"""
        print("\n📊 요약 통계 생성...")
        
        summary = {}
        
        # 전체 통계
        if '평균연봉' in self.df.columns:
            summary['전체'] = {
                '평균': self.df['평균연봉'].mean(),
                '중위값': self.df['평균연봉'].median(),
                '최소': self.df['평균연봉'].min(),
                '최대': self.df['평균연봉'].max(),
                '표준편차': self.df['평균연봉'].std(),
                '개수': len(self.df)
            }
        
        # 직군별 통계
        if '직군' in self.df.columns:
            summary['직군별'] = self.df.groupby('직군')['평균연봉'].agg([
                'count', 'mean', 'median', 'min', 'max', 'std'
            ]).round(0)
        
        # 경력별 통계
        if '경력' in self.df.columns:
            summary['경력별'] = self.df.groupby('경력')['평균연봉'].agg([
                'count', 'mean', 'median', 'min', 'max'
            ]).round(0)
        
        return summary
    
    def save_processed_data(self, output_file='data/processed/salary_data_clean.xlsx'):
        """정제된 데이터 저장"""
        self.df.to_excel(output_file, index=False)
        print(f"\n💾 저장 완료: {output_file}")
        
        # 요약 통계도 저장
        summary_file = output_file.replace('.xlsx', '_summary.xlsx')
        
        with pd.ExcelWriter(summary_file, engine='openpyxl') as writer:
            # 전체 데이터
            self.df.to_excel(writer, sheet_name='전체데이터', index=False)
            
            # 직군별 요약
            if '직군' in self.df.columns:
                pivot_job = self.df.groupby('직군')['평균연봉'].agg(['mean', 'median', 'count']).round(0)
                pivot_job.to_excel(writer, sheet_name='직군별요약')
            
            # 경력별 요약
            if '경력' in self.df.columns:
                pivot_career = self.df.groupby('경력')['평균연봉'].agg(['mean', 'median', 'count']).round(0)
                pivot_career.to_excel(writer, sheet_name='경력별요약')
        
        print(f"💾 요약 저장: {summary_file}")
        
        return self.df

# 실행 예시
if __name__ == "__main__":
    processor = SalaryDataProcessor('data/raw/jobkorea_salary_raw.xlsx')
    
    # 데이터 정제
    df_clean = processor.clean_data()
    
    # 통계 추가
    df_clean = processor.add_statistics()
    
    # 요약 생성
    summary = processor.generate_summary()
    print("\n=== 전체 통계 ===")
    print(summary['전체'])
    
    # 저장
    processor.save_processed_data()
```

### Extracted Code (python)

```python
# run_all.py
"""
전체 프로세스 자동 실행
"""

import os
from datetime import datetime
from jobkorea_scraper_selenium import JobkoreaSeleniumScraper
from data_processing import SalaryDataProcessor

def main():
    print("="*60)
    print("🤖 잡코리아 연봉 데이터 수집 자동화")
    print(f"⏰ 시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    # 1단계: 데이터 수집
    print("\n[1/3] 데이터 수집 시작...")
    scraper = JobkoreaSeleniumScraper(headless=True)
    
    try:
        # 채용공고 검색
        keywords = ['백엔드 개발자', '프론트엔드 개발자', '마케터', '영업']
        
        for keyword in keywords:
            print(f"\n🔍 검색어: {keyword}")
            scraper.scrape_job_posting_salaries(keyword, max_pages=3)
        
        # 데이터 저장
        raw_file = f'data/raw/jobkorea_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
        scraper.save_to_excel(raw_file)
        
    finally:
        scraper.close()
    
    # 2단계: 데이터 정제
    print("\n[2/3] 데이터 정제 시작...")
    processor = SalaryDataProcessor(raw_file)
    df_clean = processor.clean_data()
    df_clean = processor.add_statistics()
    
    # 3단계: 저장 및 요약
    print("\n[3/3] 결과 저장 및 요약...")
    final_file = processor.save_processed_data()
    
    summary = processor.generate_summary()
    
    print("\n" + "="*60)
    print("✅ 전체 프로세스 완료!")
    print(f"⏰ 종료 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📊 최종 데이터: {len(df_clean)}개")
    print("="*60)
    
    # 요약 출력
    if '전체' in summary:
        print("\n=== 수집 요약 ===")
        for key, value in summary['전체'].items():
            if isinstance(value, float):
                print(f"{key}: {value:.0f}")
            else:
                print(f"{key}: {value}")

if __name__ == "__main__":
    main()
```

### Extracted Code (python)

```python
# config.py
"""
설정값 관리
"""

# 스크래핑 설정
SCRAPING_CONFIG = {
    'max_pages': 5,
    'delay_min': 1,
    'delay_max': 3,
    'timeout': 10,
    'retry_count': 3,
}

# URL 설정
URLS = {
    'base': 'https://www.jobkorea.co.kr',
    'salary': 'https://www.jobkorea.co.kr/salary',
    'search': 'https://www.jobkorea.co.kr/Search',
}

# 직군 코드 (실제 코드로 수정 필요)
JOB_CATEGORIES = [
    {'name': '개발', 'code': 'dev', 'keywords': ['백엔드', '프론트엔드', '풀스택', '데이터']},
    {'name': '마케팅', 'code': 'mkt', 'keywords': ['디지털마케팅', '퍼포먼스', '브랜드']},
    {'name': '영업', 'code': 'sales', 'keywords': ['기업영업', '영업관리', 'B2B']},
    {'name': '디자인', 'code': 'design', 'keywords': ['UXUI', '그래픽', '제품']},
    {'name': 'HR', 'code': 'hr', 'keywords': ['인사', '채용', 'HRD']},
]

# 파일 경로
PATHS = {
    'raw_data': 'data/raw',
    'processed_data': 'data/processed',
    'output': 'output',
    'logs': 'logs',
}

# 엑셀 설정
EXCEL_CONFIG = {
    'engine': 'openpyxl',
    'date_format': '%Y-%m-%d',
    'number_format': '#,##0',
}
```

### Extracted Code (txt)

```txt
# requirements.txt
# pip install -r requirements.txt

requests==2.31.0
beautifulsoup4==4.12.2
pandas==2.1.4
openpyxl==3.1.2
lxml==4.9.3
selenium==4.16.0
webdriver-manager==4.0.1
fake-useragent==1.4.0
tqdm==4.66.1
```

### Extracted Code (bash)

```bash
# 1. 필요 라이브러리 설치
pip install -r requirements.txt

# 2. 폴더 구조 생성
python setup_folders.py

# 3. HTML 구조 분석 (먼저 실행 필수!)
python analyze_html.py

# 4. 실제 스크래핑 실행
python run_all.py

# 5. 결과 확인
# data/processed/ 폴더에서 엑셀 파일 확인
```

### Extracted Code (python)

```python
# custom_scraper.py
from jobkorea_scraper_selenium import JobkoreaSeleniumScraper

# 1. 스크래퍼 초기화 (브라우저 보이게)
scraper = JobkoreaSeleniumScraper(headless=False)

# 2. 원하는 검색어로 수집
scraper.scrape_job_posting_salaries("백엔드 개발자", max_pages=10)

# 3. 저장
scraper.save_to_excel('custom_output.xlsx')

# 4. 종료
scraper.close()
```

### Extracted Code (python)

```python
# 해결: 수동 설치
from selenium import webdriver

driver_path = "C:/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
```

### Extracted Code (python)

```python
# 해결: 더 많은 우회 설정
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
```

### Extracted Code (python)

```python
# 해결: HTML 저장해서 분석
with open('debug.html', 'w', encoding='utf-8') as f:
    f.write(driver.page_source)
# → debug.html 열어서 실제 클래스명 확인
```
