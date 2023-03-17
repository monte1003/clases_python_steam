from pydantic import BaseModel
class PersonaBiblioteca(BaseModel):
    id:str
    nombre:str
    edad:str
    libros:dict
    libro_prestado:str
    fecha_libro_prestado:str
    
class PersonaActualizar(BaseModel):
    id:str
    nombre:str
    edad:str