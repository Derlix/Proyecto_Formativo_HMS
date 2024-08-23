from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_class import Base  # Asumiendo que `Base` viene de tu configuración de SQLAlchemy

class EntradaReporte(Base):
    __tablename__ = "entrada_reporte"

    id_entrada_reporte = Column(Integer, primary_key=True, index=True)
    id_tarjeta_registro_hotelero = Column(Integer, ForeignKey("tarjeta_registro_hotelero_check_in.id_tarjeta_registro_hotelero_check_in"))

    # Relación opcional si quieres acceder a los detalles del registro
    tarjeta_registro_hotelero = relationship("TarjetaRegistroHoteleroCheckIn", back_populates="entradas_reportes")


