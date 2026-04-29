"""
이번 주차 주간보고 생성
"""
from pathlib import Path
from datetime import datetime
import json

# 현재 주차 계산
def get_current_week():
    now = datetime.now()
    first_day = datetime(now.year, 1, 1)
    day_of_year = now.timetuple().tm_yday
    week = (day_of_year + first_day.weekday()) // 7 + 1
    return f"W{week}, {now.month}월 {((now.day - 1) // 7) + 1}주차"

# manifest.json 에서 최근 활동 읽기
def get_recent_activities(manifest_path: Path, limit: int = 10):
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 최근 변환된 문서들
    recent = []
    for filepath, entry in manifest.items():
        converted = entry.get('converted_at', '')
        category = entry.get('category', 'Uncategorized')
        tags = entry.get('tags', [])

        # 최근 7 일 이내
        if converted and converted[:10] >= '2026-04-08':
            recent.append({
                'path': filepath,
                'category': category,
                'tags': tags,
                'date': converted[:10]
            })

    # 날짜순 정렬
    recent.sort(key=lambda x: x['date'], reverse=True)
    return recent[:limit]

# 보고 생성
def generate_report():
    BASE_DIR = Path(__file__).parent.parent
    manifest_path = BASE_DIR / 'manifest.json'

    week = get_current_week()
    activities = get_recent_activities(manifest_path)

    # 카테고리별 그룹핑
    by_category = {}
    for item in activities:
        cat = item['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(item)

    report = f"""# 생산기술 HR 실 주간업무 보고 ({week})

**보고일자:** {datetime.now().strftime('%Y-%m-%d')}
**작성:** HR 실

---

## 1. 금주 완료 사항

"""

    # 카테고리별 정리
    for category, items in sorted(by_category.items()):
        report += f"### [{category}]\n\n"
        for item in items:
            filename = Path(item['path']).name
            tags = ', '.join(item['tags']) if item['tags'] else ''
            report += f"- {filename}\n"
            if tags:
                report += f"  - 태그: {tags}\n"
        report += "\n"

    report += f"""---

## 2. 특이사항

- 특이사항 없음

---

## 3. 차주 계획 사항

- 금주 업무 연속 진행
- 추가 지시사항 반영

---

*본 보고는 Zavis_Brain Harness 가 자동 생성했습니다.*
"""

    # 저장
    output_dir = BASE_DIR / 'harness' / 'output'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f'weekly_report_{datetime.now().strftime("%Y%m%d")}.md'

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"[REPORT] 주간보고 생성 완료: {output_path}")
    print(f"\n=== 생성된 보고 ===\n")
    print(report)

    return output_path

if __name__ == "__main__":
    generate_report()
