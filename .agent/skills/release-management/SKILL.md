---
name: release-management
description: Estándares para el proceso de liberación de un plugin QGIS con validación de calidad.
trigger: al preparar lanzamientos, actualizar versiones o usar el workflow /release-plugin
---

# Gestión de Releases (Plugin QGIS)

Controla el ciclo de vida de las versiones del plugin, garantizando que cada entrega cumpla con los estándares del repositorio oficial de QGIS y los lineamientos de calidad del proyecto.

## Cuándo usar este skill
- Al finalizar una fase de desarrollo y preparar una nueva versión.
- Al actualizar `metadata.txt` o la configuración del empaquetado.
- Al generar notas de versión o actualizar el changelog.
- Al usar el workflow `/release-plugin`.

## Grado de Libertad
- **Estricto**: El proceso de empaquetado y los requisitos del `metadata.txt` de QGIS son innegociables.

## Workflow Detallado

### Fase 1: Calidad y Preparación
1. **Análisis de Calidad**:
   Asegurar que no hay violaciones arquitectónicas graves y que la complejidad ciclomática está controlada.
2. **Actualizar Badges**: Reflejar métricas en `README.md`.

### Fase 2: Versionado y Documentación

> [!IMPORTANT]
> **CHECKLIST COMPLETO DE DOCUMENTOS A ACTUALIZAR**:
>
> | # | Archivo | Qué actualizar |
> |:--|:--------|:--------------|
> | 1 | `metadata.txt` | `version` + `changelog` (escapar `%%`) |
> | 2 | `README.md` | Badge `Version`, sección "What's New" |
> | 3 | `CHANGELOG.md` | Mover `[Unreleased]` a `[X.Y.Z]` con fecha |
> | 4 | Resumen de Versión | Generar documento de Notas de Versión en `docs/releases/` |

1. **Sincronización**: Actualizar `metadata.txt` (incluyendo changelog completo para QGIS).
2. **Estándares de Versionamiento y Registro (CRÍTICO)**:
   - **[Semantic Versioning (SemVer)](https://semver.org/spec/v2.0.0.html)**:
     - MAJOR (X): Cambios incompatibles (Breaking Changes / Migración de QGIS 3 a 4).
     - MINOR (Y): Nuevas funcionalidades retrocompatibles.
     - PATCH (Z): Correcciones de errores (Bugfixes).
   - **[Keep a Changelog](https://keepachangelog.com/es/1.0.0/)**:
     - Mantener `CHANGELOG.md` alineado con el estándar.

### Fase 3: Verificación Técnica
1. Lograr que la suite completa de tests de integración de QGIS pase sin errores.
2. Ejecutar chequeo en entorno limpio (ej: `make docker-test`).

### Fase 4: Git y Etiquetado
1. Commit de release: `chore(release): prepare vX.Y.Z`.
2. Etiqueta: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`.
3. Push: `git push origin main --tags`.

### Fase 5: Empaquetado y Distribución
1. Build: Crear el empaquetado `.zip` (usando `pb_tool`, `make package` o herramienta preferida).
2. Validar ZIP: Asegurarse de excluir `__pycache__`, `.git`, tests y archivos ocultos (`.env`, `.gitignore`).
3. Carga: Subir a [plugins.qgis.org](https://plugins.qgis.org/) si es un plugin público, o distribuir internamente.

## Instrucciones y Reglas

### Detalle de Archivos Críticos
- **metadata.txt**: Debe contener `version`, `qgisMinimumVersion` válido y el `changelog` formateado según exigen los repositorios de QGIS.

### Plantilla de Release Notes
```markdown
# Release vX.Y.Z - [Title]
Highlights:
- **feat**: ...
- **fix**: ...
Published Artifacts: `plugin_name.X.Y.Z.zip`
```

## Checklist de Calidad
- [ ] ¿Se han actualizado todas las referencias de versión de PyQGIS (`metadata.txt`)?
- [ ] ¿El archivo ZIP ha sido depurado (sin basura técnica ni tests)?
- [ ] ¿Se han seguido las reglas de Git Tagging?
- [ ] ¿Los tests pasan satisfactoriamente en entorno QGIS aislado?
