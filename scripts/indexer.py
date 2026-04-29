"""
인덱스 생성기 (Index Generator)
- manifest.json 을 읽어서 역색인 (inverted index) 생성
- 카테고리별, 태그별 문서 목록 생성
- 검색 성능 향상을 위한 프리컴퓨트
"""
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict


def build_index(manifest_path: str, output_path: str):
    """manifest.json 으로 역색인 생성"""

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 역색인 구조
    index = {
        "generated_at": datetime.now().isoformat(),
        "total_documents": len(manifest),
        "by_category": defaultdict(list),
        "by_tag": defaultdict(list),
        "by_month": defaultdict(list),
        "recent_documents": [],
    }

    # 문서 처리
    for filepath, entry in manifest.items():
        # 카테고리 인덱스
        category = entry.get('category', 'Uncategorized')
        index["by_category"][category].append({
            "path": filepath,
            "md_path": entry.get('md_path'),
            "priority": entry.get('priority', 90),
        })

        # 태그 인덱스
        tags = entry.get('tags', [])
        for tag in tags:
            index["by_tag"][tag].append({
                "path": filepath,
                "md_path": entry.get('md_path'),
            })

        # 월별 인덱스 (converted_at 기준)
        converted = entry.get('converted_at', '')
        if converted:
            month = converted[:7]  # "2026-04"
            index["by_month"][month].append({
                "path": filepath,
                "md_path": entry.get('md_path'),
            })

        # 최근 문서 (최대 20 개)
        index["recent_documents"].append({
            "path": filepath,
            "md_path": entry.get('md_path'),
            "category": category,
            "tags": tags,
            "converted_at": converted,
        })

    # 최근 문서 정렬 (최신순)
    index["recent_documents"].sort(
        key=lambda x: x.get('converted_at', ''),
        reverse=True
    )
    index["recent_documents"] = index["recent_documents"][:20]

    # defaultdict 를 일반 dict 로 변환 (JSON 직렬화 위해)
    index["by_category"] = dict(index["by_category"])
    index["by_tag"] = dict(index["by_tag"])
    index["by_month"] = dict(index["by_month"])

    # 인덱스 저장
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"[INDEX] 생성 완료: {output_path}")
    print(f"  - 총 문서: {index['total_documents']}개")
    print(f"  - 카테고리: {len(index['by_category'])}개")
    print(f"  - 태그: {len(index['by_tag'])}개")

    return index


def generate_summary(index: dict) -> str:
    """인덱스 요약 마크다운 생성"""

    md = ["# 📊 Zavis_Brain 인덱스 요약", ""]
    md.append(f"> **생성일시:** {index['generated_at']}")
    md.append(f"> **총 문서:** {index['total_documents']}개")
    md.append("")

    # 카테고리별 요약
    md.append("## 📁 카테고리별 문서")
    md.append("")
    md.append("| 카테고리 | 문서 수 |")
    md.append("|----------|--------|")
    for cat, docs in sorted(index['by_category'].items(), key=lambda x: -len(x[1])):
        md.append(f"| {cat} | {len(docs)} |")
    md.append("")

    # 태그별 요약
    md.append("## 🏷️ 태그별 문서")
    md.append("")
    md.append("| 태그 | 문서 수 |")
    md.append("|------|--------|")
    for tag, docs in sorted(index['by_tag'].items(), key=lambda x: -len(x[1])):
        md.append(f"| {tag} | {len(docs)} |")
    md.append("")

    # 월별 요약
    md.append("## 📅 월별 문서")
    md.append("")
    md.append("| 월 | 문서 수 |")
    md.append("|----|--------|")
    for month, docs in sorted(index['by_month'].items(), reverse=True):
        md.append(f"| {month} | {len(docs)} |")
    md.append("")

    # 최근 문서
    md.append("## 🕐 최근 추가된 문서")
    md.append("")
    for doc in index['recent_documents'][:10]:
        cat = doc.get('category', 'Uncategorized')
        tags = ', '.join(doc.get('tags', []))
        md.append(f"- **{Path(doc['path']).name}** ({cat}) - {doc['converted_at'][:10]}")
        if tags:
            md.append(f"  - 태그: {tags}")
    md.append("")

    return "\n".join(md)


if __name__ == "__main__":
    # 경로를 동적으로 계산 (인코딩 문제 회피)
    BASE_DIR = Path(__file__).parent.parent
    MANIFEST_PATH = BASE_DIR / "manifest.json"
    INDEX_PATH = BASE_DIR / "harness" / "index.json"
    SUMMARY_PATH = BASE_DIR / "harness" / "INDEX_SUMMARY.md"

    # 인덱스 생성
    index = build_index(str(MANIFEST_PATH), str(INDEX_PATH))

    # 요약 마크다운 생성
    summary = generate_summary(index)
    with open(SUMMARY_PATH, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"[SUMMARY] 생성 완료: {SUMMARY_PATH}")
