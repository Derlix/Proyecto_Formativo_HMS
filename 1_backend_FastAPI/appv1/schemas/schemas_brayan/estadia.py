from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime

from sqlalchemy import INTEGER

class EstadiaBase(BaseModel):
    id_estadia: Annotated[str, INTEGER]
    dias:  Annotated[str, INTEGER(max_length=2)]
    noches: Annotated[str, INTEGER(max_length=2)]


class EstadiaResponse(EstadiaBase):
    id_estadia: int
    dias:  int
    noches: int
