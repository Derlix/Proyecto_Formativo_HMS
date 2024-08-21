import enum
from typing import Annotated
from pydantic import BaseModel

from sqlalchemy import INTEGER, FLOAT

class TipoTabitacionEnum(enum.Enum):
    suite = "SUITE"
    suite_jr = "SUITE JR"
    sencilla = "SECILLA"
    doble = "DOBLE"

class CategoriaHabitacionBase(BaseModel):
    id_categoria_habitacion = Annotated[str, INTEGER]
    tarifa:  Annotated[float, FLOAT(max_length=(10,2))]
    tipo_habitacion: TipoTabitacionEnum


class CategoriaHabitacionResponse(CategoriaHabitacionBase):
    id_categoria_habitacion: int
    tarifa:  float
    tipo_habitacion: TipoTabitacionEnum