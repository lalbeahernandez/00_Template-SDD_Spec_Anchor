# Fuente de skills propia (`runkids/skillshare`)

Este directorio corresponde al modo proyecto **visible** de Skillshare.
La fuente es `skills/` y los destinos en `config.yaml` son `claude`, `codex`
y `opencode`, todos en modo `copy` (Windows).

Actualmente contiene solo `skills/coordinar-entrega/SKILL.md`, tomada de la
plantilla de coordinación de la guía. **No** contiene `spec-generator`.
No se han creado skills back/front/análisis/verificación: deben surgir de
procedimientos y ejemplos aprobados, sin duplicar las reglas de `AGENTS.md`.

```powershell
skillshare sync -p --dry-run
skillshare sync -p
skillshare status -p
```

No edites las copias de `.claude/skills/`, `.agents/skills/` ni
`.opencode/skills/`. Nunca copies las skills `openspec-*` aquí:
`openspec init` y `openspec update` mantienen sus archivos directamente
bajo los directorios específicos de cada herramienta.

La carpeta `agents/` está vacía. El ZIP conserva las carpetas vacías por
medio de entradas de directorio; Git no las versionará hasta que incluyan
archivos. No se añaden `.gitkeep` artificiales.

Guías oficiales: https://github.com/runkids/skillshare y
https://github.com/runkids/skillshare/blob/main/website/docs/understand/project-skills.md
