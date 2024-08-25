from appv1.crud.usuarios import create_usuario_sql, get_usuarios_by_email
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.usuarios import UsuarioCreate,UsuarioResponse
from appv1.routers.login import get_current_user 
from appv1.crud.permisos import get_permissions
from db.database import get_db


router = APIRouter()
MODULE = 'usuarios'

@router.post("/create")
async def insert_usuarios(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db),
    current_user: UsuarioResponse = Depends(get_current_user)
):
    permisos = get_permissions(db,current_user.usuario_rol, MODULE)
    if not permisos.p_insert:
        raise HTTPException(status_code=401,detail="Usuario no autorizado")
    if current_user.usuario_rol != 'SuperAdmin':
        if usuario.usuario_rol == 'SuperAdmin':
            raise HTTPException(status_code=401,detail="Usuario no autorizado")
    respuesta = create_usuario_sql(db, usuario)
    if respuesta:
        return {"mensaje": "Usuario registrado con éxito"}
    else:
        raise HTTPException(status_code=500, detail="Error al crear el usuario.")

@router.get("/read", response_model=UsuarioResponse)
async def get_usuario_email(
    email:str,
    db:Session = Depends(get_db),
):
    usuarios = get_usuarios_by_email(db,email)
    if len(usuarios) == 0:
        raise HTTPException(status_code=404, detail="No hay usuarios")
    return usuarios
