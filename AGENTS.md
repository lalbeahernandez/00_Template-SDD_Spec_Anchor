# AGENTS.md — Acuerdos de trabajo compartidos

## Ámbito y fuentes de verdad
- Reglas comunes del repositorio para Claude Code, Codex y OpenCode.
- `CLAUDE.md` importa este archivo; comprobar las instrucciones realmente reconocidas.
- `skillshare/skills/` es la fuente única de skills **propias** distribuidas por
  `runkids/skillshare` a `.claude/skills/`, `.agents/skills/`, `.opencode/skills/`.
- Las skills `openspec-*` y los comandos OpenSpec los administra **OpenSpec**.
  No copiarlos a `skillshare/skills/` ni modificarlos manualmente.
- `openspec/config.yaml` define contexto/reglas documentales, no instala CLI/plugins.
- Las invocaciones (`/plan`, `$openspec-propose`, `$astra-advisor:orchestration`,
  `/goal`) dependen de cada host: usa la equivalencia disponible y verificada.
- NO presupongas que Codex plugins o modelos específicos funcionen en Claude
  Code u OpenCode. Si no están disponibles, solicita alternativa aprobada.

## Estado de la preparación
Para aplicar el flujo completo de la guía, comprueba Astra Advisor, Graft,
Ponytail, OpenSpec y las skills pertinentes, o alternativas acordadas.
Registra capacidades y versiones comprobadas. No des por instalado nada
por aparecer en este archivo. No reinstales herramientas en cada encargo.

## Antes de actuar
Lee los AGENTS.md aplicables, README, comandos del repo y estado de Git.
Preserva cambios locales, controles obligatorios y bloques de herramientas.
No publiques ni despliegues sin autorización. No expongas secretos.

## Entrada: /plan -> documentar con OpenSpec -> aprobar -> Astra
Cada encargo funcional comienza en /plan, sin implementar ni escribir archivos.
Consulta las especificaciones existentes y acuerda el alcance y los goals.
Tras salir de /plan, la primera autorización permite SOLO documentar el cambio
con $openspec-propose. No equivale a permiso para implementar.
Revisa los documentos, registra el ID y la revisión aprobada, y espera la
aprobación explícita de ejecución antes de usar $astra-advisor:orchestration.
Ejecuta ese plan, no otro. Si cambia el alcance, actualiza los documentos
afectados y solicita nueva aprobación antes de ejecutar lo nuevo.

## OpenSpec: alcance y fuente única del encargo
Usa el esquema y configuración comprobados en openspec/config.yaml.
Por defecto, usa OpenSpec para funcionalidades y cambios no triviales.
Una corrección trivial solo omite estos documentos mediante una excepción
acordada; conserva /plan, goal, verificación y las reglas de Git.
El cambio activo vive en openspec/changes/<cambio>/; las especificaciones
consolidadas están en openspec/specs/. Lee solo las partes relevantes.
proposal.md, specs/, design.md y tasks.md son los documentos del esquema
spec-driven. Respeta el esquema instalado si usa una estructura distinta.
Personaliza config.yaml y esta política; no edites las skills generadas.
No des por aprobada una propuesta solo porque existe o la CLI la valida.

## Coordinación y estado compartido
Astra es el único responsable de actualizar tasks.md y aceptar entregas.
Cada sesión recibe el cambio, la tarea, sus requisitos y los archivos necesarios;
no debe editar por su cuenta los documentos compartidos ni otra tarea.
Asegura que cada worktree recibe la revisión aprobada de los documentos.
No mantengas otra lista autoritativa en el chat ni lances por separado
$openspec-apply-change como un ejecutor rival. Si se usa, será dentro
de la coordinación de Astra, con las mismas reglas y tareas.
Marca la casilla de una tarea solo cuando su verificación y revisión estén
resueltas. Si existe un bloqueo o falta evidencia, deja el estado pendiente.

## Roles
Astra recibe el cambio documentado y aprobado, coordina y acepta entregas.
Luna, en Max si está disponible, implementa las tareas definidas.
Terra o GPT-6.1 Sol, si está disponible, asesora sobre dudas acotadas.
Comprueba modelos y esfuerzos reales: este archivo no los configura.

## Un goal por tarea
Cada tarea tendrá ID, goal observable, alcance y exclusiones, archivos,
contexto de entrada, skills, dependencias, responsable, aceptación,
verificación prevista y condición de parada. Acuerda límites de intentos.
Fija el goal en cada sesión con /goal si lo admite; si no, en sus instrucciones.

## Sesiones independientes, no subagentes
Es la estrategia solicitada. Comprueba que puedes abrir sesiones,
darles instrucciones y recuperar resultados; no simules esa capacidad.
Entrega solo goal, instrucciones aplicables, skills, contratos y contexto
necesario. Coordina mediante resúmenes y evidencias, no historiales completos.
Usa worktrees para escrituras paralelas y evita solapamientos de archivos.
Si no es posible, informa y acuerda otra estrategia antes de continuar.

## Skills aplicables: catálogo real
- Coordinación: `coordinar-entrega`, fuente
  `skillshare/skills/coordinar-entrega/SKILL.md`, tras `skillshare sync -p`.
  Úsala exclusivamente tras aprobar el cambio OpenSpec y su revisión; requiere
  la capacidad de coordinación real y aprobada.
- OpenSpec: registrar después de `openspec init` las `openspec-*` **reales** de
  cada host y su ruta; no se suministran dentro de Skillshare.
- Las skills de back/front/análisis/verificación están pendientes de crear a
  partir de ejemplos aprobados del proyecto; no se atribuye contenido inexistente.
Completa o elimina los siguientes campos cuando existan skills verdaderas:
- Back: [nombre y ruta reales] -- cambios en API, lógica y datos.
- Front: [nombre y ruta reales] -- componentes, estados y estilos.
- Análisis/gráficos: [nombre y ruta reales] -- cuando lo pida la tarea.
- Verificación: [nombre y ruta reales] -- validación del cambio.
- Coordinación adicional: [solo si hay un procedimiento distinto confirmado].
- OpenSpec: [skills generadas realmente disponibles] -- documentar y cerrar.
Los corchetes son campos pendientes, no skills instaladas.
Aplica las pertinentes a cada tarea; no cargues todas ni copies sus cuerpos.
Todas las skills y roles remiten a la política de verificación de este archivo.
No hay skills corporativas de back/front cargadas por defecto.
No inventes estándares ni URLs de repos ajenos.

## Límites de herramientas externas
Astra Advisor y Ponytail son plugins de Codex de terceros: ni su instalación
ni sus hooks están autorizados por este repositorio. Graft no se ejecuta
sin revisar el `--dry-run`. En otros hosts, acuerda una alternativa si no
existe compatibilidad comprobada. Registrar versiones y capacidades reales
según `docs/PREPARACION.md` antes de trabajo funcional.

## Graft y Ponytail
Usa Graft para localizar contexto y confirma la información en el código.
No cargues todo el grafo en cada sesión; no publiques cachés ni secretos.
Capa conceptual, proveedores, telemetría y configuración global requieren
revisión y autorización. Respeta los permisos de las herramientas.
Aplica Ponytail: reutiliza patrones y resuelve solo el alcance aprobado.
No añadas dependencias, abstracciones ni refactors especulativos.
No recortes seguridad, validación, accesibilidad ni manejo de errores.

## Política única de verificación
No ejecutes tests tras cada edición. Al terminar la implementación de una
tarea, revisa el diff y verifica lo modificado y sus dependencias afectadas.
Antes de ese punto, ejecuta solo lo imprescindible para reproducir un fallo
o desbloquear una decisión. Añade o actualiza pruebas según el cambio y riesgo.
No crees suites ajenas al alcance ni cobertura por volumen.
No omitas CI, seguridad, revisiones de Astra ni controles obligatorios.
Justifica ampliaciones u omisiones. No afirmes éxitos sin evidencias.
Valida las especificaciones al preparar su aprobación y tras cambios relevantes
con openspec validate <cambio> --strict. No sustituye pruebas de la aplicación.

## Commit por tarea y entrega
Tras verificación y revisión, crea un commit atómico por tarea con cambios,
con su ID y descripción conforme al repo. Incluye solo archivos de esa tarea.
No mezcles cambios ajenos, no crees commits vacíos ni alteres identidades Git.
No hagas push, merges protegidos ni despliegues sin autorización.
Entrega ID, goal, estado, sesión, skills, cambios, verificación, riesgos y hash.
Comprueba la integración. Si falta validación imprescindible, la tarea no
está terminada. Informa del consumo solo cuando haya datos observados.

## Cierre documental y archivo
Trata la preparación documental y el cierre como tareas acotadas con sus goals.
Versiona openspec/ y las skills generadas según las reglas del repo; separa los
commits documentales de los funcionales cuando sean tareas diferentes.
Entrega hashes en el informe: no intentes incluir un hash en su propio commit.
Tras revisar tareas e integración y recibir autorización, sincroniza las specs
y archiva el cambio mediante las skills disponibles. Revisa el diff, no
sobrescribas cambios de otros, registra la ruta real archivada y el commit.
No uses el archivo como excusa para ignorar pendientes o saltar validaciones.
No borres el historial ni hagas push o despliegue por haber archivado.
