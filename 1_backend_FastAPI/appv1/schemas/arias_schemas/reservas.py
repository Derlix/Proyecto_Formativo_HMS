from pydantic import BaseModel, condecimal, constr
from typing import Annotated, Optional
from datetime import datetime

class ReservaBase(BaseModel):
    fecha_reserva: datetime
    empresa: Annotated[Optional[str], constr(max_length=30)] = None
    valor_deposito: condecimal(max_digits=10, decimal_places=2)
    forma_pago: Annotated[str, constr(regex='^(EFECTIVO|DEBITO|CREDITO|TRANSFERENCIA)$')]

class ReservaCreate(ReservaBase):
    pass

class ReservaResponse(ReservaBase):
    id_reserva: int

class ReservaUpdate(BaseModel):
    id_huesped: Optional[int] = None
    fecha_reserva: Optional[datetime] = None
    empresa: Optional[Annotated[str, constr(max_length=30)]] = None
    valor_deposito: Optional[condecimal(max_digits=10, decimal_places=2)] = None
    forma_pago: Optional[Annotated[str, constr(regex='^(EFECTIVO|DEBITO|CREDITO|TRANSFERENCIA)$')]] = None
