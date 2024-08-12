from sqlalchemy import create_engine, Column, Integer, String, Float, Enum, ForeignKey, DateTime, Table, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Habitaciones(Base):
    __tablename__ = 'habitaciones'
    
    id_habitacion = Column(Integer, primary_key=True, unique=True)
    id_usuarios = Column(Integer, ForeignKey('usuarios.id_usuarios'))
    estado = Column(Enum('Activo'))
    piso = Column(Integer)
    precio_actual = Column(Float)
    categoria_id = Column(Integer, ForeignKey('categoria_habitacion.id_categoria_habitacion'))
    id_hotel = Column(Integer, ForeignKey('hoteles.id_hotel'))
    id_descuento = Column(Integer, ForeignKey('descuento.id_descuento'))