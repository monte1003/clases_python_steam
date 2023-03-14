from fastapi import FastAPI
from typing import Union
app = FastAPI()
#Registramos una función en mi app en ruta (endpoint)
# Cada ruta ejecuta una función
# "/" ruta raíz
# Solo podemos tener una función por verbo en una ruta
@app.get("/")
def hola():
    return {"Hello": "World"}


@app.get("/adios")
def adios():
    return "adios mundo"


@app.get("/pato")
def diccionario():
    return {
        "Nombre":"Isaac",
        "Apellido":"Monterrosa"   
    }

@app.get("/pepito")
def mundo():
    return f"El mundo es {2+2}"

@app.get("/salcedo")
def osasuna():
    return [1,2,3,4,5]

