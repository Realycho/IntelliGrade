from fastapi import APIRouter, HTTPException, status, Depends # Depends might not be needed yet
from app.schemas.user import UserCreate, User, UserLogin # UserLogin is new here
from app.core.security import hash_password, verify_password # verify_password is new
import uuid

router = APIRouter()

# In-memory storage for users (for now, until DB is integrated)
# This is NOT suitable for production.
fake_users_db = [] 

@router.post("/users/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: UserCreate):
    # Check if user already exists (simple check by email for this fake DB)
    for existing_user in fake_users_db:
        if existing_user["email"] == user_in.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )
    
    hashed_pass = hash_password(user_in.password)
    
    # Create a user dictionary (simulating DB record)
    # Note: In a real DB, 'id' would be auto-generated.
    # 'is_active' would default to True or based on verification logic.
    new_user_data = {
        "id": uuid.uuid4(), # Generate a new UUID for the user
        "email": user_in.email,
        "full_name": user_in.full_name,
        "hashed_password": hashed_pass, # Store hashed password
        "is_active": True 
    }
    fake_users_db.append(new_user_data)
    
    # Return the User model, excluding the password
    return User(
        id=new_user_data["id"],
        email=new_user_data["email"],
        full_name=new_user_data["full_name"],
        is_active=new_user_data["is_active"]
    )

@router.post("/auth/login")
async def login_for_access_token(form_data: UserLogin):
    user_found = None
    for user_in_db in fake_users_db:
        if user_in_db["email"] == form_data.email:
            user_found = user_in_db
            break
    
    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"}, # Or "Token" if not using Bearer for JWT later
        )
    
    if not verify_password(form_data.password, user_found["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # For now, just a success message. JWT generation will be added later.
    return {"message": "Login successful"}
