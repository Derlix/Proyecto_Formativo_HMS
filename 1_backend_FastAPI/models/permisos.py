from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models.base_class import Base

class Permission(Base):
    __tablename__ = 'permisos'
    nombre_rol = Column(String(15), ForeignKey('roles.nombre_rol'), primary_key=True)
    nombre_modulo = Column(String(60), ForeignKey('modulos.nombre_modulo'), primary_key=True)
    p_select = Column(Boolean, default=True)
    p_insert = Column(Boolean, default=True)
    p_update = Column(Boolean, default=True)
    p_delete = Column(Boolean, default=True)

    rol = relationship("Role")
    modulo = relationship("Modulo")
