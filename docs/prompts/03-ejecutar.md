# Prompt 03-ejecutar

Plantilla derivada de la guía. Sustituye `mi-cambio` por el ID real y verifica
que las skills indicadas estén instaladas.

```text
Apruebo los documentos revisados del cambio "mi-cambio"
en openspec/changes/mi-cambio/ y autorizo ejecutar sus tareas.
Usa la revisión que acabo de aprobar; identifica su referencia antes de empezar.

Usa $astra-advisor:orchestration siguiendo AGENTS.md.
Astra coordina. Usa tasks.md como lista única y no replantees el cambio.
Asigna sesiones independientes, no subagentes, con goal, contexto mínimo,
skills pertinentes y acceso a los documentos aprobados. Respeta dependencias.
Solo Astra actualiza tasks.md: las sesiones devuelven cambios y evidencias.
No lances $openspec-apply-change como otro flujo independiente.

Verifica al terminar cada implementación según AGENTS.md; antes, solo lo
imprescindible. Revisa la integración y haz un commit por tarea con cambios.
No reinstales, no hagas push, no despliegues y no archives todavía.
Si falta capacidad, hay un bloqueo o cambia el alcance, informa y detente
para acordarlo; no cambies requisitos sin aprobarlos. Entrega hashes reales.
```
