from sqlalchemy import  Column, Integer, String, Enum,  DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class huesped(Base):
    __tablename__ = 'huesped'
    
    id_huesped = Column(Integer, primary_key=True, unique=True)
    tipo_documento = Column(Enum('CC, CE, TI, Pasaporte'))
    numero_documento = Column(String(15))
    tipo_huesped = Column(Enum('transeunte, permanente, funcionario'))
    edad = Column(String(3))
    email = Column(String(100), unique=True)
    nacionalidad = Column(String(50))
    expedida = Column(DateTime)