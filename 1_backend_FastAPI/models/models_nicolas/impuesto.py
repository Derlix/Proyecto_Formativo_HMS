from sqlalchemy import Column, Float, Integer, String
from models.base_class import Base

class Impuesto(Base):
    __tablename__ = 'impuestos'

    id_impuesto = Column( Integer , autoincrement=True ,primary_key=True)
    descripcion = Column(String(150))
    tasa = Column(Float(5,2))

      