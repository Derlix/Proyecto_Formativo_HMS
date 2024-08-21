import enum
from sqlalchemy import Column, Integer, ForeignKey, Float, Enum
from models.base_class import Base  # Asumiendo que `Base` viene de tu configuración de SQLAlchemy

class TipoTabitacionEnum(enum.Enum):
    suite = "SUITE"
    suite_jr = "SUITE JR"
    sencilla = "SECILLA"
    doble = "DOBLE"

class CategoriaHabitacion(Base):
    __tablename__ = "categoria_habitacion"

    id_categoria_habitacion = Column(Integer, primary_key=True, autoincrement=True)
    tarifa = Column(Float(10,2))
    tipo_habitacion =  Column(Enum(TipoTabitacionEnum))