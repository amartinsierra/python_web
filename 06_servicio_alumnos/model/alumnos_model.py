from pydantic import BaseModel, EmailStr, Field

""" class Alumno(BaseModel):
    idAlumno:int
    nombre:str=Field(min_length=5,max_length=25)
    curso:str
    nota:float=Field(ge=0,le=10)
    email:EmailStr """

class Alumno(BaseModel):
    idAlumno:int
    nombre:str
    curso:str
    nota:float
    email:str
 