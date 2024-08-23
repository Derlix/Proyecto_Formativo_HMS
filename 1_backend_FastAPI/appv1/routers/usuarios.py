from appv1.crud.usuarios import create_usuario_sql
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.schemas.usuarios import UsuarioCreate
from db.database import get_db
from typing import List
from appv1.crud.hoteles import get_all_hoteles
#from appv1.routers.login import get_current_usuarios


router = APIRouter()
MODULE = 'usuarios'

@router.post("/create")
async def insert_usuarios(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    # Si el id_hotel no fue proporcionado, mostrar los hoteles disponibles
    if not usuario.id_hotel:
        hoteles_disponibles = get_all_hoteles(db)
        return {
            "mensaje": "Por favor, seleccione un hotel.",
            "hoteles_disponibles": hoteles_disponibles
        }
    
    # Crear el usuario si se ha proporcionado un id_hotel
    respuesta = create_usuario_sql(db, usuario)
    if respuesta:
        return {
            "mensaje": "Usuario registrado con éxito"
        }
