from sqlalchemy import INTEGER
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException
from appv1.schemas.juanca_schemas.habitaciones import HabitacionCreate, HabitacionResponse

from sqlalchemy import text

def create_room(db: Session, room: HabitacionCreate):
    try:
        params = {
            "numero_habitacion": room.numero_habitacion,
            "estado": room.estado.value,
            "piso": int(room.piso),
            "precio_actual": float(room.precio_actual),
            "id_usuario": room.id_usuario,
            "id_categoria_habitacion": room.id_categoria_habitacion,
        }
        print(params)
        
        sql_query = text(
            "INSERT INTO habitaciones (numero_habitacion, estado, piso, precio_actual, id_usuario, id_categoria_habitacion) "
            "VALUES (:numero_habitacion, :estado, :piso, :precio_actual, :id_usuario, :id_categoria_habitacion)"
        )
        db.execute(sql_query, params)
        db.commit()

        # Aquí es donde necesitas envolver la consulta en la función text()
        last_id = db.execute(text("SELECT LAST_INSERT_ID()")).fetchone()[0]
        
        return {"id_habitacion": last_id, **params}

    except IntegrityError as e:
        db.rollback()
        if 'Duplicate entry' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error. La habitación ya existe")
        else:
            raise HTTPException(status_code=400, detail="Error de integridad al crear la habitación")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear la habitación: {str(e)}")



def get_all_rooms(db: Session):
    try:
        sql_query = text("SELECT * FROM habitaciones")
        result = db.execute(sql_query).fetchall()
        print(result)  # Agregar esta línea para ver el resultado en la consola
        return result
    except SQLAlchemyError as e:
        print(str(e))  # Imprimir el error
        raise HTTPException(status_code=500, detail="Error al obtener habitaciones")



def get_room_by_id(db: Session, room_id: int) -> HabitacionResponse:
    try:
        sql_query = text("SELECT * FROM habitaciones WHERE id_habitacion = :room_id")
        result = db.execute(sql_query, {"room_id": room_id}).fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="Habitación no encontrada")

        # Mapeo del resultado a un esquema Pydantic
        habitacion = HabitacionResponse(
            id_habitacion=result.id_habitacion,
            numero_habitacion= result.numero_habitacion,
            estado=result.estado,
            piso=result.piso,
            precio_actual=result.precio_actual,
            id_usuario=result.id_usuario,
            id_categoria_habitacion=result.id_categoria_habitacion
        )

        return habitacion

    except SQLAlchemyError as e:
        print(f"Error al obtener habitación: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener habitación")



# Actualizar una habitación
def update_room(db: Session, room_id: int, room: HabitacionCreate):
    try:
        # Verificar si la habitación existe
        existing_room = db.execute(text("SELECT * FROM habitaciones WHERE id_habitacion = :room_id"), {"room_id": room_id}).fetchone()
        if not existing_room:
            return None
        
        # Actualizar la habitación
        sql_query = text(
            "UPDATE habitaciones SET "
            "numero_habitacion = :numero_habitacion,"
            "estado = :estado, "
            "piso = :piso, "
            "precio_actual = :precio_actual, "
            "id_usuario = :id_usuario, "
            "id_categoria_habitacion = :id_categoria_habitacion "
            "WHERE id_habitacion = :room_id"
        )

        params = {
            "numero_habitacion": room.numero_habitacion,
            "estado": room.estado.value,
            "piso": room.piso,
            "precio_actual": room.precio_actual,
            "id_usuario": room.id_usuario,
            "id_categoria_habitacion": room.id_categoria_habitacion,
            "room_id": room_id
        }
        db.execute(sql_query, params)
        db.commit()

        # Obtener la habitación actualizada
        updated_room = db.execute(text("SELECT * FROM habitaciones WHERE id_habitacion = :room_id"), {"room_id": room_id}).fetchone()

        # Verificar si se obtuvo la habitación actualizada
        if updated_room:
            # Convertir la tupla en diccionario manualmente si es necesario
            updated_room_dict = {
                "id_habitacion": updated_room[0],  # Ajusta el índice según el orden de las columnas en la tupla
                "numero_habitacion": updated_room[1],
                "estado": updated_room[2],
                "piso": updated_room[3],
                "precio_actual": updated_room[4],
                "id_usuario": updated_room[5],
                "id_categoria_habitacion": updated_room[6]
            }
            return updated_room_dict
        else:
            return None

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error de integridad al actualizar la habitación")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al actualizar la habitación")

    
# Eliminar habitacion
def delete_room(db: Session, room_id: int):
    try:
        sql_query = text("DELETE FROM habitaciones WHERE id_habitacion = :room_id")
        result = db.execute(sql_query, {"room_id": room_id})
        db.commit()
        if result.rowcount == 0:
            return False
        return {"message": "Habitación eliminada exitosamente"}

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error de integridad al eliminar la habitación")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al eliminar la habitación")
