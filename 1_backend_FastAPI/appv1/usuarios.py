from pydantic import BaseModel,EmailStr,StringConstraints
from datetime import datetime
from typing import Annotated,Optional,List

class UsuarioBase(BaseModel):
    nombre_completo: Annotated[str, StringConstraints(max_length=80)]
    email: EmailStr
    usuario_rol: Annotated[str, StringConstraints(max_length=15)]

class UsuarioCreate(UsuarioBase):
    passhash: Annotated[str, StringConstraints(max_length=30)]
    id_hotel: Optional[int] = None  # Ahora es opcional

    
class UsuarioResponse(UsuarioBase):
    id_usuario: str
    estado_usuario: bool = True
    creado_en: datetime
    actualizado_en: datetime

class UsuarioUpdate(BaseModel):
    nombre_completo: Optional[Annotated[str, StringConstraints(max_length=80)]] = None
    email: Optional[EmailStr] = None
    usuario_rol: Optional[Annotated[str, StringConstraints(max_length=15)]] = None
    estado_usuario: bool = None

class PaginatedUsuariosResponse(BaseModel):
    usuarios: List[UsuarioResponse]
    total_paginas: int
    pagina_actual: int
    pagina_cantidad: int

