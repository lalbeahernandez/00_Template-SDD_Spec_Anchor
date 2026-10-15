# Preparación de Windows (sin instalaciones automáticas)

Todos los comandos se lanzan desde la **raíz del proyecto de código** que
se quiera configurar. Evita ejecutar instalaciones sin la aprobación y permisos
del equipo; anota versiones y salidas en `docs/PREPARACION.md` (o equivalente).

## 1. Preflight

```powershell
.\scripts\check-environment.ps1
python .\scripts\validate_repo.py
Get-Location
git status --short
git branch --show-current
```

Confirma cuenta autorizada de cada agente, permisos, Node, cambios locales,
acceso a Git y comportamiento de Windows. Revisa `README.md` y `AGENTS.md`.
No pegues claves o código de clientes en herramientas no aprobadas.

## 2. Skillshare (runkids/skillshare)

Instala Skillshare siguiendo la documentación oficial y revisando antes el
instalador. En sistemas que lo requieran, usa `mode: copy` como ya indica
`skillshare/config.yaml`. No repitas `skillshare init -p` sobre esta
estructura existente.

```powershell
skillshare --version
skillshare sync -p --dry-run
skillshare sync -p
skillshare status -p
```

## 3. OpenSpec (Fission-AI)

Node.js requerido >= **20.19.0**. Verifica la versión en el mismo entorno que
utiliza Codex/Claude Code/OpenCode. Tras autorizar la versión e instalación:

```powershell
node --version
npm --version
npm install -g @fission-ai/openspec@latest
openspec --version
```

`@latest` es una referencia mutable; registrar la versión exacta instalada o
sustituir por una aprobada para fijar reproducibilidad.
Si ya hay `openspec/` o skills generadas, inspección previa obligatoria.
La config del repo **no** implica que la CLI esté instalada o inicializada.

```powershell
# Después de revisar configuración y permisos:
openspec init --tools claude,codex,opencode
git status --short
```

Para una instalación restringida al flujo Codex de la guía se podría usar
`openspec init --tools codex`. La variante de arriba añade el soporte que
solicitaste para los tres. No usar `--force` para borrar archivos existentes.
No copiar `openspec-*` a Skillshare; OpenSpec gestiona sus copias. Revisar
rutas, variantes reales de invocación y reiniciar sesiones si no aparecen.

## 4. Astra Advisor (Codex: plugin de terceros)

```powershell
# Ejemplo publicado; NO ejecutar sin revisar y aprobar versión y permisos.
codex plugin marketplace add DannyMac180/astra-advisor --ref main
codex plugin add astra-advisor@astra-advisor
```

La skill suele invocarse como `$astra-advisor:orchestration` **en Codex cuando
el plugin esté instalado y reconocido**. No cambia el modelo principal ni
convierte mágicamente a otros hosts en ejecutores compatibles. Comprueba
si el entorno puede crear sesiones independientes reales. La coordinación de
sesiones separadas NO equivale a delegación predeterminada de subagentes.

## 5. Graft (revisar antes de init real)

```powershell
# Son referencias de la guía, sujetas a autorización del equipo.
npm install -g @nanonets/graft
graft init --agents agents --no-global --dry-run
# Solo si la simulación y los permisos son aceptados:
graft init --agents agents --no-global
graft build
graft map
```

La capa conceptual `--deep`, el proveedor de modelo, la telemetría y la salida
de código requieren evaluación aparte. La caché `graft/` no se versiona.
Revisa cualquier bloque que añada a AGENTS.md antes de incorporarlo.

## 6. Ponytail (Codex: plugin de terceros)

```powershell
# Opcional; aprobación previa de hooks, scripts y compatibilidad.
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```

Inspecciona `/hooks` y versiones antes de ejecutarlos. En Claude/OpenCode
aplica el principio de simplicidad mediante `AGENTS.md` si no hay integración
confirmada del plugin; no declares el plugin instalado allí.

## 7. Consolidar y comprobar

Revisa conflictos entre `AGENTS.md`, bloques de Graft y `openspec/config.yaml`;
no reemplaces reglas válidas existentes. Confirma skills con su ruta, modelos
y capacidades disponibles. Abre sesión nueva para que los agentes detecten
configuración recién generada. Actualiza `docs/PREPARACION.md` con **hechos**.

No crees cambios OpenSpec ni inicies implementación como consecuencia de
instalar herramientas: eso ocurre más adelante, tras `/plan` y aprobaciones.
