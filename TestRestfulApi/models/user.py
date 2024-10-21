from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

# Base class for model definitions
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    nick_name = Column(String(50), nullable=True)
    phone = Column(String(20), nullable=True)
    role = Column(Integer, ForeignKey('role.id'))
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, id, name, nick_name, phone, role, create_time, update_time):
        self.id = id
        self.name = name
        self.nick_name = nick_name
        self.phone = phone
        self.role = role
        self.create_time = create_time
        self.update_time = update_time

    roles = relationship("Role", back_populates="owner")

class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False)
    level = Column(String(20), nullable=False)
    responsibility = Column(String(20), nullable=False)
    create_time = Column(DateTime, default=datetime.utcnow)
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, id, name, level, responsibility, create_time, update_time):
        self.id = id
        self.name = name
        self.level = level
        self.responsibility = responsibility
        self.create_time = create_time
        self.update_time = update_time

    owner = relationship("User", back_populates="roles")

# class UserRoleMap(Base):
#     __tablename__ = "user_role_map"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("user.id"))
#     role_id = Column(Integer, ForeignKey("role.id"))
#     create_time = Column(DateTime, default=datetime.utcnow)
#     update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     user = relationship("User", back_populates="user_role_maps")
#     role = relationship("Role", back_populates="user_role_maps")
