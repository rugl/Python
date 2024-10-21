from pydantic import BaseModel
from datetime import datetime
from schemas.roleSchemas import RoleOut  # Correctly import RoleOut

class UserBase(BaseModel):
    name: str
    nick_name: str
    phone: str
    role: int

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserOut(BaseModel):
    id: int
    create_time: datetime
    update_time: datetime
    role: RoleOut

    class Config:
    #     # orm_mode = True
    #     # from_attributes = True
        model_config = {'from_attributes': True}