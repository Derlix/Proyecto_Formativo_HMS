from typing import List
from appv1.crud.nicolas_crud.impuestos import create_tax, delete_tax, get_all_tax, get_tax_by_id, update_tax
from appv1.schemas.nicolas_schemas.Impuesto import ImpuestoResponse,ImpuestoCreate, ImpuestoUpdate
from fastapi import APIRouter,Depends,HTTPException
from db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/create")
async def insert_tax(tax: ImpuestoCreate, db: Session = Depends(get_db)):
    respuesta = create_tax(db, tax)
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

#Endpoint para actualizar un usuario
@router.put("/update/", response_model=dict)
def update_tax_by_id( tax_id: str, tax: ImpuestoUpdate, db: Session = Depends(get_db)):  
        
    verify_tax = get_tax_by_id(db, tax_id)
    if verify_tax is None:
        raise HTTPException(status_code=404, detail="Impuesto no encontrado")
    
    db_tax = update_tax(db, tax_id, tax)
    if db_tax:
        return {"mensaje": "registro actualizado con éxito"}
    
@router.delete("/delete/{id_impuesto}", response_model=dict)
def delete_tax_by_id(id_impuesto: str, db: Session = Depends(get_db)):  

    tax = get_tax_by_id(db, id_impuesto)
    if tax is None:
        raise HTTPException(status_code=404, detail="Impuesto no encontrado")
    
    result = delete_tax(db, id_impuesto)
    if result:
        return {"mensaje": "Impuesto eliminado con éxito"}
    