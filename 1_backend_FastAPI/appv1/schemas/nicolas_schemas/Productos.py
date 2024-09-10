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
    id_producto: int
    nombre_producto: str
    descripcion: str
    precio_actual: float

class ProductoUpdate(ProductoBase):
    nombre_producto: Annotated[str, StringConstraints(max_length=50)]  = None
    descripcion: Annotated[str, StringConstraints(max_length=150)] = None
    precio_actual: condecimal(max_digits=10, decimal_places=2) = None

class PaginatedProductResponse(BaseModel):
    productos: list[ProductoResponse]
    total_pages: int
    current_page: int
    page_size: int