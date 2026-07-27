#!/usr/bin/env python3
"""
Evolution Gate - csp-brain Type 자동 분류의 안전장치

이 스크립트는 다음 워크플로우를 실행한다:
1. Vault 스캔하여 type 이 없는 문서들을 분석
2. 분류 규칙 적용하여 type 제안 (즉시 적용하지 않음)
3. audit_log 에 이력 기록
4. validation_sample: 10 개 무작위 추출
5. clarify 도구를 통해 인간 검증 요청 (이 스크립트는 JSON 출력만 하고, Hermes 가 clarify 호출)
6. 인간 승인 시, 실제 문서에 type 필드 적용

사용법:
    python scripts/evolution_gate.py --batch-size 100 --dry-run

출력:
    - .pending_changes/ 에 patch 파일들 생성
    - audit_logs/classification_YYYY-MM-DD.json 에 이력 기록
    - validation_sample.json 에 검증용 10 개 샘플 출력 (Hermes 가 이를 clarify 로 전달)
"""

import argparse
import json
import os
import random
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import yaml

# Vault 루트 경로 (스크립트 위치 기준 2 단계 상위)
VAULT_ROOT = Path(__file__).parent.parent
PENDING_DIR = VAULT_ROOT / ".pending_changes"
AUDIT_LOG_DIR = VAULT_ROOT / "audit_logs"


# 분류 규칙 (Rule-based Classifier)
# HR 의 '직무 역량 모델'과 유사하게, 명확한 기준으로 분류한다.
CLASSIFICATION_RULES = {
    "Project": {
        "keywords": ["onboarding", "project", "initiative", "milestone", "deliverable"],
        "frontmatter_keys": ["onboarding", "project_id"],
        "confidence_weight": 1.0
    },
    "Person": {
        "keywords": ["profile", "bio", "resume", "이정민", "Tony Lee", "김민수", "박지영"],
        "frontmatter_keys": ["person_id", "role"],
        "confidence_weight": 1.2  # 사람 이름은 높은 신뢰도
    },
    "Meeting": {
        "keywords": ["meeting", "sync", "standup", "retro", "sprint planning"],
        "frontmatter_keys": ["meeting_date", "attendees"],
        "confidence_weight": 0.9
    },
    "Reflection": {
        "keywords": ["reflect", "retro", "learning", "insight", "growth"],
        "frontmatter_keys": ["reflection_date"],
        "confidence_weight": 0.85
    },
    "Concept": {
        "keywords": ["concept", "model", "framework", "theory", "principle"],
        "frontmatter_keys": ["concept_id"],
        "confidence_weight": 0.8
    },
    "Resource": {
        "keywords": ["url", "link", "resource", "reference", "citation"],
        "frontmatter_keys": ["url", "link"],
        "confidence_weight": 0.9
    },
    "Note": {
        "keywords": [],  # 기본값
        "frontmatter_keys": [],
        "confidence_weight": 0.5  # 낮은 신뢰도 (기본 분류)
    }
}


def scan_vault() -> List[Path]:
    """type 이 없는 모든 Markdown 문서를 스캔한다."""
    docs = []
    for md_file in VAULT_ROOT.rglob("*.md"):
        # attachments/ 디렉토리는 제외
        if "attachments" in md_file.parts:
            continue
        
        # frontmatter 확인
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        if not content.startswith("---"):
            continue
        
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue
        
        try:
            frontmatter = yaml.safe_load(parts[1])
            if frontmatter and "type" in frontmatter:
                continue  # 이미 type 이 할당됨
        except yaml.YAMLError:
            pass  # 파싱 오류는 스킵
        
        docs.append(md_file)
    
    return docs


def extract_h1(content: str) -> Optional[str]:
    """Markdown 본문에서 첫 번째 H1 을 추출한다."""
    lines = content.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    return None


def classify_document(doc_path: Path) -> Tuple[str, float, str]:
    """
    문서를 분석하여 type 을 제안한다.
    
    반환:
        (proposed_type, confidence, rule_applied)
    """
    with open(doc_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # frontmatter 파싱
    frontmatter = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2]
            except yaml.YAMLError:
                pass
    
    # H1 추출
    h1 = extract_h1(body)
    filename = doc_path.stem.lower()
    
    # 분류 점수 계산
    scores: Dict[str, float] = {}
    applied_rules: Dict[str, str] = {}
    
    for type_name, rule in CLASSIFICATION_RULES.items():
        score = 0.0
        rules_matched = []
        
        # 키워드 매칭 (filename + body)
        text_to_search = f"{filename} {body[:500]}".lower()  # 본문 앞 500 자만
        for keyword in rule["keywords"]:
            if keyword.lower() in text_to_search:
                score += rule["confidence_weight"]
                rules_matched.append(f"keyword: '{keyword}'")
        
        # frontmatter 키 매칭
        for key in rule["frontmatter_keys"]:
            if key in frontmatter:
                score += rule["confidence_weight"] * 1.5  # frontmatter 는 더 높은 가중치
                rules_matched.append(f"frontmatter: '{key}'")
        
        # H1 매칭 (사람 이름 등)
        if h1:
            for keyword in rule["keywords"]:
                if keyword.lower() in h1.lower():
                    score += rule["confidence_weight"] * 2  # H1 은 매우 높은 가중치
                    rules_matched.append(f"H1: '{keyword}'")
        
        if score > 0:
            scores[type_name] = score
            applied_rules[type_name] = ", ".join(rules_matched)
    
    # 최고 점수 type 선택
    if not scores:
        return "Note", 0.5, "default: no rules matched"
    
    best_type = max(scores.keys(), key=lambda t: scores[t])
    confidence = min(scores[best_type] / 5.0, 1.0)  # 0~1 로 정규화
    rule_applied = applied_rules[best_type]
    
    return best_type, confidence, rule_applied


def create_patch(doc_path: Path, proposed_type: str) -> Path:
    """
    문서에 type 을 추가하는 patch 파일을 생성한다.
    실제 적용은 인간 승인 후에 이루어진다.
    """
    rel_path = doc_path.relative_to(VAULT_ROOT)
    patch_file = PENDING_DIR / f"{rel_path.parent.name}_{rel_path.name}.patch"
    patch_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(doc_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"Invalid frontmatter: {doc_path}")
    
    frontmatter_str = parts[1]
    body = parts[2]
    
    # type 추가
    new_frontmatter = f"type: {proposed_type}\n{frontmatter_str}"
    new_content = f"---{new_frontmatter}---{body}"
    
    with open(patch_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    return patch_file


def save_audit_log(records: List[dict], batch_id: str):
    """분류 이력을 audit_log 에 기록한다."""
    AUDIT_LOG_DIR.mkdir(parents=True, exist_ok=True)
    
    # 기존 audit_log 로드 (있으면)
    today = datetime.now().strftime("%Y-%m-%d")
    audit_file = AUDIT_LOG_DIR / f"classification_{today}.json"
    
    existing_records = []
    if audit_file.exists():
        with open(audit_file, "r", encoding="utf-8") as f:
            existing_records = json.load(f)
    
    # 새 기록 추가
    existing_records.extend(records)
    
    with open(audit_file, "w", encoding="utf-8") as f:
        json.dump(existing_records, f, indent=2, ensure_ascii=False)
    
    print(f"📝 Audit log saved: {audit_file}")


def sample_for_validation(pending_docs: List[dict], sample_size: int = 10) -> List[dict]:
    """
    검증용 샘플을 추출한다.
    층화 추출 (stratified sampling) 을 사용하여 Type 별 균형을 맞춘다.
    """
    # 처리된 문서가 샘플 수보다 적으면 전체를 샘플로 사용
    if len(pending_docs) <= sample_size:
        return pending_docs
    
    # Type 별 그룹화
    by_type: Dict[str, List[dict]] = {}
    for doc in pending_docs:
        t = doc["proposed_type"]
        if t not in by_type:
            by_type[t] = []
        by_type[t].append(doc)
    
    # Type 별 균등 추출 (최소 1 개씩)
    samples = []
    types = list(by_type.keys())
    per_type = max(1, sample_size // len(types))
    
    for t, docs in by_type.items():
        sampled = random.sample(docs, min(per_type, len(docs)))
        samples.extend(sampled)
    
    # 부족하면 무작위로 채움
    if len(samples) < sample_size:
        remaining = sample_size - len(samples)
        all_docs = [d for docs in by_type.values() for d in docs]
        remaining_pool = [d for d in all_docs if d not in samples]
        if remaining_pool:
            remaining_samples = random.sample(remaining_pool, min(remaining, len(remaining_pool)))
            samples.extend(remaining_samples)
    
    return samples[:sample_size]


def main():
    parser = argparse.ArgumentParser(description="Evolution Gate: Type classification with human approval")
    parser.add_argument("--batch-size", type=int, default=100, help="Number of documents to process in this batch")
    parser.add_argument("--offset", type=int, default=0, help="Offset for pagination (skip first N docs)")
    parser.add_argument("--dry-run", action="store_true", help="Do not create patch files, only show what would be done")
    parser.add_argument("--validation-sample", type=int, default=10, help="Number of samples for human validation")
    args = parser.parse_args()
    
    print(f"🔍 Scanning vault for unclassified documents...")
    all_docs = scan_vault()
    
    if not all_docs:
        print("✅ All documents are already classified!")
        return
    
    print(f"📊 Found {len(all_docs)} unclassified documents")
    
    # 배치 처리
    batch_docs = all_docs[args.offset : args.offset + args.batch_size]
    print(f"📦 Processing batch: {len(batch_docs)} documents (offset: {args.offset})")
    
    # 분류 실행
    pending_docs = []
    batch_id = f"batch_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}"
    
    for doc_path in batch_docs:
        proposed_type, confidence, rule_applied = classify_document(doc_path)
        rel_path = str(doc_path.relative_to(VAULT_ROOT))
        
        record = {
            "timestamp": datetime.now().isoformat(),
            "document": rel_path,
            "proposed_type": proposed_type,
            "confidence": round(confidence, 2),
            "rule_applied": rule_applied,
            "human_approved": None,  # 아직 승인 안 됨
            "batch_id": batch_id
        }
        
        pending_docs.append(record)
        
        if not args.dry_run:
            try:
                patch_file = create_patch(doc_path, proposed_type)
                print(f"  📄 Created patch: {patch_file.name}")
            except Exception as e:
                print(f"  ❌ Failed to create patch for {rel_path}: {e}")
    
    # Audit log 기록
    if not args.dry_run:
        save_audit_log(pending_docs, batch_id)
    
    # 검증용 샘플 추출
    validation_samples = sample_for_validation(pending_docs, args.validation_sample)
    
    # 샘플을 JSON 으로 출력 (Hermes 가 이를 clarify 로 전달)
    sample_file = PENDING_DIR / "validation_sample.json"
    with open(sample_file, "w", encoding="utf-8") as f:
        json.dump(validation_samples, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Batch complete!")
    print(f"   - Pending changes: {len(pending_docs)} documents")
    print(f"   - Validation samples: {len(validation_samples)} documents")
    print(f"   - Batch ID: {batch_id}")
    print(f"\n🔍 Validation samples saved to: {sample_file}")
    print(f"\n📋 다음 단계:")
    print(f"   1. Hermes 가 validation_sample.json 을 읽어 clarify 로 인간 검증 요청")
    print(f"   2. 인간이 80% 이상 승인하면, .pending_changes/ 의 patch 파일들을 실제 문서에 적용")
    print(f"   3. git add + commit 하여 변경사항 확정")
    
    # JSON 출력 (Hermes 가 파싱하여 clarify 에 사용)
    print(f"\n--- VALIDATION_SAMPLE_START ---")
    print(json.dumps(validation_samples, indent=2, ensure_ascii=False))
    print(f"--- VALIDATION_SAMPLE_END ---")


if __name__ == "__main__":
    main()
