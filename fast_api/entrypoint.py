from fastapi import FastAPI
from typing import Union
app = FastAPI()
#Registramos una función en mi app en ruta (endpoint)
# Cada ruta ejecuta una función
# "/" ruta raíz
# Solo podemos tener una función por verbo en una ruta
@app.get("/hola")
def hola():
    return {"Hello": "World"}

# Esto es una ruta estatica
#Area de un Cuadrado
@app.get("/cuadrado/{lado}")
def calcular(lado:float):
    area = lado * lado
    return f"El área del cuadrado es de {area}"

@app.get("/edad/{nombre}/{edad}")

def mayor_menor(
    nombre:str,
    edad:int
):
    if edad>=18:
        return f"{nombre} al tener {edad} años es mayor de edad"
    return f"{nombre} al tener {edad} años es menor de edad"