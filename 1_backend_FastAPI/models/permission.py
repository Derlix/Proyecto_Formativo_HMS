from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models.base_class import Base

class Permission(Base):
    __tablename__ = 'permissions'
    rol_name = Column(String(15), ForeignKey('roles.role_name'),primary_key=True)
    module_name = Column(String(15), ForeignKey('modules.module_name'),primary_key=True)
    p_select = Column(Boolean, default=True)
    p_insert = Column(Boolean, default=True)
    p_update = Column(Boolean, default=True)
    p_delete = Column(Boolean, default=True)

    role = relationship("Role")
    module = relationship("Module")