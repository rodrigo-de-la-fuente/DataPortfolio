# Lección 5.1 — Estructura de carpetas

## Objetivo

Aprender a organizar cualquier proyecto de forma profesional para que sea fácil de entender, mantener y ampliar.

### ¿Por qué es importante?

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


### La idea principal

Cada carpeta debe tener **una única responsabilidad**: Piensa en una casa. La cocina es para cocinar. El dormitorio es para dormir. El garaje es para guardar el coche. No mezclamos funciones. Con un proyecto ocurre exactamente lo mismo.

> **La organización no sirve únicamente para proyectos grandes; sirve para que los proyectos pequeños puedan crecer sin convertirse en un caos.**


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

## Buenas prácticas

- Separa siempre datos y código.
- No guardes imágenes junto a los scripts.
- No pongas notebooks dentro de `src`.
- Guarda los resultados en `outputs`.
- Nunca modifiques los datos originales.
- Utiliza la misma estructura en todos tus proyectos.

---
