from typing import List
from appv1.crud.juanca_crud.habitacines import get_all_rooms, get_room_by_id, create_room, delete_room, update_room
from appv1.schemas.juanca_schemas.habitaciones import HabitacionResponse, HabitacionCreate
from fastapi import APIRouter,Depends,HTTPException # type: ignore
from db.database import get_db
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy import text # type: ignore

router = APIRouter()

# Create a new habitacion
@router.post("/", response_model=HabitacionResponse)
async def create_new_room(room: HabitacionCreate, db: Session = Depends(get_db)):
    try:
        room_created = create_room(db, room)
        return room_created
    except HTTPException as e:
        raise e

# Obtener todas las habitaciones
@router.get("/", response_model=List[HabitacionResponse])
async def read_all_rooms(db: Session = Depends(get_db)):
    habitaciones = get_all_rooms(db)
    if not habitaciones:
        raise HTTPException(status_code=404, detail="No hay habitaciones")
    return habitaciones

# Get a specific habitacion by id
@router.get("/{id_habitacion}", response_model=HabitacionResponse)
async def read_room(id_habitacion: int, db: Session = Depends(get_db)):
    room = get_room_by_id(db, id_habitacion)
    if not room:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    return room


# Actualizar Habitacion
@router.put("/{id_habitacion}", response_model=HabitacionResponse)
async def update_room_info(id_habitacion: int, room: HabitacionCreate, db: Session = Depends(get_db)):
    updated_room = update_room(db, id_habitacion, room)
    if not updated_room:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    return updated_room


# Eliminar habitacion 
@router.delete("/{id_habitacion}")
async def delete_room_info(id_habitacion: int, db: Session = Depends(get_db)):
    deleted_room = delete_room(db, id_habitacion)
    if not deleted_room:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    return deleted_room
