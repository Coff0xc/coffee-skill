# draw.io / diagrams.net Public Notes

Use these notes when the user asks why this skill outputs `.drawio` files.

## Public Source Findings

- diagrams.net/draw.io saves editable diagrams as XML and commonly uses the `.drawio` extension.
- draw.io lets users view and edit diagram XML source through `Extras > Edit Diagram`; the page XML starts and ends with `<mxGraphModel>`.
- draw.io can open shared diagram data from `.drawio`, `.xml`, `.png`, `.svg`, and `.pdf` when diagram data is embedded.
- draw.io can insert Mermaid diagrams through `Arrange > Insert > Advanced > Mermaid`, but Mermaid is only an intermediate option here; this skill should still deliver editable draw.io output.

## Practical Consequences

- Prefer `.drawio` for source-controlled, editable research figures.
- Treat PNG/SVG/PDF as preview/export formats.
- Keep diagram structure as nodes and edges before generating XML.
- Do not claim raster exports were produced unless a real export command or UI action ran.

## Official References

- https://www.drawio.com/doc/faq/export-to-xml
- https://www.drawio.com/doc/faq/diagram-source-edit
- https://www.drawio.com/blog/share-to-edit-diagrams
- https://www.drawio.com/doc/faq/arrange-insert-menu
