#!/usr/bin/env python3
"""
데모 스크립트 - API 호출 없이 시스템 테스트

이 스크립트는 API 키 없이도 실행할 수 있습니다.
컨텍스트 로드, 스킬 로드, 프롬프트 생성을 테스트합니다.
"""

import sys
from pathlib import Path

# src 모듈 경로 추가
sys.path.insert(0, str(Path(__file__).parent))

from src.config import load_config
from src.context_loader import ContextLoader
from src.skill_loader import SkillLoader
from src.generator import ContentGenerator
from src.logger import setup_logger
import logging


def main():
    # 디버그 로깅 활성화
    setup_logger(level=logging.INFO, log_file=False)

    print("=" * 60)
    print("AI 공동 집필 시스템 - 데모 (API 호출 없음)")
    print("=" * 60)

    # 1. 설정 로드
    print("\n[1] 설정 로드")
    config = load_config()
    print(f"    Base Dir: {config.base_dir}")
    print(f"    Model: {config.model}")
    print(f"    API Key: {'설정됨' if config.anthropic_api_key else '미설정'}")

    # 2. 컨텍스트 로드
    print("\n[2] 컨텍스트 로드")
    context_loader = ContextLoader(config.context_dir)
    context = context_loader.load_all()

    if context.voice_dna:
        print(f"    ✓ Voice DNA")
        print(f"      - 이름: {context.voice_dna.identity.get('name')}")
        print(f"      - 역할: {context.voice_dna.identity.get('role')}")
    else:
        print(f"    ✗ Voice DNA (없음)")

    if context.icp:
        print(f"    ✓ ICP")
        print(f"      - 요약: {context.icp.persona_summary.get('one_line_description', 'N/A')[:50]}...")
    else:
        print(f"    ✗ ICP (없음)")

    if context.business_profile:
        print(f"    ✓ Business Profile")
        print(f"      - 이름: {context.business_profile.basic_info.get('name')}")
    else:
        print(f"    ✗ Business Profile (없음)")

    # 3. 스킬 로드
    print("\n[3] 스킬 로드")
    skill_loader = SkillLoader(config.skills_dir)
    skills = skill_loader.list_skills()

    if skills:
        print(f"    발견된 스킬 ({len(skills)}개):")
        for skill_name in skills:
            info = skill_loader.get_skill_info(skill_name)
            if info:
                print(f"      - {skill_name}: {info['title']}")
    else:
        print("    발견된 스킬 없음")

    # 4. 스킬 상세 테스트
    if "ai-tutorial" in skills:
        print("\n[4] 스킬 상세 테스트 (ai-tutorial)")
        skill = skill_loader.load_skill("ai-tutorial")
        if skill:
            print(f"    제목: {skill.title}")
            print(f"    사용법: {skill.usage}")
            print(f"    설명: {skill.description[:80]}...")

            template = skill.get_template()
            if template:
                print(f"    템플릿: {template[:100]}...")

    # 5. 프롬프트 생성 테스트 (드라이런)
    print("\n[5] 프롬프트 생성 테스트 (드라이런)")
    generator = ContentGenerator(model=config.model)

    if "ai-tutorial" in skills:
        skill = skill_loader.load_skill("ai-tutorial")
        dry_run_result = generator.generate_dry_run(
            user_prompt="Claude로 이메일 자동화하기",
            context=context,
            skill=skill
        )

        # 요약 출력
        lines = dry_run_result.split("\n")
        print(f"    프롬프트 생성 완료")
        print(f"    시스템 프롬프트 라인 수: {len([l for l in lines if l.strip()])}")

        # 일부 출력
        print("\n    [프롬프트 미리보기]")
        print("    " + "-" * 40)
        preview_lines = dry_run_result[:800].split("\n")
        for line in preview_lines[:15]:
            print(f"    {line}")
        print("    ...")
        print("    " + "-" * 40)

    # 6. 컨텍스트 프롬프트 변환 테스트
    print("\n[6] 컨텍스트 → 프롬프트 변환")
    context_prompt = context.to_prompt_context()
    print(f"    변환된 프롬프트 길이: {len(context_prompt)} 문자")

    print("\n" + "=" * 60)
    print("데모 완료!")
    print("=" * 60)

    print("\n다음 단계:")
    print("  1. .env 파일 생성: cp .env.example .env")
    print("  2. API 키 설정: ANTHROPIC_API_KEY=...")
    print("  3. 실행: python run.py interactive")
    print()


if __name__ == "__main__":
    main()
