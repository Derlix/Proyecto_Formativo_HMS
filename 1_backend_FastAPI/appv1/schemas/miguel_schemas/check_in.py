import enum
from typing import Optional
from pydantic import BaseModel

# Enumeraciones
class EquipajeEnum(enum.Enum):
    si = "SI"
    no = "NO"

class LlegadaEnum(enum.Enum):
    con_reserva = "CON RESERVA"
    sin_reserva = "SIN RESERVA"

class MedioLlegadaEnum(enum.Enum):
    aereo = "AEREO"
    terrestre = "TERRESTRE"

# Modelos Pydantic
class CheckIn(BaseModel):
    id_check_in: int
    id_reserva: int
    medio_llegada: MedioLlegadaEnum
    llegada_situacion: LlegadaEnum
    equipaje: EquipajeEnum

class CheckInCreate(BaseModel):
    id_reserva: int
    medio_llegada: MedioLlegadaEnum
    llegada_situacion: LlegadaEnum
    equipaje: EquipajeEnum

class CheckInResponse(CheckIn):
    pass

class CheckInEdit(BaseModel):
    id_reserva: Optional[int] = None
    medio_llegada: Optional[MedioLlegadaEnum] = None
    llegada_situacion: Optional[LlegadaEnum] = None
    equipaje: Optional[EquipajeEnum] = None
