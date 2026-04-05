---
name: project-context
description: Summary of the purpose, architecture, and structure of the {{PROJECT_NAME}} project.
trigger: when starting new tasks, requesting summaries, or explaining the plugin architecture.
---

# {{PROJECT_NAME}} Project Context

Provides a comprehensive view of the {{PROJECT_NAME}} plugin, facilitating consistent architectural decision-making.

## When to use this skill
- At the start of a session to refresh architectural knowledge.
- When proposing structural changes or new integrations.
- When the user requests the current project status.

## Degree of Freedom
- **Guided**: Use this information as a reference frame to propose solutions aligned with the project's vision.

## Workflow
1. **Reading**: Consult `AI_CONTEXT.md` and `PROJECT_SUMMARY.md`.
2. **Analysis**: Identify boundaries between `core`, `gui`, and relevant modules.
3. **Validation**: Ensure new proposals do not violate defined decoupling.

## Instructions and Rules

### Purpose
{{PROJECT_NAME}} is an advanced tool that allows for {{BRIEF_DESCRIPTION}} within QGIS, optimizing the workflow.

### Core Architecture
- **Local First**: Prioritizes local performance and efficient memory management.
- **UI-Agnostic**: The processing core must function independently of Qt graphics elements.
- **3-Level Validation**: (Type, Schema, Business) in all domain services.

### Folder Structure
- `core/`: Plugin brain (servers, core logic).
- `gui/`: Dynamic and responsive user interface.
- `scripts/`: Utility and synchronization tools.

## Quality Checklist
- [ ] Does the proposal respect Core/GUI separation?
- [ ] Does it align with the "Local First" vision?
- [ ] Is 3-level validation integrity maintained?
