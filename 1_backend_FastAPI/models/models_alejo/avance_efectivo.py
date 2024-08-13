from sqlalchemy import   Column, ForeignKey, Integer,  Enum,  DateTime,Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class avance_efectivo(Base):
    __tablename__ = 'avance_efectivo'
    
    id_avance_efectivo = Column(Integer, primary_key=True, unique=True)  
    fecha = Column(DateTime)
    id_huesped = Column(Integer)
    id_habitacion = Column(Integer)
    valor = Column(Float(10,2))
    id_usuario_elaborado = Column(Integer)
    id_usuario_autorizado = Column(Integer)
    
    