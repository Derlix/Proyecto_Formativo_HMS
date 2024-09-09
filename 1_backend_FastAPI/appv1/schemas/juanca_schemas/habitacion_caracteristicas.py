from pydantic import BaseModel
from typing import Optional

class HabitacionCaracteristicaBase(BaseModel):
    id_habitacion: Optional[int]
    id_caracteristica: Optional[int]

class HabitacionCaracteristicaCreate(HabitacionCaracteristicaBase):
    id_habitacion: Optional[int]
    id_caracteristica: Optional[int]

class HabitacionCaracteristicaResponse(HabitacionCaracteristicaBase):
    id_habitacion: Optional[int]
    id_caracteristica: Optional[int]
