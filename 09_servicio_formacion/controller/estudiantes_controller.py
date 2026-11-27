from typing import List
from fastapi import APIRouter, HTTPException,Response
from service.formacion_service import Formacion_Service
from model.estudiantes_model import Estudiante
router=APIRouter()
estudiante_service=Formacion_Service()
@router.get(path="/estudiantes/{min}/{max}",response_model=List[Estudiante])
def estudiantes_nota(min:float,max:float):
    return estudiante_service.buscar_por_rango(min,max)
@router.post(path="/estudiantes",response_model=Estudiante)
def nuevo_estudiante(estudiante:Estudiante,response:Response):
    if(estudiante_service.alta_estudiante(estudiante)):
        response.status_code=201
        return estudiante
    raise HTTPException(status_code=409,detail="Los datos del estudiante no son válidos")