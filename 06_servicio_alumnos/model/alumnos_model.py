from pydantic import BaseModel

class Alumno(BaseModel):
    idAlumno:int
    nombre:str
    curso:str
    nota:float
    email:str
 