# coffee-skill Nederlandse referentie

## Wat is het

`coffee-skill` is een skillpakket voor Codex. Het dekt software engineering, AI Agent/RAG, API's en data, UI en documenten, defensieve beveiliging, detectie, incident response en kwetsbaarheidsbeheer.

## Waarom bestaat het

- Te veel kleine skills maken automatisch triggeren onbetrouwbaar.
- Veel clients kiezen skills vooral op basis van frontmatter `name` en `description` in `SKILL.md`.
- Security-workflows hebben duidelijke grenzen nodig voor autorisatie en defensief gebruik.
- Praktisch werk vraagt om verifieerbare stappen, niet alleen algemeen advies.

## Waarom gebruiken

- Het consolideert 87 bronskills in 15 brede capability-skills.
- `coff0xc-skill-router` is de fallback wanneer een specifieke skill niet automatisch start.
- Elke skill bevat scope, uitsluitingen, capability matrix, workflowfasen, bewijsniveaus, harde gates, validatie en anti-patterns.
- Security-inhoud blijft gericht op geautoriseerde verdediging, detectie, hardening, verificatie en rapportage.

## Hoe gebruiken

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-cloud-devsecops to review Kubernetes and CI/CD risk.
```

Als automatisch triggeren mist:

```text
Use coff0xc-skill-router to choose the right skill.
```

## Waar gebruiken

- Lokale Codex skill directories.
- Compatibele clients die `SKILL.md` mappen laden.
- Engineering, AI-systemen, documentatie, defensieve security, detectie en kwetsbaarheidsbeheer.

## Als triggeren faalt

1. Controleer of mapnaam en frontmatter `name` overeenkomen.
2. Herstart of refresh Codex na het kopiëren.
3. Verwijder dubbele skillnamen.
4. Roep `coff0xc-skill-router` expliciet aan.

## Veiligheidsgrens

Gebruik het alleen op assets, code, logs, samples, labs en trainingsomgevingen die je bezit of expliciet mag beoordelen. Niet gebruiken voor ongeautoriseerde toegang, credentialdiefstal, persistence, evasion, C2, phishingverzameling, data-exfiltratie of destructieve acties.
