from typing import List
from appv1.crud.nicolas_crud.productos import create_products, delete_product, get_all_products, get_all_products_paginated, get_product_by_id, update_product
from appv1.schemas.nicolas_schemas.Productos import PaginatedProductResponse, ProductoCreate, ProductoResponse, ProductoUpdate
from fastapi import APIRouter,Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/create")
async def insert_product(producto: ProductoCreate, db: Session = Depends(get_db)):
    respuesta = create_products(db, producto)
    if respuesta:
        return {"mensaje":"producto registrado con exito"}
    else:
        return {"mensaje":"El producto no se ha podido registrar con exito"}

@router.get("/get-all/", response_model=List[ProductoResponse])
async def read_all_tax(db: Session= Depends(get_db)):
    product = get_all_products(db)
    if len(product) == 0:
        raise HTTPException(status_code=404, detail="No hay Productos")
    return product

# Endpoint para actualizar un producto
@router.put("/update/", response_model=dict)
def update_product_by_id(product_id: str, product: ProductoUpdate, db: Session = Depends(get_db)):
    
        
    verify_product = get_product_by_id(db, product_id)
    if verify_product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    db_product = update_product(db, product_id, product)
    if db_product:
        return {"mensaje": "Producto actualizado con éxito"}

@router.delete("/delete/{id_producto}", response_model=dict)
def delete_product_by_id(id_producto: str, db: Session = Depends(get_db)):

    product = get_product_by_id(db, id_producto)
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    result = delete_product(db, id_producto)
    if result:
        return {"mensaje": "Producto eliminado con éxito"}
    
# Productos paginados
@router.get("/products-by-page/", response_model=PaginatedProductResponse)
def get_all_products_by_page( page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    products, total_pages = get_all_products_paginated(db, page, page_size)
    return {
        "productos": products,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
    }
