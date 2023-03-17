
from pydantic import BaseModel
class PersonaBiblioteca(BaseModel):
    id:int
    nombre:str
    edad:int
    libros:dict
    libro_prestado:str
    fecha_libro_prestado:str
    
class PersonaActualizar(BaseModel):
    nombre:str