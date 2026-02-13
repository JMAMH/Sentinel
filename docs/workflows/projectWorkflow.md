### Flujo Completo de Trabajo y Arquitectura Cognitiva

Este documento describe el flujo real de trabajo dentro de Sentinel, desde la creación de un proyecto hasta la ejecución avanzada con memoria persistente y control inteligente del entorno.

---

# 1️⃣ Gestión de Proyectos

Una vez configurado el sistema, el usuario puede comenzar a trabajar en proyectos desde la interfaz principal.

Si no existen proyectos previos, el panel estará vacío.
Si existen, podrá:

* Continuarlos desde el último estado.
* Gestionarlos (editar, duplicar, eliminar).
* Revisar su estado actual.

---

## 📌 Creación de Proyecto

Cada proyecto requiere:

* **Nombre único** (no repetido).
* **Descripción opcional**.
* **Imagen representativa**:

  * Galería predeterminada (colores sólidos o degradados).
  * Imagen local personalizada (opcional).

---

## 🧭 Tipo de Proyecto

El usuario deberá elegir entre dos rutas principales:

### A. Crear proyecto desde cero

Opciones disponibles:

1. **Proyecto local**

   * Selección de carpeta de trabajo.
   * Ejemplo:

     ```
     C:/Users/[usuario]/Desktop/proyecto1
     ```

2. **Proyecto en host externo**

   * Requiere conexión SSH.
   * Selección de carpeta remota.

3. **Repositorio de GitHub**

   * Conexión a cuenta GitHub.
   * Clonado o creación de repositorio.
   * Selección de carpeta local de trabajo.

---

### B. Continuar proyecto existente

El usuario selecciona una carpeta ya existente.

Diferencias clave respecto a proyecto nuevo:

* Sentinel analiza la estructura actual.
* Detecta tecnologías usadas.
* Realiza preguntas orientadas a entender el sistema actual.
* Actualiza memoria antes de ejecutar nuevas tareas.

A partir de ahí, el flujo converge con el de un proyecto nuevo.

---

# 2️⃣ Fase de Preparación (Proyecto Nuevo)

Antes de escribir código, Sentinel inicia una fase de definición estratégica.

El usuario conversa con la IA utilizando prompts guiados que ayudan a:

* Definir problemática.
* Establecer alcance.
* Determinar finalidad.
* Seleccionar stack tecnológico.
* Identificar requisitos clave.

Este proceso está diseñado para:

* Guiar usuarios sin experiencia.
* Estructurar proyectos complejos.
* Reducir ambigüedad temprana.

Puede omitirse si el proyecto es simple (ej. script pequeño en Python).

---

# 3️⃣ Entrada al Entorno de Desarrollo

Una vez finalizada la preparación:

* El chat se desplaza a un panel lateral.
* Se abre el área principal de trabajo.
* Se inicializa una instancia integrada tipo Visual Studio Code.

Aquí comienza el desarrollo real.

---

## 👁 Visualización en Tiempo Real

El usuario podrá ver:

* Archivos creándose.
* Código escribiéndose.
* Cambios en vivo.
* Logs operativos en el chat lateral.

Ejemplos de logs:

* “Escribiendo archivo principal main.py”
* “Ejecutando npm install”
* “Levantando servidor local”

---

# 4️⃣ Sistema de Permisos en Tiempo Real

Si la IA intenta ejecutar algo que no tiene permitido:

Se mostrará un mensaje como:

> “Ejecutar npm install
> Nota de la IA: necesario para poder ejecutar la aplicación posteriormente.”

El usuario podrá elegir:

* ✅ Ejecutar solo esta vez
* ❌ No ejecutar
* 🔁 Ejecutar y no volver a preguntar

Si elige “no volver a preguntar”:

* Se crea un antecedente en el proyecto.
* Se actualiza `.ai/identity/permissions.md`.
* La IA podrá ejecutar ese comando automáticamente en el futuro.

Esto transforma el flujo de:

> “Arregla esto en @main.py”
> “Necesito permiso para pip install…”

a un flujo más limpio:

> “Arregla esto en @main.py”
> “Aplicando cambios… testeando… optimizando… listo.”

Menos fricción, más autonomía progresiva.

---

## 🛠 Gestión Manual de Permisos

Existe un panel de gestión donde el usuario puede:

* Revocar permisos otorgados.
* Añadir permisos manualmente.
* Ajustar antecedentes.

Se advertirá que modificar permisos manualmente puede afectar la estabilidad si el contenido no coincide con la realidad del entorno.

---

# 5️⃣ Ventanas Adicionales Dinámicas

Sentinel puede abrir ventanas auxiliares cuando sea necesario:

* Navegador interno (para visualizar aplicaciones web).
* Consolas de ejecución.
* Paneles de logs extendidos.

Esto permite:

* Validación visual.
* Contexto adicional para cambios UI.
* Debug más preciso.

---

# 6️⃣ Arquitectura Cognitiva: La Carpeta `.ai/`

Sentinel funciona como un MCP avanzado para programación.

El núcleo de su inteligencia persistente reside en la carpeta:

```
.ai/
```

---

## 🧠 PRINCIPIO FUNDAMENTAL

`.ai/` no es caché.
`.ai/` no es contexto temporal.
`.ai/` es la mente externa persistente de Sentinel.

Sentinel:

* Lee `.ai/` antes de actuar.
* Actualiza `.ai/` después de actuar.
* Confía más en `.ai/` que en el chat.

---

Perfecto.
Voy a reescribir el **Capítulo 7** enfocándolo específicamente en **qué hace cada carpeta**, cuál es su función operativa dentro del sistema y cómo interactúan entre sí.

Mantendré una jerarquía clara con múltiples niveles de `#` para que encaje directamente como capítulo dentro de tu documentación.

---

# 7️⃣ Estructura Cognitiva Completa

La carpeta `.ai/` es el núcleo estructural que permite a Sentinel operar con memoria persistente, coherencia técnica y continuidad estratégica.

Cada subcarpeta cumple una función específica dentro del sistema cognitivo del agente.
No es almacenamiento auxiliar: es una arquitectura diseñada para separar identidad, estrategia, memoria estructural, ejecución y estado.

---

## 📁 Estructura General

```txt
.ai/
├── identity/
├── project/
├── memory/
├── runtime/
├── git/
├── embeddings/
└── state/
```

A continuación se describe en detalle qué hace cada sección.

---

### 🔹 `identity/` — Identidad y Límites Operativos

Define cómo debe comportarse Sentinel dentro de este proyecto específico.

```txt
.ai/identity/
├── sentinel.md
├── permissions.md
└── capabilities.md
```

#### ¿Qué función cumple?

Esta carpeta controla la personalidad operativa y los límites de acción del agente.
Evita comportamientos inconsistentes entre ejecuciones.

### `sentinel.md`

Define:

* Rol del agente en el proyecto.
* Nivel de autonomía permitido.
* Estilo de trabajo (conservador, agresivo, incremental).
* Idioma principal.
* Criterios de calidad esperados.

📌 Función clave: mantener coherencia conductual.

### `permissions.md`

Define lo que está permitido ejecutar:

* Carpetas accesibles.
* Comandos automáticos.
* Comandos que requieren confirmación.
* Acciones prohibidas.

📌 Función clave: seguridad y control.

Sentinel consulta este archivo antes de ejecutar acciones sensibles.

### `capabilities.md`

Define qué herramientas existen en el entorno:

* git
* docker
* npm
* python
* ssh
* otros entornos instalados

📌 Función clave: delimitar capacidades técnicas reales.

Diferencia importante:

* **Capabilities** = lo que puede hacer técnicamente.
* **Permissions** = lo que tiene autorizado hacer.

---

### 🔹 `project/` — Definición Estratégica

Contiene la verdad conceptual del proyecto.

```txt
.ai/project/
├── vision.md
├── scope.md
├── requirements.md
├── constraints.md
└── glossary.md
```

#### ¿Qué función cumple?

Evita que el proyecto pierda dirección con el tiempo.
Actúa como contrato estratégico interno.

### `vision.md`

Define:

* Problema que se resuelve.
* Usuario objetivo.
* Qué significa éxito.

📌 Función clave: mantener enfoque.

### `scope.md`

Define:

* Qué está incluido.
* Qué está explícitamente excluido.

📌 Función clave: evitar expansión innecesaria.

### `requirements.md`

Contiene:

* Requisitos funcionales.
* Requisitos no funcionales (rendimiento, seguridad, escalabilidad).

📌 Función clave: marco técnico obligatorio.

### `constraints.md`

Incluye:

* Limitaciones técnicas.
* Restricciones legales.
* Presupuesto.
* Tiempo.

📌 Función clave: evitar decisiones inviables.

### `glossary.md`

Define términos importantes del dominio.

📌 Función clave: reducir ambigüedad semántica.

---

### 🔹 `memory/` — Memoria Estructural y Lógica

Es el cerebro operativo del proyecto.

```txt
.ai/memory/
├── structure/
├── logic/
├── decisions/
└── history/
```

#### ¿Qué función cumple?

Permite que Sentinel entienda el sistema sin releer todo el código constantemente.

### 🔸 `memory/structure/` — Organización Física

Describe cómo está construido el proyecto.

```txt
memory/structure/
├── folders.md
└── files/
```

### `folders.md`

Explica:

* Responsabilidad de cada carpeta.
* Qué directorios ignorar.
* Organización general.


### `files/*.md`

Cada archivo relevante tiene su documentación estructurada.

Contiene:

* Propósito.
* Responsabilidades.
* Dependencias.
* Suposiciones.
* Riesgos.

📌 Función clave: permitir cambios quirúrgicos.

Sentinel consulta estos `.md` antes de tocar el código fuente.

### 🔸 `memory/logic/` — Funcionamiento Interno

Describe cómo interactúan las partes del sistema.

```txt
memory/logic/
├── data_flow.md
├── state_management.md
└── integrations.md
```

Incluye:

* Flujo de datos.
* Gestión de estados.
* Integraciones externas.
* Autenticación.
* Pagos.

📌 Función clave: preservar coherencia funcional.

### 🔸 `memory/decisions/` — Justificación Arquitectónica

Registra por qué se tomaron decisiones técnicas.

```txt
memory/decisions/
├── architecture.md
├── tech_stack.md
└── rejected_options.md
```

Incluye:

* Arquitectura elegida.
* Stack tecnológico.
* Opciones descartadas y motivos.

📌 Función clave: evitar contradicciones futuras.

### 🔸 `memory/history/` — Evolución y Errores

Registro histórico del proyecto.

```txt
memory/history/
├── changelog.md
├── failed_attempts.md
└── known_issues.md
```

Incluye:

* Cambios importantes.
* Intentos fallidos.
* Problemas conocidos.

📌 Función clave: evitar repetir errores.

---

### 🔹 `runtime/` — Contexto de Ejecución

Representa el estado técnico actual del entorno.

```txt
.ai/runtime/
├── environment.md
├── services.md
├── commands.md
└── logs.md
```

Contiene:

* Variables de entorno.
* Servicios activos.
* Últimos comandos ejecutados.
* Errores recientes.

📌 Función clave: coherencia operativa en tiempo real.

Evita que Sentinel repita acciones innecesarias.

---

### 🔹 `git/` — Estrategia de Versionado

Gestiona la relación entre memoria y control de versiones.

```txt
.ai/git/
├── strategy.md
├── commits.md
└── branches.md
```

Incluye:

* Convenciones de commit.
* Estrategia de ramas.
* Política de snapshots internos.

📌 Función clave: trazabilidad estructurada.

---

### 🔹 `embeddings/` — Índice Semántico

Capa de búsqueda inteligente.

```txt
.ai/embeddings/
├── index.meta.json
└── README.md
```

Contiene:

* Información de indexación.
* Modelo usado.
* Carpetas indexadas.

📌 Función clave: búsqueda semántica eficiente en proyectos grandes.

No define decisiones, solo facilita recuperación contextual.

---

### 🔹 `state/` — Estado Cognitivo Actual

Representa la conciencia inmediata del agente.

```txt
.ai/state/
├── last_run.md
├── current_focus.md
└── todo.md
```

---

### `last_run.md`

Describe:

* Última acción ejecutada.
* Resultado.
* Errores encontrados.

📌 Función clave: continuidad entre ejecuciones.

### `current_focus.md`

Indica:

* Área activa de trabajo.
* Componentes sensibles.
* Elementos que no deben tocarse.

📌 Función clave: evitar interferencias.

### `todo.md`

Lista:

* Próximos pasos sugeridos.
* Pendientes técnicos.
* Mejoras detectadas.

📌 Función clave: planificación incremental.

---

#### 🧠 Interacción Entre Carpetas

El flujo cognitivo general es:

1. `identity/` define cómo actuar.
2. `project/` define hacia dónde ir.
3. `memory/` explica cómo está construido.
4. `runtime/` muestra qué está pasando ahora.
5. `git/` asegura trazabilidad.
6. `embeddings/` permite búsqueda inteligente.
7. `state/` mantiene continuidad inmediata.

La combinación de estas capas convierte a Sentinel en un agente con memoria estructurada, no en un simple generador de código contextual.

---

# 9️⃣ Embeddings y Búsqueda Semántica

Además de los archivos `.md`, Sentinel genera una representación vectorial del proyecto.

Esto permite:

* Búsqueda semántica.
* Evitar leer archivos irrelevantes.
* Intervenciones quirúrgicas en proyectos grandes (+6000 líneas).
* Cambios específicos a funciones sin alterar estructura completa.

Los `.md` permiten:

* Entender propósito antes que implementación.
* Reducir errores.
* Minimizar modificaciones innecesarias.

---

# 🔟 Sincronización con Cambios Manuales del Usuario

Si el usuario modifica código manualmente:

* El Git interno detecta cambios (`git diff`).
* Antes de ejecutar nuevas tareas, Sentinel:

  * Analiza los cambios.
  * Actualiza la memoria correspondiente.
  * Documenta la nueva realidad del sistema.
* Luego procede con la nueva solicitud.

Esto evita inconsistencias entre memoria y código real.

---

# 1️⃣1️⃣ Autonomía Progresiva

Con el tiempo, el proyecto evoluciona hacia:

* Menos preguntas.
* Más contexto persistente.
* Mayor precisión.
* Cambios más quirúrgicos.
* Flujo continuo y limpio.

Sentinel no solo escribe código.
Sentinel mantiene coherencia estructural a largo plazo.