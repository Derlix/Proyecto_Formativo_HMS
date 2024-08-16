from sqlalchemy import  Column, Integer, String, Enum,  DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class huespedes(Base):
    __tablename__ = 'huespedes'
    
    id_huesped = Column(Integer, primary_key=True, unique=True)
    nombre_completo = Column(String(80))
    tipo_documento = Column(Enum('CC','TI','Pasaporte','Cedula_extranjera'))
    numero_documento = Column(String(15))
    fecha_expedicion = Column(DateTime)
    email = Column(String(100), unique=True)
    telefono = Column(String(15))
    ocupacion = Column(String(50))
    direccion = Column(String(50))