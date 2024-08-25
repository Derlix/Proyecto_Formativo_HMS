from sqlalchemy import Column, Float, Integer, String
from models.base_class import Base

class Producto(Base):
    __tablename__ = 'productos'

    id_producto = Column(Integer, primary_key=True, autoincrement=True)
    nombre_producto = Column(String(50))
    descripcion = Column(String(150))
    precio_actual = Column(Float(10,2))