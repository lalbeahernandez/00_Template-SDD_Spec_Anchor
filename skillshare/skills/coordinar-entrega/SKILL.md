---
name: coordinar-entrega
description: Ejecutar con Astra un cambio OpenSpec documentado y aprobado tras /plan, con goals, sesiones y evidencias. No usar para saltarse las aprobaciones ni para planificar un segundo encargo.
---

1. Leer los AGENTS.md aplicables. Comprobar herramientas y skills sin reinstalar.
2. Exigir ID, ruta y revisión del cambio aprobado. La aprobación para escribir
   documentación no autoriza implementar. Si falta autorización, detenerse.
3. Leer las especificaciones vigentes y los documentos relevantes del cambio.
   Usar tasks.md como lista única y conservar los IDs. No generar otro plan.
4. Usar $astra-advisor:orchestration con los roles y límites de AGENTS.md.
   Mantener una sola coordinación; no lanzar openspec-apply-change en paralelo.
5. Asignar a cada sesión ID, goal, alcance, archivos, skills, dependencias,
   aceptación, verificación y parada. Confirmar capacidades y permisos reales.
6. Preferir sesiones independientes, no subagentes. Dar contexto mínimo y
   acceso a la revisión aprobada. Coordinar worktrees y archivos sin solaparlos.
7. Usar las skills pertinentes, Graft para orientarse y Ponytail para simplificar.
   Respetar la política única de verificación y commits de AGENTS.md.
8. Recibir evidencias y revisar integración. Solo Astra actualiza tasks.md.
   No completar tareas con verificación imprescindible pendiente.
9. Registrar un commit por tarea con cambios. Informar hashes reales,
   bloqueos y consumo observado; no inventar resultados ni hacer push.
10. Ante cambios de alcance, actualizar la propuesta y pedir nueva aprobación.
11. Con el resultado aceptado y el cierre autorizado, sincronizar las specs,
    archivar y entregar la ruta y el commit documental reales. Si falta una
    skill o verificación necesaria, informar; no simular el cierre.

Consultar references/ejemplos.md solo si existe y contiene ejemplos aprobados.
