# coffee-skill riferimento italiano

## Che cos'è

`coffee-skill` è un pacchetto di skill per Codex. Copre ingegneria software, AI Agent/RAG, API e dati, UI e documenti, sicurezza difensiva, rilevamento, risposta agli incidenti e gestione delle vulnerabilità.

## Perché esiste

- Troppe skill piccole rendono poco affidabile l'attivazione automatica.
- Molti client scelgono le skill soprattutto dal frontmatter `name` e `description` in `SKILL.md`.
- I workflow di sicurezza richiedono limiti chiari di autorizzazione e uso difensivo.
- Il lavoro reale richiede passaggi verificabili, non solo consigli generici.

## Perché usarlo

- Consolida 87 skill sorgente in 15 skill complete.
- `coff0xc-skill-router` è il fallback quando una skill specifica non si attiva.
- Ogni skill include ambito, esclusioni, matrice di capacità, fasi, livelli di evidenza, gate, validazione e anti-pattern.
- La sicurezza resta focalizzata su difesa autorizzata, rilevamento, hardening, verifica e report.

## Come usarlo

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-detection-response to write detection rules.
```

Se l'attivazione automatica non funziona:

```text
Use coff0xc-skill-router to choose the right skill.
```

## Dove usarlo

- Directory locali delle skill Codex.
- Client compatibili con cartelle `SKILL.md`.
- Engineering, sistemi AI, documentazione, sicurezza difensiva, detection e gestione vulnerabilità.

## Se il trigger fallisce

1. Controlla che il nome della cartella corrisponda al frontmatter `name`.
2. Riavvia o aggiorna Codex dopo la copia.
3. Rimuovi nomi skill duplicati.
4. Invoca esplicitamente `coff0xc-skill-router`.

## Limite di sicurezza

Usalo solo su asset, codice, log, campioni, lab e ambienti di training che possiedi o sei autorizzato a valutare. Non usarlo per accesso non autorizzato, furto di credenziali, persistenza, evasione, C2, raccolta phishing, esfiltrazione o azioni distruttive.
