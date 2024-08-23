
import enum
from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime

from sqlalchemy import DATE, FLOAT, INTEGER




class MetodoPagoType(enum.Enum):
    efectivo = "EFECTIVO"
    tarjeta = "TARJETA"
    transferencia = "TRANSFERENCIA"



class EstadoType(enum.Enum):
    pendiente = "PENDIENTE"
    pagada = "PAGADA"
    cancelada = "CANCELADA"   
    


class FacturacionBase(BaseModel):
    id_facturacion: Annotated[int, INTEGER]
    id_check_in: Annotated[int, INTEGER] 
    subtotal:   Annotated[float, FLOAT(max_length=(10,2))]
    impuestos:   Annotated[float, FLOAT(max_length=(10,2))]
    total:   Annotated[float, FLOAT(max_length=(10,2))]
    total_precio_productos:   Annotated[float, FLOAT(max_length=(10,2))]
    metodo_pago: MetodoPagoType
    estado: EstadoType
    fecha_salida: Annotated[datetime, DATE]

    
   
class  FacturacionUpdate(FacturacionBase):
    subtotal:  Optional[  Annotated[float, FLOAT(max_length=(10,2))]] = None
    impuestos:  Optional[  Annotated[float, FLOAT(max_length=(10,2))]] = None
    total:   Optional[ Annotated[float, FLOAT(max_length=(10,2))]] = None
    total_precio_productos:   Optional[ Annotated[float, FLOAT(max_length=(10,2))]] = None
    metodo_pago:  Optional[ MetodoPagoType] = None
    estado:  Optional[ EstadoType] = None
    fecha_salida:  Optional[ Annotated[datetime, DATE]] = None


    
class  FacturacionResponse(FacturacionBase):
    id_facturacion: int
    

    
class PaginatedFacturacionResponse(BaseModel):
    facturaciones: List[FacturacionResponse]
    total_pages: int
    current_page: int
    page_size: int   
    