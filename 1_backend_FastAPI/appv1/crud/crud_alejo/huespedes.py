from fastapi import HTTPException
from appv1.schemas.schemas_alejo.huespedes import HuespedCreate, HuespedDelete, HuespedUpdate
from core.security import get_hashed_password
from core.utlis import generateuser_id
from sqlalchemy.orm import Session
from sqlalchemy import false, text
from sqlalchemy.exc import SQLAlchemyError, IntegrityError




def get_huesped_by_id(db: Session, id_huesped: str):
    sql = text("SELECT * FROM huespedes WHERE id_huesped = :id_huesped")
    result = db.execute(sql, {"id_huesped": id_huesped}).fetchone()
    return result



 
def create_huesped_sql(db: Session, huesped: HuespedCreate):
    try:
        sql_query = text(
        "INSERT INTO huespedes (id_huesped, nombre_completo, tipo_documento, numero_documento, fecha_expedicion, email, telefono, ocupacion, direccion) "
        "VALUES (:id_huesped, :nombre_completo, :tipo_documento, :numero_documento, :fecha_expedicion, :email, :telefono, :ocupacion, :direccion)"
        )

    
        params = {
            "id_huesped": generateuser_id(),
            "nombre_completo": huesped.nombre_completo,
            "tipo_documento": huesped.email,
            "numero_documento": huesped.numero_documento,
            "fecha_expedicion": huesped.fecha_expedicion,
            "email": huesped.email,
            "telefono": huesped.telefono,
            "ocupacion": huesped.ocupacion,
            "direccion": huesped.direccion,
        }
        db.execute(sql_query, params)
        db.commit()
        return True  
    
    except IntegrityError as e:
        db.rollback()  
        print(f"Error al crear huesped: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID generado automaticamente ya existe. Volver a intentar")
            if 'for key \'email\'' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El email ya está registrado")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear huesped")
    except SQLAlchemyError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear huesped: {e}")
        raise HTTPException(status_code=500, detail="Error al crear huesped")
    


def get_huesped_by_email(db: Session, p_email: str):
        try:
             sql = text("SELECT * FROM huespedes WHERE email = :email")
             result = db.execute(sql, {"email": p_email}).fetchone()
             
             return result
        
        except SQLAlchemyError as e:
            print(f"Error al buscar huesped por email: {e}")
            raise HTTPException(status_code=500, detail="Error al buscar huesped por email")


def get_all_huespedes(db: Session):
        try:
             sql = text("SELECT * FROM huespedes WHERE huesped_status = True")
             result = db.execute(sql).fetchall()
             return result
        
        except SQLAlchemyError as e:
            print(f"Error al buscar huesped: {e}")
            raise HTTPException(status_code=500, detail="Error al buscar huesped")
        
        
def update_huesped(db: Session, id_huesped: str, huesped:HuespedUpdate):
    try:
        sql = "UPDATE huespedes SET "
        params = {"id_huesped": id_huesped}
        updates = []
        if huesped.nombre_completo:
            updates.append("nombre_completo = :nombre_completo")
            params["nombre_completo"] = huesped.nombre_completo
        if huesped.tipo_documento:
            updates.append("tipo_documento = :tipo_documento")
            params["tipo_documento"] = huesped.tipo_documento
        if huesped.numero_documento:
            updates.append("numero_documento = :numero_documento")
            params["numero_documento"] = huesped.numero_documento
        if huesped.fecha_expedicion:
            updates.append("fecha_expedicion = :fecha_expedicion")
            params["fecha_expedicion"] = huesped.fecha_expedicion
        if huesped.email:
            updates.append("email = :email")
            params["email"] = huesped.email
        if huesped.telefono:
            updates.append("telefono = :telefono")
            params["telefono"] = huesped.telefono
        if huesped.ocupacion:
            updates.append("ocupacion = :ocupacion")
            params["ocupacion"] = huesped.ocupacion
        if huesped.direccion:
            updates.append("direccion = :direccion")
            params["direccion"] = huesped.direccion
        if huesped.huesped_status is not None:
            updates.append("huesped_status = :huesped_status")
            params["huesped_status"] = huesped.huesped_status
        sql += ", ".join(updates) + " WHERE id_huesped = :id_huesped"         

        sql = text(sql)
        
        db.execute(sql, params)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  
        print(f"Error al actualizar huesped: {e}")
        if 'for key \'email\'' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error. El email ya está registrado")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al actualizar huesped")
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al actualizar huesped: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar huesped")
    


def delete_huesped(db: Session, id_huesped:str, huesped: HuespedDelete):
    try:
        sql = "UPDATE huespedes SET "
        params = {"id_huesped": id_huesped}
        updates = []
        if huesped.huesped_status is not None:
            updates.append("huesped_status = :huesped_status")
            params["huesped_status"] = huesped.huesped_status
        sql += ", ".join(updates) + " WHERE id_huesped = :id_huesped"         
     
        sql = text(sql)
        
        db.execute(sql, params)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al eliminar huesped: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar huesped")



def get_all_huespedes_paginated(db: Session, page: int = 1, page_size: int = 10):
    try:
       
        offset = (page - 1) * page_size

        sql = text(
            "SELECT id_huesped, nombre_completo, tipo_documento, numero_documento, fecha_expedicion, email, telefono, ocupacion, direccion, huesped_status, created_at, updated_at "
            "FROM huespedes "
            "ORDER BY created_at DESC "  
            "LIMIT :page_size OFFSET :offset"
        )
        params = {
            "page_size": page_size,
            "offset": offset
        }
        result = db.execute(sql, params).mappings().all()

        count_sql = text("SELECT COUNT(*) FROM huepedes")
        total_users = db.execute(count_sql).scalar()

        total_pages = (total_users + page_size - 1) // page_size

        return result, total_pages
    except SQLAlchemyError as e:
        print(f"Error al obtener todos los huespedes: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener todos los huespedes")
    