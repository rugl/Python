from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User, Base
from models.role import Role
from sqlalchemy.orm import joinedload
from schemas.userSchemas import UserCreate, UserUpdate, UserOut
from schemas.roleSchemas import RoleOut
from typing import List

# GET method: Retrieve all users
def get_users(db: Session) -> List[UserOut]:
    users = db.query(User).options(joinedload(User.roles)).all()

    # return [
    #     UserOut(
    #         id= user.id,
    #         create_time= user.create_time,
    #         update_time= user.update_time
    #     )
    #     for user in users
    # ]
    # return [UserOut.model_validate(user.__dict__) for user in users]

    userList = []

    for user in users:
        role = user.roles
        userOut = UserOut(
            id=user.id,
            create_time=user.create_time,
            update_time=user.update_time,
            role=RoleOut(
                id=role.id,
                name=role.name,
                level=role.level,
                responsibility=role.responsibility
            ) if role else None  # Handle case where role might be None
        )

        userList.append(userOut)
    return userList

# GET method: Retrieve a user by ID
def get_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).options(joinedload(User.roles)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    print(user.__dict__)
    return user

# POST method: Create a new user
def create_user(user: UserCreate, db: Session):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# PUT method: Update an existing user
def update_user(user_id: int, user: UserUpdate, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

# PATCH method: Partially update a user
def patch_user(user_id: int, user: UserUpdate, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

# # DELETE method: Delete a user by ID
def delete_user(user_id: int, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}