from pydantic import BaseModel, condecimal, StringConstraints
from typing import Annotated, Optional
from enum import Enum
from sqlalchemy import INTEGER


class estadoEnum(str, Enum):
    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"
    MANTENIMIENTO = "MANTENIMIENTO"


class HabitacionBase(BaseModel):
    estado: estadoEnum
    piso: Optional[int]
    precio_actual: condecimal(max_digits=10, decimal_places=2)
    id_usuario: Optional[Annotated[str, StringConstraints(max_length=30)]]
    numero_habitacion: Annotated[str, StringConstraints(max_length=30)]
    id_categoria_habitacion: Optional[int]


class HabitacionCreate(HabitacionBase):
    piso: Optional[int]
    precio_actual: condecimal(max_digits=10, decimal_places=2)
    numero_habitacion: Annotated[str, StringConstraints(max_length=30)]

class HabitacionResponse(HabitacionBase):
    id_habitacion: int

class HabitacionUpdate(HabitacionBase):
    estado: Optional[estadoEnum]
    piso: Optional[int]
    precio_actual: condecimal(max_digits=10, decimal_places=2)
    id_usuario: Optional[Annotated[str, StringConstraints(max_length=30)]]
    numero_habitacion: Annotated[str, StringConstraints(max_length=30)]
    id_categoria_habitacion: Optional[int]


class HabitacionDelete(HabitacionBase):
    id_habitacion: int

