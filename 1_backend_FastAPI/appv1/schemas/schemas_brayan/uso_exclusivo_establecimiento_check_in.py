import enum
from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime

from sqlalchemy import DATE, FLOAT, INTEGER, ENUM

class EquipajeEnum(enum.Enum):
    con = "con"
    sin = "sin"


class FormaPagoEnum(enum.Enum):
    efectivo = "efectivo"
    tarjeta_credito = "tarjeta_credito"
    transferencia =  "transferencia"


class LlegadaEnum(enum.Enum):
    con_reserva = "con_reserva"
    sin_reserva = "sin_reserva"
   

class Uso_exclusivo_establecimiento_check_in_Create(BaseModel):
    id_uso_exlusivo_establecimiento_check_in = Annotated[int, INTEGER]
    id_hotel =  Annotated[int, INTEGER]
    id_ocupantes =  Annotated[int, INTEGER]
    id_habitacion =  Annotated[int, INTEGER]
    tarifa =   Annotated[float, FLOAT(max_length=(10,2))]
    impuesto =  Annotated[float, FLOAT(max_length=(10,2))]
    fecha_llegada = Annotated[datetime, DATE]
    fecha_salida =  Annotated[datetime, DATE]
    id_estadia =  Annotated[int, INTEGER]
    equipaje =   EquipajeEnum
    forma_pago =  FormaPagoEnum
    id_factura_cuenta_huesped_check_out = Annotated[int, INTEGER]
    llegada =  LlegadaEnum
    empresa = Annotated[str, StringConstraints]


class Uso_exclusivo_establecimiento_check_in_Response(Uso_exclusivo_establecimiento_check_in_Create):
    id_uso_exlusivo_establecimiento_check_in = int
    id_hotel =   int
    id_ocupantes =  int
    id_habitacion =   int
    tarifa =   float
    impuesto =  float
    fecha_llegada = datetime
    fecha_salida =  datetime
    id_estadia =  int
    equipaje =   EquipajeEnum
    forma_pago =  FormaPagoEnum
    id_factura_cuenta_huesped_check_out = int
    llegada =  LlegadaEnum
    empresa = str
