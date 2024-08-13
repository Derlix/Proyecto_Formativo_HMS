from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_class import Base  # Asumiendo que `Base` viene de tu configuración de SQLAlchemy



class SalidaReporte(Base):
    __tablename__ = "salida_reporte"

    id_salida_reporte = Column(Integer, primary_key=True, index=True)
    id_cuenta_huesped = Column(Integer, ForeignKey("factura_cuenta_huesped_check_out.id_factura_cuenta_huesped_check_out"))

    # Relación opcional si quieres acceder a los detalles de la cuenta
    cuenta_huesped = relationship("FacturaCuentaHuespedCheckOut", back_populates="salidas_reportes")
