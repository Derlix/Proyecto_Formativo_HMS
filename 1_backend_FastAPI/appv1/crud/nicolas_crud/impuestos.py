from http.client import HTTPException
from appv1.schemas.nicolas_schemas.Impuesto import ImpuestoCreate, ImpuestoUpdate
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from fastapi import  HTTPException

def get_tax_by_id(db: Session, id_impuesto: str):
    sql = text("SELECT * FROM impuestos WHERE id_impuesto = :id_impuesto")
    result = db.execute(sql, {"id_impuesto": id_impuesto}).fetchone()
    return result

def create_tax(db: Session, tax:ImpuestoCreate):
    try:
        sql_query = text(
        "INSERT INTO impuestos(descripcion, tasa)"
        "VALUES (:descripcion, :tasa)"
        
        )
        params = {
            "descripcion": tax.descripcion,
            "tasa": tax.tasa
        }
        db.execute(sql_query, params)
        db.commit()
        return True 
    
    except IntegrityError as e:
        db.rollback()
        print(f"Error al crear impuesto: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El id del impuesto ya existe")
            else:
                raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear impuesto")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear impuesto: {e}")
        raise HTTPException(status_code=500, detail="Error al crear el impuesto")

def get_all_tax(db: Session):
    try:
        sql = text("SELECT * FROM impuestos")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar impuestos: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar impuestos")
    
def update_tax(db: Session, id_impuesto: str, impuesto: ImpuestoUpdate):
    try:
        sql = "UPDATE impuestos SET "
        params = {"id_impuesto": id_impuesto}
        updates = []
        if impuesto.descripcion:
            updates.append("descripcion = :descripcion")
            params["descripcion"] = impuesto.descripcion
        if impuesto.tasa:
            updates.append("tasa = :tasa")
            params["tasa"] = impuesto.tasa

        for ind, valor in enumerate(updates):
                    if len(updates) - 1 == ind:
                        sql += valor
                    else:
                        sql += valor + ", "

        sql += " WHERE id_impuesto = :id_impuesto"
        
        # Envuelve la consulta SQL en text()
        sql = text(sql)

        db.execute(sql, params)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al actualizar impuesto: {e}")
        if not id_impuesto:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al actualizar impuesto")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al actualizar impuesto: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar impuesto")
   

def delete_tax(db: Session, id_impuesto: int):
    try:
        sql = text("DELETE FROM impuestos WHERE id_impuesto = :id_impuesto")
        db.execute(sql, {"id_impuesto": id_impuesto})
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al eliminar impuesto: {e}")
        raise HTTPException(status_code=400, detail="Error. Integridad de datos al eliminar impuesto")
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al eliminar impuesto: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar impuesto")