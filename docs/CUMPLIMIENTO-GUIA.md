# Matriz de cumplimiento de la guía aportada

Se adapta su flujo Codex a tres hosts **sin inventar compatibilidad universal**.

| Paso | Requisito | Implementación en repo | Lo que queda por realizar en el equipo |
|---|---|---|---|
| 1 | Cuenta, repo y Git | `AGENTS.md`, `docs/PREPARACION.md` | Verificar cuenta, ruta, rama y cambios locales |
| 2 | Astra Advisor | `docs/INSTALACION-WINDOWS.md`, `AGENTS.md` | Autorizar, instalar, comprobar skill y sesiones |
| 3 | Graft | Instrucciones dry-run y caché ignorada | Aprobar instalación y revisar `graft init --dry-run` |
| 4 | Ponytail | Política de simplicidad | Revisar plugin, hooks y permisos (Codex) |
| 5 | OpenSpec | `openspec/config.yaml` con `spec-driven` | Instalar CLI, `init --tools` y comprobar skills reales |
| 6 | Skills del proyecto | `coordinar-entrega` en Skillshare | Elicitar ejemplos reales para back, front, análisis, tests |
| 7 | Sesiones independientes | Regla, formato de entrega y preflight | Confirmar capacidades; plan de worktrees |
| 8 | Verificaciones | Política única en `AGENTS.md` | Identificar comandos de tests reales del proyecto |
| 9 | Commits por tarea | Política atómica y límites de autorización | Git real, hooks y evidencias |
| 10 | Consolidar `AGENTS.md` | Archivo raíz, import en Claude y catálogo | Revisar reglas preexistentes y plugins que lo modifiquen |
| 11 | `/plan` → OpenSpec → Astra → cierre | `docs/FLUJO-DIARIO.md`, prompts y plantillas | Activar modos y aprobar cada fase por separado |

**No cubierto automáticamente:** instalación de CLI, autorización de terceros,
selección de modelo/effort, reconocimiento de skills por el host, políticas
corporativas no aportadas, creación de cambios de producto, ejecución de tests,
commits funcionales, push o despliegue.

**Exclusiones intencionales:** `spec-generator` (eliminada por petición),
skills de back/front inventadas, tareas OpenSpec de ejemplo tomadas como tareas
reales, y una integración ficticia de Astra con Claude/OpenCode.

Los flujos de OpenSpec pueden variar según perfil/versión: inspecciona lo
generado antes de utilizar nombres de skills de la guía. `AGENTS.md` define
normas permanentes; `openspec/config.yaml` define documentos y no lo sustituye.
