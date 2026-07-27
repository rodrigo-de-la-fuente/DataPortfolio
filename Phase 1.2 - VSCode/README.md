# VSCode Learning

![roadmap-to-VSCode](/imgs/vscode.png)

# Lección 2.1 — Entorno y configuración de Visual Studio Code

> **Objetivo:** Configurar Visual Studio Code como un entorno de desarrollo profesional y comprender su interfaz para trabajar de forma eficiente durante todo el roadmap.

---

## Objetivos de aprendizaje

- Comprender la interfaz de VS Code.
- Configurar el editor para trabajar cómodamente.
- Crear un espacio de trabajo profesional.
- Entender qué es un *Workspace*.
- Dejar VS Code preparado para las siguientes lecciones.

---

# Qué es Visual Studio Code

Visual Studio Code (VS Code) es un **editor de código ligero, gratuito y altamente extensible**.

Su filosofía es sencilla:

> Empieza con un editor rápido y añade únicamente las herramientas que necesites mediante extensiones.

Gracias a ello puede utilizarse para desarrollar en Python, SQL, JavaScript, C++, Java y muchos otros lenguajes.

---

# La interfaz de VS Code

La ventana principal está organizada en varias zonas:

```text
┌──────────────────────────────────────────────┐
│ Barra de título                              │
├──────────────────────────────────────────────┤
│ Menú                                         │
├───────────────┬──────────────────────────────┤
│ Activity Bar  │                              │
│               │                              │
│ Explorer      │                              │
│ Search        │      Editor                  │
│ Source Control│                              │
│ Run           │                              │
│ Extensions    │                              │
├───────────────┴──────────────────────────────┤
│ Panel inferior (Terminal, Output, Problems)  │
├──────────────────────────────────────────────┤
│ Barra de estado                              │
└──────────────────────────────────────────────┘
```

## Explorer

Permite visualizar la estructura del proyecto:

- Carpetas.
- Archivos.
- Organización del repositorio.

Es la herramienta principal para navegar por el proyecto.

---

## Editor

Es la zona donde se escribe y modifica el código.

Permite trabajar simultáneamente con varios archivos mediante pestañas.

---

## Barra lateral

La barra lateral reúne las herramientas más importantes.

### Explorer

Gestiona archivos y carpetas.

### Search

Busca texto en todo el proyecto.

Muy útil cuando un proyecto contiene muchos archivos.

### Source Control

Integra Git dentro de VS Code.

Permite:

- Revisar cambios.
- Hacer commits.
- Comparar versiones.
- Gestionar ramas.

### Run and Debug

Permite ejecutar programas y depurarlos.

Será fundamental durante el desarrollo en Python.

### Extensions

Desde aquí se instalan y administran todas las extensiones.

---

# Terminal integrada

Una de las características más útiles de VS Code.

Puede abrirse mediante:

```text
Ctrl + `
```

o, en macOS:

```text
⌃ `
```

Desde ella pueden ejecutarse comandos como:

```bash
git status

python

pip

conda

pytest
```

Todo sin abandonar el editor.

---

# Configuración recomendada

Acceder desde:

```text
Code → Settings
```

o mediante:

```text
⌘ ,
```

## Auto Save

Se recomienda **desactivarlo** durante el aprendizaje de Git para controlar conscientemente cuándo se modifican los archivos.

---

## Tamaño de fuente

Valores cómodos:

- 15
- 16
- 17

---

## Tab Size

Para Python:

```text
4 espacios
```

---

## Word Wrap

Activado para evitar desplazamientos horizontales.

---

## Minimap

Opcional.

Muchos desarrolladores prefieren desactivarlo para ganar espacio.

---

## Tema

No existe un tema "correcto".

Lo importante es que resulte cómodo durante largas sesiones de trabajo.

---

# Cómo abrir un proyecto correctamente

Siempre debe abrirse una carpeta completa:

```text
File
→ Open Folder...
```

o desde la terminal:

```bash
code nombre-del-proyecto
```

Así VS Code reconoce correctamente toda la estructura del proyecto.

---

# ¿Qué es un Workspace?

Un **Workspace** guarda:

- Carpetas abiertas.
- Configuración específica.
- Terminales.
- Ajustes del proyecto.

Puede contener una única carpeta o varias (Multi-root Workspace).

---

# Sincronización

VS Code permite sincronizar entre distintos equipos:

- Configuración.
- Temas.
- Atajos.
- Extensiones.

Muy útil cuando se trabaja desde varios ordenadores.

---

# Buenas prácticas

- Abrir siempre carpetas completas.
- Utilizar la terminal integrada.
- Mantener un proyecto por ventana cuando sea posible.
- Cerrar pestañas innecesarias.
- Utilizar la búsqueda para localizar archivos y funciones rápidamente.

