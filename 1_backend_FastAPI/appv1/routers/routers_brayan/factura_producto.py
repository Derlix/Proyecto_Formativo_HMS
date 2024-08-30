from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from appv1.crud.crud_brayan.facturacion import update_factura
from appv1.schemas.schemas_brayan.factura_producto import Factura_productoBase, Factura_productoResponse, Factura_productoUpdate,Factura_productoConDetalles, FacturaConProductosResponse

from db.database import get_db
from appv1.crud.crud_brayan.factura_producto import create_factura_producto_sql, delete_producto_factura, get_productos_de_factura_by_id, update_productos_factura, get_factura_productos_by_id, get_all_factura_productos

router = APIRouter()


@router.post("/create_factura_producto", response_model=dict)
def insert_factura_producto(
    factura_producto: Factura_productoBase,
    db: Session = Depends(get_db)
):
    try:
        respuesta = create_factura_producto_sql(db, factura_producto)
        if respuesta:
            return {"mensaje": "productos en la factura registrada con éxito"}
    except HTTPException as e:
        raise e



@router.get("/get_productos_factura_by_id/", response_model=FacturaConProductosResponse)
def read_factura_productos_by_id(id_facturacion: int, db: Session = Depends(get_db)):
    factura_productos = get_productos_de_factura_by_id(db, id_facturacion)
    return factura_productos



@router.put("/update_productos_factura/{id_factura_producto}", response_model=dict)
def update_factura_by_id(
    id_factura_producto: int,
    factura_producto: Factura_productoUpdate,
    db: Session = Depends(get_db)
):
    try:
        # Verifica si el producto de la factura existe
        verufy_factura_producto = get_factura_productos_by_id(db, id_factura_producto)
        if verufy_factura_producto is None:
            raise HTTPException(status_code=404, detail="Producto de factura no encontrado")

        # Actualiza el producto de la factura
        respuesta = update_productos_factura(db, id_factura_producto, factura_producto)
        if respuesta:
            return {"mensaje": "Producto de factura actualizado con éxito"}

    except HTTPException as e:
        raise e
    except Exception as e:
        # Manejo de errores genéricos
        print(f"Error al actualizar producto de factura: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor al actualizar el producto de factura.")
    


    
@router.delete("/delete_producto_factura/{id_factura_producto}", response_model=dict)
def delete_producto_factura_by_id(id_factura_producto: int, db: Session = Depends(get_db)):
    try:
        factura = get_factura_productos_by_id(db, id_factura_producto)
        if factura is None:
            raise HTTPException(status_code=404, detail="id Factura producto no encontrada")

        result = delete_producto_factura(db, id_factura_producto)
        if result:
            return {"mensaje": "producto de la factura eliminado con éxito"}
    except HTTPException as e:
        raise e




@router.get("/get_all_facturas_y_productos", response_model=List[FacturaConProductosResponse])
def read_all_factura_productos(db: Session = Depends(get_db)):
    try:
        facturas_productos = get_all_factura_productos(db)
        return facturas_productos
    except HTTPException as e:
        raise e
    except Exception as e:
        # Manejo de errores genéricos
        print(f"Error al obtener todas las facturas y productos: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor al obtener todas las facturas y productos.")        