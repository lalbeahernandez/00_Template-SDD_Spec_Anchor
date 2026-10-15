# Prompt 02-documentar

Plantilla derivada de la guía. Sustituye `mi-cambio` por el ID real y verifica
que las skills indicadas estén instaladas.

```text
$openspec-propose

El plan de las tareas está acordado y ya he salido de /plan.
Autorizo SOLO documentar el cambio "mi-cambio".

Usa openspec/config.yaml y el plan acordado para redactar proposal.md,
las diferencias de specs/, design.md y tasks.md. No replanifiques.
Conserva los IDs, goals, alcance, skills, dependencias, aceptación,
verificación y condiciones de parada. No inventes rutas o comandos.
Revisa las especificaciones existentes para decidir qué se añade o modifica.
Valida el cambio con openspec validate mi-cambio --strict.
Trata esta preparación documental como una tarea con su commit, si procede
según AGENTS.md; no hagas push ni edites el código del producto.

Muestra los documentos, dudas y la revisión lista para aprobar.
No implementes, no abras sesiones ejecutoras y no archives. Detente.
```
