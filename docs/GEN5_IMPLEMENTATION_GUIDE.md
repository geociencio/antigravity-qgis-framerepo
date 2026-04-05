# Guía Maestra de Implementación: Antigravity Gen 5 🌍

Esta guía detalla el estándar **Antigravity Gen 5** para el desarrollo agéntico de plugins QGIS y proyectos Python avanzados. Este sistema prioriza la modularidad, la orquestación mediante MCP y la automatización del mantenimiento de la "memoria" del proyecto.

---

## 1. Principios Gen 5
- **Modularidad Basada en Directorios**: Las habilidades (skills) no son archivos sueltos, sino carpetas con contexto.
- **Orquestación MCP**: Interfaz estandarizada para que agentes externos interactúen con el dominio del proyecto.
- **Sincronización de Memoria**: Herramientas automáticas que mantienen `AGENTS.md` y `AI_CONTEXT.md` actualizados.
- **Seguridad "Portal-Ready"**: Escaneos locales que replican los criterios de aprobación de QGIS Plugin Portal.

---

## 2. Estructura del Repositorio

```text
/
├── .agent/                  # Núcleo Agéntico
│   ├── skills/              # Directorio de Habilidades (Gen 5)
│   │   └── <skill-name>/
│   │       └── SKILL.md     # Definición y Frontmatter
│   ├── workflows/           # Workflows Agénticos (.md)
│   ├── AGENTS.md            # Matriz de Capacidades (Auto-sync)
│   └── next_steps.md        # Memoria de Sesión (Paso de testigo)
├── docs/                    # Documentación Técnica
│   └── DEVELOPMENT_LOG.md   # Diario de Ingeniería (OBLIGATORIO)
├── scripts/                 # Herramientas de Automatización
│   ├── mcp_server.py        # Orquestación MCP
│   ├── security_scan.py     # Auditoría de Seguridad
│   └── skill_sync.py        # Sincronizador de Metadatos
├── pyproject.toml           # Configuración de uv y dependencias
└── AI_CONTEXT.md            # Análisis de Arquitectura (via ai-ctx)
```

---

## 3. Configuración del Entorno (uv)

Antigravity Gen 5 utiliza `uv` para una gestión de dependencias ultrarrápida y reproducible.

### Dependencias Críticas (`pyproject.toml`):
```toml
[project]
dependencies = [
    "ai-context-core>=3.0.1",
    "pyyaml>=6.0.1",
]

[dependency-groups]
dev = [
    "ruff>=0.4.0",
    "black==24.1.0",
    "bandit>=1.7.0",
    "detect-secrets>=1.5.0",
]
```

---

## 4. Implementación de Skills y Workflows

### Skills (Habilidades)
Cada skill debe residir en su carpeta dentro de `.agent/skills/`. El archivo `SKILL.md` debe incluir YAML frontmatter:

```markdown
---
name: nombre-de-la-habilidad
description: Qué hace la habilidad de forma concisa.
trigger: Cuándo debe el agente invocar esta habilidad.
---
# Instrucciones detalladas...
```

### Workflows (Flujos de Trabajo)
Los workflows guían al agente en tareas complejas mediante pasos numerados y validaciones.

---

## 5. Herramientas de Orquestación

### `skill_sync.py`
Mantiene la coherencia entre las carpetas de skills y la documentación centralizada.
- **Acción**: Lee todos los `SKILL.md`, valida sus metadatos y genera la tabla en `AGENTS.md`.

### `mcp_server.py`
Proporciona una interfaz JSON-RPC para que herramientas externas (como Claude Desktop o plugins de IDE) puedan llamar a herramientas específicas del dominio del proyecto (ej: `validate_geology`, `check_i18n`).

### `security_scan.py`
Ejecuta `bandit` y `detect-secrets`. Es esencial para asegurar que el código es apto para entornos de producción y cumple con los requisitos del portal QGIS.

---

## 6. Integración CI/CD (GitHub Actions)

Crea `.github/workflows/gen5-quality.yml` para automatizar la calidad:

```yaml
name: Antigravity Gen 5 Quality Gate

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh
      - name: Install dependencies
        run: uv sync --all-groups
      - name: Lint and Format check
        run: |
          uv run ruff check .
          uv run ruff format --check .
      - name: Security Scan
        run: uv run python scripts/security_scan.py
```

---

## 7. Protocolo de Gestión de Sesión

### Iniciar Sesión (`/inicia-sesion`)
1. Consultar `.agent/next_steps.md`.
2. Revisar `AI_CONTEXT.md` para métricas actuales.
3. Ejecutar `uv run ai-ctx analyze` para refrescar el estado cerebral.

### Cerrar Sesión (`/cierra-sesion`)
1. Documentar logros en `docs/DEVELOPMENT_LOG.md`.
2. Actualizar `.agent/next_steps.md` con los pendientes.
3. Ejecutar `uv run python scripts/skill_sync.py` para asegurar que la "memoria" agéntica esté sincronizada.
4. `git commit -m "chore(docs): close session [tema]"`

---

> [!TIP]
> La clave de Gen 5 es que el proyecto **se auto-describe**. Mantener `skill_sync.py` y `ai-ctx` como parte del flujo diario garantiza que la IA asistente nunca pierda el contexto.
