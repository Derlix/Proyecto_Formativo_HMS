import enum
from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime



class tipo_documentoEnum (enum.Enum):
    cedula = 'CC'
    tarjeta_identidad = 'TI'
    pasaporte ='Pasaporte'
    cedual_extranjeria = 'Cedula_extranjera'
    

class HuespedCreate(BaseModel):
   
    nombre_completo: Annotated[str, StringConstraints(max_length=80)]
    tipo_documentoEnum: tipo_documentoEnum
    numero_documento: Annotated[str, StringConstraints(max_length=15)]
    fecha_expedicion: Annotated[str, StringConstraints(max_length=15)]
    email: EmailStr
    telefono: Annotated[str, StringConstraints(max_length=15)]
    ocupacion: Annotated[str, StringConstraints(max_length=50)]
    direccion: Annotated[str, StringConstraints(max_length=50)]
    
class HuespedResponse(HuespedCreate):
    id_huesped: int
    created_at: datetime
    updated_at: datetime


class HuespedUpdate(BaseModel):
    nombre_completo: Optional[Annotated[str, StringConstraints(max_length=80)]] = None
    tipo_documentoEnum: tipo_documentoEnum
    numero_documento: Optional [Annotated[str, StringConstraints(max_length=15)]] = None
    fecha_expedicion: Optional [Annotated[str, StringConstraints(max_length=15)]]= None
    email: Optional [EmailStr] = None
    telefono: Optional [Annotated[str, StringConstraints(max_length=15)]] = None
    ocupacion: Optional [Annotated[str, StringConstraints(max_length=50)]] = None
    direccion: Optional [Annotated[str, StringConstraints(max_length=50)]] = None

class PaginatedHuespedResponse(BaseModel):
    huespedes: List[HuespedResponse]
    total_pages: int
    current_page: int
    page_size: int
