from typing import List
from appv1.crud.juanca_crud.habitaciones_caracteristicas import (
    create_habitacion_caracteristica,
    get_all_habitacion_caracteristicas,
    get_habitacion_caracteristica_by_id,
    update_habitacion_caracteristica,
    delete_habitacion_caracteristica
)
from appv1.schemas.juanca_schemas.habitacion_caracteristicas import (
    HabitacionCaracteristicaResponse,
    HabitacionCaracteristicaCreate
)
from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

# Crear una nueva habitacion_caracteristica
@router.post("/", response_model=HabitacionCaracteristicaResponse)
async def create_new_habitacion_caracteristica(
    caracteristica: HabitacionCaracteristicaCreate, db: Session = Depends(get_db)
):
    try:
        caracteristica_created = create_habitacion_caracteristica(db, caracteristica)
        return caracteristica_created
    except HTTPException as e:
        raise e

# Obtener todas las habitacion_caracteristicas
@router.get("/", response_model=List[HabitacionCaracteristicaResponse])
async def read_all_habitacion_caracteristicas(db: Session = Depends(get_db)):
    caracteristicas = get_all_habitacion_caracteristicas(db)
    if not caracteristicas:
        raise HTTPException(status_code=404, detail="No hay características de habitaciones")
    return caracteristicas

# Obtener una habitacion_caracteristica específica por ID
@router.get("/{id_habitacion}/{id_caracteristica}", response_model=HabitacionCaracteristicaResponse)
async def read_habitacion_caracteristica(
    id_habitacion: int, id_caracteristica: int, db: Session = Depends(get_db)
):
    caracteristica = get_habitacion_caracteristica_by_id(db, id_habitacion, id_caracteristica)
    if not caracteristica:
        raise HTTPException(status_code=404, detail="Característica de habitación no encontrada")
    return caracteristica


@router.put("/{id_habitacion}/{id_caracteristica}", response_model=HabitacionCaracteristicaResponse)
async def update_habitacion_caracteristica_info(
    id_habitacion: int,
    id_caracteristica: int,
    caracteristica: HabitacionCaracteristicaCreate,
    db: Session = Depends(get_db)
):
    updated_caracteristica = update_habitacion_caracteristica(db, id_habitacion, id_caracteristica, caracteristica)
    if not updated_caracteristica:
        raise HTTPException(status_code=404, detail="Característica de habitación no encontrada")
    return updated_caracteristica


# Eliminar una habitacion_caracteristica
@router.delete("/{id_habitacion}/{id_caracteristica}")
async def delete_habitacion_caracteristica_info(
    id_habitacion: int, id_caracteristica: int, db: Session = Depends(get_db)
):
    deleted_caracteristica = delete_habitacion_caracteristica(db, id_habitacion, id_caracteristica)
    if not deleted_caracteristica:
        raise HTTPException(status_code=404, detail="Característica de habitación no encontrada")
    return {"detail": "Característica de habitación eliminada exitosamente"}
