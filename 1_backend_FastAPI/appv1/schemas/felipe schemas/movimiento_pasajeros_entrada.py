import datetime
from typing import Annotated
from pydantic import BaseModel

class EntradaBase(BaseModel):
      id_entrada_registro_hotelero: int

class EntradaCreate(BaseModel):
       id_entrada_reporte: int
       id_entrada_registro_hotelero: int  

class EntradaResponse(BaseModel):
       id_entrada_reporte: int
       id_entrada_registro_hotelero: int  
       created_at: datetime
       updated_at: datetime

class EntradaUpdate(BaseModel):
       id_entrada_reporte: int
       id_entrada_registro_hotelero: int 