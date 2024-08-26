from fastapi import HTTPException
from core.security import get_hashed_password
from core.utlis import generateuser_id
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Consultar permisos de un rol por cada modulo
def get_permissions(db: Session, rol: str,modulo:str):
    try:
        sql = text("SELECT p_select,p_insert,p_update,p_delete FROM permisos WHERE nombre_rol = :rol AND nombre_modulo = :modulo")
        result = db.execute(sql, {"rol": rol,"modulo":modulo}).fetchone()
        return result

    except SQLAlchemyError as e:
        print(f"Error al obtener permisos: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuario por email")