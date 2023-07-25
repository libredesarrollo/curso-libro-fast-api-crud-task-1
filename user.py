from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from schemes import UserCreate
from authentication import password, authentication
from database import database, models

user_router = APIRouter()

@user_router.post('/token')
def create_token(form_data : OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm), db: Session = Depends(database.get_database_session)):
    email = form_data.username
    password = form_data.password

    user = authentication.authenticate(email,password,db)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    token = authentication.create_access_token(user, db)
    return {"access_token": token.access_token}

@user_router.post('/register', status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db:Session = Depends(database.get_database_session)): #  -> models.User

    user_exist = db.query(models.User).filter(models.User.email == user.email).first()
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User email already exist")
    
    hashed_password = password.get_password_hash(user.password)
    print(hashed_password)

    userdb = models.User(name=user.name, 
                         email= user.email, 
                         surname = user.surname, 
                         website= user.website, 
                         hashed_password=hashed_password)
    
    db.add(userdb)
    db.commit()
    db.refresh(userdb)

    # return userdb

    return {
        "message": "User created succefully"
    }

@user_router.delete("/logout", status_code=status.HTTP_200_OK, dependencies=[Depends(authentication.logout)])
def logout():
    return {'msj': 'ok'}

