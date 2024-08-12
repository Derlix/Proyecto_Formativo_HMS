from sqlalchemy import create_engine, Column, Integer, String, Float, Enum, ForeignKey, DateTime, Table, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    
    id_usuarios = Column(Integer, primary_key=True, unique=True)
    nombre_completo = Column(String(255))
    email = Column(String(255))
    pashash = Column(String(255))
    usuario_rol = Column(String(255), ForeignKey('roles.nombre_rol'))
    id_hotel = Column(Integer, ForeignKey('hoteles.id_hotel'))