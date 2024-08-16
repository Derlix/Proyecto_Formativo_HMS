import enum
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

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
