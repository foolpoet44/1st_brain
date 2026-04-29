"""
EX Intelligence Signal Monitor
- Pulse 신호 수집 및 저장
- 통계적 이상 감지
- 액션 트리거 규칙 엔진
"""
import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from dataclasses import dataclass
import statistics


@dataclass
class Signal:
    """Pulse 신호 데이터"""
    category: str       # Self, Relation, Organization
    issue: str          # 번아웃, 성장단절, 등
    score: float        # 0-100 점
    trend: str          # 'up', 'down', 'stable'
    detected_at: str
    org_unit: str       # 조직명
    comment: str = ""   # 자유 응답


class SignalDetector:
    """통계적 이상 감지"""

    def __init__(self, window_size: int = 4, z_threshold: float = 2.0):
        """
        Args:
            window_size: 이동 평균 창 크기 (주)
            z_threshold: Z-score 임계값
        """
        self.window_size = window_size
        self.z_threshold = z_threshold

    def detect_anomaly(self, scores: List[float]) -> Dict:
        """이상 점수 감지"""
        if len(scores) < 3:
            return {"is_anomaly": False, "reason": "데이터 부족"}

        current = scores[-1]
        mean = statistics.mean(scores[:-1])
        stdev = statistics.stdev(scores[:-1]) if len(scores) > 3 else 10

        z_score = (current - mean) / stdev if stdev > 0 else 0

        is_anomaly = abs(z_score) > self.z_threshold
        trend = "down" if z_score < -self.z_threshold else ("up" if z_score > self.z_threshold else "stable")

        return {
            "is_anomaly": is_anomaly,
            "z_score": round(z_score, 2),
            "mean": round(mean, 1),
            "stdev": round(stdev, 1),
            "trend": trend,
            "current": current
        }

    def detect_sharp_drop(self, scores: List[float], threshold: float = 10) -> bool:
        """급격한 하락 감지"""
        if len(scores) < 2:
            return False
        return (scores[-2] - scores[-1]) > threshold


class ActionTrigger:
    """신호 → 액션 규칙 엔진"""

    def __init__(self):
        self.rules = {
            "burnout": {
                "trigger": "score < 40 OR drop > 15",
                "actions": [
                    "1on1 면담 권장",
                    "워크로드 조정 검토",
                    "EAP 프로그램 안내"
                ]
            },
            "growth": {
                "trigger": "score < 50",
                "actions": [
                    "성장 경로 면담",
                    "교육 기회 제안",
                    "멘토 매칭"
                ]
            },
            "leadership": {
                "trigger": "score < 45",
                "actions": [
                    "리더십 코칭",
                    "360 도 피드백",
                    "1on1 스킬 교육"
                ]
            },
            "collaboration": {
                "trigger": "score < 50",
                "actions": [
                    "팀 빌딩 세션",
                    "역할 명확화 워크샵",
                    "갈등 중재"
                ]
            }
        }

    def evaluate(self, signal: Signal) -> List[Dict]:
        """신호에 따른 액션 반환"""
        actions = []

        # 점수 기반 규칙
        if signal.score < 40:
            actions.append({
                "priority": "HIGH",
                "type": "immediate",
                "message": f"즉시 조치 필요: {signal.issue} 점수가 {signal.score}점입니다",
                "recommended": self.rules.get(signal.category.lower(), {}).get("actions", ["면담 권장"])
            })
        elif signal.score < 60:
            actions.append({
                "priority": "MEDIUM",
                "type": "follow_up",
                "message": f"모니터링 필요: {signal.issue} 점수가 {signal.score}점입니다",
                "recommended": self.rules.get(signal.category.lower(), {}).get("actions", ["추적 관찰"])
            })

        # 트렌드 기반 규칙
        if signal.trend == "down":
            actions.append({
                "priority": "WATCH",
                "type": "trend",
                "message": f"하락 트렌드 감지: {signal.issue}",
                "recommended": ["주간 단위 모니터링"]
            })

        return actions


class EXIntelligenceDB:
    """신호 데이터 저장소"""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.signals: List[Signal] = []
        self._load()

    def _load(self):
        """데이터 로드"""
        if self.db_path.exists():
            with open(self.db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.signals = [Signal(**s) for s in data]
            print(f"[DB] 로드 완료: {len(self.signals)}개 신호")
        else:
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            print(f"[DB] 새 데이터베이스 생성: {self.db_path}")

    def _save(self):
        """데이터 저장"""
        data = [
            {
                "category": s.category,
                "issue": s.issue,
                "score": s.score,
                "trend": s.trend,
                "detected_at": s.detected_at,
                "org_unit": s.org_unit,
                "comment": s.comment
            }
            for s in self.signals
        ]
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_signal(self, signal: Signal):
        """신호 추가"""
        self.signals.append(signal)
        self._save()

    def get_history(self, org_unit: str, issue: str, weeks: int = 8) -> List[float]:
        """과거 점수 조회"""
        cutoff = datetime.now() - timedelta(weeks=weeks)
        history = []

        for s in reversed(self.signals):
            if s.org_unit == org_unit and s.issue == issue:
                try:
                    date = datetime.fromisoformat(s.detected_at)
                    if date >= cutoff:
                        history.append(s.score)
                except:
                    pass

        return history

    def get_latest_signals(self, org_unit: Optional[str] = None, limit: int = 20) -> List[Signal]:
        """최신 신호 조회"""
        signals = self.signals
        if org_unit:
            signals = [s for s in signals if s.org_unit == org_unit]
        return list(reversed(signals))[:limit]


def create_sample_data(db: EXIntelligenceDB):
    """샘플 데이터 생성 (데모용)"""
    sample_issues = [
        ("Self", "번아웃"),
        ("Self", "성장단절"),
        ("Relation", "리더십신뢰"),
        ("Relation", "협업마찰"),
        ("Organization", "방향불신"),
        ("Organization", "보상공정성"),
    ]

    org_units = ["EXG 팀", "HR 팀", "전략담당", "제조 AX"]

    for week in range(8, 0, -1):
        date = datetime.now() - timedelta(weeks=week)
        for category, issue in sample_issues:
            for org in org_units:
                # 랜덤 스코어 (트렌드 포함)
                base_score = 55 + (hash(issue + org) % 30)
                noise = (week % 3 - 1) * 5
                score = min(100, max(0, base_score + noise))

                signal = Signal(
                    category=category,
                    issue=issue,
                    score=score,
                    trend="stable",
                    detected_at=date.isoformat(),
                    org_unit=org,
                    comment=f"샘플 데이터 {week}주차"
                )
                db.add_signal(signal)

    print(f"[SAMPLE] {len(sample_issues) * len(org_units) * 8}개 샘플 데이터 생성")


if __name__ == "__main__":
    # 경로를 동적으로 계산
    BASE_DIR = Path(__file__).parent.parent
    DB_PATH = BASE_DIR / "harness" / "ex_signals.json"

    # DB 초기화
    db = EXIntelligenceDB(DB_PATH)

    # 샘플 데이터 생성 (첫 실행시)
    if len(db.signals) < 10:
        create_sample_data(db)

    # 분석 데모
    print("\n=== EX Intelligence 데모 ===")

    detector = SignalDetector()
    trigger = ActionTrigger()

    # 최신 신호 분석
    latest = db.get_latest_signals(limit=5)
    for signal in latest:
        history = db.get_history(signal.org_unit, signal.issue)
        analysis = detector.detect_anomaly(history)

        print(f"\n[{signal.org_unit}] {signal.issue}: {signal.score}점")
        print(f"  - 평균: {analysis['mean']}, Z-score: {analysis['z_score']}")
        print(f"  - 이상: {analysis['is_anomaly']}, 트렌드: {analysis['trend']}")

        actions = trigger.evaluate(signal)
        if actions:
            for action in actions:
                print(f"  - [{action['priority']}] {action['message']}")
