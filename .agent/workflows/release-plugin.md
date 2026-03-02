---
description: Proceso unificado de liberación (QGIS Release Flow) basado en la guía de IA
agent: QA Engineer
skills: [release-management, qa-qgis-docker, commit-standards]
validation: |
  - Verificar que la suite de tests pasa en Docker / Local
  - Confirmar que métricas de código (`qgis-analyzer` o similar) son aceptables
  - Asegurar Zero High-Severity Security Findings
  - Validar que las versiones están sincronizadas en archivos clave (`metadata.txt`)
  - Verificar que ZIP se generó correctamente sin basura
---

Sigue este flujo de 5 fases para realizar una liberación oficial del plugin para QGIS.

### Fase 1: Calidad y Preparación

🤖 **Agent Action**: Usar skill **release-management** para validar checklist completo de pre-release.

1. **Analizar Calidad**:
   // turbo
   ```bash
   # EJEMPLO PYTHON: qgis-analyzer analyze . u otra herramienta
   {{COMPLEXITY_CHECK_COMMAND}}
   ```

   🤖 **Agent Action**: Verificar que:
   - Overall Plugin Score es aceptable.
   - No hay violaciones críticas de QGIS compliance (uso de `QgsTask` correcto).

2. **Actualizar Badges**: Actualizar métricas de calidad en `README.md` según los resultados.

### Fase 2: Versionamiento y Documentación

🤖 **Agent Action**: Usar skill **release-management** para sincronizar versiones automáticamente.

1. **Sincronizar Versión (Semantic Versioning)**:
   - Acatar `X.Y.Z` (Major.Minor.Patch).
   - Actualizar `version` y `changelog` explícitamente en `metadata.txt`.
     - ⚠️ **CRÍTICO**: Escapar todo `%` como `%%` en el changelog (e.g., `100%%` no `100%`).
   - Actualizar `version` en `pyproject.toml` (si existe).
   - Actualizar el badge de versión en `README.md`.

2. **Actualizar `README.md` (OBLIGATORIO)**:
   🤖 **Agent Action**: Verificar y actualizar todos los badges y referencias de versión en `README.md`.
   - Sección de "What's New": Resumir los cambios principales de esta versión.

   🤖 **Agent Action**: Validar que las versiones coinciden exactamente a lo largo del proyecto.

3. **Changelog Técnico (Keep A Changelog)**: Mover `[Unreleased]` a la nueva versión en `CHANGELOG.md` usando los tipos válidos (`Added`, `Changed`, `Fixed`, etc).

4. **Notas de Lanzamiento**:
   🤖 **Agent Action**: Generar release notes estructuradas en la carpeta `docs/releases/`.

### Fase 3: Verificación

🤖 **Agent Action**: Usar skill **qa-qgis-docker** para validar tests y skill **commit-standards** para linting.

1. **Linting & Formatting**:
   // turbo
   ```bash
   {{LINTER_FIX_COMMAND}}
   ```
2. **Tests**:
   // turbo
   ```bash
   {{MASTER_TEST_COMMAND}}
   ```

   🤖 **Agent Action**: Alertar si algún test falla o si hay regresión en cobertura.

### Fase 4: Git y Tagging

🤖 **Agent Action**: Usar skill **commit-standards** para mensaje de commit.

1. **Commit de Preparación**:
   Asegurar que `.qgisignore` está actualizado y optimizado.
   ```bash
   git add metadata.txt pyproject.toml CHANGELOG.md README.md docs/releases/ .qgisignore
   git commit -m "chore(release): prepare vX.Y.Z"
   ```

2. **Tag**: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
3. **Push**: `git push origin main && git push origin vX.Y.Z`

### Fase 5: Empaquetado y Distribución

🤖 **Agent Action**: Usar skill **release-management** para validar artifacts y proceso de publicación.

1. **Build ZIP Optimizado**:
   // turbo
   ```bash
   # EJEMPLO: pb_tool zip o make package
   make package VERSION=main
   ```
   (Verificar en `dist/` o directorio de build).

   🤖 **Agent Action**:
   - Validar contenido del ZIP (sin logs, sin `sample_data`, sin caches `__pycache__`).
   - Verificar `sha256` checksum si aplica.

2. **GitHub Release**:
   ```bash
   gh release create vX.Y.Z --title "vX.Y.Z" --notes-file docs/releases/RELEASE_NOTES_vX.Y.Z.md dist/*.zip --draft
   ```

3. **Portal QGIS**: Subir el ZIP a [plugins.qgis.org](https://plugins.qgis.org/).

## Resultado Esperado
- Versión oficial empaquetada lista para QGIS Plugin Repository.
- Documentación y tags de Git sincronizados.
- Plugin validado técnicamente y limpio de artifacts de desarrollo.
