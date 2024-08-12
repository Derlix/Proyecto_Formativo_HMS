from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from models.models_brayan.base_class import Base


class Ocupantes(Base):
    __tablename__ = 'ocupantes'
    id_ocupantes = Column(Integer, primary_key=True, unique=True)
    adultos = Column(Integer(25))
    niños = Column(Integer(25))
  



