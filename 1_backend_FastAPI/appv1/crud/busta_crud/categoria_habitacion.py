from http.client import HTTPException
from appv1.schemas.busta_schemas.categoria_habitacion import CategoriaHabitacionCreate,CategoriaHabitacionUpdate
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

# Buscar categoria por habitacion:

def get_room_categorie_id(db: Session, id_categoria_habitacion: int ):
    try:
        sql_query = text("SELECT * FROM categoria_habitacion WHERE id_categoria_habitacion = :id_categoria_habitacion")
        result = db.execute(sql_query, {"id_categoria_habitacion": id_categoria_habitacion}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar categoria: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar categoria")
    
    
def update_categoria_habitacion(db: Session, id_categoria_habitacion: int, categoria_habitacion: CategoriaHabitacionUpdate):
    try:
        sql = "UPDATE categoria_habitacion SET "
        params = {"id_categoria_habitacion": id_categoria_habitacion}
        updates = []
        
        if categoria_habitacion.precio_fijo:
            updates.append("precio_fijo = :precio_fijo")
            params["precio_fijo"] = categoria_habitacion.precio_fijo
        
        if categoria_habitacion.tipo_habitacion:
            updates.append("tipo_habitacion = :tipo_habitacion")
            params["tipo_habitacion"] = categoria_habitacion.tipo_habitacion
        
        if categoria_habitacion.id_hotel is not None:
            updates.append("id_hotel = :id_hotel")
            params["id_hotel"] = categoria_habitacion.id_hotel

        # Si no hay campos para actualizar, retorna error
        if not updates:
            raise HTTPException(status_code=400, detail="No hay campos para actualizar")
        
        sql += ", ".join(updates) + " WHERE id_categoria_habitacion = :id_categoria_habitacion"
        
        # Envuelve la consulta SQL en text()
        sql = text(sql)
        
        db.execute(sql, params)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad
        print(f"Error al actualizar la categoría de habitación: {e}")
        raise HTTPException(status_code=400, detail="Error de integridad de datos al actualizar categoría de habitación")
    except SQLAlchemyError as e:
        db.rollback()  # Revertir la transacción en caso de otro tipo de error
        print(f"Error al actualizar la categoría de habitación: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar la categoría de habitación")


def get_all_cateogories_paginated(db: Session, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size

        sql = text(
        "SELECT id_categoria_habitacion, precio_fijo, tipo_habitacion,id_hotel "
        "FROM categoria_habitacion "
        "LIMIT :page_size OFFSET :offset"
        )
        params = {
            "page_size": page_size,
            "offset": offset
        }
        result = db.execute(sql, params).mappings().all()

        count_sql = text("SELECT COUNT(*) FROM categoria_habitacion")
        total_users = db.execute(count_sql).scalar()

        total_pages = (total_users + page_size - 1) // page_size

        return result, total_pages
    except SQLAlchemyError as e:
        print(f"Error al obtener todas las categorias: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener todas las cateogias")
    