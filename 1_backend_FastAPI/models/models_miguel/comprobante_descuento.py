from sqlalchemy import VARCHAR, create_engine, Column, Integer, String, Float, Enum, ForeignKey, DateTime, Table, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ComprobanteDescuento(Base):
    __tablename__ = 'comprobante_descuento'
    
    id_comprobante_descuento = Column(Integer, primary_key=True, unique=True)
    id_habitacion = Column(Integer, ForeignKey('habitaciones.id_habitacion'))
    id_huesped = Column(Integer, ForeignKey('huespedes.id_huesped'))
    id_usuario_elaborado = Column(Integer, ForeignKey('usuarios.id_usuarios'))
    id_usuario_autorizado = Column(Integer, ForeignKey('usuarios.id_usuarios'))
    descripcion = Column(VARCHAR(40))
    activo = Column(SmallInteger)
