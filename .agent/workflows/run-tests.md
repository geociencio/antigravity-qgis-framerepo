---
description: Procedimiento estándar para ejecutar pruebas unitarias y de integración de forma fiable
agent: QA Engineer
skills: [qa-standards]
validation: |
  - Verificar que todos los tests críticos pasen
  - Confirmar que el entorno de CI o local reporta éxito (Exit Code 0)
---

Este workflow describe la manera estándar de ejecutar y validar la batería de pruebas del proyecto, asegurando que no haya regresiones.

> **NOTA PARA EL DESARROLLADOR:** Ajusta los comandos de prueba específicos de tu proyecto reemplazando `{{TEST_COMMAND}}`.

1. **Test Ligeros / Unitarios (Fast Feedback)**:
   Ejecuta las pruebas rápidas que no requieren levantar infraestructura pesada.
   ```bash
   # EJEMPLO: pytest tests/unit/
   # EJEMPLO JS: npm run test:unit
   {{UNIT_TEST_COMMAND}}
   ```

2. **Test de Integración (End-to-End)**:
   Ejecuta las pruebas que conectan múltiples módulos o requieren el entorno completo.
   ```bash
   # EJEMPLO: pytest tests/integration/
   # EJEMPLO JS: npm run cypress:run
   {{INTEGRATION_TEST_COMMAND}}
   ```

3. **Check de Calidad Completo (Definitive Master Check)**:
   El control de salud definitivo suele ejecutarse en un entorno aislado similar a producción (ej. Docker).
   // turbo
   ```bash
   # EJEMPLO: make docker-test
   {{MASTER_TEST_COMMAND}}
   ```

**Key Notes (Configurables por Proyecto):**
- **Aislamiento de Tests**: Evitar ejecutar pruebas unitarias e integración en el mismo hilo de ejecución si hay estado compartido (ej. Bases de Datos, Mocks persistentes).
- **Cobertura**: Asegúrate de que los frameworks generen un reporte de cobertura (ej: `--cov` en python, `--coverage` en jest).

🤖 **Agent Action**: Usar skill **qa-standards** para interpretar los fallos (leer la salida de consola o archivos de log generados) y validar si la estretegia de Mocks o asilaimento fue correcta.

## Resultado Esperado
- Informe claro del estado de estabilidad del proyecto ("En verde" o "En rojo").
- Identificación precisa de regresiones o fallos en tests específicos.
- Confirmación de si el código es seguro para ser integrado en la rama principal.
