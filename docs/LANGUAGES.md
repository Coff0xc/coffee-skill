# Language References

These files are short usage references for international users. They explain what `coffee-skill` is, why it exists, why it is useful, how to use it, where it fits, and what to do when automatic skill triggering misses. The core skills include engineering, AI Agent/RAG, API/data, UI/report output, Office/PDF file delivery, research draw.io diagrams, and defensive security.

The skills themselves are primarily Chinese + English. These reference files are not separate skill implementations.

## Available References

| Language | File |
|---|---|
| English | [README.en.md](i18n/README.en.md) |
| 中文 | [README.zh-CN.md](i18n/README.zh-CN.md) |
| 日本語 | [README.ja.md](i18n/README.ja.md) |
| 한국어 | [README.ko.md](i18n/README.ko.md) |
| Español | [README.es.md](i18n/README.es.md) |
| Français | [README.fr.md](i18n/README.fr.md) |
| Deutsch | [README.de.md](i18n/README.de.md) |
| Português do Brasil | [README.pt-BR.md](i18n/README.pt-BR.md) |
| Italiano | [README.it.md](i18n/README.it.md) |
| Nederlands | [README.nl.md](i18n/README.nl.md) |
| Polski | [README.pl.md](i18n/README.pl.md) |
| Русский | [README.ru.md](i18n/README.ru.md) |
| العربية | [README.ar.md](i18n/README.ar.md) |
| Türkçe | [README.tr.md](i18n/README.tr.md) |
| हिन्दी | [README.hi.md](i18n/README.hi.md) |
| Bahasa Indonesia | [README.id.md](i18n/README.id.md) |
| Tiếng Việt | [README.vi.md](i18n/README.vi.md) |
| ไทย | [README.th.md](i18n/README.th.md) |

## Universal Fallback Phrase

If a specific skill does not auto-trigger, use the router:

```text
Use coff0xc-skill-router to choose the right skill.
```

Chinese equivalent:

```text
使用 coff0xc-skill-router 帮我选择合适 skill
```

## Notes For Translators

- Keep skill names unchanged.
- Keep manual invocation examples explicit.
- Do not translate `SKILL.md`, `frontmatter`, `name`, `description`, `Codex`, `RAG`, `API`, `SIEM`, `YARA`, `Sigma`, `CVE`, `Kubernetes`, or other technical identifiers unless a local convention is stronger.
- Security wording must preserve authorization and defensive scope.
