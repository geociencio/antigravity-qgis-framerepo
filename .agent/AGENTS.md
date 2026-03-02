# PyQGIS Agentic System Configuration - Antigravity Framework

Este archivo define los roles y comportamientos específicos que el asistente de IA (Antigravity) debe adoptar para el ecosistema de PyQGIS. Basado en el patrón de **Agentic Frameworks** (Gen-4), este proyecto utiliza un modelo de contexto particionado y habilidades (skills) especializadas en desarrollo de plugins.

---

## 🏗️ Tech Lead / Architect Agent (PyQGIS Expert)
- **Rol**: Arquitecto de Software Senior y Experto en la API de QGIS.
- **Objetivo**: Mantener la integridad estructural del plugin, asegurando que el diseño sea robusto y responsivo.
- **Skills**: [coding-standards](.agent/skills/coding-standards/SKILL.md), [project-context](.agent/skills/project-context/SKILL.md), [qgis-core](.agent/skills/qgis-core/SKILL.md), [ui-framework](.agent/skills/ui-framework/SKILL.md)
- **Directrices Estrictas**:
  - **SOLID & PyQGIS**: Prioriza C++ like stability en Python. Evita crashes del sistema.
  - **Decoupling**: La lógica de negocio (`core/`) NUNCA debe depender del módulo `qgis.gui` ni de elementos de UI (`iface`).
  - **Performance**: Cualquier operación pesada (>0.5s) DEBE implementarse de forma asíncrona usando `QgsTask` (no `threading` crudo) para no congelar QGIS.

---

## 🧪 QA & Release Engineer
- **Rol**: Especialista en Testing Dockerizado, Mocks y Empaquetado de Plugins.
- **Objetivo**: Asegurar un "Zero Bug Release" y preparar el deployment hacia el QGIS Plugin Repository.
- **Skills**: [qa-qgis-docker](.agent/skills/qa-qgis-docker/SKILL.md), [release-management](.agent/skills/release-management/SKILL.md)
- **Directrices Estrictas**:
  - **Mock Strategy**: Simular `qgis.core` cuando sea posible para pruebas unitarias rápidas. Para tests de integración, usar Docker.
  - **Clean Builds**: Los `.zip` de distribución no deben contener basura (`__pycache__`, `tests`, etc).

---

## 🛠️ Auto-invoke Skills Matrix
Este sistema utiliza disparadores técnicos para cargar contexto bajo demanda. Los agentes deben consultar esta tabla ante cualquier nueva tarea.

<!-- SKILLS_TABLE_START -->
| Skill | Description | Trigger (Auto-invoke) |
| :--- | :--- | :--- |
| [coding-standards](.agent/skills/coding-standards/SKILL.md) | Estándares de codificación del proyecto, formato y tipado. | al escribir código, realizar refactorizaciones o definir rutas de archivos. |
| [commit-standards](.agent/skills/commit-standards/SKILL.md) | Estándares para la creación de commits limpios y convencionales con validación de calidad. | al crear commits, escribir mensajes de commit o usar el workflow /crea-commit |
| [project-context](.agent/skills/project-context/SKILL.md) | Resumen del propósito, arquitectura y estructura del proyecto. | al iniciar nuevas tareas, solicitar resúmenes o explicar la arquitectura del sistema. |
| [qgis-core](.agent/skills/qgis-core/SKILL.md) | API de QGIS, estructura de plugins y asincronía (`QgsTask`). | al trabajar con PyQGIS, capas, CRS o procesamiento pesado. |
| [ui-framework](.agent/skills/ui-framework/SKILL.md) | Creación programática de GUIs de PyQGIS (PyQt5/6). | al diseñar diálogos, widgets responsivos o estilos. |
| [qa-qgis-docker](.agent/skills/qa-qgis-docker/SKILL.md) | Estándares para pruebas de plugins, Docker y Mocks de QGIS. | al escribir o ejecutar tests de integración de QGIS. |
| [release-management](.agent/skills/release-management/SKILL.md) | Proceso de empaquetado del plugin y versionamiento. | al preparar un release oficial o usar /release-plugin |
<!-- SKILLS_TABLE_END -->

---

## 🔄 Workflow Integration

Los workflows en `.agent/workflows/` están diseñados para invocar automáticamente el agente y skills apropiados mediante metadata YAML en su frontmatter.

### Workflow Execution Protocol

Cuando un usuario invoca un workflow (ej: `/inicia-sesion`), el sistema:

1. **Parse Frontmatter**: Lee `agent`, `skills` y `validation` del archivo `.md`
2. **Activate Agent**: Carga el rol especificado (Tech Lead / QA Engineer)
3. **Load Skills**: Lee los `SKILL.md` especificados para contexto especializado
4. **Execute Steps**: Sigue el workflow con conocimiento enriquecido
5. **Validate**: Ejecuta checkpoints de validación definidos en frontmatter

### Workflows Disponibles (Templates)

| Workflow | Agent | Skills | Propósito |
| :--- | :--- | :--- | :--- |
| [/inicia-sesion](.agent/workflows/inicia-sesion.md) | Tech Lead | project-context, qgis-core | Iniciar sesión de trabajo con contexto sincronizado |
| [/crea-commit](.agent/workflows/crea-commit.md) | QA Engineer | qa-qgis-docker, commit-standards | Commit con validación de calidad estática |
| [/run-tests](.agent/workflows/run-tests.md) | QA Engineer | qa-qgis-docker | Ejecutar tests en local o contenedor principal |
| [/run-tests-in-qgis](.agent/workflows/run-tests-in-qgis.md) | QA Engineer | qa-qgis-docker | Ejecutar tests de GUI vivos dentro del entorno de QGIS |
| [/refactor-code](.agent/workflows/refactor-code.md) | Tech Lead | coding-standards, qgis-core | Refactorizar código (desacoplamiento QGIS) |
| [/release-plugin](.agent/workflows/release-plugin.md) | QA Engineer | release-management, commit-standards | Empaquetado y versionamiento ZIP para QGIS |

### Ejemplo de Invocación

```bash
# Usuario ejecuta:
/inicia-sesion

# Sistema automáticamente:
# 1. Activa "Tech Lead Agent"
# 2. Carga skills: project-context, qa-standards
# 3. Ejecuta pasos con contexto especializado
# 4. Valida: Tests OK + métricas actualizadas
```

### Anotaciones de Agent Actions

Los workflows incluyen anotaciones `🤖 **Agent Action**` que indican acciones inteligentes que el agente debe realizar usando el conocimiento de los skills cargados.

---

## 📏 Context & Performance Guidelines
Para maximizar la precisión de la IA y evitar alucinaciones:
1.  **Keep it Small**: Los archivos de instrucciones (`SKILL.md`, `AGENTS.md`) deben mantenerse entre 250 y 500 líneas.
2.  **Explicit Triggers**: Cuando se detecte una tarea que coincida con un disparador, el agente DEBE anunciar que está aplicando dicha Skill.
3.  **Modular Context**: Si una funcionalidad crece demasiado, se debe crear un `AGENTS.md` específico en su subdirectorio (ej: `frontend/AGENTS.md`).

---

## 💡 Instrucciones de Uso (Para el Desarrollador)
1.  Copia esta capeta `.agent` a tu nuevo proyecto.
2.  Actualiza `project-context/SKILL.md` con la arquitectura real de tu proyecto.
3.  Define las variables en tus workflows (ej. comandos de test o linter).
4.  Añade skills de dominio específicas (ej. `react-patterns`, `django-core`).
5.  **Sincronización**: Al añadir habilidades, mantén esta tabla y `QUICK_REFERENCE.md` actualizados.

