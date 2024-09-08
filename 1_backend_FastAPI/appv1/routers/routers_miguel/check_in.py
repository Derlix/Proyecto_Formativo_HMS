from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from appv1.schemas.miguel_schemas.check_in import CheckInCreate, CheckInEdit, CheckInResponse
from db.database import get_db
from appv1.crud.crud_miguel.check_in import create_checkin_sql, delete_check_in, get_all_check_in, get_check_in_by_id, update_check_in

router = APIRouter()


@router.post("/create_checkin")
async def insert_checkin(
    check_in: CheckInCreate,
    db: Session = Depends(get_db)
):
    try:
        respuesta = create_checkin_sql(db, check_in)
        if respuesta:
            return {"mensaje": "Check in registrado con éxito"}
    except HTTPException as e:
        raise e
    
    
@router.get("/get_checkin", response_model=List[CheckInResponse])
async def get_checkin(
    db: Session = Depends(get_db)
    
    

):
    respuesta = get_all_check_in(db)
    if len(respuesta) == 0:
        raise HTTPException(status_code=404, detail="No hay checkin")
    return respuesta


@router.get("/checkin/{id_check_in}", response_model=CheckInResponse)
def get_check_in_endpoint(id_check_in: int, db: Session = Depends(get_db)):
    return get_check_in_by_id(db, id_check_in)


@router.put("/checkin/{id_check_in}")
def update_check_in_endpoint(id_check_in: int, check_in_update: CheckInEdit, db: Session = Depends(get_db)):
    return update_check_in(db, id_check_in, check_in_update)


@router.delete("/checkin/{id_check_in}")
def delete_check_in_endpoint(id_check_in: int, db: Session = Depends(get_db)):
    return delete_check_in(db, id_check_in)


