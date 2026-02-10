# Sentinel Roadmap: De Script a Agente Autónomo

## Fase 0: El Núcleo (MVP Técnico) - "El Cerebro"
- [ ] Implementar el loop básico: Análisis -> Plan -> Ejecución -> Verificación.
- [ ] Estructura de memoria `.ai/`: `identity.md`, `project.md`, `memory.md`.
- [ ] Conexión con Gemini 1.5 Pro/Flash vía API.
- [ ] Herramientas de lectura básica: `ls`, `tree`, `cat`.

## Fase 1: Memoria y Contexto - "La Conciencia"
- [ ] Sistema de resúmenes: Generar `.ai/summaries/*.md` para archivos grandes.
- [ ] Indexación selectiva: Evitar `node_modules`, `.git`, y binarios.
- [ ] Seguimiento de cambios humanos: Detectar cambios fuera del agente y documentarlos.
- [ ] Referencias explícitas: Soporte para `@filename` en el chat.

## Fase 2: Acción y Seguridad - "Las Manos"
- [ ] Integración con Git: Commits automáticos con mensajes semánticos.
- [ ] Sistema de Rollback: Revertir al último estado funcional si fallan los tests.
- [ ] Ejecución de comandos: Terminal integrada para `npm`, `pip`, `docker`.
- [ ] Análisis de Logs: Leer salida de consola para detectar errores 500 o fallos de compilación.

## Fase 3: Interfaz y Senses - "Los Sentidos"
- [ ] Extensión VS Code (Sensor): Enviar errores de LSP (líneas rojas) al agente.
- [ ] App de Escritorio (Tauri): Interfaz "Modo Teatro" para ver el flujo de trabajo.
- [ ] Gestión de permisos visual: Panel para autorizar qué carpetas/comandos puede tocar la IA.

## Fase 4: Producto y Distribución - "El Ciudadano"
- [ ] Empaquetado: Python embebido + Tauri (Plug & Play).
- [ ] Perfiles de Usuario: Modos "Vibecoder", "Learner", y "Senior".
- [ ] Versión Community vs Pro: Definir límites de proyectos y funciones avanzadas.