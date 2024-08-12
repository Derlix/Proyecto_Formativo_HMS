import datetime
from typing import Annotated
from pydantic import BaseModel

class ReporteEntradaSalidaBase(BaseModel):
      id_entrada_reporte: int
      id_salida_reporte: int
      

class ReporteEntradaSalidaCreate(BaseModel):
        id_reporte_entrada_salida: int
        id_entrada_reporte: int
        id_salida_reporte: int 

class ReporteEntradaSalidaResponse(BaseModel):
        id_reporte_entrada_salida: int
        id_entrada_reporte: int
        id_salida_reporte: int
        

class ReporteEntradaSalidaUpdate(BaseModel):
       id_reporte_entrada_salida: int
       id_entrada_reporte: int
       id_salida_reporte: int