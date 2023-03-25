
from pydantic import BaseModel
class PersonaBiblioteca(BaseModel):
    id:int
    nombre:str
    edad:int
    libros:dict
    id_libro:int
    libro_prestado:str
    
    
class PersonaActualizar(BaseModel):
    nombre:str