from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

# Base class for model definitions
Base = declarative_base()

class UserRoleMap(Base):
    __tablename__ = "user_role_map"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    role_id = Column(Integer, ForeignKey("role.id"))
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="user_role_maps")
    role = relationship("Role", back_populates="user_role_maps")
