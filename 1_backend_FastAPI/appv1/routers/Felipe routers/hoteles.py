from typing import List
from fastapi import APIRouter, Depends, HTTPException
from appv1.crud.hoteles import create_hotel_sql, delete_hotel, get_all_hoteles, get_hotel_by_id, update_hotel, get_all_hotels_paginated
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.hoteles import HotelesCreate, HotelesResponse, HotelesUpdate, PaginatedHotelResponse
from db.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
router = APIRouter()


@router.post("/hoteles/create/")
async def insert_hotel(hotel: HotelesCreate, db: Session = Depends(get_db)):
    respuesta = create_hotel_sql(db, hotel)
    if respuesta:
      return {"mensaje":"hotel creado con exito"}

@router.get("/hoteles/get_all/", response_model=List[HotelesResponse])
async def read_all_hotels(db:Session = Depends(get_db) ):
   hoteles = get_all_hoteles(db)
   if len(hoteles) == 0:
       raise HTTPException(status_code=500, detail="No hay hoteles")
   return hoteles

@router.put("/hoteles/update/", response_model=dict)
def update_hotel_by_id(hotel_id: int, hotel: HotelesUpdate, db: Session = Depends(get_db)):
    hotelito = get_hotel_by_id(db, hotel_id)
    if hotelito is None:
         raise HTTPException(status_code=500, detail="No hay hotel encontrado")
    db_user = update_hotel(db, hotel_id, hotel)
    if db_user:
     return {"mensaje": "hotel actualizado con éxito" }
    
@router.delete("/hoteles/delete/{id_hotel}", response_model=dict)
def delete_hotel_by_id(id_hotel: int, db: Session = Depends(get_db)):
     usero = get_hotel_by_id(db, id_hotel)
     if usero is None:
         raise HTTPException(status_code=500, detail="No hay hotel encontrado")

     result = delete_hotel(db, id_hotel)
     if result:
        return {"mensaje": "hotel eliminado con éxito"}
     
@router.get("/hoteles/get_hotel_by_id/", response_model=HotelesResponse)
async def read_hotel_by_id(id_hotel:int, db:Session = Depends(get_db) ):
   hotel = get_hotel_by_id(db, id_hotel)
   if hotel is None:
       raise HTTPException(status_code=500, detail="Usuario no encontrado")
   
   return hotel

@router.get("/hoteles-by-page/", response_model=PaginatedHotelResponse)
def get_all_hoteles_by_page(
   page: int = 1,
   page_size: int = 10,
   db: Session = Depends(get_db),                          
   ):

   
   hoteles, total_pages = get_all_hotels_paginated(db, page, page_size)

   return {
        "hoteles": hoteles,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
   }
