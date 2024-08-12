from sqlalchemy import create_engine, Column, Integer, String, Float, Enum, ForeignKey, DateTime, Table, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Reservas(Base):
    __tablename__ = 'reservas'
    
    id_reservas = Column(Integer, primary_key=True)
    id_huesped = Column(Integer, ForeignKey('huespedes.id_huesped'))
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuarios'))
    id_habitacion = Column(Integer, ForeignKey('habitaciones.id_habitacion'))
    id_cambio_reserva = Column(Integer, ForeignKey('cambio_reserva.id_cambio_reserva'))
    id_comprobante_deposito_reserva = Column(Integer, ForeignKey('comprobante_deposito_reserva.id_comprobante_deposito_reserva'))
    personas = Column(Integer)
    llegada_fecha = Column(DateTime)
    salida_fecha = Column(DateTime)