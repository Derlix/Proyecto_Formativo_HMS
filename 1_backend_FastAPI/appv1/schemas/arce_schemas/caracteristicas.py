from pydantic import BaseModel, condecimal, constr

class Caracteristica(BaseModel):
    id_caracteristica: int
    nombre_caracteristicas: constr(max_length=250)
    adicional: condecimal(max_digits=10, decimal_places=2)

class CaracteristicaCreate(BaseModel):
    nombre_caracteristicas: constr(max_length=250)
    adicional: condecimal(max_digits=10, decimal_places=2)

class CaracteristicaResponse(BaseModel):
    id_caracteristica: int
    nombre_caracteristicas: constr(max_length=250)
    adicional: condecimal(max_digits=10, decimal_places=2)

    class Config:
        orm_mode = True