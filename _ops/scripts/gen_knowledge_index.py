#!/usr/bin/env python3
"""지식 인덱스 데이터 생성기 (_data/knowledge.json).

Jekyll 발행 전에 실행한다. github-pages Jekyll 에는 git 수정시각을 읽는
플러그인이 없고 발행 문서의 ~75% 가 날짜 프론트매터를 갖고 있지 않으므로,
진짜 '최신 수정순'은 git 의 마지막 커밋 시각으로만 신뢰성 있게 잡을 수 있다.

git log 한 번을 훑어 파일별 마지막 커밋 ISO 날짜를 구하고, 발행 대상 지식
문서를 최신순으로 정렬해 _data/knowledge.json 으로 떨군다. knowledge.html 은
이 데이터를 폴더별로 묶어 렌더링한다.

전제: 워크플로 checkout 이 fetch-depth: 0 (전체 히스토리) 이어야 파일별
마지막 커밋 시각이 정확하다.
"""
import subprocess
import json
import os
import re
import fnmatch

# 발행 대상 지식 폴더 (knowledge.html / _config.yml 과 일치시킬 것)
DIRS = ["wiki", "concepts", "projects", "outputs", "people",
        "decisions", "weekly", "research"]
EXCLUDE_GLOBS = ["concepts/extracted-*.md"]
EXCLUDE_FILES = {"outputs/weekly/2026-W18.md"}


def last_commit_dates():
    """파일별 마지막 커밋 ISO 날짜를 git log 한 번으로 수집."""
    out = subprocess.run(
        ["git", "log", "--name-only", "--format=@%cI", "--", *DIRS],
        capture_output=True, text=True,
    ).stdout
    mtime = {}
    cur = ""
    for line in out.splitlines():
        if line.startswith("@"):
            cur = line[1:]
        elif line.strip():
            f = line.strip()
            if f not in mtime:  # git log 는 최신순 → 첫 등장이 마지막 커밋
                mtime[f] = cur
    return mtime


def excluded(path):
    if path in EXCLUDE_FILES:
        return True
    return any(fnmatch.fnmatch(path, g) for g in EXCLUDE_GLOBS)


def title_of(path):
    try:
        txt = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        return os.path.basename(path)
    m = re.search(r"^---\s*$(.*?)^---\s*$", txt, re.M | re.S)
    if m:
        t = re.search(r"^title:\s*(.+?)\s*$", m.group(1), re.M)
        if t:
            return t.group(1).strip().strip("\"'")
    h = re.search(r"^#\s+(.+)$", txt, re.M)
    if h:
        return h.group(1).strip()
    return os.path.basename(path)[:-3]


def main():
    mtime = last_commit_dates()
    tracked = subprocess.run(
        ["git", "ls-files", *DIRS], capture_output=True, text=True
    ).stdout.split()

    items = []
    for path in tracked:
        if not path.endswith(".md"):
            continue
        if path.split("/")[0] not in DIRS:
            continue
        if excluded(path) or not os.path.exists(path):
            continue
        items.append({
            "path": path,
            "url": "/" + path[:-3] + ".html",
            "title": title_of(path),
            "dir": path.split("/")[0],
            "date": mtime.get(path, "")[:10],
        })

    # 최신 수정순 (날짜 내림차순; 날짜 없는 문서는 뒤로)
    items.sort(key=lambda x: x["date"], reverse=True)

    os.makedirs("_data", exist_ok=True)
    with open("_data/knowledge.json", "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=1)
    print(f"knowledge index: {len(items)} docs -> _data/knowledge.json")


if __name__ == "__main__":
    main()
