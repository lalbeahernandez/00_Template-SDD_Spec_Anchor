# Skillshare + OpenSpec — Claude Code, Codex y OpenCode

Usa [runkids/skillshare](https://github.com/runkids/skillshare), **no skills.sh**.

> **Alcance real**: este ZIP deja preparadas las **reglas, estructura y plantillas**;
> **no** instala los CLI ni plugins, no crea sesiones, no inicializa integrations
> OpenSpec en el equipo, no hace commits ni configura modelos. Confirma cada
> capacidad en el entorno de trabajo. No contiene `spec-generator`.

## Qué incluye

- **Una fuente de skills propia:** `skillshare/skills/` con una sola skill de
  coordinación `coordinar-entrega`. Back/front/análisis/verificación quedan
  pendientes de ejemplos aprobados (nada inventado).
- **Tres destinos** de Skillshare en modo `copy`: Claude Code (`.claude/skills/`),
  Codex (`.agents/skills/`) y OpenCode (`.opencode/skills/`).
- **OpenSpec `spec-driven`:** `openspec/config.yaml` con las reglas documentales
  de la guía. `openspec/specs/` y `openspec/changes/` están vacíos.
- **Normas permanentes:** `AGENTS.md` y `CLAUDE.md` (importa `AGENTS.md`).
- **Guías:** instalación Windows, preflight, flujo diario, prompts y trazabilidad
  requisito-archivo.
- **Validación estática:** `python scripts/validate_repo.py` y CI GitHub Actions.

## Preparación rápida (Windows / PowerShell)

1. Abre PowerShell **en la raíz del repo** y lee `AGENTS.md` y `docs/INSTALACION-WINDOWS.md`.
2. Comprueba el entorno (no instala ni modifica nada):

   ```powershell
   .\scripts\check-environment.ps1
   python .\scripts\validate_repo.py
   ```

3. Instala **con permisos aprobados** Skillshare y sincroniza las skills propias:

   ```powershell
   skillshare sync -p --dry-run
   skillshare sync -p
   skillshare status -p
   ```

4. Cuando corresponda y previa autorización, instala OpenSpec (Node >= 20.19.0)
   e inicializa su integración para **los tres** asistentes:

   ```powershell
   openspec --version
   openspec init --tools claude,codex,opencode
   git status --short
   ```

   Si ya existe OpenSpec, **revisa** configuración y diff antes de invocar init.
   No uses `--force`. OpenSpec genera sus propias skills y comandos en los
   directorios de cada host; **no** se replican mediante Skillshare. Tras ello
   inspecciona `.agents/skills/openspec-*`, `.claude/skills/openspec-*` y
   `.opencode/skills/openspec-*`, reinicia las sesiones y verifica invocaciones.

5. Revisa con el equipo la instalación de **Astra Advisor, Graft y Ponytail**;
   son herramientas **opcionales hasta su aprobación** y no se incluyen.
   Consulta `docs/INSTALACION-WINDOWS.md` y `docs/PREPARACION.md`.

## Flujo por encargo

**Plan en modo `/plan` (sin cambios) → OpenSpec solo documentación → revisión y
aprobación de la revisión → coordinación por Astra si está disponible → pruebas
focalizadas y commit por tarea → autorización de cierre → sync + archive.**

Autorizar documentar **NO** autoriza implementar; aprobar implementación **NO**
autoriza archivar, hacer push ni desplegar. Para hosts sin los mismos controles,
verifica las capacidades y acuerda el equivalente, sin simular acciones.
Consulta [`docs/FLUJO-DIARIO.md`](docs/FLUJO-DIARIO.md).

## Skillshare y OpenSpec no son el mismo gestor

| Contenido | Fuente y dueño | Regla |
|---|---|---|
| Skills propias (`coordinar-entrega`, futuras back/front) | `skillshare/skills/` | Editar la fuente, luego `skillshare sync -p` |
| Skills y comandos `openspec-*` | `openspec init`/`openspec update` | No copiarlos ni editarlos manualmente |
| Requisitos, cambios, estado | `openspec/` | `tasks.md` es el único checklist del cambio |
| Normativa compartida | `AGENTS.md` | Sin políticas de tests repetidas en skills |

`mode: copy` requiere resincronizar después de cambiar una skill propia. Si
una ruta ya contiene archivos creados por otra herramienta, revisar el plan de
sincronización; **no ejecutar `--force` para resolver conflictos a ciegas**.

## ¿Se usa como repositorio central o en un proyecto de código?

- **Repositorio central:** aquí se versionan skills, reglas y plantillas; el
  `openspec/` de esta raíz documentaría cambios **a este repo**, no a otro.
- **Otro proyecto:** adapta `AGENTS.md`, incorpora `CLAUDE.md` y `skillshare/`
  y configura **su propio** `openspec/` con la CLI y la política documental.
  Revisa reglas existentes y conflictos antes de copiar: no sobrescribas.

No hay URL de GitHub creada, ni dependencias del equipo instaladas.

## Documentación

- [`docs/INSTALACION-WINDOWS.md`](docs/INSTALACION-WINDOWS.md)
- [`docs/PREPARACION.md`](docs/PREPARACION.md)
- [`docs/FLUJO-DIARIO.md`](docs/FLUJO-DIARIO.md)
- [`docs/CUMPLIMIENTO-GUIA.md`](docs/CUMPLIMIENTO-GUIA.md)
- [`docs/INTEGRACIONES.md`](docs/INTEGRACIONES.md)
- [`docs/prompts/`](docs/prompts/)

Fuentes: [Skillshare](https://github.com/runkids/skillshare) ·
[OpenSpec](https://github.com/Fission-AI/OpenSpec) ·
[Astra Advisor](https://github.com/DannyMac180/astra-advisor).
