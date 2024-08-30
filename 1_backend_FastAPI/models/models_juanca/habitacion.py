from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_class import Base

class Habitacion(Base):
    __tablename__ = "habitaciones"

    id_habitacion = Column(Integer, primary_key=True, autoincrement=True)
    estado = Column(Enum("ACTIVO", "INACTIVO", "MANTENIMIENTO"), nullable=False)
    piso = Column(Integer, nullable=False)
    precio_actual = Column(Float(10, 2), nullable=False)
    id_usuario = Column(String(30), ForeignKey("usuarios.id_usuario"), nullable=False)
    id_categoria_habitacion = Column(Integer, ForeignKey("categoria_habitacion.id_categoria_habitacion"), nullable=False)
    
    caracteristicas = relationship("HabitacionCaracteristica", back_populates="habitacion")
