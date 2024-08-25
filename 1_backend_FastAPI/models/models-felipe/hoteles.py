from sqlalchemy import Column, String
from models.base_class import Base
from sqlalchemy.orm import relationship


class Category(Base):
      __tablename__ = 'hoteles'
      id_hotel = Column( int , autoincrement=True ,primary_key=True)
      nombre = Column(String(80))
      ubicacion = Column(String(45))
      direccion = Column(String(70))
      telefono = Column(String(15))
      
     
