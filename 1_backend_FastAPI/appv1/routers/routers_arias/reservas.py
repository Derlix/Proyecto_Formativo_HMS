from appv1.crud.crud_arias.reservas import leer_all_reservas
from appv1.schemas.arias_schemas.reservas import ReservaResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from db.database import get_db

router = APIRouter()

@router.get("/get_all", response_model=List[ReservaResponse])
async def read_all_reservas(
    db:Session = Depends(get_db)   
):
    reservas = leer_all_reservas(db)

    return reservas

@app. on_event("startup")
def on_startup():
    test_db_connection()