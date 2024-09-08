
import enum
from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime

from sqlalchemy import DATE, FLOAT, INTEGER


class MetodoPagoType(str, enum.Enum):
    efectivo = 'EFECTIVO'
    tarjeta = 'TARJETA'
    transferencia = 'TRANSFERENCIA'

class EstadoType(str, enum.Enum):
    pendiente = 'PENDIENTE'
    pagada = 'PAGADA'
    cancelada = 'CANCELADA'

class FacturaDetail(BaseModel):
    id_facturacion: int
    check_in: int
    subtotal: float
    impuestos: float
    total: float
    total_precio_productos: float
    metodo_pago: MetodoPagoType
    estado: EstadoType
    fecha_salida: datetime



class Factura_productosDetail(BaseModel):
    id_factura_producto: int
    id_producto: int
    cantidad: int
    precio_unitario: float

class ProductosDetail(BaseModel):
    nombre_producto: str
    descripcion: str
    precio_actual: float


class Factura_productoBase(BaseModel):
    id_facturacion: int
    id_producto: int
    cantidad: int
    fecha: datetime
    precio_unitario: float

   
class  Factura_productoUpdate(BaseModel):
    cantidad: Optional[int] = None
    fecha: Optional[datetime] = None
    precio_unitario: Optional[float] = None

    
class  Factura_productoResponse(Factura_productoBase):
    id_factura_producto: int
    id_facturacion: int
    id_producto: int
    cantidad: int
    fecha: datetime
    precio_unitario: float
   

  

class Factura_productoConDetalles(BaseModel):
    factura_producto: Factura_productosDetail
    productos: ProductosDetail
  

class FacturaConProductosResponse(BaseModel):
    factura: FacturaDetail
    productos: List[Factura_productoConDetalles]


    
class PaginatedFactura_productosResponse(BaseModel):
    facturas_producto: List[Factura_productoResponse]
    total_pages: int
    current_page: int
    page_size: int
    