from typing import Annotated, List, Optional
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime

from sqlalchemy import INTEGER

class OcupantesBase(BaseModel):
    id_ocupante: Annotated[str, INTEGER]
    adultos:  Annotated[str, INTEGER(max_length=2)]
    niños: Annotated[str, INTEGER(max_length=2)]


class OcupantesResponse(OcupantesBase):
    id_ocupante: int
    adultos:  int
    niños: int
