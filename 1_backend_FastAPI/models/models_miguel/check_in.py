from sqlalchemy import VARCHAR, create_engine, Column, Integer, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class CheckIn(Base):
    __tablename__ = 'check_in'
    
    id_check_in = Column(Integer, primary_key=True, unique=True)
    id_reserva = Column(Integer, ForeignKey('reservas.id_reserva'))
    medio_llegada = Column(Enum('AEREO', 'TERRESTRE'))
    llegada_situacion = Column(Enum('CON RESERVA', 'SIN RESERVA'))
    equipaje = Column(Enum('SI', 'NO'))
    suma_en_letras = Column(VARCHAR(40))



