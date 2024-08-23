import datetime
from sqlalchemy import Column, Date, Enum, Float, ForeignKey, Integer, PrimaryKeyConstraint, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from models.base_class import Base




class Factura_producto(Base):
    __tablename__ = 'factura_producto'
    id_facturacion = Column(Integer, ForeignKey('facturacion.id_facturacion'), primary_key=True)
    id_producto = Column(Integer, ForeignKey('productos.id_producto'), primary_key=True)
    cantidad = Column(Integer)
    fecha = Column(DateTime)
    precio_unitario =  Column(Float(10,2))
    __table_args__ = (
        PrimaryKeyConstraint('id_facturacion', 'id_producto'),
    )

