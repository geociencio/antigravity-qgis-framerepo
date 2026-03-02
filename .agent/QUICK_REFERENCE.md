# Guía Rápida: PyQGIS Agentic Framework (Gen-4)

**Versión**: 4.0 (PyQGIS Template)

---

## 📋 Resumen Ejecutivo

El framework **Antigravity (PyQGIS)** proporciona un sistema base de **skills** y **workflows** integrados que automatizan la invocación de agentes especializados y conocimiento contextual para estandarizar del desarrollo de Plugins de QGIS profesionales.

---

## 🛠️ Skills Base Disponibles

| Skill | Descripción | Cuándo Usar |
|:------|:------------|:------------|
| [commit-standards](.agent/skills/commit-standards/SKILL.md) | Estándares de Conventional Commits | Al crear commits, validar mensajes |
| [coding-standards](.agent/skills/coding-standards/SKILL.md) | Formateo, tipado y estilo de código | Al escribir o refactorizar código |
| [project-context](.agent/skills/project-context/SKILL.md) | Arquitectura y propósito del plugin | Al iniciar tareas o necesitar contexto global |
| [qgis-core](.agent/skills/qgis-core/SKILL.md) | API de QGIS, asincronía (`QgsTask`) | Al interactuar con capas o recursos de PyQGIS |
| [ui-framework](.agent/skills/ui-framework/SKILL.md) | Generación Programática de PyQt5/6 | Al diseñar widgets, diálogos responsivos |
| [qa-qgis-docker](.agent/skills/qa-qgis-docker/SKILL.md) | Entorno Dockerizado y QGIS Mocks | Al escribir/ejecutar tests aislando QGIS |
| [release-management](.agent/skills/release-management/SKILL.md) | Empaquetado y Semantic Versioning | Al preparar releases para el repositorio de QGIS |


---

## 🔄 Workflows Base Disponibles

### Desarrollo Diario

| Workflow | Agent | Skills | Propósito |
|:---------|:------|:-------|:----------|
| [/inicia-sesion](.agent/workflows/inicia-sesion.md) | Tech Lead | project-context, qgis-core | Iniciar sesión de trabajo PyQGIS con contexto sincronizado |
| [/crea-commit](.agent/workflows/crea-commit.md) | QA Engineer | qa-qgis-docker, commit-standards | Commit con validación estática de calidad |
| [/run-tests](.agent/workflows/run-tests.md) | QA Engineer | qa-qgis-docker | Ejecutar tests en contenedor Docker o mock |
| [/run-tests-in-qgis](.agent/workflows/run-tests-in-qgis.md) | QA Engineer | qa-qgis-docker | Ejecutar tests de integración dentro del entorno vivo de QGIS |
| [/cierra-sesion](.agent/workflows/cierra-sesion.md) | QA Engineer | qa-qgis-docker, commit-standards | Cerrar sesión con logs actualizados |

### Refactorización y Calidad

| Workflow | Agent | Skills | Propósito |
|:---------|:------|:-------|:----------|
| [/refactor-code](.agent/workflows/refactor-code.md) | Tech Lead | coding-standards, qgis-core | Refactorizar código (desacoplamiento UI/Core) |

### Release Management

| Workflow | Agent | Skills | Propósito |
|:---------|:------|:-------|:----------|
| [/release-plugin](.agent/workflows/release-plugin.md) | QA Engineer | release-management, qa-qgis-docker | Release y empaquetado del plugin (.zip) |

---

## 🎯 Casos de Uso Comunes

### Iniciar Sesión de Desarrollo
```bash
/inicia-sesion
```
**Qué hace**:
- Activa "Tech Lead Agent"
- Carga skills: project-context, qa-standards
- Sincroniza contexto base.
- Ejecuta los tests configurados en el proyecto.
- Valida métricas de calidad iniciales.

### Crear Commit con Validación
```bash
/crea-commit
```
**Qué hace**:
- Activa "QA Engineer Agent"
- Carga skills: qa-standards, commit-standards
- Ejecuta linters/formatters.
- Genera 2-3 opciones de mensaje siguiendo Conventional Commits.
- Valida formato y scope.

### Refactorizar Código Complejo
```bash
/refactor-code
```
**Qué hace**:
- Activa "Tech Lead Agent"
- Carga skills: coding-standards, project-context
- Analiza la complejidad del código.
- Aplica principios de diseño definidos en project-context.
- Valida que la complejidad bajó y los tests pasan.

---

## 🔧 Extensibilidad y Personalización

Para adaptar este framework a tu proyecto:

### Añadir Nueva Skill
1. Crear directorio: `.agent/skills/[nombre-skill]/`
2. Crear `SKILL.md` con frontmatter YAML:
   ```yaml
   ---
   name: nombre-skill
   description: Descripción breve
   trigger: cuándo auto-invocar
   scope: root
   ---
   ```
3. Ejecutar `skill_sync.py` (si está configurado) o actualizar `AGENTS.md` manualmente.

### Añadir Nuevo Workflow
1. Crear archivo: `.agent/workflows/[nombre].md`
2. Añadir frontmatter YAML:
   ```yaml
   ---
   description: Descripción del workflow
   agent: Tech Lead | QA Engineer
   skills: [skill1, skill2]
   validation: |
     - Checkpoint 1
     - Checkpoint 2
   ---
   ```
3. Añadir anotaciones `🤖 **Agent Action**` en pasos clave.

---

## 📚 Referencias

- [AGENTS.md](file:///home/jmbernales/qgispluginsdev/sec_interp/antigravity-framerepo/.agent/AGENTS.md) - Definición completa de agentes y matriz de skills.

---

**Última actualización**: 2026-03-01
**Versión del sistema**: 2.0 (Agnostic Template)

