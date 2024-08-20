from pydantic import BaseModel

class HotelResponse(BaseModel):
    id_hotel: int
    nombre: str
    ubicacion: str
    direccion: str
    telefono: str

    class Config:
        orm_mode = True
