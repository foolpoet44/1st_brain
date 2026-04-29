"""
파일 시스템 감시자 (File System Watcher)
- 원본 폴더 (S:\★Y26) 감시
- 새 파일/변경 파일 감지
- manifest.json 자동 업데이트
"""
import os
import json
import hashlib
import time
from datetime import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent, FileCreatedEvent

from manifest_schema import ManifestEntry, auto_categorize, auto_extract_tags


class ManifestWatcher(FileSystemEventHandler):
    """파일 변경 감지 → manifest.json 업데이트"""

    def __init__(self, source_dir: str, vault_dir: str, manifest_path: str):
        self.source_dir = Path(source_dir)
        self.vault_dir = Path(vault_dir)
        self.manifest_path = Path(manifest_path)
        self.manifest = self._load_manifest()

    def _load_manifest(self) -> dict:
        """manifest.json 로드"""
        if self.manifest_path.exists():
            with open(self.manifest_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def _save_manifest(self):
        """manifest.json 저장"""
        with open(self.manifest_path, 'w', encoding='utf-8') as f:
            json.dump(self.manifest, f, ensure_ascii=False, indent=4)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] manifest.json 업데이트됨")

    def _compute_hash(self, filepath: Path) -> str:
        """SHA256 해시 계산"""
        sha256 = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha256.update(chunk)
        return sha256.hexdigest()

    def _get_md_path(self, source_path: Path) -> str:
        """원본 파일 경로 → 마크다운 파일 경로 변환"""
        rel_path = source_path.relative_to(self.source_dir)
        md_name = f"{source_path.stem}.md"

        # Zavis_Brain 루트에 직접 저장
        return str(self.vault_dir / md_name)

    def _update_entry(self, filepath: Path):
        """단일 엔트리 업데이트"""
        if not filepath.suffix.lower() in ['.pptx', '.xlsx', '.pdf', '.docx', '.png', '.jpg']:
            return

        rel_path = str(filepath).replace('/', '\\')
        current_hash = self._compute_hash(filepath)

        # 기존 엔트리 확인
        existing = self.manifest.get(rel_path)

        if existing and existing.get('hash') == current_hash:
            # 변경 없음
            return

        # 새 엔트리 생성/업데이트
        entry = ManifestEntry(
            hash=current_hash,
            mtime=filepath.stat().st_mtime,
            converted_at=datetime.now().isoformat(),
            priority=90,
            md_path=self._get_md_path(filepath),
        )

        # 자동 카테고리 및 태그 추출 (마크다운 내용 읽기)
        md_path = Path(entry.md_path)
        if md_path.exists():
            content = md_path.read_text(encoding='utf-8')[:5000]  # 첫 5000 자만
            entry.category = auto_categorize(rel_path, content)
            entry.tags = auto_extract_tags(rel_path, content)
            entry.word_count = len(content.split())
            entry.last_indexed = datetime.now().isoformat()

        self.manifest[rel_path] = entry.dict()
        self._save_manifest()

    def on_modified(self, event):
        """파일 수정 감지"""
        if isinstance(event, FileModifiedEvent) and not event.is_directory:
            filepath = Path(event.src_path)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] 감지: {filepath.name}")
            self._update_entry(filepath)

    def on_created(self, event):
        """파일 생성 감지"""
        if isinstance(event, FileCreatedEvent) and not event.is_directory:
            filepath = Path(event.src_path)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] 신규: {filepath.name}")
            self._update_entry(filepath)


def start_watching(source_dir: str, vault_dir: str, manifest_path: str):
    """감시 시작"""
    event_handler = ManifestWatcher(source_dir, vault_dir, manifest_path)

    # 기존 파일 초기 스캔
    print("[INIT] 기존 파일 스캔 중...")
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(('.pptx', '.xlsx', '.pdf', '.docx', '.png', '.jpg')):
                event_handler._update_entry(Path(root) / file)

    # 감시 시작
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()

    print(f"[WATCHING] {source_dir} 감시 시작 (중단: Ctrl+C)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[STOPPED] 감시 종료")
    observer.join()


if __name__ == "__main__":
    # 경로를 동적으로 계산 (인코딩 문제 회피)
    BASE_DIR = Path(__file__).parent.parent

    # 설정
    SOURCE_DIR = r"S:\★Y26"  # 원본 폴더 (사용자 환경에 맞게 수정)
    VAULT_DIR = str(BASE_DIR)  # Obsidian Vault
    MANIFEST_PATH = BASE_DIR / "manifest.json"

    start_watching(SOURCE_DIR, VAULT_DIR, str(MANIFEST_PATH))
