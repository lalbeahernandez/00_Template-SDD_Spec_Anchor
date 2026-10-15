# Un plan, un cambio OpenSpec y una coordinación

**No** ejecutar instalaciones en cada encargo: sigue la preparación inicial.
En hosts sin modo `/plan` textual, activa el control real de planificación;
no simules que se ha activado. Los prompts bajo `docs/prompts/` siguen la guía.

## A. Planificar sin modificar archivos

- Abre planificación real (`/plan` si existe).
- Lee AGENTS.md, skills pertinentes, specs consolidadas y código necesario.
- Para cada tarea acuerda: **ID, goal observable, alcance, exclusiones, archivos,
  responsable, skills, dependencias, aceptación, verificación, parada y límite**.
- No escribas código, cambios OpenSpec, ni abras sesiones ejecutoras.
- Obtén conformidad sobre el plan y sal de planificación.

## B. Autorizar solo la documentación

- Solicita `$openspec-propose` **solo si la skill está disponible** en el host.
- Genera/actualiza `openspec/changes/<id>/proposal.md`, los deltas `specs/`,
  `design.md` y `tasks.md` del esquema `spec-driven` instalado.
- Valida cuando estén listos para aprobación: `openspec validate <id> --strict`.
- Haz commit de documentación si hay cambios y las reglas de Git lo permiten.
- Detente. **Documentar NO autoriza implementar.**

## C. Aprobación explícita de ejecución

- Revisa requisitos, alcance, IDs, aceptación, comandos de verificación.
- Identifica **ID y revisión exacta aprobada** del cambio.
- Si cambian requisitos, actualizar documentos y obtener nueva aprobación.

## D. Astra coordina la ejecución del MISMO cambio

- Si Astra Advisor está realmente disponible y autorizado en Codex, utiliza
  `$astra-advisor:orchestration` para la revisión aprobada.
- Preferencia: **sesiones independientes** con contexto mínimo y goal; no
  subagentes ni CLI anidados improvisados. Sin capacidad, acuerda alternativa.
- Usa worktrees para escrituras paralelas; no solapar los mismos archivos.
- `tasks.md` es **la única lista autoritativa**; solo Astra cambia su estado.
- No ejecutar `openspec-apply-change` por separado como flujo competidor.

## E. Verificación y commits

- Evita repetir pruebas tras cada edición. Al terminar **cada tarea**, revisa
  el diff y ejecuta pruebas relevantes del cambio y dependencias afectadas.
- Amplía pruebas para contratos, auth, seguridad, datos o servicios compartidos.
  CI/herramientas obligatorias nunca se omiten.
- Tras comprobar, commit atómico por tarea con cambios, por ejemplo
  `feat: [T01] nombre del cambio`. No commits vacíos ni `push` implícito.
- Entrega evidencia, riesgos, estado y hash. Comprobar además **integración**.

## F. Aceptación y cierre documental

- Recibe aprobación **separada** de cierre.
- Usa las skills OpenSpec de sincronización y archivo si están disponibles,
  evitando doble aplicación de deltas. Revisa diferencias y bloqueos.
- Commit documental de cierre cuando corresponda; registra la ruta archivada.
- Archivar **no** reemplaza validación ni autoriza despliegue/push.

Para erratas triviales puede acordarse una excepción ligera a OpenSpec, pero
se conservan plan, goal, verificación, seguridad y Git según AGENTS.md.
