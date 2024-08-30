import datetime
from pydantic import BaseModel
from typing import Optional
import enum

# Enumeraciones
class EquipajeEnum(str, enum.Enum):
    SI = "SI"
    NO = "NO"

class LlegadaEnum(str, enum.Enum):
    CON_RESERVA = "CON RESERVA"
    SIN_RESERVA = "SIN RESERVA"

class MedioLlegadaEnum(str, enum.Enum):
    AEREO = "AEREO"
    TERRESTRE = "TERRESTRE"

# Modelos Pydantic
class CheckInBase(BaseModel):
    id_reserva: int 
    medio_llegada: MedioLlegadaEnum
    llegada_situacion: LlegadaEnum
    equipaje: EquipajeEnum
    

class ReservaDetail(BaseModel):
    id_reserva: int  
    fecha_reserva: datetime.date
    empresa: str
    valor_deposito: float
    forma_pago: str

    
class HuespedDetail(BaseModel):
    nombre_completo: str
    numero_documento: str


class CheckInCreate(CheckInBase):
    pass

class CheckInResponse(BaseModel):
    id_check_in: int
    reserva: ReservaDetail
    huesped: HuespedDetail
    medio_llegada: MedioLlegadaEnum
    llegada_situacion: LlegadaEnum
    equipaje: EquipajeEnum

class CheckInEdit(BaseModel):
    id_reserva: Optional[int] = None
    medio_llegada: Optional[MedioLlegadaEnum] = None
    llegada_situacion: Optional[LlegadaEnum] = None
    equipaje: Optional[EquipajeEnum] = None
    
    
