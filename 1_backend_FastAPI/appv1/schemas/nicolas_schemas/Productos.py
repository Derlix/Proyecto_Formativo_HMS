from typing import Annotated
from pydantic import BaseModel, StringConstraints
from sqlalchemy import Float

class ProductoBase(BaseModel):
    nombre_producto: Annotated[str, StringConstraints(max_length=50)]
    descripcion: Annotated[str, StringConstraints(max_length=150)]
    precio_actual: Annotated[float, Float(max_length=(10,2))]
    
class ProductoCreate(BaseModel):
    nombre_producto: Annotated[str, StringConstraints(max_length=50)]
    descripcion: Annotated[str, StringConstraints(max_length=150)]
    precio_actual: Annotated[float, Float(max_length=(10,2))]
    
   
class ProductoResponse(BaseModel):
    nombre_producto: str
    descripcion: str
    precio_actual: float
    