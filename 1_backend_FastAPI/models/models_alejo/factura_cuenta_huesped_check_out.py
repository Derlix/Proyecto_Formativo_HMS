from sqlalchemy import  Boolean, Column, ForeignKey, Integer, String, Enum,  DateTime,Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class factura_cuenta_huesped_check_out(Base):
    __tablename__ = 'factura_cuenta_huesped_check_out'
    
    id_factura_cuenta_huesped_check_out = Column(Integer, primary_key=True, unique=True)
    id_tarjeta_registro_hotelero_check_in = Column(Integer, ForeignKey('tarjeta_registro_hotelero_check_in.id_tarjeta_registro_hotelero_check_in'))
    fecha_salida_check_out = Column(DateTime)
    balance_inicial = Column(Float(10,2))
    balance_final = Column(Float(10,2))
    impuesto = Column(Float(10,2))
    id_avance_efectivo = Column(Integer, ForeignKey('avance_efectivo.id_avance_efectivo'))
    estado = Column(Boolean)
    seguro = Column(Integer)