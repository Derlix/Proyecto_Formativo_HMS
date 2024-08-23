from typing import Annotated, Optional
from pydantic import BaseModel, StringConstraints
from datetime import datetime

class HotelesCreate(BaseModel):
    nombre: Annotated[str, StringConstraints(max_length=80)]
    ubicacion: Annotated[str, StringConstraints(max_length=45)]
    direccion:  Annotated[str, StringConstraints(max_length=70)]
    telefono:  Annotated[str, StringConstraints(max_length=15)]
    
   
class HotelesResponse(BaseModel):
    nombre: str
    ubicacion: str
    direccion: str
    telefono: str
    
class HotelesUpdate(BaseModel):
    nombre: Optional[Annotated[str, StringConstraints(max_length=80)]] = None
    ubicacion: Optional[Annotated[str, StringConstraints(max_length=45)]] = None
    direccion: Optional[Annotated[str, StringConstraints(max_length=70)]] = None
    telefono: Optional[Annotated[str, StringConstraints(max_length=15)]] = None