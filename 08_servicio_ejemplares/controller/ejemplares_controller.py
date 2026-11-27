from typing import List
from fastapi import APIRouter, HTTPException, Response
from service.ejemplares_service import Ejemplares_Service
from model.libro_model import Ejemplar
router=APIRouter()
service=Ejemplares_Service()
@router.get("/ejemplar/{isbn}",response_model=Ejemplar)
def buscar_ejemplar(isbn:int):
    return service.buscar_ejemplar(isbn)