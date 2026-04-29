"""
manifest.json 스키마 정의 (v2.0)
- 기존: hash, mtime, converted_at, priority
- 추가: category, tags, csp_insight, md_path, word_count, last_indexed
"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ManifestEntry(BaseModel):
    """단일 문서 메타데이터 엔트리"""
    hash: str = Field(..., description="SHA256 파일 해시")
    mtime: float = Field(..., description="최종 수정 시간 (Unix timestamp)")
    converted_at: str = Field(..., description="마크다운 변환 일시")
    priority: int = Field(default=90, description="우선순위 (0-100)")

    # ▼▼▼ Phase 1 확장 필드 ▼▼▼
    category: Optional[str] = Field(default=None, description="자동 분류 카테고리")
    tags: Optional[List[str]] = Field(default=None, description="자동 추출 태그")
    csp_insight: Optional[str] = Field(default=None, description="CSP 인사이트 요약")
    md_path: Optional[str] = Field(default=None, description="변환된 마크다운 파일 경로")
    word_count: Optional[int] = Field(default=None, description="마크다운 단어 수")
    last_indexed: Optional[str] = Field(default=None, description="마지막 인덱싱 일시")

    class Config:
        extra = "allow"  # 미래 확장을 위해 허용


# ManifestV2 는 Pydantic v2 에서 RootModel 로 변경되었으나,
# manifest.json 은 단순 dict 이므로 스키마 검증은 선택적으로 사용


# 카테고리 자동 분류를 위한 매핑 규칙
CATEGORY_RULES = {
    "Strategy_Planning": ["보고", "계획", "전략", "소개", "개편", "역량"],
    "Meeting_Notes": ["회의록", "커미티", "위원"],
    "Weekly_Report": ["주간", "W48", "W50", "주차"],
    "HR_Data": ["인원", "명단", "현황", "취득", "교육"],
    "Pulse_EX": ["Pulse", "EX", "경험", "모니터링", "임원"],
    "AX_DX": ["AX", "DX", "Domain", "인증", "아카데미"],
    "Reference": ["Guidebook", "PDF", "Taxonomy"],
}


def auto_categorize(filepath: str, content: str = "") -> str:
    """파일 경로와 내용으로 자동 카테고리 분류"""
    combined = f"{filepath} {content}".lower()

    scores = {}
    for category, keywords in CATEGORY_RULES.items():
        score = sum(1 for kw in keywords if kw.lower() in combined)
        scores[category] = score

    if max(scores.values()) == 0:
        return "Uncategorized"

    return max(scores, key=scores.get)


def auto_extract_tags(filepath: str, content: str = "") -> List[str]:
    """파일에서 자동 태그 추출"""
    tags = []

    # 파일 확장자 기반 태그
    if ".pptx" in filepath:
        tags.append("slide")
    elif ".xlsx" in filepath:
        tags.append("excel")
    elif ".pdf" in filepath:
        tags.append("pdf")
    elif ".docx" in filepath:
        tags.append("word")

    # 날짜 패턴 추출 (YYMMDD 또는 YYYYMMDD)
    import re
    date_patterns = re.findall(r'\d{6,8}', filepath)
    if date_patterns:
        tags.append(f"date_{date_patterns[-1]}")

    # 팀/조직명 추출
    team_patterns = [
        ("EXG", "EXG 팀"),
        ("HR", "HR"),
        ("PRI", "PRI"),
        ("AX", "AX"),
        ("DX", "DX"),
    ]
    for pattern, tag in team_patterns:
        if pattern in filepath.upper():
            tags.append(tag)

    return list(set(tags))[:10]  # 최대 10 개 태그
