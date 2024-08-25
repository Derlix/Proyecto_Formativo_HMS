
import enum
from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime

from sqlalchemy import DATE, FLOAT, INTEGER


class Factura_productoBase(BaseModel):
    id_facturacion: Annotated[int, INTEGER]
    id_producto: Annotated[int,INTEGER]
    cantidad:   Annotated[int,INTEGER]
    fecha: Annotated[datetime, DATE]
    precio_unitario:   Annotated[float, FLOAT(max_length=(10,2))]
  

   
class  Factura_productoUpdate(Factura_productoBase):
    cantidad: Optional[int] = None
    fecha: Optional[datetime] = None
    precio_unitario: Optional[float] = None

    
class  Factura_productoResponse(Factura_productoBase):
    id_facturacion: int
    id_producto: int
    cantidad: int
    fecha: datetime
    precio_unitario: float
    

    
class PaginatedFacturacionResponse(BaseModel):
    facturas_producto: List[Factura_productoResponse]
    total_pages: int
    current_page: int
    page_size: int
    