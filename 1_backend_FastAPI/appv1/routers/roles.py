from fastapi import HTTPException
from appv1.crud.roles import create_roles_sql,get_roles_by_rolesname,get_all_roles
from fastapi import APIRouter,Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.schemas.roles import RolCreate
from db.database import get_db
from typing import List


router = APIRouter()

@router.post("/create")
async def insert_rol(rol: RolCreate, db: Session = Depends(get_db)):
    respuesta = create_roles_sql(db,rol)
    if respuesta:
        return {"mensaje":"Rol Registrado con exito"}
    

@router.get("/get_rol_by_rolname", response_model=RolCreate)
async def read_rol_by_rolname(rol: str, db: Session = Depends(get_db)):
    role = get_roles_by_rolesname(db, rol)
    if role is None:
        raise HTTPException(status_code=404, detail="No hay roles")
    return role



@router.get("/get_all_roles", response_model=List[RolCreate])
async def read_all_roles(db:Session = Depends(get_db)):
    roles = get_all_roles(db)
    if len(roles)== 0:
        raise HTTPException(status_code=404, detail="No hay roles")
    return roles