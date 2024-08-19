from fastapi import HTTPException
from sqlalchemy.orm import Session 
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import text


#Leer reservas 

def leer_all_reservas(db:Session):
    try:
        sql_query = text (
            "SELECT * FROM RESERVAS"
        )
        result = db.execute(sql_query).fetchall()
        return result
    except IntegrityError as e:
        print(f"Error al buscar reservas: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar reservas")