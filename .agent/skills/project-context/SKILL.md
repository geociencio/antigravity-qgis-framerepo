---
name: project-context
description: Resumen del propósito, arquitectura y estructura del proyecto.
trigger: al iniciar nuevas tareas, solicitar resúmenes o explicar la arquitectura del sistema.
---

# Contexto del Proyecto

Proporciona una visión integral de la arquitectura del proyecto, facilitando la toma de decisiones coherentes y alineadas con la visión técnica.

> **NOTA PARA EL DESARROLLADOR:** Este archivo es una plantilla. Debes rellenarlo con la información arquitectónica de tu proyecto real.

## Cuándo usar este skill
- Al inicio de una sesión para refrescar la arquitectura.
- Al proponer cambios estructurales o nuevas integraciones.
- Cuando el usuario solicita un estado actual o resumen del proyecto.

## Grado de Libertad
- **Guiado**: Utilizar esta información como marco de referencia inmutable para proponer soluciones alineadas con la visión del proyecto. No proponer arquitecturas alternativas a menos que el usuario lo solicite explícitamente.

## Workflow
1. **Lectura**: Consultar el `AI_CONTEXT.md` (si existe) y las directrices de este archivo.
2. **Análisis**: Identificar los límites entre las diferentes capas de la arquitectura (ej: Frontend vs Backend, Core vs Plugin).
3. **Validación**: Asegurar que las nuevas propuestas no violen el desacoplamiento definido.

## Instrucciones y Reglas

### Propósito del Proyecto
[Describe aquí brevemente qué hace tu aplicación y quiénes son los usuarios finales. Ej: Plataforma SaaS para gestión de inventarios en tiempo real].

### Arquitectura Core
[Añade las reglas de oro de tu arquitectura. Ejemplos:]
- **API First**: Todo el backend debe exponerse mediante una API RESTful o GraphQL.
- **Microfrontends**: La UI está dividida en submódulos gestionados por Webpack Module Federation.
- **Event-Driven**: La comunicación entre servicios críticos se hace a través de RabbitMQ.

### Estructura de Carpetas 
[Explica cómo está organizado tu repositorio. Ejemplos:]
- `src/core/`: Cerebro del backend (Modelos, Casos de Uso).
- `src/ui/`: Interfaz de usuario (Componentes React/Vue).
- `infrastructure/`: Configuración de Terraform, Docker o Kubernetes.

## Checklist de Calidad Arquitectónica
- [ ] ¿La propuesta respeta la separación de responsabilidades (Seperation of Concerns)?
- [ ] ¿Se alinea con la visión técnica (ej. "Local First", "Cloud Native")?
- [ ] ¿Se mantiene la integridad de los contratos entre interfaces/módulos?
