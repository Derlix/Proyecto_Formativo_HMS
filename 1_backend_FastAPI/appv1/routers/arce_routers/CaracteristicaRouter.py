from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.arce_crud.caracteristica import crear_caracteristica, eliminar_caracteristica, obtener_caracteristicas
from appv1.schemas.arce_schemas.caracteristicas import CaracteristicaCreate, CaracteristicaResponse
from db.database import get_db

router = APIRouter()

@router.post("/feature-create")
async def crearCaracteristica(rol: CaracteristicaCreate, db: Session = Depends(get_db)):
    respuesta = crear_caracteristica(db,rol)
    if respuesta:
        return {"mensaje":"caracteristica Registrada con exito"}
    
@router.get("/get-all-features/", response_model=List[CaracteristicaResponse])
def read_all( db: Session = Depends(get_db)):
    return obtener_caracteristicas(db)

@router.delete("/feature-delete/{caracteristica_id}")
async def eliminarCaracteristica(caracteristica_id: int, db: Session = Depends(get_db)):
    respuesta = eliminar_caracteristica(db, caracteristica_id)
    if respuesta:
        return {"mensaje": "Característica eliminada con éxito"}