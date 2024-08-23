from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from appv1.schemas.hoteles import  HotelesCreate, HotelesResponse, HotelesUpdate
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


def get_hotel_by_id(db: Session, hotel_id: int):
    sql = text("SELECT * FROM hoteles WHERE id_hotel = :id_hotel")
    result = db.execute(sql, {"id_hotel": hotel_id}).fetchone()
    print(result)
    return result

def create_hotel_sql(db: Session, hotel: HotelesCreate):

    try:
        sql_query = text(
            "INSERT INTO hoteles (nombre, ubicacion, direccion, telefono) "
            "VALUES (:nombre, :ubicacion, :direccion, :telefono)"
        )
        params = {
            "nombre": hotel.nombre,
            "ubicacion": hotel.ubicacion,
            "direccion": hotel.direccion,
            "telefono": hotel.telefono
        }
        db.execute(sql_query, params)
        db.commit()
        return True  # Retorna True si la inserción fue exitosa
    
    except IntegrityError as e:
            db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
            print(f"Error al crear el hotel: {e}")
            if 'Duplicate entry' in str(e.orig):
             if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID del hotel ya está en uso")
            else:
             raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear el hotel")
    
    except SQLAlchemyError as e:
            db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
            print(f"Error al crear hotel: {e}")
            raise HTTPException(status_code=500, detail="Error al crear el hotel")
   
def get_all_hoteles(db: Session):
    try:
         sql = text("SELECT * FROM hoteles")
         result = db.execute(sql).fetchall()
         return result
    except SQLAlchemyError as e:
            db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
            print(f"Error al obtener los hoteles: {e}")
            raise HTTPException(status_code=500, detail="Error al buscar las hoteles")
    
def update_hotel(db: Session, id_hotel: int, hotel: HotelesUpdate):
    try:

        sql = "UPDATE hoteles SET "
        params = {"id_hotel": id_hotel}
        updates = []
        if hotel.nombre:
            updates.append("nombre = :nombre")
            params["nombre"] = hotel.nombre
        if hotel.ubicacion:
            updates.append("ubicacion = :ubicacion")
            params["ubicacion"] = hotel.ubicacion
        if hotel.direccion:
            updates.append("direccion = :direccion")
            params["direccion"] = hotel.direccion
        if hotel.telefono:
            updates.append("telefono = :telefono")
            params["telefono"] = hotel.telefono
        sql += ", ".join(updates) + " WHERE id_hotel = :id_hotel"
        
        # Envuelve la consulta SQL en text()
        sql = text(sql)
        
        db.execute(sql, params)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al actualizar hotel: {e}")
        raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al actualizar hotel")
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al actualizar hotel: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar hotel")
    
def delete_hotel(db: Session, id_hotel: int):
    try:
        sql = text("DELETE FROM hoteles WHERE id_hotel = :id_hotel")
        db.execute(sql, {"id_hotel": id_hotel})
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al eliminar hotel: {e}")
        raise HTTPException(status_code=400, detail="Error. Integridad de datos al eliminar hotel")
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al eliminar hotel: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar hotel")
     
