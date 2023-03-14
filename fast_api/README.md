# FASTAPI
----
## Creación del Entorno Virtual
1. Instalar librería del entorno virtual ````pip install virtualenv````
2. Creación de entorno virtual ````python -m virtualenv [NOMBRE]````
3. Verificar librerías python global ````pip freeze ```` deben salir varías librerías (Instaladas)
4. Entro a mi entorno virtual (EN WINDOWS DESDE GIT-BASH) ````source venv/Scripts/activate```` y sale el nombre de mi entorno virtual el mi línea de comandos.

## Instalar FastAPI
1. Instalación de FastAPI ````pip install fastapi uvicon````

## Introducción FastAPI
- @app.get("/") es un atributo de mi app, get (obtener)
- "/" es mi ruta raíz
- Solo podemos tener una función por verbo en una ruta
