# coffee-skill referência em português do Brasil

## O que é

`coffee-skill` é um pacote de skills para Codex. Ele cobre engenharia de software, AI Agent/RAG, APIs e dados, UI e documentos, segurança defensiva, detecção, resposta a incidentes e gestão de vulnerabilidades.

## Por que existe

- Muitas skills pequenas tornam o acionamento automático menos confiável.
- Muitos clientes escolhem skills principalmente pelo frontmatter `name` e `description` de `SKILL.md`.
- Workflows de segurança precisam de limites claros de autorização e uso defensivo.
- Trabalho real precisa de passos verificáveis, não apenas recomendações genéricas.

## Por que usar

- Consolida 87 skills de origem em 15 skills amplas de capacidade.
- Adiciona `coff0xc-skill-router` como fallback quando uma skill específica não aciona.
- Cada skill inclui escopo, exclusões, matriz de capacidades, fases, níveis de evidência, gates, validação e antipadrões.
- Segurança fica focada em defesa autorizada, detecção, hardening, verificação e relatório.

## Como usar

Você pode pedir naturalmente:

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-detection-response to write detection rules.
```

Se não acionar automaticamente:

```text
Use coff0xc-skill-router to choose the right skill.
```

## Onde usar

- Diretórios locais de skills do Codex.
- Clientes compatíveis com pastas `SKILL.md`.
- Engenharia, sistemas de IA, documentação, segurança defensiva, detecção e gestão de vulnerabilidades.

## Quando o acionamento falhar

1. Verifique se o nome da pasta corresponde ao frontmatter `name`.
2. Reinicie ou atualize o Codex depois de copiar.
3. Remova nomes de skill duplicados.
4. Chame `coff0xc-skill-router` explicitamente.

## Limite de segurança

Use apenas em ativos, código, logs, amostras, laboratórios e ambientes de treinamento que você possui ou tem autorização explícita para avaliar. Não use para acesso não autorizado, roubo de credenciais, persistência, evasão, C2, coleta de phishing, exfiltração de dados ou ações destrutivas.
