from typing import List
from appv1.crud.nicolas_crud.impuestos import create_tax, get_all_tax
from appv1.schemas.nicolas_schemas.Impuesto import ImpuestoResponse,ImpuestoCreate
from fastapi import APIRouter,Depends,HTTPException
from db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/create")
async def insert_tax(category: ImpuestoCreate, db: Session = Depends(get_db)):
    respuesta = create_tax(db, category)
    if respuesta:
        return {"mensaje":"impuesto registrado con exito"}
    else:
        return {"mensaje":"La impuesto no se ha podido registrar con exito"}



@router.get("/get-all/", response_model=List[ImpuestoResponse])
async def read_all_tax(db: Session= Depends(get_db)):
    tax = get_all_tax(db)
    if len(tax) == 0:
        raise HTTPException(status_code=404, detail="No hay impuestos")
    return tax