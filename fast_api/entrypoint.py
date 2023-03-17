from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(
    title="Mi Biblioteca",
    version="final"
)

biblioteca = {}
from esquemas import PersonaBiblioteca
from esquemas import PersonaActualizar


@app.get("/",tags=["Home"])
def hello_world_check():
    return {
        "Titulo":"Biblioteca Steam",
        "Version":"v0.0.1"
    }
    
@app.get("/persona",tags=["Biblioteca Total"])
def total():
    """
    Función que retorna todos los usuarios registrados en mi biblioteca

    Returns:
        dicc: Mi biblioteca (Base de datos) 
    """
    return biblioteca

@app.get("/personas/{id}",tags=["Visualizar Usuario"])
def personas_one(id:int):
    """
    Función que Visualiza la información de solo un usuario de mi base de datos

    Args:
        id (str): La id del usuario para acceder a su información

    Returns:
        usuario (dicc): Retorna la información del usuario (un Diccionario) donde se encuentra su id, su nombre, su edad y el libro que presto
    """
    return biblioteca[id]



@app.post("/personas/{id}/{nombre}/{edad}/{libro_prestado}/{fecha_libro}",tags=["Añadir Usuario"])
def personas_add(request:PersonaBiblioteca):
    """
    Función que añade un usuario a nuestra la base de datos, la biblioteca

    Args:
        request (PersonaBiblioteca): Como Argumento le pasamos un objeto de la clase PersonaBiblioteca donde le pedimos un nombre, una edad, un libro Prestado, su fecha de prestamo y su id
        El id de la instancia se lo asignaremos como clave de nuestro diccionario y el contenido como su valor
    
    Return:
        Esta función no retorna nada pues su unica función es agregar ese usuario a nuestra biblioteca.
    """
    biblioteca_interna = {
        "Nombre":request.nombre,
        "Edad":request.edad,
        "Libros":{
            "Libro Prestado": request.libro_prestado,
            "Fecha Libro Prestado":request.fecha_libro_prestado
        }
    }
    biblioteca[request.id] = biblioteca_interna
    

@app.put("/personas/{id}/",tags=["Actualizar Usuario"])

def actualizar(id:int,
                rr:PersonaActualizar):
    """

    Args:
        rr (PersonaActualizar): _description_

    Returns:
        _type_: _description_
    """
    biblioteca[id]["Nombre"] = rr.nombre
    return biblioteca[id]
@app.delete("/personas/{id}/",tags=["Eliminar Usuario"])
def eliminar(id:int):
    """
    Esta funcion elimina el usuario por medio de su id, accede a el y con el método .pop() lo eliminamos
    Args:
        id (str): id del usuario
    """
    biblioteca.pop(id)
    