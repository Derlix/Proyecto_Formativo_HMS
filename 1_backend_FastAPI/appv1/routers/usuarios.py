from appv1.crud.usuarios import create_usuario_sql, get_usuarios_by_email,get_all_users,get_usuario_by_id,update_user,get_all_users_paginated,delete_usuarios
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.schemas.usuarios import UsuarioCreate,UsuarioResponse
from appv1.routers.login import get_current_user 
from appv1.crud.permisos import get_permissions

from appv1.schemas.usuarios import PaginatedUsuariosResponse, UsuarioUpdate
from db.database import get_db

from typing import Dict, List

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
    current_user : UsuarioResponse = Depends(get_current_user)
):
    permisos = get_permissions(db, current_user.user_role, MODULE)
    if current_user.mail != email: 
        if not permisos.p_select:
            raise HTTPException(status_code=401, detail="Usuario no autorizado")
    usuarios = get_usuarios_by_email(db,email)
    if len(usuarios) == 0:
        raise HTTPException(status_code=404, detail="No hay usuarios")
    return usuarios



@router.get("/get-all/",response_model = List[UsuarioResponse])
async def read_all_user(
    db: Session = Depends(get_db),
    current_user : UsuarioResponse = Depends(get_current_user)
):
    permisos = get_permissions(db, current_user.usuario_rol, MODULE)
    if not permisos.p_select: 
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
        
    usuarios = get_all_users(db)
    if len(usuarios) == 0:
        raise HTTPException(status_code=404, detail="No hay usuarios")
    return usuarios

# Endpoint para actualizar un usuario
@router.put("/update/", response_model=dict)
def update_user_by_id(
    id_usuario: str,
    user: UsuarioUpdate,
    db: Session = Depends(get_db),
    current_user : UsuarioResponse = Depends(get_current_user)
):
    permisos = get_permissions(db, current_user.usuario_rol, MODULE)
    if current_user.id_usuario != id_usuario: 
        if not permisos.p_update:
            raise HTTPException(status_code=401, detail="Usuario no autorizado")
    verify_user = get_usuario_by_id(db, id_usuario)
    if verify_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db_user = update_user(db, id_usuario, user)
    if db_user:
        return {"mensaje": "registro actualizado con éxito",
                "nombre_usuario":user.nombre_completo,
                "id_usuario":id_usuario}
    
# usuarios paginados
@router.get("/users-by-page/", response_model=PaginatedUsuariosResponse)
def get_all_users_by_page(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
    current_user : UsuarioResponse = Depends(get_current_user)
):
    permisos = get_permissions(db, current_user.usuario_rol, MODULE)
    if not permisos.p_select: 
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    users, total_pages = get_all_users_paginated(db, page, page_size)

    return {
        "usuarios": users,
        "total_paginas": total_pages,
        "pagina_actual": page,
        "pagina_cantidad": page_size
    }

@router.delete("/delete/{id_usuario}", response_model=dict)
def delete_user_by_id(
    id_usuario: str,
    db: Session = Depends(get_db),
    current_user : UsuarioResponse = Depends(get_current_user)
):
    permisos = get_permissions(db, current_user.usuario_rol, MODULE)
    if current_user.id_usuario != id_usuario: 
        if not permisos.p_delete:
            raise HTTPException(status_code=401, detail="Usuario no autorizado")
    user = get_usuario_by_id(db, id_usuario)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    result = delete_usuarios(db, id_usuario)
    if result:
        return {"mensaje": "Usuario eliminado con éxito"}
    