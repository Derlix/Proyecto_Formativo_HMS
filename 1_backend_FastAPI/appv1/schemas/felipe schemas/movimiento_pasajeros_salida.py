import datetime
from typing import Annotated
from pydantic import BaseModel

class SalidaBase(BaseModel):
      id_cuenta_huesped: int

class SalidaCreate(BaseModel):
       id_salida_reporte: int
       id_cuenta_huesped: int  

class SalidaResponse(BaseModel):
       id_salida_reporte: int
       id_cuenta_huesped: int  
       created_at: datetime
       updated_at: datetime

class SalidaUpdate(BaseModel):
       id_salida_reporte: int
       id_cuenta_huesped: int 