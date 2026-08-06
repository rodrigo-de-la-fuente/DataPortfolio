# Lección 5.1 — Estructura de carpetas

## Objetivo

El objetivo es aprender a organizar cualquier proyecto de forma profesional para que sea fácil de entender, mantener y ampliar.

### Por qué esto importa para tu portfolio

Un proyecto pequeño puede funcionar con todos los archivos mezclados:

```text
Proyecto/

main.py
datos.csv
imagen.png
modelo.pkl
script2.py
script3.py
README.md
resultado.xlsx
grafico1.png
grafico2.png
notas.txt
```

Pero conforme el proyecto crece empiezan los problemas:

- No sabes qué archivos son importantes.
- No recuerdas dónde guardar nuevos datos.
- Cuesta encontrar el código.
- Otra persona no entiende la estructura.
- Es fácil borrar archivos por error.

Una buena organización evita todo esto.

---

### La idea principal

Cada carpeta debe tener **una única responsabilidad**: Piensa en una casa. La cocina es para cocinar. El dormitorio es para dormir. El garaje es para guardar el coche. No mezclamos funciones. Con un proyecto ocurre exactamente lo mismo.

> **La organización no sirve únicamente para proyectos grandes; sirve para que los proyectos pequeños puedan crecer sin convertirse en un caos.**

---

## Estructura estándar

En proyectos de Data Analytics y Data Science utilizaremos normalmente una estructura como esta:

```text
Proyecto/

├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│
├── src/
│
├── outputs/
│   ├── figures/
│   ├── reports/
│   └── models/
│
├── docs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

1. `data/`: Contiene **todos los datos del proyecto**. Nunca mezcles datos con código. Normalmente se divide en tres carpetas:

    ```text
    data/

    ├── raw/
    ├── processed/
    └── external/
    ```

    1.2 `raw/`: Guarda los datos originales. **Nunca deben modificarse.** 

        Ejemplo:

        ```text
        clientes.csv
        ventas.xlsx
        ```

    1.3 `processed/`: Contiene los datos ya limpios y preparados para el análisis.

        Ejemplo:

        ```text
        ventas_limpias.csv
        clientes_final.csv
        ```

    1.4 `external/`: Datos descargados de fuentes externas.

        Ejemplos:

        - INE
        - Kaggle
        - Banco Mundial
        - Eurostat

2. `notebooks/`: Aquí viven los cuadernos de Jupyter. Se utilizan para:

   - Explorar datos.
   - Probar ideas.
   - Crear visualizaciones.
   - Hacer experimentos.

    Ejemplo:

    ```text
    EDA.ipynb
    Modelo.ipynb
    Experimentos.ipynb
    ```
    > **Importante:** el código definitivo del proyecto no debería quedarse únicamente en los notebooks.

3. `src/`: Es la carpeta donde vive el código fuente. Cuando un proyecto crece, la mayor parte del código termina aquí.

    ```text
    src/

    limpieza.py
    visualizacion.py
    modelo.py
    utils.py
    ```

4. `outputs/`: Contiene todos los archivos generados por el programa. Por ejemplo gráficos, informes, modelos entrenados, archivos Excel, imágenes... Normalmente se organiza así:

    ```text
    outputs/

    ├── figures/
    ├── reports/
    └── models/
    ```

5. `docs/`: Contiene documentación adicional del proyecto.

    Ejemplos:

    ```text
    manual.md
    diagramas/
    explicaciones.md
    ```

6. `README.md`: Es la puerta de entrada del proyecto. Debe explicar qué hace el proyecto, cómo instalarlo, cómo ejecutarlo, tecnologías utilizadas, estructura del proyecto, resultados obtenidos.

7.  `requirements.txt`: Lista todas las librerías necesarias. Permite instalar todas las dependencias con un único comando.

    Ejemplo:

    ```text
    pandas
    numpy
    matplotlib
    scikit-learn
    ```


8.  `.gitignore`: Indica a Git qué archivos y carpetas **no deben subirse al repositorio**.

---

## Flujo típico de un proyecto

Cada elemento tiene su lugar:

```text
Datos originales (raw) 
        │
        ▼
 Limpieza (src)
        │
        ▼
Datos procesados
        │
        ▼
   Análisis
        │
        ▼
Visualizaciones
        │
        ▼
Resultados (outputs)
```

---

## Ejemplo completo

```text
AnalisisVentas/

├── data/
│   ├── raw/
│   │   └── ventas2025.csv
│   │
│   └── processed/
│       └── ventas_limpias.csv
│
├── notebooks/
│   └── exploracion.ipynb
│
├── src/
│   ├── limpiar.py
│   ├── analizar.py
│   └── visualizar.py
│
├── outputs/
│   ├── figures/
│   │   └── ventas_mes.png
│   │
│   └── reports/
│       └── informe.pdf
│
├── docs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

Con esta estructura, cualquier persona entiende rápidamente dónde se encuentra cada tipo de archivo.

---

## Buenas prácticas

- Separa siempre datos y código.
- No guardes imágenes junto a los scripts.
- No pongas notebooks dentro de `src`.
- Guarda los resultados en `outputs`.
- Nunca modifiques los datos originales.
- Utiliza la misma estructura en todos tus proyectos.

---

# Lección 5.2 — `.gitignore`

## Objetivo

El objetivo es aprender qué archivos deben formar parte de un proyecto profesional y cuáles **nunca** deberían subirse a GitHub.

### Por qué esto importa para tu portfolio

Imagina que un reclutador entra en uno de tus repositorios y ve esto:

```text
__pycache__/
.venv/
.ipynb_checkpoints/
.DS_Store
archivo.tmp
backup.py
modelo_v2_final_final.pkl
```

La primera impresión será de desorden. En cambio, un repositorio limpio transmite inmediatamente que sabes cómo trabajar.

> **Git debe guardar tu trabajo, no el ruido que generan las herramientas. Un buen `.gitignore` mantiene el repositorio limpio, seguro y profesional, y hace que muestre solo aquello que aporta valor.**

---

## Qué es `.gitignore`

Es un archivo de texto que le dice a Git:

> **"Aunque estos archivos existan en mi ordenador, no quiero que los controles ni los subas al repositorio."**

Git simplemente los ignora.

---

## Por qué existe

Durante el desarrollo aparecen muchos archivos que generan automáticamente Python, VSCode, Jupyter Notebook y el sistema operativo. Pueden volver a crearse en cualquier momento. Además, contienen información privada, así que no tiene sentido almacenarlos en GitHub.

Supongamos este proyecto:

```text
analisis_supermercado/

├── src/
├── data/
├── README.md
├── main.py
├── .gitignore
├── __pycache__/
├── .venv/
└── .DS_Store
```

Las carpetas `__pycache__/`, `.venv/` y el archivo `.DS_Store` no los has creado tú. Los generan automáticamente Python, el entorno virtual y el sistema operativo. Sin un `.gitignore`, Git intentará subirlos.

¿Qué ocurre sin `.gitignore`? Al ejecutar:

```bash
git status
```

podrías obtener:

```text
Untracked files:

__pycache__/
.venv/
.DS_Store
.ipynb_checkpoints/
```

Git piensa que quizá quieras añadirlos al repositorio. Pero realmente no quieres.

---

## Cómo funciona

Dentro del archivo escribimos una regla por línea.

Por ejemplo:

```text
__pycache__/
```

Git ignorará esa carpeta.

Otro ejemplo:

```text
*.log
```

Ignorará todos los archivos cuya extensión sea `.log`. Un ejemplo típico para proyectos en Python

```text
# Caché de Python
__pycache__/
*.py[cod]

# Entornos virtuales
.venv/
venv/
env/

# Jupyter Notebook
.ipynb_checkpoints/

# Variables de entorno
.env

# macOS
.DS_Store

# Visual Studio Code
.vscode/

# Modelos grandes
*.pkl
*.joblib
```

Este archivo será prácticamente el mismo en la mayoría de tus proyectos.

* **¿Por qué ignorar `__pycache__`?** Python crea automáticamente esta carpeta. Contiene archivos compilados que pueden regenerarse en cualquier momento y, por tanto, nunca deben subirse al repositorio.

Ejemplo:

```text
__pycache__/

main.cpython-313.pyc
utils.cpython-313.pyc
```

* **¿Por qué ignorar `.venv`?** Cuando creas un entorno virtual se generan cientos o miles de archivos. Todos pueden volver a crearse ejecutando:

```bash
pip install -r requirements.txt
```

Por eso añadimos `.venv` al `.gitignore`.

* **¿Por qué ignorar `.env`?** Imagina un archivo así:

```text
OPENAI_API_KEY=xxxxxxxx
PASSWORD=123456
TOKEN=abcdef
```

Si subes este archivo a GitHub, acabas de publicar tus claves privadas. Es uno de los errores más comunes entre desarrolladores principiantes.

¿Y los datos? Depende del tamaño y del objetivo del proyecto: archivos de datos pequeños sí pueden subirse, pero archivos de datos grandes (p.ej., imágenes de varios gigabytes, vídeos, modelos grandes, bases de datos muy pesadas...) normalmente no. En estos casos se utilizan soluciones específicas como **Git LFS** o almacenamiento externo.


¿Y los modelos entrenados? Aquí también depende del tamaño del modelo: Un modelo de unos pocos cientos de KB puede formar parte del proyecto, pero uno de varios gigabytes normalmente no.

La regla general a seguir será:

> **Solo sube aquello que sea necesario para entender, ejecutar o reproducir el proyecto.**

**⚠️ Muy importante: `.gitignore` *no elimina archivos*. Simplemente evita que Git los controle. El archivo sigue existiendo en tu ordenador.** 

---

## Un error muy frecuente

Creas el archivo `.env` y lo subes al repositorio. Más tarde lo añades al `.gitignore` y piensas que ya está solucionado. Pues no, porque Git ya estaba siguiendo ese archivo: `.gitignore` **solo afecta a archivos que Git todavía no está controlando**. Para dejar de seguir un archivo ya versionado hay que eliminarlo del índice de Git sin borrarlo del disco haciendo:

```bash
git rm --cached .env
```

Después podrás hacer un nuevo commit y Git dejará de seguir ese archivo.

---

## Aplicación al portfolio

Todos los proyectos de tu GitHub deberán incluir un `.gitignore` adecuado. Así, cualquier persona que visite tus repositorios encontrará únicamente:

- Código fuente.
- Documentación.
- Datos relevantes.
- Resultados importantes.

Y no cientos de archivos temporales generados automáticamente.

---

## Buenas prácticas

- Crea el `.gitignore` al comenzar el proyecto.
- Nunca subas archivos con contraseñas o claves API.
- Ignora carpetas generadas automáticamente.
- Ignora los entornos virtuales.
- Mantén siempre el repositorio limpio.

---

## Plantilla de `.gitignore`

Crea un archivo  con el siguiente contenido:

```text
# Caché de Python
__pycache__/
*.py[cod]

# Entornos virtuales
.venv/
venv/
env/

# Jupyter Notebook
.ipynb_checkpoints/

# Variables de entorno
.env

# macOS
.DS_Store

# Visual Studio Code
.vscode/

# Modelos grandes
*.pkl
*.joblib
```

Después ejecuta:

```bash
git status
```

Y comprueba que esos archivos y carpetas ya no aparecen como pendientes de añadir.


# Lección 5.3 — Gestión de entornos

## Objetivo

El objetivo de esta lección es aprender qué es un entorno virtual, por qué todos los proyectos profesionales utilizan uno y cómo gestionarlo correctamente.

### Por qué esto importa para tu portfolio

Imagina que un reclutador descarga uno de tus proyectos desde GitHub e intenta ejecutarlo. Si necesita instalar librerías "a ojo" porque no sabe cuáles utilizaste, es muy probable que el proyecto no funcione. En cambio, un proyecto profesional permite recrear exactamente el mismo entorno en pocos minutos. Recuerda que...

> **Un proyecto no está terminado hasta que otra persona puede ejecutarlo en su ordenador.**

---

## El problema y la solución

Supongamos que desarrollas dos proyectos distintos. El proyecto A necesita `pandas 2.3`, `numpy 2.1` y `matplotlib 3.10`. Mientras, el proyecto B necesita `pandas 1.5` y `tensorflow 2.15`. Si se instalan todas las librerías directamente en el ordenador, tarde o temprano aparecerán conflictos entre versiones, y un proyecto puede dejar de funcionar simplemente porque otro ha actualizado una dependencia.

### La solución: los entornos virtuales

Un entorno virtual es una instalación **aislada** de Python con sus propias librerías. Es decir, cada proyecto tiene su propio entorno independiente. Visualmente:

```text
Mi ordenador

├── Proyecto_A
│   └── .venv/
│
├── Proyecto_B
│   └── .venv/
│
└── Proyecto_C
    └── .venv/
```

Cada carpeta `.venv` es completamente independiente de las demás.

---

## Ventajas de utilizar entornos virtuales

- Cada proyecto utiliza las versiones de librerías que necesita.
- Se evitan conflictos entre proyectos.
- Es mucho más fácil compartir el proyecto.
- Si el entorno se estropea, basta con recrearlo.

---

## Pasos para crear un entorno virtual

1. Desde la carpeta del proyecto ejecuta `python -m venv .venv`. Se creará una carpeta llamada `.venv/` que contendrá una instalación aislada de Python.

2. Activar el entorno: La activación depende del sistema operativo. En macOS/Linux se hace `source .venv/bin/activate`. Cuando el entorno esté activo, normalmente la terminal mostrará algo parecido a `(.venv)` al principio de la línea de comandos.

3. Instalar librerías: Con el entorno activado, ejecutar `pip install pandas matplotlib scikit-learn`. Las librerías se instalarán únicamente dentro de ese proyecto.

4. Guardar las dependencias: Cuando el proyecto tenga instaladas todas las librerías necesarias, hacer `pip freeze > requirements.txt`. El archivo generado permite reconstruir el entorno en cualquier ordenador y tendrá un aspecto similar a este:

```text
matplotlib==3.10.1
numpy==2.1.0
pandas==2.3.0
scikit-learn==1.7.0
```

Para recrear el entorno, otra persona solo tendrá que ejecutar `pip install -r requirements.txt` para instalar exactamente las mismas dependencias.

### Por qué `.venv` está en `.gitignore`

Porque contiene miles de archivos que pueden generarse automáticamente. No tiene sentido subirlos al repositorio. Lo único que necesitas compartir es `requirements.txt` y así cada usuario recreará su propio entorno local.

---

## Flujo de trabajo profesional

Cada vez que empieces un proyecto seguirás un proceso parecido a este:

```text
Crear proyecto
      │
      ▼
Crear entorno virtual
      │
      ▼
Activar entorno
      │
      ▼
Instalar librerías
      │
      ▼
Desarrollar
      │
      ▼
Actualizar requirements.txt
```

Con la práctica este flujo se convertirá en una rutina.

---

## Errores frecuentes

- Trabajar sin activar el entorno: Las librerías se instalan en el Python global del sistema.
- Subir `.venv` a GitHub: El repositorio aumenta enormemente de tamaño y contiene miles de archivos innecesarios.
- Olvidar actualizar `requirements.txt`: Otras personas no podrán reproducir el proyecto correctamente.
- Compartir un proyecto sin indicar las dependencias: Obligas a quien lo descargue a adivinar qué librerías necesita instalar.

---

## Aplicación a tu portfolio

Todos los proyectos que construiremos durante esta hoja de ruta incluirán, como mínimo:

```text
README.md
requirements.txt
.gitignore
```

Y el archivo `.gitignore` contendrá como mínimo:

```text
.venv/
```

Gracias a ello, cualquier persona podrá clonar el repositorio, crear un entorno virtual, e instalar las dependencias necesarias para ejecutar el proyecto sin problemas. Este es el estándar esperado en proyectos profesionales.

Recuerda que...
> **Un proyecto profesional no depende del ordenador donde fue creado. Gracias a los entornos virtuales y a `requirements.txt`, cualquier persona puede recrear exactamente el mismo entorno de trabajo.**

---

## Buenas prácticas

- Crea un entorno virtual para cada proyecto.
- Activa el entorno antes de instalar librerías.
- Mantén actualizado `requirements.txt`.
- Nunca subas `.venv` a GitHub.
- Comprueba de vez en cuando que el proyecto puede recrearse desde cero utilizando únicamente el repositorio.

---

