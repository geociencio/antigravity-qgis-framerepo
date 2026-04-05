# Antigravity QGIS Reference (Gen 5)

## 🏗️ QGIS Architecture
- **Extract-then-Compute**: Mandated for all processing logic.
- **Core/GUI Separation**: Never import qgis.gui in core/.
- **QgsTask**: Use for all long-running operations.

## 🚀 QGIS Commands
- `uv sync`: Setup dependencies.
- `python3 scripts/skill_sync.py`: Sync agent system.
- `make docker-test`: Run native QGIS integration tests.
