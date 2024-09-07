from pydantic import BaseModel, condecimal, StringConstraints
from typing import Annotated, Optional,List

class CategoriaHabitacionBase(BaseModel):
    precio_fijo: condecimal(max_digits=10, decimal_places=2)
    tipo_habitacion: Annotated[str, StringConstraints(max_length=40)]
    id_hotel: Optional[int]

class CategoriaHabitacionCreate(CategoriaHabitacionBase):
    precio_fijo: condecimal(max_digits=10, decimal_places=2)
    tipo_habitacion: Annotated[str, StringConstraints(max_length=40)]
    
class CategoriaHabitacionUpdate(BaseModel):
    precio_fijo: Optional[condecimal(max_digits=10, decimal_places=2)] = None
    tipo_habitacion: Optional[Annotated[str, StringConstraints(max_length=40)]] = None
    id_hotel: Optional[int] = None

class CategoriaHabitacionResponse(CategoriaHabitacionBase):
    id_categoria_habitacion: int
    precio_fijo: float
    tipo_habitacion: str
    id_hotel: int

class PaginatedCategoriaHabitacionResponse(BaseModel):
    categories: List[CategoriaHabitacionResponse]
    total_pages: int
    current_page: int
    page_size: int
