from pydantic import BaseModel, condecimal, constr
from typing import Optional
from datetime import datetime
from enum import Enum

# Usa el mismo Enum que en tu modelo SQLAlchemy
class FormaPagoEnum(str, Enum):
    EFECTIVO = "EFECTIVO"
    DEBITO = "DEBITO"
    CREDITO = "CREDITO"
    TRANSFERENCIA = "TRANSFERENCIA"

class ReservaBase(BaseModel):
    fecha_reserva: datetime
    empresa: Optional[constr(max_length=30)] = None
    valor_deposito: condecimal(max_digits=10, decimal_places=2)
    forma_pago: FormaPagoEnum  # Usamos el Enum aquí

class ReservaCreate(ReservaBase):
    pass

class ReservaResponse(ReservaBase):
    id_reserva: int

class ReservaUpdate(BaseModel):
    id_huesped: Optional[int] = None
    fecha_reserva: Optional[datetime] = None
    empresa: Optional[constr(max_length=30)] = None
    valor_deposito: Optional[condecimal(max_digits=10, decimal_places=2)] = None
    forma_pago: Optional[FormaPagoEnum] = None  # Usamos el Enum aquí
