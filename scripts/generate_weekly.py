"""
주간 변화 다이제스트 생성기.

왜 필요한가:
Git과 manifest는 "파일이 바뀌었다"는 사실을 알려주지만, 사용자는
"그래서 무엇이 중요하게 바뀌었나"를 알고 싶어 한다. 이 스크립트는
최근 변경을 사람이 읽을 수 있는 주간 브리핑으로 모은다.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


def run_git(args: list[str]) -> str:
    """Git 명령을 실행하고 실패하면 빈 문자열을 반환한다."""
    try:
        result = subprocess.run(
            ["git", "-c", "core.quotePath=false", *args],
            cwd=BASE_DIR,
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def week_range(today: date) -> tuple[date, date, str]:
    """ISO 주차 기준 월요일~일요일 범위를 계산한다."""
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=6)
    iso = today.isocalendar()
    return start, end, f"{iso.year}-W{iso.week:02d}"


def git_changed_files(since: date, until: date) -> list[dict[str, str]]:
    """주간 Git 변경 파일을 수집한다."""
    output = run_git([
        "log",
        "--name-status",
        "--pretty=format:commit %h %ad %s",
        "--date=short",
        f"--since={since.isoformat()} 00:00:00",
        f"--until={until.isoformat()} 23:59:59",
    ])
    if not output:
        return []

    changes: list[dict[str, str]] = []
    current_commit = ""
    for line in output.splitlines():
        if line.startswith("commit "):
            current_commit = line
            continue
        if not line.strip() or "\t" not in line:
            continue
        parts = line.split("\t")
        status = parts[0]
        # Rename/Copy는 old path와 new path가 함께 나오므로 최종 경로를 사용한다.
        path = parts[-1]
        changes.append({
            "status": status,
            "path": path,
            "commit": current_commit,
        })
    return changes


def git_recent_commits(limit: int = 8) -> list[str]:
    output = run_git(["log", "--oneline", f"-{limit}"])
    return output.splitlines() if output else []


def untracked_files(limit: int = 20) -> list[str]:
    output = run_git(["status", "--short"])
    if not output:
        return []
    return [line for line in output.splitlines() if line.startswith("?? ")][:limit]


def manifest_recent(since: date, until: date, limit: int = 20) -> list[dict[str, object]]:
    manifest_path = BASE_DIR / "manifest.json"
    if not manifest_path.exists():
        return []

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    recent = []
    for filepath, entry in manifest.items():
        converted = entry.get("converted_at", "")
        if not converted:
            continue
        try:
            converted_date = datetime.fromisoformat(converted).date()
        except ValueError:
            continue
        if since <= converted_date <= until:
            recent.append({
                "path": filepath,
                "category": entry.get("category", "Uncategorized"),
                "tags": entry.get("tags", []),
                "date": converted_date.isoformat(),
            })

    recent.sort(key=lambda item: item["date"], reverse=True)
    return recent[:limit]


def summarize_changes(changes: list[dict[str, str]]) -> dict[str, object]:
    by_area = Counter()
    by_status = Counter()
    examples = defaultdict(list)

    for change in changes:
        path = change["path"]
        area = path.split("/", 1)[0] if "/" in path else "root"
        by_area[area] += 1
        by_status[change["status"]] += 1
        if len(examples[area]) < 5:
            examples[area].append(path)

    return {
        "by_area": by_area,
        "by_status": by_status,
        "examples": examples,
    }


def infer_insights(changes: list[dict[str, str]], recent_manifest: list[dict[str, object]]) -> list[str]:
    insights = []
    changed_paths = [change["path"] for change in changes]

    if any(path.startswith("_ops/") or path.startswith("scripts/") for path in changed_paths):
        insights.append("운영 체계 변경이 있었다. 다음 사용 시 status와 change-log를 먼저 확인해야 한다.")
    if any(path.startswith("wiki/") for path in changed_paths):
        insights.append("정리된 지식 위키가 갱신되었다. 관련 개념의 연결과 중복 여부를 확인할 필요가 있다.")
    if any(path.startswith("projects/") for path in changed_paths):
        insights.append("프로젝트 상태나 근거 문서가 갱신되었다. Compiled Truth와 Timeline의 일관성을 확인해야 한다.")
    if recent_manifest:
        insights.append("원자료 또는 변환 산출물이 새로 감지되었다. 지식으로 승격할 항목과 보관만 할 항목을 구분해야 한다.")
    if not insights:
        insights.append("이번 주 Git 기준 의미 있는 변경이 적다. inbox와 미추적 파일을 확인해 누락된 변화가 있는지 점검한다.")

    return insights


def render_digest(target_date: date) -> tuple[Path, str]:
    start, end, week_id = week_range(target_date)
    changes = git_changed_files(start, end)
    recent_manifest = manifest_recent(start, end)
    summary = summarize_changes(changes)
    commits = git_recent_commits()
    untracked = untracked_files()
    insights = infer_insights(changes, recent_manifest)

    lines = [
        "---",
        f'title: "{week_id} Weekly Change Digest"',
        f"created: {date.today().isoformat()}",
        f"week: {week_id}",
        "type: digest",
        "status: draft",
        "tags: [weekly, digest, change-briefing]",
        "---",
        "",
        f"# {week_id} 주간 변화 다이제스트",
        "",
        f"> 범위: {start.isoformat()} ~ {end.isoformat()}",
        "",
        "## 1. 이번 주 한 줄 요약",
        "",
        f"- Git 기준 변경 파일 {len(changes)}건, manifest 기준 신규/갱신 자료 {len(recent_manifest)}건을 확인했다.",
        "",
        "## 2. 영역별 변경",
        "",
    ]

    if summary["by_area"]:
        for area, count in summary["by_area"].most_common():
            lines.append(f"### {area} ({count}건)")
            for path in summary["examples"][area]:
                lines.append(f"- `{path}`")
            lines.append("")
    else:
        lines.append("- Git 기록 기준 변경 파일 없음")
        lines.append("")

    lines.extend([
        "## 3. 핵심 해석",
        "",
    ])
    for item in insights:
        lines.append(f"- {item}")
    lines.append("")

    lines.extend([
        "## 4. 최근 커밋",
        "",
    ])
    if commits:
        lines.extend([f"- `{commit}`" for commit in commits])
    else:
        lines.append("- Git 커밋 기록 없음")
    lines.append("")

    lines.extend([
        "## 5. 미추적 파일",
        "",
    ])
    if untracked:
        lines.extend([f"- `{item}`" for item in untracked])
    else:
        lines.append("- 없음")
    lines.append("")

    lines.extend([
        "## 6. manifest 기준 최근 자료",
        "",
    ])
    if recent_manifest:
        for item in recent_manifest[:10]:
            tags = ", ".join(item.get("tags", []))
            tag_text = f" / {tags}" if tags else ""
            lines.append(f"- `{Path(str(item['path'])).name}` ({item['category']}{tag_text})")
    else:
        lines.append("- 해당 주차 신규/갱신 자료 없음")
    lines.append("")

    lines.extend([
        "## 7. 다음 확인",
        "",
        "- `_ops/change-log.md`에 이번 주 핵심 변화가 기록되었는지 확인한다.",
        "- `inbox/`와 미추적 파일 중 지식으로 승격할 항목이 있는지 확인한다.",
        "- 프로젝트 README의 Compiled Truth가 실제 최신 상태와 맞는지 확인한다.",
        "",
        "*Generated by CSP-Brain weekly change digest*",
    ])

    output_dir = BASE_DIR / "outputs" / "weekly"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{week_id}.md"
    content = "\n".join(lines) + "\n"
    return output_path, content


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate weekly change digest.")
    parser.add_argument(
        "--date",
        help="기준일 YYYY-MM-DD. 생략하면 오늘 날짜를 사용한다.",
    )
    args = parser.parse_args()

    target_date = date.today()
    if args.date:
        target_date = datetime.strptime(args.date, "%Y-%m-%d").date()

    output_path, content = render_digest(target_date)
    output_path.write_text(content, encoding="utf-8")
    print(f"[DIGEST] 생성 완료: {output_path}")


if __name__ == "__main__":
    main()
