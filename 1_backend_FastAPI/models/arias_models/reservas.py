from sqlalchemy import Column, Integer, DateTime, String, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from models.base_class import Base


class FormaPago(Enum):
    EFECTIVO = "EFECTIVO"
    DEBITO = "DEBITO"
    CREDITO = "CREDITO"
    TRANSFERENCIA = "TRANSFERENCIA"

class Reserva(Base):
    __tablename__ = 'reservas'

    id_reserva = Column(Integer, primary_key=True, autoincrement=True)
    id_huesped = Column(Integer, ForeignKey('huespedes.id_huesped'), nullable=False)
    fecha_reserva = Column(DateTime, nullable=False)
    empresa = Column(String(30))
    valor_deposito = Column(Float(precision=2), nullable=False,default=0)
    forma_pago = FormaPago

    huesped = relationship("Huesped")

