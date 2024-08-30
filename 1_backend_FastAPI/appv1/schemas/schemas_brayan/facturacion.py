from typing import Dict, List, Optional
from pydantic import BaseModel
from datetime import datetime
import enum

class MetodoPagoType(enum.Enum):
    efectivo = "EFECTIVO"
    tarjeta = "TARJETA"
    transferencia = "TRANSFERENCIA"

class EstadoType(enum.Enum):
    pendiente = "PENDIENTE"
    pagada = "PAGADA"
    cancelada = "CANCELADA"


class ReservaDetail(BaseModel):
    fecha_reserva: datetime
    empresa: str
    valor_deposito: float
    forma_pago: str


class HuespedDetail(BaseModel):
    nombre_completo: str
    numero_documento: str


class CheckInDetail(BaseModel):
    id_reserva: int
    medio_llegada: str
    llegada_situacion: str
    equipaje: str


class ProductosDetail(BaseModel):
  nombre_producto: str
  descripcion: str
  precio_actual: float


class FacturacionBase(BaseModel):

    id_check_in: int
    subtotal: float
    impuestos: float
    total: float
    total_precio_productos: float
    metodo_pago: MetodoPagoType
    estado: EstadoType
    fecha_salida: datetime

class FacturacionCreate(FacturacionBase):
    pass

class FacturacionUpdate(BaseModel):
    subtotal: Optional[float] = None
    impuestos: Optional[float] = None
    total: Optional[float] = None
    total_precio_productos: Optional[float] = None
    metodo_pago: Optional[MetodoPagoType] = None
    estado: Optional[EstadoType] = None
    fecha_salida: Optional[datetime] = None



class FacturacionResponse(BaseModel):
    id_facturacion: int
    check_in: CheckInDetail
    reserva: ReservaDetail
    huesped: HuespedDetail
    subtotal: float
    impuestos: float
    total: float
    total_precio_productos: float
    metodo_pago: MetodoPagoType
    estado: EstadoType
    fecha_salida: datetime




class PaginatedFacturacionResponse(BaseModel):
    facturaciones: List[FacturacionResponse]
    total_pages: int
    current_page: int
    page_size: int

