from typing import Annotated
from pydantic import BaseModel, StringConstraints, condecimal

class ImpuestoBase(BaseModel):
    descripcion: Annotated[str, StringConstraints(max_length=150)]
    tasa: condecimal(max_digits=10, decimal_places=2)
    

class ImpuestoCreate(ImpuestoBase):
    descripcion: Annotated[str, StringConstraints(max_length=150)]
    tasa: condecimal(max_digits=10, decimal_places=2)
    
   
class ImpuestoResponse(ImpuestoBase):
    id_impuesto: int

class ImpuestoUpdate(ImpuestoBase):
    descripcion: Annotated[str, StringConstraints(max_length=150)] = None
    tasa: condecimal(max_digits=10, decimal_places=2) = None