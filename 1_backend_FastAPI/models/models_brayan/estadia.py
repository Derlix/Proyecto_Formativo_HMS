from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from models.models_brayan.base_class import Base


class Estadia(Base):
    __tablename__ = 'estadia'
    id_estadia = Column(Integer, primary_key=True, unique=True)
    dias = Column(Integer(100))
    noches = Column(Integer(100))
  



