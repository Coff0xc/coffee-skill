# coffee-skill polska referencja

## Co to jest

`coffee-skill` to pakiet umiejętności dla Codex. Obejmuje inżynierię oprogramowania, AI Agent/RAG, API i dane, UI i dokumenty, bezpieczeństwo defensywne, detekcję, reakcję na incydenty i zarządzanie podatnościami.

## Dlaczego istnieje

- Zbyt wiele małych umiejętności sprawia, że automatyczne uruchamianie jest zawodne.
- Wiele klientów wybiera umiejętności głównie na podstawie frontmatter `name` i `description` w `SKILL.md`.
- Prace bezpieczeństwa wymagają jasnych granic autoryzacji i defensywnego użycia.
- Praktyczna praca wymaga weryfikowalnych kroków, a nie tylko ogólnych porad.

## Dlaczego warto używać

- Konsoliduje 87 źródłowych umiejętności w 15 szerokich skillów.
- `coff0xc-skill-router` działa jako fallback, gdy konkretna umiejętność się nie uruchomi.
- Każdy skill zawiera zakres, wyłączenia, macierz możliwości, fazy pracy, poziomy dowodów, bramki, walidację i antywzorce.
- Treści bezpieczeństwa pozostają skupione na autoryzowanej obronie, detekcji, utwardzaniu, weryfikacji i raportowaniu.

## Jak używać

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-detection-response to write detection rules.
```

Jeśli automatyczne uruchomienie nie zadziała:

```text
Use coff0xc-skill-router to choose the right skill.
```

## Gdzie używać

- Lokalne katalogi skillów Codex.
- Zgodne klienty ładujące foldery `SKILL.md`.
- Engineering, systemy AI, dokumentacja, defensywne bezpieczeństwo, detekcja i zarządzanie podatnościami.

## Gdy trigger zawiedzie

1. Sprawdź, czy nazwa folderu odpowiada frontmatter `name`.
2. Uruchom ponownie lub odśwież Codex po skopiowaniu.
3. Usuń zduplikowane nazwy skillów.
4. Wywołaj `coff0xc-skill-router` jawnie.

## Granica bezpieczeństwa

Używaj tylko wobec zasobów, kodu, logów, próbek, laboratoriów i środowisk szkoleniowych, które posiadasz lub masz wyraźną zgodę oceniać. Nie używaj do nieautoryzowanego dostępu, kradzieży poświadczeń, utrwalania dostępu, omijania zabezpieczeń, C2, phishingu, eksfiltracji danych ani działań destrukcyjnych.
