# ATS_MATCHER
Muestra si tu chamba es compatible

Descripción

Aplicación en Python con FastAPI que analiza qué tan bien coincide un currículum con una descripción de puesto. Calcula un puntaje de similitud usando TF-IDF y Cosine Similarity, extrae términos clave y muestra palabras faltantes que deberían incluirse. Incluye una interfaz web sencilla y una API REST.

Tecnologías:

Python 3.11+

FastAPI

Uvicorn

SQLModel

scikit-learn

Jinja2

Instalación

Clonar el repositorio.

Crear y activar un entorno virtual:

Windows:

python -m venv .venv
.\.venv\Scripts\activate


Linux/Mac:

python -m venv .venv
source .venv/bin/activate


Instalar dependencias:

pip install -r requirements.txt


Ejecutar el servidor:

Si main.py está dentro de src/ats_matcher:

python -m uvicorn ats_matcher.main:app --reload --app-dir src


Si main.py está directamente en ats_matcher:

python -m uvicorn main:app --reload

Uso

Acceder en el navegador a:

http://127.0.0.1:8000


La interfaz permite pegar el texto del currículum y de la vacante para obtener el puntaje de coincidencia y los términos clave.
La documentación de la API está disponible en:

http://127.0.0.1:8000/docs

Endpoints principales

GET / formulario web.

POST /api/score recibe JSON con resume y job y devuelve puntaje, términos relevantes y términos faltantes.

GET /docs documentación interactiva.

Estructura
ats_matcher/
 └─ src/
    └─ ats_matcher/
       ├─ main.py
       ├─ scoring.py
       ├─ keywords.py
       ├─ storage.py
       ├─ schemas.py
       └─ templates/
           ├─ base.html
           └─ index.html
requirements.txt
README.md

Dependencias

El archivo requirements.txt incluye:

fastapi

uvicorn

jinja2

sqlmodel

scikit-learn

numpy

pydantic

python-multipart

Futuras mejoras

Lectura automática de archivos PDF.

Exportación de reportes en PDF.

Interfaz más completa con frameworks modernos.

Integración con modelos de lenguaje para sugerencias más avanzadas.
