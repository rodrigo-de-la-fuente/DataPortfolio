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

---

# Lección 2.3 — Atajos y productividad en Visual Studio Code

> **Objetivo:** Aprender los atajos de teclado más importantes de Visual Studio Code para trabajar de forma rápida y eficiente, reduciendo la dependencia del ratón.

**Objetivos de aprendizaje**:

- Utilizar la Paleta de Comandos.
- Abrir archivos y buscarlos rápidamente.
- Buscar texto en todo un proyecto.
- Comentar, mover y duplicar líneas de código.
- Utilizar múltiples cursores.
- Dividir el editor y navegar entre pestañas.
- Formatear documentos y renombrar símbolos de forma inteligente.


## ¿Por qué usar atajos?

Cada vez que apartas las manos del teclado para coger el ratón interrumpes tu flujo de trabajo. La diferencia puede parecer pequeña, pero tras cientos de acciones al día supone un ahorro considerable de tiempo y concentración. La idea es sencilla:

> **Utiliza el teclado para navegar y el ratón solo cuando realmente aporte comodidad.**

## Atajos

1. La paleta de comandos: Es la herramienta más importante de VS Code. Desde ella puedes acceder prácticamente a cualquier función del editor. Por ejemplo:
   - Cambiar el tema.
   - Abrir la configuración.
   - Ejecutar tareas.
   - Seleccionar el intérprete de Python.
   - Formatear un documento.
   - Instalar extensiones.
    El atajo es:
        ```text
        ⌘⇧P
        ```

2. Abrir archivos rápidamente:

    ```text
    ⌘P
    ```

    Empieza a escribir el nombre del archivo:

    ```text
    README
    ```

    o

    ```text
    main.py
    ```

    VS Code localizará el archivo inmediatamente, incluso en proyectos con cientos de archivos.


3. Buscar texto en todo el proyecto

    ```text
    ⌘⇧F
    ```

    Permite buscar una palabra o frase en todos los archivos del proyecto.

    Ejemplo:

    ```text
    load_data
    ```

    VS Code mostrará todas las apariciones.

4. Buscar y reemplazar
   - Buscar dentro del archivo:
        ```text
        ⌘F
        ```

   - Buscar y reemplazar: Muy útil para renombrar variables o corregir texto repetido.

        ```text
        ⌥⌘F
        ```

5. Terminal integrada: Permite alternar rápidamente entre el editor y la terminal.

    ```text
    ⌃`
    ```



6. Comentar código:

    ```text
    ⌘/
    ```

7. Duplicar una línea: Muy útil para crear variaciones de una línea de código sin necesidad de copiar y pegar.

    ```text
    ⌥⇧↓
    ```

    o

    ```text
    ⌥⇧↑
    ```

8. Mover líneas: Permite reorganizar el código rápidamente.

   - Mover una línea hacia arriba:

        ```text
        ⌥↑
        ```

   - Mover una línea hacia abajo:

        ```text
        ⌥↓
        ```

9. Selección múltiple

   - Añadir un nuevo cursor:

    ```text
    ⌥ + clic
    ```

    Ahora puedes escribir en varios lugares al mismo tiempo.

10. Seleccionar la siguiente coincidencia: Ideal para editar varias apariciones de una variable. Selecciona una palabra y pulsa:

    ```text
    ⌘D
    ```

    Cada pulsación añade otra coincidencia a la selección.

11. Ir a una línea concreta:

    ```text
    ⌃G
    ```
    Introduce el número de línea y pulsa **Enter**.


12. Navegar entre pestañas: Permite cambiar rápidamente entre los archivos abiertos.

    ```text
    ⌃Tab
    ```

13. Dividir el editor: Muy útil para...
    - Comparar archivos.
    - Consultar documentación mientras programas.
    - Revisar cambios.
    El atajo es:
    ```text
    ⌘\
    ```
    Obtendrás dos editores uno junto al otro.

14. Formatear un documento:

    ```text
    ⌥⇧F
    ```

    Si tienes instalado un formateador compatible, el código se reorganizará automáticamente. Más adelante se configurará un formateador específico para Python.

15. Renombrado inteligente: Coloca el cursor sobre una variable, función o clase y pulsa:

    ```text
    F2
    ```

    VS Code actualizará automáticamente todas las referencias del proyecto. Es mucho más seguro que buscar y reemplazar manualmente.

## Los 10 atajos más importantes

| Atajo | Acción |
|--------|--------|
| `⌘⇧P` | Paleta de Comandos |
| `⌘P` | Abrir archivo |
| `⌘F` | Buscar dentro del archivo |
| `⌘⇧F` | Buscar en todo el proyecto |
| `⌃\`` | Mostrar/Ocultar la terminal |
| `⌘/` | Comentar o descomentar |
| `⌘D` | Selección múltiple |
| `⌃G` | Ir a una línea |
| `⌘\` | Dividir el editor |
| `⌥⇧F` | Formatear documento |

No es necesario memorizar todos desde el primer día. Empieza utilizando tres o cuatro con frecuencia y el resto acabarán formando parte de tu flujo de trabajo de manera natural.

## Buenas prácticas

- Prioriza el uso del teclado frente al ratón en tareas repetitivas.
- Utiliza la Paleta de Comandos cuando no recuerdes dónde está una opción.
- Aprovecha el renombrado inteligente para evitar errores.
- Divide el editor cuando necesites comparar archivos o consultar documentación.

---

# Lección 2.4 — La Terminal Integrada de Visual Studio Code

> **Objetivo:** Aprender a utilizar la terminal integrada de VS Code como herramienta principal para trabajar con Git, Python y el sistema operativo, evitando cambiar constantemente entre aplicaciones.

**Objetivos de aprendizaje**:
- Abrir y gestionar varias terminales.
- Ejecutar comandos de Git y Python.
- Navegar por directorios con soltura.
- Personalizar el uso de la terminal.
- Comprender cuándo utilizar la terminal y cuándo la interfaz gráfica.


## Qué es la terminal integrada

La terminal integrada es una consola que se ejecuta **dentro de Visual Studio Code**. No es diferente de la Terminal de macOS o PowerShell en Windows; simplemente está integrada en el editor. Gracias a ello puedes:

- Editar código.
- Ejecutar programas.
- Utilizar Git.
- Instalar paquetes.
- Lanzar pruebas.

Todo sin abandonar VS Code.


## Abrir la terminal

El atajo más utilizado es:

```text
⌃`
```

También puedes acceder desde:

```text
Terminal
→ New Terminal
```

La terminal aparecerá en el panel inferior del editor.

## Dónde empieza la terminal

Cuando abres una carpeta en VS Code, la terminal se sitúa automáticamente en la raíz del proyecto.

Ejemplo:

```text
Roadmap-to-Success/
│
├── README.md
├── ejercicios/
└── scripts/
```

La terminal comenzará en:

```bash
Roadmap-to-Success $
```

De esta forma no es necesario escribir continuamente comandos como:

```bash
cd ...
```

## Ejecutar comandos

La terminal funciona igual que cualquier otra consola del sistema operativo.

Ejemplos:

- Mostrar el directorio actual:

    ```bash
    pwd
    ```

- Listar archivos:

    ```bash
    ls
    ```

- Consultar el estado del repositorio:

    ```bash
    git status
    ```

- Ejecutar un programa Python:

    ```bash
    python hola.py
    ```

## Crear varias terminales

Puedes trabajar con varias terminales abiertas simultáneamente.

Ejemplo:

```text
Terminal 1 → Git

Terminal 2 → Python

Terminal 3 → Servidor local
```

Para crear una nueva terminal pulsa el botón:

```text
+
```

situado en la esquina superior derecha del panel de terminales.

### Cambiar entre terminales

Cada terminal aparece como una pestaña. Puedes cambiar entre ellas sin perder el estado de los procesos que estén ejecutándose. Esto resulta especialmente útil cuando:

- Ejecutas un servidor.
- Realizas pruebas.
- Trabajas con Git al mismo tiempo.


### Dividir la terminal

La terminal también puede dividirse. Obtendrás una distribución similar a esta:

```text
┌────────────┬────────────┐
│ Terminal 1 │ Terminal 2 │
└────────────┴────────────┘
```

Muy útil para ejecutar varios procesos simultáneamente.

## Elegir el intérprete

Dependiendo del sistema operativo podrás utilizar distintos intérpretes. En macOS:

- zsh
- bash
- fish

En Windows:

- PowerShell
- Command Prompt
- Git Bash

Durante este roadmap utilizaremos **zsh** en macOS.


## Limpiar la terminal

Cuando la terminal acumula demasiada información puedes limpiarla con:

```bash
clear
```

o mediante el atajo:

```text
⌘K
```

La pantalla se limpia, aunque el historial continúa disponible.

## Interrumpir un proceso

Si un programa queda ejecutándose indefinidamente puedes detenerlo mediante:

```text
Ctrl + C
```

Es uno de los atajos más importantes cuando trabajes con scripts o servidores.


## Historial de comandos

Utiliza las flechas del teclado para recuperar comandos anteriores.

- Comando anterior:

    ```text
    ↑
    ```

- Comando siguiente:

    ```text
    ↓
    ```

Así evitarás escribir repetidamente los mismos comandos.

## Autocompletado

La terminal también dispone de autocompletado.

Por ejemplo:

    ```bash
    git sta
    ```

Al pulsar **Tab**, la terminal completa automáticamente el comando siempre que sea posible. Lo mismo ocurre con nombres de archivos y carpetas.


## Terminal + Git

Un flujo de trabajo habitual será:

    ```bash
    git status

    git add .

    git commit -m "Añadir nueva funcionalidad"

    git push
    ```

Todo ello sin abandonar VS Code.

## Terminal + Python

También podrás ejecutar programas o instalar bibliotecas.

- Ejecutar un script:

    ```bash
    python main.py
    ```

- Instalar un paquete:

    ```bash
    pip install pandas
    ```

Más adelante aprenderás a utilizar entornos virtuales desde la terminal.


## ¿Terminal o interfaz gráfica?

VS Code ofrece botones para realizar muchas tareas relacionadas con Git. Sin embargo, es recomendable dominar primero los comandos de terminal porque:

- Funcionan igual en cualquier entorno.
- Ofrecen un mayor control.
- Facilitan la resolución de problemas.
- Son una habilidad muy valorada profesionalmente.

La interfaz gráfica debe entenderse como un complemento, no como un sustituto.


## Buenas prácticas

- Utiliza la terminal integrada como herramienta principal de trabajo.
- Familiarízate con los comandos más frecuentes.
- Aprovecha el historial de comandos para evitar repetir tareas.
- Mantén la terminal organizada cuando trabajes con varios procesos simultáneamente.
- Mantén una terminal por tarea cuando el proyecto sea complejo.
- Limpia la terminal periódicamente para mejorar la legibilidad.
- Comprueba siempre en qué directorio te encuentras utilizando `pwd`.
- No cierres una terminal si hay un proceso importante ejecutándose sin saber qué está haciendo.

---