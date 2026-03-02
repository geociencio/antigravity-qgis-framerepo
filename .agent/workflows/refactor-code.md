---
description: Workflow guiado para refactorización de código con validación de complejidad
agent: Tech Lead
skills: [coding-standards, project-context]
validation: |
  - Verificar que complejidad ciclomática general se redujo
  - Confirmar que tests siguen pasando después de la refactorización
  - Validar que no se introdujeron violaciones de arquitectura (Core vs UI)
---

Este workflow guía la refactorización de código siguiendo los estándares del proyecto y usando conocimiento arquitectónico.

## Cuándo Usar Este Workflow

- Cuando analizadores de código estático (Sonarqube, ESLint, Ruff) detectan métodos muy complejos.
- Cuando la arquitectura base se siente acoplada o difícil de testear.
- Antes de añadir nuevas funcionalidades a módulos o clases muy extensas.


## Pasos de Refactorización

1. **Identificar Objetivo de Refactorización**:
   // turbo
   ```bash
   # EJEMPLO PYTHON: radon cc . -a
   # EJEMPLO JS: eslint .
   {{COMPLEXITY_CHECK_COMMAND}}
   ```

   🤖 **Agent Action**: Identificar hotspots y deuda técnica leyendo métricas o preguntando al usuario sobre los puntos de dolor actuales.

2. **Cargar Contexto Especializado**:

   🤖 **Agent Action**: Leer `project-context` para entender los límites arquitectónicos del módulo que se va a refactorizar. Asegurar adherencia a `coding-standards`.

3. **Aplicar Refactorización**:

   🤖 **Agent Action**: Aplicar principios SOLID. Reducir complejidad ciclomática extrayendo métodos o moviendo lógica a clases/servicios dedicados. Mantener TDD si es posible.

4. **Validar con Tests**:
   // turbo
   ```bash
   # Ejecutar control completo de tests
   {{MASTER_TEST_COMMAND}}
   ```

   🤖 **Agent Action**: Usar skill **qa-standards** para asegurar que no hay regresiones y que se mantienen/mejoran las pruebas unitarias afectadas.

5. **Verificar Métricas de Calidad**:
   // turbo
   ```bash
   {{COMPLEXITY_CHECK_COMMAND}}
   ```

   🤖 **Agent Action**: Confirmar mejora en las métricas y reducción de código "spaghetti".

6. **Commit de Refactorización**:
   Usar workflow `/crea-commit` con mensaje técnico estructurado, asegurando un prefijo `refactor:`.

## Resultado Esperado
- Código más mantenible, testeable y con menor complejidad cognitiva.
- Cero regresiones funcionales confirmadas por pruebas automatizadas.
- Documentación técnica (docstrings/JSDoc) actualizada o mejorada.
