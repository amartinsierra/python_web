from typing import List
from fastapi import APIRouter, HTTPException
from model.libros_model import Libro
from service.libros_service import LibrosService
router=APIRouter()
service=LibrosService()
@router.post("/libro",response_model=Libro)
def guardar_libro(libro:Libro):
    if service.alta_libro(libro)==None:
        raise HTTPException(status_code=409,detail="No admite isbn repetido")
    return libro
@router.get("/libro/{isbn}",response_model=Libro)
def buscar_libro(isbn:int):
    return service.buscar_libro(isbn)
@router.delete("/libro/{isbn}")
def eliminar_libro(isbn:int):
    service.eliminar_libro(isbn)