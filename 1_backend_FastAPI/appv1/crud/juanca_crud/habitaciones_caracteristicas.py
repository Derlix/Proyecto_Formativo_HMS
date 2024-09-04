from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from fastapi import HTTPException
from appv1.schemas.juanca_schemas.habitacion_caracteristicas import HabitacionCaracteristicaCreate, HabitacionCaracteristicaResponse
from fastapi import APIRouter

router = APIRouter()

# Define tus rutas aquí


# Crear una nueva habitacion_caracteristica
def create_habitacion_caracteristica(db: Session, caracteristica: HabitacionCaracteristicaCreate):
    try:
        params = {
            "id_habitacion": caracteristica.id_habitacion,
            "id_caracteristica": caracteristica.id_caracteristica,
        }

        sql_query = text(
            "INSERT INTO habitacion_caracteristicas (id_habitacion, id_caracteristica) "
            "VALUES (:id_habitacion, :id_caracteristica)"
        )
        db.execute(sql_query, params)
        db.commit()

        return params

    except IntegrityError as e:
        db.rollback()
        if 'Duplicate entry' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error. La característica de habitación ya existe")
        else:
            raise HTTPException(status_code=400, detail="Error de integridad al crear la característica de habitación")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear la característica de habitación: {str(e)}")


# Obtener todas las habitacion_caracteristicas
def get_all_habitacion_caracteristicas(db: Session):
    try:
        sql_query = text("SELECT * FROM habitacion_caracteristicas")
        result = db.execute(sql_query).fetchall()
        return result
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener características de habitaciones")


# Obtener una habitacion_caracteristica por ID
def get_habitacion_caracteristica_by_id(db: Session, id_habitacion: int, id_caracteristica: int) -> HabitacionCaracteristicaResponse:
    try:
        sql_query = text(
            "SELECT * FROM habitacion_caracteristicas WHERE id_habitacion = :id_habitacion AND id_caracteristica = :id_caracteristica"
        )
        result = db.execute(sql_query, {"id_habitacion": id_habitacion, "id_caracteristica": id_caracteristica}).fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="Característica de habitación no encontrada")

        # Mapeo del resultado a un esquema Pydantic
        caracteristica = HabitacionCaracteristicaResponse(
            id_habitacion=result.id_habitacion,
            id_caracteristica=result.id_caracteristica
        )

        return caracteristica

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error al obtener la característica de habitación")

def update_habitacion_caracteristica(
    db: Session,
    old_id_habitacion: int,
    old_id_caracteristica: int,
    caracteristica: HabitacionCaracteristicaCreate
):
    try:
        # Verificar si la característica antigua existe
        existing_caracteristica = db.execute(
            text(
                "SELECT * FROM habitacion_caracteristicas WHERE id_habitacion = :old_id_habitacion AND id_caracteristica = :old_id_caracteristica"
            ),
            {"old_id_habitacion": old_id_habitacion, "old_id_caracteristica": old_id_caracteristica}
        ).fetchone()

        if not existing_caracteristica:
            raise HTTPException(status_code=404, detail="La característica de habitación no encontrada")

        # Eliminar la característica antigua
        db.execute(
            text(
                "DELETE FROM habitacion_caracteristicas WHERE id_habitacion = :old_id_habitacion AND id_caracteristica = :old_id_caracteristica"
            ),
            {"old_id_habitacion": old_id_habitacion, "old_id_caracteristica": old_id_caracteristica}
        )

        # Insertar la nueva característica
        sql_query = text(
            "INSERT INTO habitacion_caracteristicas (id_habitacion, id_caracteristica) "
            "VALUES (:id_habitacion, :id_caracteristica)"
        )
        params = {
            "id_habitacion": caracteristica.id_habitacion,
            "id_caracteristica": caracteristica.id_caracteristica
        }
        db.execute(sql_query, params)
        db.commit()

        return params

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error de integridad al actualizar la característica de habitación")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al actualizar la característica de habitación")



# Eliminar una habitacion_caracteristica
def delete_habitacion_caracteristica(db: Session, id_habitacion: int, id_caracteristica: int):
    try:
        sql_query = text(
            "DELETE FROM habitacion_caracteristicas WHERE id_habitacion = :id_habitacion AND id_caracteristica = :id_caracteristica"
        )
        result = db.execute(sql_query, {"id_habitacion": id_habitacion, "id_caracteristica": id_caracteristica})
        db.commit()

        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Característica de habitación no encontrada")
        
        return {"message": "Característica de habitación eliminada exitosamente"}

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error de integridad al eliminar la característica de habitación")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al eliminar la característica de habitación")
