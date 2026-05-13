# coffee-skill deutsche Referenz

## Was ist das

`coffee-skill` ist ein Skill-Paket für Codex. Es deckt Softwareentwicklung, AI Agent/RAG, APIs und Daten, UI und Dokumente, defensive Sicherheit, Detection, Incident Response und Schwachstellenmanagement ab.

## Warum es existiert

- Zu viele kleine Skills machen automatisches Auslösen unzuverlässig.
- Viele Clients wählen Skills hauptsächlich über das frontmatter `name` und `description` in `SKILL.md`.
- Sicherheitsworkflows brauchen klare Grenzen für Autorisierung und defensive Nutzung.
- Praktische Arbeit braucht prüfbare Schritte statt nur allgemeiner Empfehlungen.

## Warum es nützlich ist

- Es konsolidiert 87 Quell-Skills in 15 umfassende Capability-Skills.
- `coff0xc-skill-router` dient als Fallback, wenn kein spezifischer Skill automatisch auslöst.
- Jeder Skill enthält Umfang, Ausschlüsse, Capability-Matrix, Arbeitsphasen, Evidenzstufen, harte Gates, Validierung und Anti-Patterns.
- Sicherheitsinhalte bleiben auf autorisierte Verteidigung, Detection, Härtung, Verifikation und Reporting beschränkt.

## Verwendung

Du kannst natürlich fragen:

```text
Use coff0xc-software-engineering to fix tests.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-cloud-devsecops to review Kubernetes and CI/CD risk.
```

Wenn kein Skill automatisch auslöst:

```text
Use coff0xc-skill-router to choose the right skill.
```

## Wo es passt

- Lokale Codex-Skill-Verzeichnisse.
- Kompatible Clients, die `SKILL.md`-Ordner laden.
- Engineering, KI-Systeme, Dokumentation, defensive Sicherheit, Detection und Schwachstellenmanagement.

## Wenn Triggering fehlschlägt

1. Prüfe, ob Ordnername und frontmatter `name` übereinstimmen.
2. Starte oder aktualisiere Codex nach dem Kopieren.
3. Entferne doppelte Skill-Namen.
4. Rufe `coff0xc-skill-router` explizit auf.

## Sicherheitsgrenze

Nutze es nur für eigene oder ausdrücklich autorisierte Assets, Code, Logs, Samples, Labs und Trainingsumgebungen. Nicht für unautorisierten Zugriff, Credential-Diebstahl, Persistenz, Evasion, C2, Phishing-Sammlung, Datenabfluss oder destruktive Aktionen verwenden.
