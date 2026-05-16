# coffee-skill referencia en español

## Qué es

`coffee-skill` es un paquete de skills para Codex. Cubre ingeniería de software, AI Agent/RAG, API y datos, UI y documentos, seguridad defensiva, detección, respuesta a incidentes y gestión de vulnerabilidades.

## Por qué existe

- Demasiadas skills pequeñas pueden hacer que el disparo automático sea poco fiable.
- Muchos clientes eligen skills principalmente desde el frontmatter `name` y `description` de `SKILL.md`.
- Las tareas de seguridad necesitan límites claros de autorización y uso defensivo.
- El trabajo real necesita pasos verificables, no solo recomendaciones generales.

## Por qué es útil

- Consolida 91 skills/workflows de origen en 17 skills de capacidad amplia más un router.
- Agrega `coff0xc-skill-router` como ruta de respaldo cuando no se activa una skill específica.
- Cada skill incluye alcance, exclusiones, matriz de capacidades, fases de trabajo, niveles de evidencia, controles duros, validación y antipatrones.
- La seguridad se mantiene enfocada en defensa autorizada, detección, endurecimiento, verificación y reporte.

## Cómo usarlo

Puedes pedirlo de forma natural:

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-detection-response to write detection rules.
```

Si no se activa automáticamente:

```text
Use coff0xc-skill-router to choose the right skill.
```

## Dónde usarlo

- Directorios locales de skills de Codex.
- Clientes compatibles con carpetas `SKILL.md`.
- Desarrollo, sistemas de IA, documentación, seguridad defensiva, detección y gestión de vulnerabilidades.

## Si falla el disparo automático

1. Verifica que el nombre de la carpeta coincida con el frontmatter `name`.
2. Reinicia o actualiza Codex después de copiar.
3. Elimina nombres de skill duplicados.
4. Invoca `coff0xc-skill-router` explícitamente.

## Límite de seguridad

Úsalo solo con activos, código, registros, muestras, laboratorios o entornos de formación propios o explícitamente autorizados. No lo uses para acceso no autorizado, robo de credenciales, persistencia, evasión, C2, recolección de phishing, exfiltración de datos o acciones destructivas.
