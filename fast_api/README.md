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
### Ejecutar Servidor
- Para ejecutar el servidor usamos el comando ````uvicorn entrypoint:app --reload```` para que se actualize solo 

### Importando FastAPI
- Para importar fastapi decimos lo siguiente ````from fastapi import FastAPI````

### Creación de Objeto
- Para crear un objeto de fastapi es ````app = FastAPI()````
---
# Buenas Prácticas
### Buenas Prácticas
- Documentación 
- Comentarios
- Organización (que sea legible)
### Código (Buenas Prácticas)
- Hello World Check
- Crear un archivo por cada componente
---

# Verbos HTTP
|metodo|accion DB|Uso|
|--|--|--|
|Post|Create|Crea un nuevo registro en nuestra base de datos
|Get|Read|Acceder, Recuperar o leer información de nuestra base de datos
|Put|Update|Actualiza Registros de nuestra base de datos|
|Delete|Eliminar|Elimina registros de nuestra base de datos|

### OS
- Es una librería que nos conecta y nos permite usar funciones del os
- os.getcwd = ````Nos muestra en donde estamos parados (carpeta)````
. os.system() = ````Imprime cadenas de texto en pantalla````

### Variables de Entorno
- Las variables de entorno son variables a las que se asignan valores externamente al programa Python. Los desarrolladores normalmente las establecen en la línea de comandos antes de invocar el ejecutable de Python. 
- Afectan el código desde afuera, sin alterar sus lógicas
- Para pasar nuestras variables de entorno usamos el comando ````from dotenv import load_dotenv````
- Las variables de entorno se crean en un archivo ````.env```` dentro de la misma carpeta