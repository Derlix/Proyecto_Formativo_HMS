from sqlalchemy import Column, String, Boolean, ForeignKey, CHAR, TIMESTAMP, DateTime, Integer
from sqlalchemy.orm import relationship
from models.base_class import Base
from datetime import datetime

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id_usuario = Column(CHAR(30), primary_key=True)
    nombre_completo = Column(String(80))
    email = Column(String(100), unique=True)
    passhash = Column(String(30))  # Ajustado a varchar(255)
    usuario_rol = Column(String(15), ForeignKey('roles.nombre_rol'))  # Ajustado para coincidir con 'roles.nombre_rol'
    estado_usuario = Column(Boolean, default=True)
    creado_en = Column(TIMESTAMP, default=datetime.now)
    actualizado_en = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    id_hotel = Column(Integer, ForeignKey('hoteles.id_hotel'))  # Ajustado a Integer

    rol = relationship("Role")
    hotel = relationship("Hotel")
