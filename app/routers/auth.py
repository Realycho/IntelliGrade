from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, User as UserSchema, UserLogin
from app.core.security import verify_password, create_access_token # create_access_token is new
from app.schemas.token import Token # New import
from app.db.session import get_db
from app.crud import crud_user

router = APIRouter()

@router.post("/users/register", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user_in.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    
    created_user = crud_user.create_user(db=db, user=user_in)
    return created_user


@router.post("/auth/login", response_model=Token) # Changed response_model
async def login_for_access_token(form_data: UserLogin, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=form_data.email)
    
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create JWT token
    # The subject of the token ('sub') can be user's email or ID.
    # Additional claims can be added to the data dictionary if needed.
    access_token_data = {"sub": db_user.email}
    # ACCESS_TOKEN_EXPIRE_MINUTES will be read from settings within create_access_token
    access_token = create_access_token(data=access_token_data)
    
    return {"access_token": access_token, "token_type": "bearer"}
