from sqlalchemy import  Float, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from models.base_class import Base

class caracteristicas(Base):
    __tablename__ = 'caracteristicas'
    
    id_caracteristicas = Column(Integer, primary_key=True, unique=True)
    nombre_caracteristicas = Column(String(250))
    adicional = Column(Float(5,2))