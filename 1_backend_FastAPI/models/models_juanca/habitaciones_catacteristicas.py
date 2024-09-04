from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_class import Base


class HabitacionCaracteristica(Base):
    __tablename__ = "habitacion_caracteristicas"

    id_habitacion = Column(Integer, ForeignKey("habitaciones.id_habitacion"), primary_key=True)
    id_caracteristica = Column(Integer, ForeignKey("caracteristicas.id_caracteristica"), primary_key=True)

    habitacion = relationship("Habitacion", back_populates="caracteristicas")
    caracteristica = relationship("Caracteristica")


