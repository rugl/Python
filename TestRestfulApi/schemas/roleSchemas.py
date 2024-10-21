from pydantic import BaseModel
from datetime import datetime

class RoleBase(BaseModel):
    name: str
    level: str
    responsibility: str

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class RoleOut(BaseModel):
    id: int
    name: str
    level: str
    responsibility: str

    class Config:
        model_config = {'from_attributes': True}
