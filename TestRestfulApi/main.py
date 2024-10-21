from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User, Base
from schemas.userSchemas import UserCreate, UserUpdate, UserOut
import controller.userC as userController
from typing import List
from fastapi.middleware.cors import CORSMiddleware

# Database connection   
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/testDB"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create database tables
# Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS (optional, if accessing from different origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET method: Retrieve all users
@app.get("/users", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    return userController.get_users(db)
    # users = db.query(User).all()
    # return users

# GET method: Retrieve a user by ID
@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return userController.get_user(user_id, db)
    # user = db.query(User).filter(User.id == user_id).first()
    # if not user:
    #     raise HTTPException(status_code=404, detail="User not found")
    # return user

# POST method: Create a new user
@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return userController.create_user(user, db)
    # new_user = User(**user.dict())
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user

# PUT method: Update an existing user
@app.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return userController.update_user(user_id, user, db)
    # db_user = db.query(User).filter(User.id == user_id).first()
    # if not db_user:
    #     raise HTTPException(status_code=404, detail="User not found")
    
    # for key, value in user.dict().items():
    #     setattr(db_user, key, value)
    
    # db.commit()
    # db.refresh(db_user)
    # return db_user

# PATCH method: Partially update a user
@app.patch("/users/{user_id}", response_model=UserOut)
def patch_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return userController.patch_user(user_id, user, db)
    # db_user = db.query(User).filter(User.id == user_id).first()
    # if not db_user:
    #     raise HTTPException(status_code=404, detail="User not found")
    
    # for key, value in user.dict(exclude_unset=True).items():
    #     setattr(db_user, key, value)
    
    # db.commit()
    # db.refresh(db_user)
    # return db_user

# DELETE method: Delete a user by ID
@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return userController.delete_user(user_id, db)
    # db_user = db.query(User).filter(User.id == user_id).first()
    # if not db_user:
    #     raise HTTPException(status_code=404, detail="User not found")
    
    # db.delete(db_user)
    # db.commit()
    # return {"message": "User deleted successfully"}