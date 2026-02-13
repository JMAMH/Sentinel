### Guía de Primer Inicio y Configuración Inicial

Esta guía describe el proceso obligatorio que ocurre **la primera vez que el usuario ejecuta Sentinel** después de la instalación.

El objetivo de esta configuración inicial es garantizar que el entorno quede correctamente preparado para trabajar con modelos de IA, gestionar proyectos y definir permisos operativos.

---

# 🚀 Bienvenida Inicial

Al abrir Sentinel por primera vez, el usuario accederá a un asistente de configuración guiado.
Este proceso es obligatorio y solo se realiza una vez (aunque la mayoría de opciones pueden modificarse posteriormente desde el panel de configuración).

---

# 1️⃣ Selección de Idioma

El usuario deberá elegir su idioma preferido.

### Alcance del idioma:

* Interfaz gráfica del programa.
* Mensajes del sistema.
* Archivos internos que interactúan con los modelos de IA.
* Configuraciones generadas automáticamente.

> ℹ️ El idioma puede modificarse en cualquier momento desde la configuración general.

---

# 2️⃣ Configuración de Modelos de IA

Sentinel requiere al menos un modelo de IA configurado para funcionar.

El usuario podrá elegir entre distintas formas de conexión:

---

## 🔑 Método 1: Conexión mediante API Key

Orientado a usuarios técnicos o desarrolladores.

* Introducción manual de API Key.
* Compatible con múltiples proveedores.
* Permite gestionar múltiples instancias del mismo proveedor.

---

## 🔐 Método 2: Inicio de Sesión con Proveedor

Alternativa más simple para usuarios no técnicos.

* Inicio de sesión mediante cuenta del proveedor.
* Autenticación guiada.
* Gestión automática de credenciales.

---

## 🤖 Proveedores Compatibles

* OpenAI
* Gemini
* Claude
* DeepSeek
* Otros compatibles mediante configuración avanzada
* Modelos locales ejecutándose en el ordenador del usuario

---

## 🖥 Modelos Locales

Usuarios avanzados pueden conectar modelos que se ejecuten localmente en su máquina.

Esto permite:

* Mayor privacidad.
* Uso sin conexión a internet.
* Control total sobre el modelo.

---

## 🔁 Sistema de Fallback y Prioridad

Sentinel permite configurar múltiples modelos simultáneamente.

El usuario podrá:

* Establecer un orden de prioridad.
* Definir modelo principal y modelos secundarios.
* Configurar fallback automático en caso de error.

**Ejemplo de prioridad:**

1. Claude
2. OpenAI
3. Gemini

Si el primer modelo falla, Sentinel intentará automáticamente con el siguiente.

---

## ⚙️ Gestión de Modelos

Para cada modelo configurado el usuario podrá:

* Activarlo o desactivarlo.
* Eliminarlo (olvidarlo).
* Configurar múltiples instancias del mismo proveedor.
* Reordenar prioridades.

Cada vez que se agregue un modelo:

* Se realizará una prueba rápida de conexión.
* El sistema confirmará si la comunicación fue exitosa.

---

# 3️⃣ Configuración de Permisos

Sentinel permite definir cómo interactuará la IA con el entorno del proyecto.

Los permisos se dividen en tres categorías:

---

## 📂 A. Permisos Predeterminados (Habilitados por Defecto)

Estos permisos están activos inicialmente:

* Leer archivos del proyecto.
* Escribir o modificar archivos del proyecto.
* Crear y editar archivos en el directorio de memoria.
* Leer información del sistema de control de versiones interno:

  * `git status`
  * `git diff`
  * `git log`

> ℹ️ Sentinel incluye un sistema de versionamiento Git interno independiente del tipo de proyecto.

---

## ⚙️ B. Permisos Condicionales (Configurables)

El usuario podrá decidir si la IA puede ejecutar comandos adicionales.

### Permisos generales:

* Ejecutar `tree`.
* Ejecutar comandos de análisis estructural.

### Permisos por proyecto:

* Usar `npm`.
* Ejecutar `docker`.
* Ejecutar `pytest`.
* Levantar servidores.
* Ejecutar tests automatizados.
* Realizar commits.
* Crear ramas en el Git principal (diferente del Git interno).
* Otros permisos para diferentes tipos de proyectos.

El usuario podrá definir:

* Si estas funciones estarán activadas por defecto en nuevos proyectos.
* Si estarán desactivadas y requerirán activación manual.

---

## ⏱ C. Permisos en Tiempo de Ejecución

Sentinel puede solicitar autorización puntual durante la ejecución de tareas sensibles.

Este sistema se detalla más profundamente en la documentación de gestión de proyectos.

---

# 4️⃣ Personalización de la Interfaz (UI)

Antes de finalizar, el usuario podrá realizar ajustes visuales y estructurales:

* Tema (claro / oscuro / personalizado).
* Ventanas visibles por defecto.
* Paneles laterales.
* Distribución del espacio de trabajo.
* Preferencias de visualización por proyecto.

Estas configuraciones pueden modificarse posteriormente.

---

# ✅ Finalización del Primer Inicio

Una vez completados todos los pasos:

* La configuración se guarda automáticamente.
* Sentinel inicializa el entorno principal.
* El usuario accede al panel principal del programa.

A partir de este momento, Sentinel está listo para comenzar a trabajar con proyectos y modelos de IA.

---

# 📌 Notas Importantes

* Todas las configuraciones pueden modificarse posteriormente.
* Es obligatorio tener al menos un modelo activo para utilizar la IA.
* Se recomienda configurar correctamente los permisos para evitar ejecuciones no deseadas.