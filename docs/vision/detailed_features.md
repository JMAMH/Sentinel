# Especificaciones Técnicas de Sentinel

## 🧠 Sistema de Memoria Evolutiva
- **Append-only Memory**: El archivo `memory.md` no se borra, se añaden hitos. La IA lo consulta para no repetir errores pasados.
- **Project Indexing**: Si el archivo supera las X líneas, la IA genera un "Map" del archivo para navegarlo sin leerlo todo (ahorro de tokens).

## 🛡️ Protocolo de Seguridad y Git
- **Shadow Git**: Antes de cada intervención, Sentinel asegura que no hay cambios sucios. Si los hay, pregunta al usuario o hace un commit de "Pre-AI change".
- **Validation Loop**: Sentinel no da por terminado un trabajo hasta que:
  1. El código compila.
  2. Los logs no muestran errores nuevos.
  3. (Opcional) El test unitario pasa.

## 👁️ Sensor de Entorno (IDE Awareness)
- **Diagnostic Feed**: La extensión de VS Code no es un chat, es un sensor que envía: *"Archivo X, Línea Y: Error de tipo 'String is not assignable to Number'"*.
- **Active Focus**: Si el usuario cambia de pestaña en VS Code, Sentinel actualiza su "foco actual".

## 📦 Gestión de Entornos Aislados
- **Auto-Environment**: Si el proyecto es Python, Sentinel debe sugerir/crear un `venv`. Si es Node, verificar `package.json`.
- **Sandbox**: Intentar que las ejecuciones de comandos ocurran en el entorno correcto sin ensuciar el sistema global del usuario.