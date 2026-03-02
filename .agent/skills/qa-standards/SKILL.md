---
name: qa-standards
description: Estándares para pruebas automáticas, CI/CD y uso de Mocks.
trigger: al escribir o ejecutar tests, diseñar estrategias de prueba o manejar infraestructura de pruebas.
---

# QA y Automatización

Garantiza la estabilidad del código mediante un entorno de ejecución controlado, estrategias de simulación (Mocks) y prácticas de CI/CD.

## Cuándo usar este skill
- Al crear nuevos casos de prueba unitarios o de integración.
- Al depurar fallos en el pipeline de CI/CD.
- Al configurar o modificar el entorno de pruebas.

## Grado de Libertad
- **Guiado**: Se deben seguir las estrategias de testing definidas en el proyecto, buscando alta cobertura y aislamiento.

## Workflow
1. **Diseño**: Aplicar estrategia "Test-Driven Development (TDD)" o "Behaviour-Driven Development (BDD)" según el proyecto.
2. **Implementación**: Crear tests usando el framework principal del proyecto (ej: `pytest`, `jest`, etc.). Aislar dependencias externas mediante Mocks.
3. **Ejecución**: Validar localmente mediante el Local Test Runner y luego en el entorno de CI/CD.
4. **Cobertura**: Verificar que se alcanza la cobertura mínima exigida (> 80%).

## Instrucciones y Reglas

### Estrategia de Testing
- **Aislamiento**: Las pruebas unitarias deben ejecutarse de forma rápida y sin dependencias externas (bases de datos, red, UI).
- **Mocks**: Simular (mockear) servicios externos y librerías de terceros complejas. Limpiar los mocks rigurosamente después de cada test.
- **Integración**: Los tests de integración deben validar el flujo completo en un entorno lo más cercano posible al de producción (ej. contenedores Docker).

### Entorno de Pruebas
- **Consistencia**: El comando de test principal (`{{TEST_COMMAND}}`) debe ser el control de salud definitivo. Si pasa en local, debe pasar en CI/CD.
- **Limpieza**: Evitar que los tests dejen estado residual en el entorno.

## Checklist de Calidad
- [ ] ¿La cobertura de nuevos servicios es satisfactoria (> 80%)?
- [ ] ¿Se limpian los patches/Mocks después de cada test?
- [ ] ¿Los tests unitarios pueden ejecutarse de forma aislada sin levantar servicios pesados?
- [ ] ¿El entorno de pruebas reporta estabilidad (0 fallos)?
