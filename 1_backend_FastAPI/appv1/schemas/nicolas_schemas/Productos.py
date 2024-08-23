from typing import Annotated
from pydantic import BaseModel, StringConstraints, condecimal

class ProductoBase(BaseModel):
    nombre_producto: Annotated[str, StringConstraints(max_length=50)]
    descripcion: Annotated[str, StringConstraints(max_length=150)]
    precio_actual: condecimal(max_digits=10, decimal_places=2)
    
class ProductoCreate(ProductoBase):
    nombre_producto: Annotated[str, StringConstraints(max_length=50)]
    descripcion: Annotated[str, StringConstraints(max_length=150)]
    precio_actual: condecimal(max_digits=10, decimal_places=2)
   
class ProductoResponse(ProductoBase):
    nombre_producto: str
    descripcion: str
    precio_actual: float

class ProductoUpdate(ProductoBase):
    nombre_producto: Annotated[str, StringConstraints(max_length=50)]
    descripcion: Annotated[str, StringConstraints(max_length=150)]
    precio_actual: condecimal(max_digits=10, decimal_places=2)