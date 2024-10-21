from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

# Base class for model definitions
Base = declarative_base()

class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False)
    level = Column(String(20), nullable=False)
    responsibility = Column(String(20), nullable=False)
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # def __init__(self, id, name, level, responsibility, create_time, update_time):
    #     self.id = id
    #     self.name = name
    #     self.level = level
    #     self.responsibility = responsibility
    #     self.create_time = create_time
    #     self.update_time = update_time

    # user_role_maps = relationship("UserRoleMap", back_populates="role_id")
    owner = relationship("User", back_populates="roles")