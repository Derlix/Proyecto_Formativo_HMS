from typing import List
from appv1.crud.nicolas_crud.impuestos import create_tax
from appv1.schemas.nicolas_schemas.Impuesto import ImpuestoResponse,ImpuestoCreate
from fastapi import APIRouter,Depends,HTTPException # type: ignore
from db.database import get_db
from sqlalchemy.orm import Session # type: ignore

router = APIRouter()

@router.post("/create")
async def insert_category(category: ImpuestoCreate, db: Session = Depends(get_db)):
    respuesta = create_tax(db, category)
    if respuesta:
        return {"mensaje":"impuesto registrado con exito"}
    else:
        return {"mensaje":"La impuesto no se ha podido registrar con exito"}



# @router.post("/get_room_categorie_name/",response_model = ImpuestoResponse)
# async def read_category_by_name(p_category_name: str, db: Session = Depends(get_db)):
#     room_categorie_name = get_room_categorie_name(db, p_category_name)
#     if room_categorie_name is None:
#         raise HTTPException(status_code=404, detail="impuesto no encontrada")
#     return room_categorie_name
