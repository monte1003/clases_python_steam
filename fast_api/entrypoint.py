from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

biblioteca = {}
from esquemas import PersonaBiblioteca
from esquemas import PersonaActualizar


@app.get("/")
def hello_world_check():
    return {
        "Titulo":"Biblioteca Steam",
        "Version":"v0.0.1"
    }
    
@app.get("/persona")
def total():
    return biblioteca

@app.get("/personas/{id}")
def personas_one(id:str):
    return biblioteca[id]



@app.post("/personas/{id}/{nombre}/{edad}/{libro_prestado}/{fecha_libro}")
def personas_add(request:PersonaBiblioteca):
    biblioteca_interna = {
        "Nombre":request.nombre,
        "Edad":request.edad,
        "Libros":{
            "Libro Prestado": request.libro_prestado,
            "Fecha Libro Prestado":request.fecha_libro_prestado
        }
    }
    biblioteca[request.id] = biblioteca_interna
    

@app.put("/personas/{id}/{nombre}/{edad}")

def actualizar(request:PersonaActualizar):
    for i in biblioteca[request.id]:
        i.nombre = request.nombre
        i.edad = request.edad
        return biblioteca[request.id]