#!/usr/bin/env python3
"""
AI 공동 집필 시스템 실행 스크립트

사용법:
    python run.py                     # 인터랙티브 모드
    python run.py skills              # 스킬 목록
    python run.py skill ai-tutorial   # 스킬 상세
    python run.py context             # 컨텍스트 보기
    python run.py generate ai-tutorial "Claude로 이메일 자동화하기"
    python run.py generate ai-tutorial "주제" --dry-run
    python run.py generate ai-tutorial "주제" -o output.md
"""

import sys
from pathlib import Path

# src 모듈 경로 추가
sys.path.insert(0, str(Path(__file__).parent))

from src.cli import main

if __name__ == "__main__":
    main()
