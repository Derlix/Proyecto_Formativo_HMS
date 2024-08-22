from typing import List
from fastapi import APIRouter, Depends,  HTTPException
from appv1.crud.crud_alejo.huespedes import create_huesped_sql, delete_huesped, get_all_huespedes, get_all_huespedes_paginated, get_huesped_by_email, get_huesped_by_id, update_huesped
from appv1.schemas.schemas_alejo.huespedes import HuespedCreate, HuespedDelete, HuespedResponse, HuespedUpdate, PaginatedHuespedResponse
from sqlalchemy.orm import Session
from db.database import get_db

router = APIRouter()


@router.post("/create_huesped")
async def insert_huesped(
   huesped: HuespedCreate, 
   db: Session = Depends(get_db)
):
   
   respuesta = create_huesped_sql(db, huesped)
   if respuesta:
      return {"mensaje":"huesped registrado con exito"}
   

   

   
@router.get("/get-huesped-by-email/", response_model=HuespedResponse)
async def read_huesped_by_email(
   email: str,
   db: Session = Depends(get_db)             
):

   huesped = get_huesped_by_email(db, email)
   if huesped is None:
      raise HTTPException(status_code=404, detail="huesped no encontrado")
   
   return huesped 




@router.get("/get-all-huespedes/", response_model=List[HuespedResponse])
async def read_all_huespedes(
   db: Session = Depends(get_db)       
):
   
   
   huespedes = get_all_huespedes(db)
   if len(huespedes)==0:
      raise HTTPException(status_code=404, detail="No hay huespedes ")
   
   return huespedes 




@router.put("/update-huesped/", response_model=dict)
def update_huesped_by_id(
   id_huesped: int,
   huesped: HuespedUpdate, 
   db: Session = Depends(get_db)            
   ):
   
   verify_user = get_huesped_by_id(db, id_huesped)
   if verify_user is None: 
      raise HTTPException(status_code=404, detail="Huesped no encontrado ")
 
   db_huesped = update_huesped(db, id_huesped, huesped)
   if db_huesped:
        return {"mensaje": "huesped actualizado con éxito"}
   


@router.get("/huespedes-by-page/", response_model=PaginatedHuespedResponse)
def get_all_huespedes_by_page(
   page: int = 1,
   page_size: int = 10,
   db: Session = Depends(get_db),                          
   ):

   
   huespedes, total_pages = get_all_huespedes_paginated(db, page, page_size)

   return {
        "huespedes": huespedes,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
   }



@router.put("/delete-huesped/{id_huesped}", response_model=dict)
def delete_huesped_by_id(
   id_huesped: int,
   huesped: HuespedDelete,
   db: Session = Depends(get_db)                  
   ):
    
   verify_user = get_huesped_by_id(db, id_huesped)
   if verify_user is None: 
      raise HTTPException(status_code=404, detail="Huesped no encontrado ")
      
   result = delete_huesped(db, id_huesped, huesped)
   if result:
        return {"mensaje": "Huesped eliminado con éxito"}


