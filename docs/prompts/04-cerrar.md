# Prompt 04-cerrar

Plantilla derivada de la guía. Sustituye `mi-cambio` por el ID real y verifica
que las skills indicadas estén instaladas.

```text
El resultado del cambio "mi-cambio" está revisado.
Autorizo su cierre documental, NO el push ni el despliegue.

Bajo la misma coordinación, confirma que no quedan tareas ni verificaciones
imprescindibles pendientes y que la integración tiene evidencias.
Usa $openspec-sync-specs para sincronizar las diferencias aprobadas con
openspec/specs/. Revisa el diff y después usa $openspec-archive-change.
No vuelvas a aplicar diferencias que ya están sincronizadas.
Si hay conflictos, tareas incompletas o una skill no disponible, informa
sin simular el cierre ni saltar comprobaciones.
Registra el commit documental de cierre y entrega su hash, la ruta real
archivada, los requisitos actualizados y los riesgos residuales.
```
