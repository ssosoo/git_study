# AI 공동 집필 시스템 (Co-Writing System)

Claude Code와 컨텍스트 엔지니어링을 활용한 AI 공동 집필 시스템입니다.

> **📌 현재 상태**: 박찬규(위키북스 편집자)의 글쓰기 스타일과 타겟 독자에 맞게 설정됨
> - Voice DNA: 블로그 글 4개 분석 기반 생성 완료
> - ICP: AI 활용에 관심있는 비기술 직군 직장인
> - Business Profile: AI 활용 실무 가이드 콘텐츠

---

## 🚀 빠른 시작

### 이 시스템은 이미 설정되어 있습니다!

컨텍스트 프로파일이 블로그 글 분석을 기반으로 생성되어 있어 바로 사용 가능합니다.

**테스트해보기:**
```
AI 실무 튜토리얼 스타일로 "ChatGPT로 이메일 자동 분류하기" 주제로 블로그 초안을 작성해줘
```

### 프로파일 커스터마이징이 필요하다면

`_prompts/` 폴더의 프롬프트를 사용하여 프로파일을 재생성하세요:

1. **Voice DNA** (`01-voice-dna-generator.md`) - 글쓰기 스타일
2. **ICP** (`02-icp-generator.md`) - 타겟 독자
3. **Business Profile** (`03-business-profile-generator.md`) - 비즈니스 정보

---

## 📁 폴더 구조

```
ai-cowriting-system/
│
├── claude.md                    # 📋 시스템 지시문 (자동 로드)
│
├── .claude/
│   └── skills/                  # 🎯 Claude Skills
│       ├── ai-tutorial/        # ★ 주력 스킬 - AI 실무 가이드
│       ├── blog-post/
│       ├── linkedin-post/
│       ├── newsletter/
│       ├── social-thread/
│       └── email-sequence/
│
├── context/                     # 👤 컨텍스트 프로파일 (설정 완료)
│   ├── voice-dna.json          # 박찬규 글쓰기 스타일
│   ├── icp.json                # AI 활용 관심 직장인
│   └── business-profile.json   # AI 실무 가이드
│
├── knowledge/                   # 📚 지식 베이스
│   ├── drafts/                 # 작업 중인 초안
│   ├── notes/                  # 아이디어, 메모
│   └── references/             # 참고 자료
│
└── _prompts/                    # 🔧 프로파일 생성 프롬프트
    ├── 01-voice-dna-generator.md
    ├── 02-icp-generator.md
    └── 03-business-profile-generator.md
```

---

## 💡 사용 예시

### AI 실무 튜토리얼 작성 (주력)
```
ai-tutorial 스킬로 "Claude Projects로 재무분석 챗봇 만들기" 주제로 블로그 초안 작성해줘
```

### LinkedIn 게시물
```
LinkedIn 게시물 하나 작성해줘. 주제는 "비개발자도 AI로 업무 자동화할 수 있다"
```

### 도구 비교 포스트
```
"ChatGPT vs Claude: 업무 자동화에 어떤 도구가 더 나을까?" 주제로 비교 포스트 작성해줘
```

### 지식 베이스 활용
```
knowledge/drafts의 최신 뉴스레터를 기반으로 소셜 스레드 만들어줘
```

### 대량 콘텐츠 생성
```
이번 달 AI 활용 주제로 LinkedIn 게시물 아이디어 10개 제안해줘
```

---

## 🛠 커스터마이징

### 글쓰기 스타일 특징 (현재 설정)

| 요소 | 설정값 |
|------|--------|
| 톤 | 친근하고 설명적인 - 옆에서 알려주는 느낌 |
| 구조 | 단계별 가이드 (첫번째, 두번째...) |
| 시그니처 마무리 | "꼭 시도해 보기 바랍니다!" |
| 특징 | 스크린샷 + 복사 가능한 프롬프트 제공 |

### 새 스킬 추가하기

1. `.claude/skills/` 폴더에 새 폴더 생성
2. `skill.md` 파일 작성 (스킬 지시문)
3. `claude.md`의 스킬 목록에 추가

### 컨텍스트 프로파일 업데이트

프로파일은 시간이 지나며 계속 개선해야 합니다:
- Voice DNA: AI 출력이 마음에 안 들 때 수정
- ICP: 독자가 변하거나 새로운 인사이트가 생길 때
- Business Profile: 비즈니스 변화 반영

---

## ⚠️ 주의사항

1. **컨텍스트 프로파일은 직접 생성해야 합니다**
   - 템플릿만으로는 "당신처럼 들리는" 결과물을 만들 수 없습니다
   - 제공된 프롬프트를 사용하여 직접 생성하세요

2. **글 샘플이 중요합니다**
   - Voice DNA 생성 시 본인의 실제 글 샘플을 제공하세요
   - 더 많은 샘플 = 더 정확한 Voice DNA

3. **점진적 개선**
   - 처음부터 완벽할 필요 없습니다
   - AI 출력을 보며 컨텍스트 프로파일을 계속 개선하세요

---

## 🔗 참고 자료

- [Claude Code 공식 문서](https://docs.anthropic.com/claude-code)
- [Cursor 공식 사이트](https://cursor.sh/)

---

## 📝 라이선스

이 시스템은 개인 및 상업적 용도로 자유롭게 사용, 수정, 배포할 수 있습니다.

---

# 2024_DS60
파이썬으로 구현해보는 필수 머신러닝/딥러닝 알고리즘
