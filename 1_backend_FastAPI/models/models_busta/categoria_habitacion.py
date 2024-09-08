import enum
from sqlalchemy import Column, Integer, ForeignKey, Float,String
from models.base_class import Base  # Asumiendo que `Base` viene de tu configuración de SQLAlchemy
from sqlalchemy.orm import relationship

# class TipoTabitacionEnum(enum.Enum):
#     suite = "SUITE"
#     suite_jr = "SUITE JR"
#     sencilla = "SECILLA"
#     doble = "DOBLE"

class CategoriaHabitacion(Base):
    __tablename__ = "categoria_habitacion"

    id_categoria_habitacion = Column(Integer, primary_key=True, autoincrement=True)
    precio_fijo = Column(Float(10,2))
    tipo_habitacion =  Column(String(40))
    id_hotel = Column(Integer,ForeignKey('hoteles.nombre'),primary_key=True)
    
    hotel = relationship("Hotel")