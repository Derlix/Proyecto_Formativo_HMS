from typing import List
from appv1.crud.nicolas_crud.impuestos import create_tax
from appv1.schemas.nicolas_schemas.Productos import ProductoCreate
from fastapi import APIRouter,Depends #type: ignore
from db.database import get_db
from sqlalchemy.orm import Session # type: ignore

router = APIRouter()

@router.post("/create")
async def insert_product(producto: ProductoCreate, db: Session = Depends(get_db)):
    respuesta = create_tax(db, producto)
    if respuesta:
        return {"mensaje":"producto registrado con exito"}
    else:
        return {"mensaje":"El producto no se ha podido registrar con exito"}


# # Endpoint para actualizar un usuario
# @router.put("/update/", response_model=dict)
# def update_user_by_id(
#     user_id: str, 
#     user: UserUpdate, 
#     db: Session = Depends(get_db),
#     current_user: UserResponse = Depends(get_current_user)
# ):  
    
#     permisos = get_permissions(db, current_user.user_role, MODULE)
#     if current_user.user_id != user_id:
#         if not permisos.p_update:
#             raise HTTPException(status_code=401, detail="Usuario no autorizado") 
        
#     verify_user = get_user_by_id(db, user_id)
#     if verify_user is None:
#         raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
#     db_user = update_user(db, user_id, user)
#     if db_user:
#         return {"mensaje": "registro actualizado con éxito"}

# @router.delete("/delete/{user_id}", response_model=dict)
# def delete_user_by_id(
#     user_id: str, 
#     db: Session = Depends(get_db),
#     current_user: UserResponse = Depends(get_current_user)
# ):  
#     permisos = get_permissions(db, current_user.user_role, MODULE)
#     if current_user.user_id != user_id:
#         if not permisos.p_delete:
#             raise HTTPException(status_code=401, detail="Usuario no autorizado") 
    
#     user = get_user_by_id(db, user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
#     result = delete_user(db, user_id)
#     if result:
#         return {"mensaje": "Usuario eliminado con éxito"}
    
# # usuarios paginados
# @router.get("/users-by-page/", response_model=PaginatedUsersResponse)
# def get_all_users_by_page(
#     page: int = 1, 
#     page_size: int = 10, 
#     db: Session = Depends(get_db),
#     current_user: UserResponse = Depends(get_current_user)
# ):
#     permisos = get_permissions(db, current_user.user_role, MODULE)
#     if not permisos.p_select:
#         raise HTTPException(status_code=401, detail="Usuario no autorizado") 
    
#     users, total_pages = get_all_users_paginated(db, page, page_size)

#     return {
#         "users": users,
#         "total_pages": total_pages,
#         "current_page": page,
#         "page_size": page_size
#     }
    
