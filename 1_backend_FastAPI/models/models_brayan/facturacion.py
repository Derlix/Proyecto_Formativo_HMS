import datetime
from sqlalchemy import Column, Date, Enum, Float, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from models.base_class import Base



class MetodoPagoType(Enum.Enum):
    efectivo = "EFECTIVO"
    tarjeta = "TARJETA"
    transferencia = "TRANSFERENCIA"



class EstadoType(Enum.Enum):
    pendiente = "PENDIENTE"
    pagada = "PAGADA"
    cancelada = "CANCELADA"    


class Facturacion(Base):
    __tablename__ = 'facturacion'
    id_facturacion = Column(Integer, primary_key=True, autoincrement=True)
    id_check_in = Column(Integer, ForeignKey('check_in.id_check_in'))
    subtotal = Column(Float(10,2))
    impuestos = Column(Float(10,2))
    total = Column(Float(10,2))
    total_precio_productos = Column(Float(10,2))
    metodo_pago = Column(Enum(MetodoPagoType))
    estado = Column(Enum(EstadoType))
    fecha_salida = Column(DateTime)


