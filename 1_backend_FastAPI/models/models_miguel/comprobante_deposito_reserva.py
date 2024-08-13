from sqlalchemy import VARCHAR, create_engine, Column, Integer, String, Float, Enum, ForeignKey, DateTime, Table, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ComprobanteDepositoReserva(Base):
    __tablename__ = 'comprobante_deposito_reserva'
    
    id_comprobante_deposito_reserva = Column(Integer, primary_key=True, unique=True)
    id_tarjeta_de_registro_hotelero_check_in = Column(Integer, ForeignKey('tarjeta_de_registro_hotelero_check_in.id_tarjeta_de_registro_hotelero_check_in'))
    fecha = Column(DateTime)
    id_huesped = Column(Integer, ForeignKey('huespedes.id_huesped'))
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuarios'))
    suma_en_letras = Column(VARCHAR(40))
    cifra = Column(Float)
    forma_pago = Column(Enum('efectivo', 'transferencia', 'tarjeta_de_credito'))
    intermediario = Column(Enum('comision_deducida', 'comision_no_deducida'))
    concepto = Column(Enum('deposito', 'cancelacion_total'))


