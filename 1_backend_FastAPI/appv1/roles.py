from pydantic import BaseModel,StringConstraints
from typing import Annotated


class RolCreate(BaseModel):
    nombre_rol: Annotated[str, StringConstraints(max_length=15)]

