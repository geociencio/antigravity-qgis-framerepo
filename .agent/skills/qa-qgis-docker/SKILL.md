---
name: qa-qgis-docker
description: Estándares para pruebas en entorno Dockerizado y uso de Mocks para QGIS.
trigger: al escribir o ejecutar tests, usar mocks o manejar infraestructura Docker para PyQGIS.
---

# QA y Automatización Docker (PyQGIS)

Garantiza la estabilidad del código mediante un entorno de ejecución controlado (Docker) y estrategias de simulación (Mocks) para PyQGIS.

## Cuándo usar este skill
- Al crear nuevos casos de prueba unitarios o de integración.
- Al depurar fallos en el pipeline de CI/CD.
- Al configurar o modificar el entorno de desarrollo Docker para QGIS.

## Grado de Libertad
- **Guiado**: Se deben seguir las estrategias de mocking definidas, pero existe libertad en el diseño de los casos de prueba.

## Workflow
1. **Diseño**: Aplicar estrategia "Mock-First" para lógica independiente de la UI.
2. **Implementación**: Crear tests usando `unittest` o `pytest`.
3. **Ejecución**: Validar localmente y luego en Docker (`make docker-test` o equivalente).
4. **Cobertura**: Verificar métricas de cobertura en nuevos servicios.

## Instrucciones y Reglas

### Estrategia de Mocking
- **Mock-First**: Aislar la lógica de dominio de las dependencias pesadas de `qgis.core` siempre que sea posible.
- **Aislamiento**: Ejecutar tests en procesos separados para evitar contaminación de Mocks.
- **Transparencia**: Cargar módulos PyQGIS reales solo en tests de integración.

### Entorno Docker
- **Imagen**: Usar `qgis/qgis:latest` (o versión específica) como base para emular el entorno de despliegue.
- **Comando Maestro**: Ejecutar la suite completa mediante contenedores asegura reproducibilidad.

## Checklist de Calidad
- [ ] ¿La cobertura de nuevos servicios es satisfactoria?
- [ ] ¿Se limpian los patches de Mocks después de cada test?
- [ ] ¿El test de integración PyQGIS se ejecuta correctamente?
- [ ] ¿El reporte de Docker muestra 0 fallos?
