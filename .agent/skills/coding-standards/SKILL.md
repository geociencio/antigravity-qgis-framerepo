---
name: coding-standards
description: Estándares de codificación, formato, convenciones de nomenclatura y calidad general del código.
trigger: al escribir código nuevo, realizar refactorizaciones o proponer patrones de diseño.
---

# Estándares de Codificación

Define las normas técnicas para asegurar un código moderno, mantenible y coherente de acuerdo con las convenciones del lenguaje y framework utilizado en el proyecto.

## Cuándo usar este skill
- Al crear nuevos componentes, módulos o funciones.
- Al realizar refactorizaciones de código existente.
- Al revisar *Pull Requests* o evaluar calidad de código.

## Grado de Libertad
- **Estricto**: El código debe adherirse a los linters configurados en el proyecto y a las mejores prácticas de la industria (SOLID, DRY, KISS).

## Workflow
1. **Diseño Cuidado**: Planificar la estructura y tipos de datos antes de escribir la lógica.
2. **Implementación Constreñida**: Seguir las convenciones de *naming* y estructura del proyecto.
3. **Documentación Activa**: Escribir comentarios aclaratorios (docstrings, JSDoc) según el estándar del lenguaje.
4. **Validación Automática**: Ejecutar los linters y formatters obligatorios (`{{LINTER_COMMAND}}`).

## Instrucciones y Reglas

### Modernidad y Seguridad
- Preferir APIs modernas del lenguaje (ej. `pathlib` en Python, manipulación inmutable de arrays en JS/TS).
- Evitar *magic strings* y *magic numbers*; extraer a constantes.

### Documentación y Tipado
- Utilizar sistemas de tipado estático siempre que el lenguaje lo soporte (TypeScript, Type Hints en Python, typing extendido).
- Documentar funciones públicas: propósito del método, argumentos esperados y valor de retorno, especialmente si el comportamiento es complejo o expuesto en un API.

### Calidad de Código
- **Complejidad Ciclomática**: Mantener métodos y funciones pequeños (idealmente < 15 en métricas de complejidad).
- **Responsabilidad Única**: Separar la lógica de interfaz de usuario de la lógica de negocio subyacente.

## Checklist de Calidad
- [ ] ¿El código refleja los principios SOLID?
- [ ] ¿Se utilizaron anotaciones de tipos consistentes?
- [ ] ¿Las funciones/clases clave están debidamente documentadas?
- [ ] ¿El código pasa limpiamente el chequeo del linter y auto-formateador configurado en el proyecto?
