from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_class import Base  # Asumiendo que `Base` viene de tu configuración de SQLAlchemy


class ReporteEntradaSalida(Base):
    __tablename__ = "reporte_entrada_salida"

    id_reporte_entrada_salida = Column(Integer, primary_key=True, index=True)
    id_entrada_reporte = Column(Integer, ForeignKey("entrada_reporte.id_entrada_reporte"))
    id_salida_reporte = Column(Integer, ForeignKey("salida_reporte.id_salida_reporte"))

    entrada_reporte = relationship("EntradaReporte", back_populates="reportes_entrada_salida")
    salida_reporte = relationship("SalidaReporte", back_populates="reportes_entrada_salida")
