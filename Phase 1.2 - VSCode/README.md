# Lección 2.1 — Entorno y configuración de Visual Studio Code

> **Objetivo:** Configurar Visual Studio Code como un entorno de desarrollo profesional y comprender su interfaz para trabajar de forma eficiente durante todo el roadmap.

**Objetivos de aprendizaje**:

- Comprender la interfaz de VS Code.
- Configurar el editor para trabajar cómodamente.
- Crear un espacio de trabajo profesional.
- Entender qué es un *Workspace*.
- Dejar VS Code preparado para las siguientes lecciones.


## Qué es Visual Studio Code

Visual Studio Code (VS Code) es un **editor de código ligero, gratuito y altamente extensible**.

Su filosofía es sencilla:

> Empieza con un editor rápido y añade únicamente las herramientas que necesites mediante extensiones.

Gracias a ello puede utilizarse para desarrollar en Python, SQL, JavaScript, C++, Java y muchos otros lenguajes.


## La interfaz de VS Code

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

1. Editor: Es la zona donde se escribe y modifica el código. Permite trabajar simultáneamente con varios archivos mediante pestañas.

2. Explorer: Es la herramienta principal para navegar por el proyecto. Permite visualizar la estructura del proyecto:
   - Carpetas.
   - Archivos.
   - Organización del repositorio.

3. Barra lateral: Reúne las herramientas más importantes...
   - Explorer: Gestiona archivos y carpetas.
   - Search: Busca texto en todo el proyecto. Muy útil cuando un proyecto contiene muchos archivos.
   - Source Control: Integra Git dentro de VS Code. Permite:
     - Revisar cambios.
     - Hacer commits.
     - Comparar versiones.
     - Gestionar ramas.
   - Run and Debug: Permite ejecutar programas y depurarlos. Será fundamental durante el desarrollo en Python.
   - Extensions: Desde aquí se instalan y administran todas las extensiones.

4. Terminal integrada: Es una de las características más útiles de VS Code. Puede abrirse mediante:

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

## Configuración recomendada

Para acceder a la configuración, hacer desde

```text
Code → Settings
```

o mediante:

```text
⌘ ,
```

Una vez llegado a la configuración, podemos configurar ciertos aspectos de la interfaz que optimizarán la experiencia de VSCode:

1. Auto Save: Se recomienda **desactivarlo** durante el aprendizaje de Git para controlar conscientemente cuándo se modifican los archivos.
2. Tamaño de fuente: Valores cómodos -> 15, 16, 17
3. Tab Size: Para Python, 4 espacios
4. Word Wrap: Activado para evitar desplazamientos horizontales.
5. Minimap: Opcional. Muchos desarrolladores prefieren desactivarlo para ganar espacio.
6. Tema: No existe un tema "correcto". Lo importante es que resulte cómodo durante largas sesiones de trabajo.

## Cómo abrir un proyecto correctamente

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

## Qué es un *Workspace*

Un **Workspace** guarda:

- Carpetas abiertas.
- Configuración específica.
- Terminales.
- Ajustes del proyecto.

Puede contener una única carpeta o varias (Multi-root Workspace).

## Sincronización

VS Code permite sincronizar entre distintos equipos:

- Configuración.
- Temas.
- Atajos.
- Extensiones.

Muy útil cuando se trabaja desde varios ordenadores.


## Buenas prácticas

- Abrir siempre carpetas completas.
- Utilizar la terminal integrada.
- Mantener un proyecto por ventana cuando sea posible.
- Cerrar pestañas innecesarias.
- Utilizar la búsqueda para localizar archivos y funciones rápidamente.

---

# Lección 2.2 — Extensiones clave de Visual Studio Code

> **Objetivo:** Convertir Visual Studio Code en un entorno de desarrollo profesional mediante la instalación de las extensiones esenciales para programación, análisis de datos y documentación.

**Objetivos parciales**:

- Comprender qué son las extensiones.
- Instalar extensiones desde el Marketplace.
- Identificar las herramientas imprescindibles para Python y Git.
- Mantener un entorno ligero y organizado.
- Preparar VS Code para el resto del roadmap.

## ¿Qué es una extensión?

Una **extensión** añade nuevas funcionalidades a Visual Studio Code. Gracias a ellas es posible incorporar:

- Soporte para nuevos lenguajes.
- Autocompletado inteligente.
- Depuración.
- Integración con Git.
- Formateo automático.
- Herramientas de inteligencia artificial.
- Temas e iconos.

VS Code está diseñado para que cada desarrollador instale únicamente las herramientas que necesita.


### Cómo instalar una extensión

#### Método 1 (recomendado)

Abrir el panel de extensiones:

```text
⇧⌘X
```

o desde:

```text
View
→ Extensions
```

Buscar el nombre de la extensión y pulsar **Install**.

#### Método 2

Abrir la Paleta de Comandos:

```text
⌘⇧P
```

Buscar:

```text
Extensions: Install Extensions
```


### Extensiones imprescindibles

#### Python

**Autor:** Microsoft

Es la extensión principal para desarrollar en Python. Incluye:

- Ejecución de programas.
- Depuración.
- Detección de entornos virtuales.
- Integración con Jupyter.
- Compatibilidad con el resto de herramientas del ecosistema Python.

#### Pylance

**Autor:** Microsoft

Añade inteligencia al editor. Permite:

- Autocompletado avanzado.
- Información sobre tipos.
- Detección temprana de errores.
- Navegación rápida entre funciones y clases.

Ejemplo:

```python
import pandas as pd

pd.
```

Al escribir el punto (`.`), Pylance muestra automáticamente todos los métodos disponibles.

#### Jupyter

Permite abrir y ejecutar archivos:

```text
.ipynb
```

Será fundamental durante las fases dedicadas al análisis de datos y Machine Learning.


#### GitHub Pull Requests

Integra GitHub directamente en VS Code. Permite:

- Revisar Pull Requests.
- Crear Pull Requests.
- Gestionar Issues.
- Revisar comentarios sin abandonar el editor.


#### Markdown All in One

Extensión especialmente útil para documentación. Añade:

- Atajos para Markdown.
- Creación automática de tablas.
- Listas inteligentes.
- Tabla de contenidos.
- Mejor experiencia escribiendo archivos `README.md`.


#### Error Lens

Muestra los errores directamente sobre la línea donde aparecen.

Ejemplo:

```python
x = "5"

print(x + 3)
```

El editor señala inmediatamente el problema sin necesidad de consultar el panel inferior.

#### GitLens

Una de las mejores extensiones para trabajar con Git. Permite conocer:

- Quién modificó cada línea.
- Cuándo se realizó el cambio.
- En qué commit.
- Historial completo de un archivo.
- Comparación entre versiones.

Especialmente útil en proyectos colaborativos.


#### Better Comments

Mejora la legibilidad de los comentarios.

Ejemplo:

```python
# TODO
# FIXME
# IMPORTANT
# NOTE
```

Cada tipo aparece con un color diferente.

#### Code Spell Checker

Comprueba la ortografía en:

- Documentación.
- Comentarios.
- Archivos Markdown.
- README.

Muy útil para mantener una documentación profesional.


#### Material Icon Theme

No modifica el funcionamiento del editor. Simplemente sustituye los iconos por otros mucho más descriptivos y agradables visualmente.

## Mantener VS Code ligero

Un error frecuente consiste en instalar decenas de extensiones "por si acaso". Es recomendable:

- Instalar únicamente las necesarias.
- Desactivar temporalmente las que no se utilicen.
- Revisar periódicamente las extensiones instaladas.

Un entorno ligero suele ser más rápido y estable.

## Buenas prácticas

- Instalar solo las extensiones que aporten valor.
- Preferir siempre extensiones mantenidas por desarrolladores reconocidos (como Microsoft).
- Mantener VS Code actualizado.
- Eliminar extensiones que ya no se utilicen.