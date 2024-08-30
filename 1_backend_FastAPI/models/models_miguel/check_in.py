import enum
from sqlalchemy import VARCHAR, create_engine, Column, Integer, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class EquipajeEnum(enum.Enum):
    si = "SI"
    no = "NO"

class LlegadaEnum(enum.Enum):
    con_reserva = "CON RESERVA"
    sin_reserva = "SIN RESERVA"

class MedioLlegadaEnum(enum.Enum):
    aereo = "AEREO"
    terrestre = "TERRESTRE"

class CheckIn(Base):
    __tablename__ = 'check_in'
    
    id_check_in = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    id_reserva = Column(Integer, ForeignKey('reservas.id_reserva'))
    medio_llegada = Column((MedioLlegadaEnum))
    llegada_situacion = Column((LlegadaEnum))
    equipaje = Column((EquipajeEnum))
    
    reserva = relationship("Reserva")
