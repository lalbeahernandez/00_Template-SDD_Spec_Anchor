# Compatibilidad, límites y responsabilidades

| Sistema | Claude Code | Codex | OpenCode |
|---|---|---|---|
| Reglas compartidas | `CLAUDE.md` importa `AGENTS.md` | `AGENTS.md` | `AGENTS.md`, verificar lectura |
| Skillshare propio | `.claude/skills/` | `.agents/skills/` | `.opencode/skills/` |
| OpenSpec skills | Generadas por `openspec init` | Generadas por `openspec init` | Generadas por `openspec init` |
| OpenSpec invocación | Según host y archivos generados | P.ej. `$openspec-propose` | Según host y archivos generados |
| Astra Advisor | Sin soporte afirmado | Plugin de terceros, opcional | Sin soporte afirmado |
| Ponytail | Aplicar simplicidad en reglas | Plugin de terceros, opcional | Aplicar simplicidad en reglas |
| Graft | Verificar entorno | Verificar entorno | Verificar entorno |

**Roles:** Astra coordina y acepta, Luna en Max implementa y Terra/otro modelo
asesora **solo si** las versiones, nombres, esfuerzos y capacidades de la
cuenta permiten hacerlo. Declarar un rol en Markdown no configura modelos.

**Dos propietarios para un mismo destino de skills:**

- **Skillshare** distribuye `coordinar-entrega` (y futuras skills propias).
- **OpenSpec** genera/actualiza `openspec-*` directamente para cada host.

Ambos pueden depositar carpetas diferentes bajo `.agents/skills/` o similares.
Inspecciona el diff y el `skillshare sync -p --dry-run` antes de sincronizar,
y evita nombres duplicados. El `.gitignore` ignora copias de Skillshare,
pero permite versionar los directorios `openspec-*` generados por OpenSpec,
según la recomendación de la guía. Si la política de tu equipo difiere,
ajusta los patrones sin ocultar archivos importantes de OpenSpec.

**Limitación de `copy`:** al editar una skill en `skillshare/skills/`, ejecuta
una nueva sincronización. Nunca edites la copia distribuida.
