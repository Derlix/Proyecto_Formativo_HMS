from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.arce_schemas.caracteristicas import CaracteristicaCreate
from core.security import get_hashed_password
from models.arce_models import caracteristicas

def crear_caracteristica(db: Session, caracteristica: CaracteristicaCreate):
    try:
        sql_query = text(
            "INSERT INTO caracteristicas (nombre_caracteristicas, adicional) "
            "VALUES (:nombre_caracteristicas, :adicional)"
        )
        params = {
            "nombre_caracteristicas": caracteristica.nombre_caracteristicas,
            "adicional": caracteristica.adicional,
          
        }
        db.execute(sql_query, params)
        db.commit()
        return True
    
    except IntegrityError as e:
        db.rollback() 
        print(f"Error al crear caracteristica: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID generado automaticamente ya existe, vuelva a intentarlo")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear caracteristica")
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al crear caracteristica: {e}")
        raise HTTPException(status_code=500, detail="Error al crear caracteristica")
    

def obtener_caracteristicas(db: Session):
    try:
        sql = text("SELECT * FROM caracteristicas")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar caracteristicas: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar caracteristicas")

    
def eliminar_caracteristica(db: Session, id_caracteristica: int):
    try:
        sql_query = text("DELETE FROM caracteristicas WHERE id_caracteristica = :id_caracteristica")
        params = {"id_caracteristica": id_caracteristica}
        result = db.execute(sql_query, params)
        db.commit()
        
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Característica no encontrada")
        
        return True
    
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al eliminar característica: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar característica")