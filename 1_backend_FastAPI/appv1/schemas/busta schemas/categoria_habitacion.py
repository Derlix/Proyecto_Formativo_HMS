from pydantic import BaseModel, condecimal, StringConstraints
from typing import Annotated, Optional

class CategoriaHabitacionBase(BaseModel):
    precio_fijo: condecimal(max_digits=10, decimal_places=2)
    tipo_habitacion: Annotated[str, StringConstraints(max_length=40)]
    id_hotel: Optional[int]

class CategoriaHabitacionCreate(CategoriaHabitacionBase):
    precio_fijo: condecimal(max_digits=10, decimal_places=2)
    tipo_habitacion: Annotated[str, StringConstraints(max_length=40)]

class CategoriaHabitacionResponse(CategoriaHabitacionBase):
    id_categoria_habitacion: int