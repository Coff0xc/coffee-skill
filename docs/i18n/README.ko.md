# coffee-skill 한국어 참고

## 이것은 무엇인가

`coffee-skill`은 Codex용 스킬 팩입니다. 소프트웨어 엔지니어링, AI Agent/RAG, API와 데이터 설계, UI/문서 출력, 방어적 보안, 탐지, 사고 대응, 취약점 관리를 다룹니다.

## 왜 만들었나

- 너무 많은 작은 스킬은 자동 트리거를 불안정하게 만듭니다.
- 많은 클라이언트는 `SKILL.md`의 frontmatter `name`과 `description`을 중심으로 스킬을 선택합니다.
- 보안 스킬에는 명확한 승인 범위와 방어 목적의 경계가 필요합니다.
- 실제 업무에는 일반 조언보다 검증 가능한 절차가 필요합니다.

## 좋은 점

- 87개의 원본 스킬을 15개의 포괄적 역량 스킬로 통합했습니다.
- 자동 트리거가 실패할 때 `coff0xc-skill-router`가 대체 라우터 역할을 합니다.
- 각 스킬에는 적용 범위, 제외 범위, 역량 매트릭스, 작업 단계, 증거 수준, 하드 게이트, 검증 체크리스트, 안티패턴이 포함됩니다.
- 보안 내용은 승인된 방어, 탐지, 강화, 검증, 보고에 초점을 둡니다.

## 사용 방법

자연스럽게 요청할 수 있습니다:

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-cloud-devsecops to review Kubernetes and CI/CD risk.
```

자동으로 트리거되지 않으면:

```text
Use coff0xc-skill-router to choose the right skill.
```

## 어디에서 사용할 수 있나

- 로컬 Codex 스킬 디렉터리.
- `SKILL.md` 폴더 형식을 읽는 호환 클라이언트.
- 개발, AI 시스템, 문서화, 방어적 보안, 탐지, 취약점 관리 업무.

## 트리거가 실패할 때

1. 폴더 이름과 frontmatter `name`이 같은지 확인합니다.
2. 복사 후 Codex를 재시작하거나 새로 고칩니다.
3. 중복된 스킬 이름을 제거합니다.
4. `coff0xc-skill-router`를 명시적으로 호출합니다.

## 보안 경계

소유했거나 명시적으로 승인된 자산, 코드, 로그, 샘플, 실험실, 교육 환경에만 사용하세요. 무단 접근, 자격 증명 탈취, 지속성, 우회, C2, 피싱 수집, 데이터 유출, 파괴적 작업에는 사용하지 마세요.
