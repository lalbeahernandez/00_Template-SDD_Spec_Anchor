# Plantilla genérica para el `tasks.md` de un cambio APROBADO

No copiar esto como una lista de tareas real sin concretar el plan. OpenSpec
creará el archivo en `openspec/changes/<id>/tasks.md` según el esquema
instalado. `tasks.md` es el único checklist autoritativo del cambio.

```markdown
## 1. [Nombre del bloque]

- [ ] 1.1 [T01] [Título de tarea]
  Goal: [resultado observable]
  Alcance: [módulos, archivos reales y exclusiones]
  Responsable: [sesión/modelo observado, o capacidad pendiente]
  Contexto: [requisitos y revisión aprobada]
  Rutas y skills: [existentes y verificadas]
  Dependencias: [IDs]
  Aceptación: [comportamiento medible]
  Verificación: [comandos aplicables, según AGENTS.md]
  Parada: [goal verificado, bloqueo o límite acordado]
  Límite: [intentos/tiempo, si se acuerda]
```

Astra es el único responsable de cambiar casillas tras aceptación. Las sesiones
entregan evidencias, no compiten editando `tasks.md`.
