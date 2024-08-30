from http.client import HTTPException
from appv1.schemas.busta_schemas.categoria_habitacion import CategoriaHabitacionCreate
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy import text # type: ignore
from sqlalchemy.exc import SQLAlchemyError,IntegrityError # type: ignore
from fastapi import  HTTPException # type: ignore

def create_room_categorie_name(db: Session, category:CategoriaHabitacionCreate):
    try:
        sql_query = text(
        "INSERT INTO categoria_habitacion(precio_fijo, tipo_habitacion, id_hotel)"
        "VALUES (:precio_fijo, :tipo_habitacion, :id_hotel)"
        
        )
        params = {
            "precio_fijo": category.precio_fijo,
            "tipo_habitacion": category.tipo_habitacion,
            "id_hotel": category.id_hotel
        }
        db.execute(sql_query, params)
        db.commit()
        return True 
    
    except IntegrityError as e:
        db.rollback()
        print(f"Error al crear categoria: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El id de categoria ya existe")
            else:
                raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear categoria")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear categoria: {e}")
        raise HTTPException(status_code=500, detail="Error al crear el categoria")

def get_all_room_categories(db: Session):
    try:
        sql = text("SELECT * FROM categoria_habitacion")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar categoria habitaciones: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar categoria habitaciones")

def get_room_categorie_name(db: Session, p_room_categorie_name: str ):
    try:
        sql_query = text("SELECT * FROM categoria_habitacion WHERE tipo_habitacion = :tipo_habitacion")
        result = db.execute(sql_query, {"tipo_habitacion": p_room_categorie_name}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar categoria: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar categoria")
    
    
# def update_user(db: Session, user_id: str, user: UserUpdate):
#     try:
#         sql = "UPDATE users SET "
#         params = {"user_id": user_id}
#         updates = []
#         if user.full_name:
#             updates.append("full_name = :full_name")
#             params["full_name"] = user.full_name
#         if user.mail:
#             updates.append("mail = :mail")
#             params["mail"] = user.mail
#         if user.user_role:
#             updates.append("user_role = :user_role")
#             params["user_role"] = user.user_role
#         if user.user_status is not None:
#             updates.append("user_status = :user_status")
#             params["user_status"] = user.user_status
#         sql += ", ".join(updates) + " WHERE user_id = :user_id"

# Envuelve la consulta SQL en text()

    #     sql = text(sql)

    #     db.execute(sql, params)
    #     db.commit()
    #     return True
    # except IntegrityError as e:
    #     db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
    #     print(f"Error al actualizar usuario: {e}")
    #     if 'for key 'mail'' in str(e.orig):
    #         raise HTTPException(status_code=400, detail="Error. El email ya está registrado")
    #     else:
    #         raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al actualizar usuario")
    # except SQLAlchemyError as e:
    #     db.rollback()
    #     print(f"Error al actualizar usuario: {e}")
    #     raise HTTPException(status_code=500, detail="Error al actualizar usuario")
    
    
# Eliminar una Categoia Habitacion
def delete_user(db: Session, id_categoria_habitacion: int):
    try:
        sql = text("UPDATE categoria_habitacion SET user_status = 0  WHERE user_id = :user_id")
        db.execute(sql, {"id_categoria_habitacion": id_categoria_habitacion})
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al eliminar usuario: {e}")
        raise HTTPException(status_code=400, detail="Error. Integridad de datos al eliminar usuario")
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al eliminar usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar usuario")