from appv1.crud.usuarios import create_usuario_sql
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.schemas.usuarios import UsuarioCreate
from db.database import get_db
from typing import List
#from appv1.routers.login import get_current_usuarios


router = APIRouter()
MODULE = 'usuarios'

@router.post("/create")
                #Esquema para recibir datos
async def insert_usuarios(
    usuarios: UsuarioCreate,
    db: Session = Depends(get_db)
    #current_usuarios: usuariosResponse = Depends(get_current_usuarios)
):
    #permisos = get_permissions(db, current_usuarios.get("rol"), MODULE)
    #if not permisos.p_insert:
    #    raise HTTPException(status_code=401, detail="Usuario no autorizado")

    #if current_usuarios.usuarios_role != 'SuperAdmin':
    #    if  usuarios.usuarios_role == 'SuperAdmin':
    #        raise HTTPException(status_code=401, detail="Usuario no autorizado")

    respuesta = create_usuario_sql(db,usuarios)
    if respuesta:
        return {
            "mensaje":"Usuario Registrado con exito"}