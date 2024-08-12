from sqlalchemy import VARCHAR, create_engine, Column, Integer, String, Float, Enum, ForeignKey, DateTime, Table, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Descuento(Base):
    __tablename__ = 'descuento'
    
    id_descuento = Column(Integer, primary_key=True, unique=True)
    porcentaje = Column(float)
    descripcion = Column(VARCHAR(30))
