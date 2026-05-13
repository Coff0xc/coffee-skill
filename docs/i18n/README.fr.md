# coffee-skill référence française

## Qu'est-ce que c'est

`coffee-skill` est un pack de compétences pour Codex. Il couvre le développement logiciel, AI Agent/RAG, les API et les données, les interfaces et documents, la sécurité défensive, la détection, la réponse aux incidents et la gestion des vulnérabilités.

## Pourquoi ce pack existe

- Trop de petites compétences rendent le déclenchement automatique instable.
- Beaucoup de clients choisissent les compétences surtout à partir du frontmatter `name` et `description` de `SKILL.md`.
- Les workflows de sécurité ont besoin de limites claires d'autorisation et d'usage défensif.
- Le travail réel demande des étapes vérifiables, pas seulement des conseils génériques.

## Pourquoi l'utiliser

- Il consolide 87 compétences source en 15 compétences complètes.
- `coff0xc-skill-router` sert de routeur de secours quand aucune compétence précise ne se déclenche.
- Chaque compétence contient le périmètre, les exclusions, une matrice de capacités, les étapes, les niveaux de preuve, les points de blocage, la validation et les anti-patterns.
- La sécurité reste centrée sur la défense autorisée, la détection, le durcissement, la vérification et le reporting.

## Comment l'utiliser

Vous pouvez demander naturellement:

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-cloud-devsecops to review CI/CD and cloud risk.
```

Si le déclenchement automatique échoue:

```text
Use coff0xc-skill-router to choose the right skill.
```

## Où l'utiliser

- Répertoires locaux de compétences Codex.
- Clients compatibles avec les dossiers `SKILL.md`.
- Ingénierie, systèmes IA, documentation, sécurité défensive, détection et gestion des vulnérabilités.

## Si le déclenchement échoue

1. Vérifiez que le nom du dossier correspond au frontmatter `name`.
2. Redémarrez ou rafraîchissez Codex après la copie.
3. Supprimez les noms de compétences en double.
4. Appelez explicitement `coff0xc-skill-router`.

## Limite de sécurité

Utilisez ce pack uniquement sur des actifs, du code, des journaux, des échantillons, des laboratoires ou des environnements de formation que vous possédez ou pour lesquels vous avez une autorisation explicite. Ne l'utilisez pas pour un accès non autorisé, le vol d'identifiants, la persistance, l'évasion, le C2, la collecte de phishing, l'exfiltration de données ou des actions destructrices.
