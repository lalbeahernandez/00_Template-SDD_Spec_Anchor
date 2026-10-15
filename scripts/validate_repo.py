#!/usr/bin/env python3
"""Comprobaciones estáticas sin instalaciones de herramientas externas."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def require(path: str) -> str:
    p = ROOT / path
    if not p.is_file():
        errors.append(f"No existe: {path}")
        return ""
    return p.read_text(encoding="utf-8")

source = require("skillshare/config.yaml")
config = require("openspec/config.yaml")
policy = require("AGENTS.md")
import_file = require("CLAUDE.md")
skill = require("skillshare/skills/coordinar-entrega/SKILL.md")
readme = require("README.md")
for path in ("docs/PREPARACION.md", "docs/FLUJO-DIARIO.md", "docs/CUMPLIMIENTO-GUIA.md",
             "docs/INSTALACION-WINDOWS.md", "docs/PLANTILLA-TAREA.md"):
    require(path)

for target in ("claude", "codex", "opencode"):
    if not re.search(rf"(?m)^\s*- name:\s*{target}\s*$", source):
        errors.append(f"Falta destino {target} en Skillshare")
if source.count("mode: copy") != 3:
    errors.append("Los tres destinos Skillshare deben usar mode: copy")
if not re.search(r"(?m)^skills:\s*\[\s*\]\s*$", source):
    errors.append("No declarar skills remotas no instaladas: se esperaba skills: []")
if not re.search(r"(?m)^schema:\s*spec-driven\s*$", config):
    errors.append("OpenSpec debería usar schema: spec-driven")
for field in ("proposal", "specs", "design", "tasks"):
    if not re.search(rf"(?m)^\s*{field}:\s*$", config):
        errors.append(f"Falta OpenSpec rule {field}")
for phrase in ("/plan", "tasks.md", "coordinar-entrega", "commit", "Astra", "verificación"):
    if phrase.casefold() not in policy.casefold():
        errors.append(f"Falta política {phrase}")
if import_file.strip() != "@AGENTS.md":
    errors.append("CLAUDE.md debe importar AGENTS.md")
if "name: coordinar-entrega" not in skill or "description:" not in skill:
    errors.append("SKILL.md inválida: frontmatter ausente")
if "AGENTS.md" not in skill:
    errors.append("La skill debe referir la política central AGENTS.md")
for p in ROOT.rglob("*"):
    if "spec-generator" in str(p).lower():
        errors.append(f"spec-generator no debe existir: {p.relative_to(ROOT)}")
if "runkids/skillshare" not in readme:
    errors.append("README debe identificar el gestor Skillshare correcto")
# Los directorios vacíos se conservan en el ZIP, no en Git hasta añadir archivos.
if errors:
    print("ERROR: " + "\nERROR: ".join(errors), file=sys.stderr)
    sys.exit(1)
print("OK: estructura, targets, esquema, skill y políticas básicas coherentes.")
