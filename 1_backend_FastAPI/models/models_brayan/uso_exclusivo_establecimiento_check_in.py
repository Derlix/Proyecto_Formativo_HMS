import enum
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, Enum, String
from sqlalchemy.orm import relationship
from models.models_brayan.base_class import Base


class EquipajeType(Enum.Enum):
    con = "con"
    sin = "sin"



class FormaPagoEnum(enum.Enum):
    efectivo = "efectivo"
    tarjeta_credito = "tarjeta_credito"
    transferencia =  "transferencia"

class llegadaEnum(enum.Enum):
    con_reserva = "con_reserva"
    sin_reserva = "sin_reserva"    


class Uso_exlusivo_establecimiento_check_in(Base):
    __tablename__ = 'Uso_exlusivo_establecimiento_check_in'
    id_uso_exlusivo_establecimiento_check_in = Column(Integer, primary_key=True, unique=True)
    id_hotel = Column(Integer, ForeignKey('hoteles.id_hotel'), primary_key=True)
    id_ocupantes = Column(Integer, ForeignKey('hoteles.id_hotel'), primary_key=True)
    id_habitacion = Column(Integer, ForeignKey('habitaciones.id_habitacion'), primary_key=True)
    tarifa = Column(Float(10,2))
    impuesto =  Column(Float(10,2))
    fecha_llegada = Column(DateTime)
    fecha_salida =  Column(DateTime)
    id_estadia =  Column(Integer, ForeignKey('estadia.id_estadia'), primary_key=True)
    equipaje =  Column(Enum(EquipajeType))
    forma_pago =  Column(Enum(FormaPagoEnum))
    id_factura_cuenta_huesped_check_out = Column(Integer, ForeignKey('factura_cuenta_huesped_check_out.id_factura_cuenta_huesped_check_out'), primary_key=True)
    llegada = Column(Enum(llegadaEnum))
    empresa = Column(String) 