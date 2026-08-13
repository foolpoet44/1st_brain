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

# Jekyll 이 애초에 HTML 을 뱉지 않는 경로.
#
# 왜 필요한가: 인덱스는 `git ls-files` 로 추적 파일을 전부 훑는데, 그중에는
# _config.yml 의 exclude 에 걸려 사이트에 발행되지 않는 폴더가 섞여 있다.
# 그대로 두면 "목록에는 보이는데 누르면 404" 인 유령 항목이 된다. 즉 이 집합은
# _config.yml 의 exclude 와 반드시 짝을 맞춰야 하는 쌍둥이 목록이다.
NOPUBLISH_DIRS = {
    # 빌드 · 설정 · 의존성
    ".obsidian", "venv", "attachments", "scripts", "_ops",
    # 서브모듈 · 임시 디렉터리
    "Understand-Anything", "open-design", "temp_skill", "tmp_deploy",
    # vault 복제본 · 미처리 원자료
    "dev", "dev2", "sync", "syncs", "sy", "raw", "inbox",
    # 코드 · 앱 (지식 문서 아님)
    "Toss", "ragapp", "harness",
    # 템플릿(플레이스홀더 {{ }}) · 사고 로그
    "templates", "thinklog",
}

EXCLUDE_GLOBS = [
    "concepts/extracted-*.md",
    "outputs/temp-*.md",
    "vault/attachments/*",
    "raw/*",          # 미처리 raw 자료 제외
    "inbox/*",        # 미처리 inbox 자료 제외
]

EXCLUDE_FILES = {
    "outputs/weekly/2026-W18.md",
    ".gitmodules",
}


def last_commit_dates():
    """파일별 마지막 커밋 ISO 날짜를 git log 한 번으로 수집.

    pathspec 을 주지 않고 저장소 전체를 훑는다. 이전 판은 폴더 화이트리스트를
    pathspec 으로 넘겼는데 그 목록 맨 앞에 루트를 뜻하는 빈 문자열("")이
    들어 있었다. git 은 빈 pathspec 을 거부하며("empty string is not a valid
    pathspec") 즉시 죽는데, 이 함수가 반환코드를 보지 않았기 때문에 실패가
    조용히 삼켜졌고 모든 문서의 date 가 "" 가 됐다. 그 결과 정렬 키가 전부
    같아져 '최신 수정순'이라는 이 페이지의 존재 이유 자체가 무력화됐다.
    발행 대상 선별은 아래 publishable() 이 맡으므로 pathspec 은 애초에
    필요 없었다.
    """
    proc = subprocess.run(
        ["git", "log", "--name-only", "--format=@%cI"],
        capture_output=True, text=True,
    )
    # 날짜 없는 인덱스는 '최신순'을 참칭하는 거짓말이다. 조용히 넘기지 않는다.
    if proc.returncode != 0:
        raise SystemExit(f"git log 실패 — 인덱스를 만들지 않는다:\n{proc.stderr.strip()}")
    out = proc.stdout
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


def publishable(path):
    """Jekyll 이 실제로 이 문서의 HTML 을 만들어 주는가."""
    segs = path.split("/")
    # Jekyll 은 . 또는 _ 로 시작하는 디렉터리를 기본적으로 건너뛴다 (.agents/, _ops/ 등)
    if any(s.startswith((".", "_")) for s in segs[:-1]):
        return False
    return segs[0] not in NOPUBLISH_DIRS


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
    # 루트 파일은 H1 이 없으면 파일명을 제목으로
    return os.path.basename(path)[:-3] if path.endswith(".md") else os.path.basename(path)


def main():
    mtime = last_commit_dates()
    tracked = subprocess.run(
        ["git", "ls-files"], capture_output=True, text=True
    ).stdout.split()

    items = []
    skipped = 0
    for path in tracked:
        if not path.endswith(".md"):
            continue

        # 발행되지 않는 경로를 실으면 클릭 시 404 나는 유령 항목이 된다
        if not publishable(path):
            skipped += 1
            continue

        if excluded(path) or not os.path.exists(path):
            continue

        # 첫 폴더명 추출 (루트 파일은 "")
        first_dir = path.split("/")[0] if "/" in path else ""
        
        items.append({
            "path": path,
            "url": "/" + path[:-3] + ".html",
            "title": title_of(path),
            "dir": first_dir if first_dir else "root",
            "date": mtime.get(path, "")[:10],
        })

    # 최신 수정순 (날짜 내림차순; 날짜 없는 문서는 뒤로)
    items.sort(key=lambda x: x["date"], reverse=True)

    dated = sum(1 for i in items if i["date"])
    # 날짜가 하나도 안 붙었다면 git log 수집이 무너진 것이다. 정렬이 거짓이
    # 되므로 배포를 통과시키지 않고 여기서 세운다.
    if items and not dated:
        raise SystemExit("날짜가 수집된 문서가 0건 — git 히스토리(fetch-depth: 0) 확인 필요")

    os.makedirs("_data", exist_ok=True)
    with open("_data/knowledge.json", "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=1)
    print(
        f"knowledge index: {len(items)} docs "
        f"(날짜 {dated}건 / 미발행 경로 {skipped}건 제외) -> _data/knowledge.json"
    )


if __name__ == "__main__":
    main()
