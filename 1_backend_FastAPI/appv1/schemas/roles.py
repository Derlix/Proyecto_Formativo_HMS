from pydantic import BaseModel,StringConstraints
from typing import Annotated


class RolCreate(BaseModel):
    rol_name: Annotated[str, StringConstraints(max_length=15)]

