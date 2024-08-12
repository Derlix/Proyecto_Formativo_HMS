from sqlalchemy import   Column, ForeignKey, Integer,  Enum,  DateTime,Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class gastos_factura(Base):
    __tablename__ = 'gastos_factura'
    
    id_gasto = Column(Integer, primary_key=True, unique=True)  
    id_factura_cuenta_huesped_check_out = Column(Integer, ForeignKey('tarjeta_registro_hotelero_check_in.id_tarjeta_registro_hotelero_check_in'))
    id_producto = Column(DateTime)
    tipo_gasto = Column(Enum('debito, credito'))
    total_gasto = Column(Float(10,2))
    