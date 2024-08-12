from sqlalchemy import  Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class huesped_factura(Base):
    __tablename__ = 'huesped_factura'
    
    id_registro = Column(Integer, primary_key=True, unique=True)
    id_huesped = Column(Integer, ForeignKey('huesped.id_huesped'))
    id_factura_cuenta_huesped_check_out = Column(Integer, ForeignKey('factura_cuenta_huesped_check_out.id_factura_cuenta_huesped_check_out  '))

    
    
    
