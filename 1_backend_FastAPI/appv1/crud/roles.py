from sqlalchemy import text
from sqlalchemy.orm import Session
from appv1.schemas.roles import RolCreate
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from fastapi import HTTPException

# Crear un roles
def create_roles_sql(db: Session, roles:RolCreate):
    sql_query = text(
        "INSERT INTO roles (nombre_rol) "
        "VALUES (:nombre_rol)"
    )
    params = {
        "nombre_rol":roles.nombre_rol
    }
    db.execute(sql_query, params)
    db.commit()
    return True  # Retorna True si la inserción fue exitosa


def get_roles_by_rolesname(db: Session, roles: str):
    try:
        sql = text("SELECT * FROM roles WHERE nombre_rol = :nombre_rol")
        result = db.execute(sql, {"nombre_rol": roles}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar roles por el nombre: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar roles por el nombre")


def get_all_roles(db: Session):
    try:
        sql = text("SELECT * FROM roles")
        result = db.execute(sql).fetchall()
        return result

    except SQLAlchemyError as e:
        print(f"Error al buscar los roles: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar roles")
        