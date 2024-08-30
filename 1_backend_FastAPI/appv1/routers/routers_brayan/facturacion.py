from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from appv1.schemas.schemas_brayan.facturacion import FacturacionCreate, FacturacionUpdate, FacturacionResponse
from db.database import get_db
from appv1.crud.crud_brayan.facturacion import create_facturacion_sql, get_factura_by_id, get_all_facturas, update_factura, delete_factura

router = APIRouter()


@router.post("/create_factura", response_model=dict)
def insert_factura(
    facturacion: FacturacionCreate,
    db: Session = Depends(get_db)
):
    try:
        respuesta = create_facturacion_sql(db, facturacion)
        if respuesta:
            return {"mensaje": "Factura registrada con éxito"}
    except HTTPException as e:
        raise e


@router.get("/get_factura_by_id/",response_model=FacturacionResponse)
def read_factura_by_id(id_facturacion: int, db: Session = Depends(get_db)):
    factura = get_factura_by_id(db, id_facturacion)
    if factura is None:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    print(factura)
    return factura




@router.get("/get_all_facturas", response_model=List[FacturacionResponse])
def read_all_facturas(db: Session = Depends(get_db)):
    facturas = get_all_facturas(db)
    if not facturas:
        raise HTTPException(status_code=404, detail="No hay facturas")
    return facturas




@router.put("/update_factura/{id_facturacion}", response_model=dict)
def update_factura_by_id(
    id_facturacion: int,
    factura: FacturacionUpdate,
    db: Session = Depends(get_db)
):
    try:
        # Verifica si la factura existe
        verufy_factura = get_factura_by_id(db, id_facturacion)
        if verufy_factura is None:
            raise HTTPException(status_code=404, detail="Factura no encontrada")

        respuesta = update_factura(db, id_facturacion, factura)
        if respuesta:
            return {"mensaje": "Factura actualizada con éxito"}
    except HTTPException as e:
        raise e



@router.delete("/delete_factura/{id_facturacion}", response_model=dict)
def delete_factura_by_id(id_facturacion: int, db: Session = Depends(get_db)):
    try:
        factura = get_factura_by_id(db, id_facturacion)
        if factura is None:
            raise HTTPException(status_code=404, detail="Factura no encontrada")

        result = delete_factura(db, id_facturacion)
        if result:
            return {"mensaje": "Factura eliminada con éxito"}
    except HTTPException as e:
        raise e
