from sqlalchemy import Column, String
from models.base_class import Base

class Role(Base):
    __tablename__ = 'roles'
    nombre_rol = Column(String(15), primary_key=True)
