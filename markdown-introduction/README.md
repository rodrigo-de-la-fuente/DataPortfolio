# Introducción a Markdown

Markdown es un lenguaje de marcado ligero que permite dar formato a un texto plano utilizando caracteres especiales y símbolos.

Se utiliza ampliamente en el desarrollo de software (para crear documentación en GitHub), en plataformas de notas y gestión de proyectos (como Notion), y en foros y redes sociales (como Reddit o Discord). Permite que el texto sea perfectamente legible tanto en su formato "crudo" como cuando se transforma automáticamente a HTML para la web.

## Objetivo

Aprender la sintaxis básica de Markdown y utilizarla para crear documentación profesional para proyectos de GitHub.

## Contenido

- Títulos y subtítulos
- Párrafos
- Listas enumeradas
- Código integrado en el texto
- Bloques de código
- Citas
- Tablas
- Enlaces
- Inserción de imágenes

## Archivos del proyecto

- `markdown_practice.md`: primera práctica de Markdown donde se aplican títulos, subtítulos, párrafos, listas, código y citas.
- `markdown_advanced.md`: segunda práctica de Markdown donde se aplican tablas, enlaces y se insertan imágenes.

## Tecnologías

- Git: crear repositorio local, hacer commits, visualizar el historial de commits, crear ramas y hacer merge sobre ellas, hacer Pull Requests
- Markdown
- GitHub
- Visual Studio Code

## Aprendizajes

Durante estas prácticas he aprendido a usar Markdown de cara a crear documentos útiles para GitHub con formato profesional, siguiendo una estructura clara para el usuario que quiera visitar el repositorio.

---

# README - Buenas prácticas

A partir de ahora, todos los proyectos que subas a GitHub deberían incluir un `README.md` bien estructurado. Un buen README responde rápidamente a las preguntas que cualquier persona se hará al entrar en tu repositorio:

- ¿Por qué existe este proyecto?
- ¿Qué hace?
- ¿Cómo lo instalo?
- ¿Cómo lo utilizo?
- ¿Qué tecnologías emplea?
- ¿Cómo está organizado?

Si el README responde a esas preguntas, el proyecto transmite profesionalidad desde el primer momento.


## La estructura estándar

La mayoría de proyectos profesionales siguen un esquema parecido a este:

```text
README.md

1. Título
2. Descripción
3. Tecnologías
4. Instalación
5. Uso
6. Estructura del proyecto
7. Resultados o capturas
8. Mejoras futuras
9. Licencia
```

No es obligatorio incluir todas las secciones, pero sí recomendable conocerlas.


1. Título: Debe ser breve y descriptivo. Evita títulos vagos como: `Proyecto Python` o `Trabajo final`. Por ejemplo:

```markdown
# DataPortfolio
```

    O:

```markdown
# Predicción de precios de viviendas
```

    

2. Descripción: Explica el propósito del proyecto en pocas líneas. Piensa que esta será probablemente la primera parte que leerá un reclutador. Un ejemplo:

```markdown
Proyecto de análisis de ventas realizado con Python y Power BI para estudiar la evolución de las ventas mensuales y detectar patrones de comportamiento.
```

3. Tecnologías: Una lista sencilla suele ser suficiente.

```markdown
## Tecnologías

- Python
- Pandas
- NumPy
- Matplotlib
- SQL
- Power BI
```

4. Instalación: Explica cómo poner el proyecto en marcha. Cuantos menos pasos necesite el usuario, mejor. Un ejemplo:

```markdown
## Instalación

git clone https://github.com/usuario/proyecto.git

cd proyecto

pip install -r requirements.txt
```
    

5. Uso: Muestra cómo ejecutar el proyecto.

```bash
python main.py
```

Si requiere parámetros:

```bash
python train.py --epochs 50
```

6. Estructura del proyecto: Es una de las secciones más útiles ya que ayuda a localizar rápidamente los archivos importantes.

```text
proyecto/

│── data/
│── notebooks/
│── src/
│── images/
│── models/
│── README.md
│── requirements.txt
```

7. Resultados: Aquí se pueden incluir imágenes o varios gráficos, y métricas.


8. Mejoras futuras: muestra que el proyecto puede evolucionar.

```markdown
## Mejoras futuras

- Añadir más variables.
- Optimizar el modelo.
- Crear una aplicación con Streamlit.
- Automatizar el entrenamiento.
```

9. Licencia: En proyectos personales basta con indicar una licencia sencilla. Si el repositorio no es público o no quieres permitir reutilización, puedes omitir esta sección.

## Ejemplo de plantilla

A continuación tienes una plantilla muy cercana a la que utilizarás en tu portfolio:

```markdown
# Análisis de ventas

Proyecto de análisis exploratorio de datos realizado con Python.

## Tecnologías

- Python
- Pandas
- Matplotlib
- Seaborn


## Instalación
```

```bash
git clone https://github.com/usuario/analisis-ventas.git

cd analisis-ventas

pip install -r requirements.txt
```

```markdown
## Uso
```

```bash
python main.py
```

```markdown
## Estructura
```

```text
analisis-ventas/

│── data/
│── notebooks/
│── src/
│── images/
│── README.md
│── requirements.txt
```

```markdown
## Resultados

[Aquí irían los resultados]

## Mejoras futuras

- Añadir nuevos indicadores.
- Automatizar el análisis.
- Publicar dashboard.

## Licencia

**MIT**
```

