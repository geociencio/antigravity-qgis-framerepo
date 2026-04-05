# NEXT STEPS - antigravity-qgis-framerepo

Para retomar el desarrollo en la próxima sesión:

## Pendientes Críticos
- [ ] **Optimización de Scripts**: Reducir complejidad ciclomática en `scripts/mcp_server.py` y `scripts/security_scan.py` (según recomendación de `ai-ctx`).
- [ ] **Docs Scaffolding**: Expandir la documentación de los blueprints de minería en `scaffold/mining/`.
- [ ] **Integración CI/CD**: Añadir GitHub Action para ejecutar `ruff` y `security_scan.py` en cada PR.

## Sugerencias
- Ejecuta `/audit-plugin` para validar la estabilidad del framework tras la migración masiva.
- Verifica la interoperabilidad del `mcp_server.py` con clientes externos de MCP.

## Retomar
Usa el comando: `/inicia-sesion`
ó
`uv run ai-ctx analyze --path .`
