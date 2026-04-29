#!/usr/bin/env python3
"""
Conversation JSON to Markdown Parser

D:\obsi\sync\raw\archive\conversations\ 폴더의 JSON 파일들을
Markdown 으로 변환하여 csp-brain 의 raw/archive/md/ 폴더에 저장합니다.
"""

import json
import os
from pathlib import Path
from datetime import datetime

# 설정
SOURCE_DIR = Path("D:/obsi/sync/raw/archive/conversations")
OUTPUT_DIR = Path("D:/obsi/sync/1st_brain/raw/archive/md")

def extract_text_from_content(content_list):
    """content 배열에서 텍스트만 추출하여 연결"""
    texts = []
    for item in content_list:
        if isinstance(item, dict):
            if item.get("type") == "text":
                texts.append(item.get("text", ""))
            elif item.get("type") == "tool_use":
                # 도구 사용 기록 요약
                tool_name = item.get("name", "unknown")
                texts.append(f"\n[Tool: {tool_name}]\n")
        elif isinstance(item, str):
            texts.append(item)
    return "".join(texts)

def parse_conversation(json_path):
    """단일 JSON 파일 파싱"""
    try:
        # UTF-8 BOM 처리
        with open(json_path, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
    except Exception as e:
        return None, f"Error loading JSON: {e}"

    # 메타데이터 추출
    uuid = data.get("uuid", "unknown")
    name = data.get("name", "No Title") or "No Title"
    created_at = data.get("created_at", "")
    updated_at = data.get("updated_at", "")

    # 날짜 추출
    try:
        date_obj = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        date_str = date_obj.strftime("%Y-%m-%d")
        time_str = date_obj.strftime("%H:%M")
    except:
        date_str = "Unknown"
        time_str = ""

    # 대화 메시지 추출
    messages = data.get("chat_messages", [])

    # Markdown 생성
    md_content = []
    md_content.append("---")
    md_content.append(f"title: {name}")
    md_content.append(f"date: {date_str}")
    md_content.append(f"time: {time_str}")
    md_content.append(f"uuid: {uuid}")
    md_content.append("type: conversation")
    md_content.append("tags: [archive, conversation]")
    md_content.append("---")
    md_content.append("")
    md_content.append(f"# {name}")
    md_content.append("")
    md_content.append(f"**날짜**: {date_str} {time_str}")
    md_content.append("")
    md_content.append("---")
    md_content.append("")

    # 대화 내용
    for i, msg in enumerate(messages):
        sender = msg.get("sender", "unknown")
        sender_label = "Human" if sender == "human" else "Claude"
        text = msg.get("text", "")
        content_list = msg.get("content", [])

        # content 배열에서 텍스트 추출
        if not text and content_list:
            text = extract_text_from_content(content_list)

        md_content.append(f"## {sender_label} (Message {i+1})")
        md_content.append("")
        if text.strip():
            md_content.append(text.strip())
        else:
            md_content.append("*(내용 없음)*")
        md_content.append("")

    md_content.append("---")
    md_content.append("")
    md_content.append(f"*Archived from: `{json_path.name}`*")

    return uuid, "\n".join(md_content)

def main():
    """메인 함수"""
    print("=" * 60)
    print("Conversation JSON → Markdown Parser")
    print("=" * 60)

    # 출력 디렉토리 생성
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 모든 JSON 파일 찾기
    json_files = list(SOURCE_DIR.rglob("*.json"))
    total = len(json_files)

    print(f"\n총 {total}개 JSON 파일 발견")
    print(f"출력 디렉토리: {OUTPUT_DIR}")
    print()

    # 변환 카운터
    success = 0
    failed = 0
    skipped = 0

    # CONVERSATION_MAP.md 에서 이미 처리된 파일 확인
    map_path = Path("D:/obsi/sync/raw/archive/CONVERSATION_MAP.md")
    processed_uuids = set()

    if map_path.exists():
        with open(map_path, "r", encoding="utf-8") as f:
            for line in f:
                if "| UUID" in line or "`unknown`" in line:
                    continue
                # UUID 추출 시도
                if "`" in line:
                    parts = line.split("`")
                    if len(parts) >= 2:
                        uuid_candidate = parts[1]
                        if len(uuid_candidate) == 36 and "-" in uuid_candidate:
                            processed_uuids.add(uuid_candidate)

    print(f"기존 처리된 UUID: {len(processed_uuids)}개")
    print()

    # 첫 50 개만 샘플 변환 (테스트용)
    # 실제 실행시에는 주석 해제
    sample_mode = False

    for i, json_path in enumerate(json_files):
        uuid = json_path.stem  # 파일명 (UUID)

        # 이미 처리된 UUID 는 스킵
        if uuid in processed_uuids:
            skipped += 1
            continue

        # 샘플 모드: 첫 50 개만
        if sample_mode and i >= 50:
            break

        # 파싱
        parsed_uuid, result = parse_conversation(json_path)

        if parsed_uuid is None:
            failed += 1
            print(f"[FAIL] {json_path.name}: {result}")
            continue

        # 출력 파일 경로
        # 날짜별로 폴더 분류
        try:
            date_part = json_path.parent.name  # "04" 등
            year_part = json_path.parent.parent.name  # "2026"
            output_subdir = OUTPUT_DIR / year_part / date_part
            output_subdir.mkdir(parents=True, exist_ok=True)
        except:
            output_subdir = OUTPUT_DIR

        output_path = output_subdir / f"{uuid}.md"

        # 저장
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result)
            success += 1

            # 진행 상황 출력 (10 개마다)
            if success % 10 == 0:
                print(f"[OK] {success}번째: {uuid}.md")
        except Exception as e:
            failed += 1
            print(f"[FAIL] {uuid}: {e}")

    # 결과 요약
    print()
    print("=" * 60)
    print("변환 완료")
    print("=" * 60)
    print(f"  성공: {success}개")
    print(f"  실패: {failed}개")
    print(f"  스킵 (이미 처리됨): {skipped}개")
    print()

if __name__ == "__main__":
    main()
