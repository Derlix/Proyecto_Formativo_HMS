from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import date, datetime
from enum import Enum
from sqlalchemy import false, true


 
class tipo_documento(str, Enum):
    CC = "CC"
    TI = "TI"
    CE = "CE"
    
class HuespedBase(BaseModel):
    nombre_completo: Annotated[str, StringConstraints(max_length=80)]
    numero_documento: Annotated[str, StringConstraints(max_length=15)]
    fecha_expedicion: date
    email: EmailStr
    telefono: Annotated[str, StringConstraints(max_length=15)]
    ocupacion: Annotated[str, StringConstraints(max_length=50)]
    direccion: Annotated[str, StringConstraints(max_length=50)]

    

class HuespedCreate(HuespedBase):
    tipo_documento: tipo_documento



class HuespedResponse(HuespedBase):
    id_huesped: int
    huesped_estado: bool = true
    created_at: datetime
    updated_at: datetime


class HuespedUpdate(BaseModel):
    nombre_completo: Optional[Annotated[str, StringConstraints(max_length=80)]] = None
    tipo_documento: tipo_documento
    numero_documento: Optional [Annotated[str, StringConstraints(max_length=15)]] = None
    fecha_expedicion: Optional [date]= None
    email: Optional [EmailStr] = None
    telefono: Optional [Annotated[str, StringConstraints(max_length=15)]] = None
    ocupacion: Optional [Annotated[str, StringConstraints(max_length=50)]] = None
    direccion: Optional [Annotated[str, StringConstraints(max_length=50)]] = None
    huesped_estado: bool = None


class HuespedDelete(BaseModel):
    huesped_estado: bool = false


class PaginatedHuespedResponse(BaseModel):
    huespedes: List[HuespedResponse]
    total_pages: int
    current_page: int
    page_size: int
