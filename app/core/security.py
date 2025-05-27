from passlib.context import CryptContext

# Initialize CryptContext. bcrypt is a good default.
# schemes defines the hashing algorithms to be used.
# deprecated="auto" will automatically mark older hashes as deprecated during verification.

# Add at the top of app/core/security.py
from datetime import datetime, timedelta, timezone # ensure timezone is imported
from typing import Optional
from jose import JWTError, jwt
from app.core.config import settings # For SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# These settings will be defined in config.py later. For now, assume they exist on settings object.
# Example: settings.SECRET_KEY, settings.ALGORITHM, settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # Use ACCESS_TOKEN_EXPIRE_MINUTES from settings, default to 15 if not set
        expire = datetime.now(timezone.utc) + timedelta(minutes=getattr(settings, 'ACCESS_TOKEN_EXPIRE_MINUTES', 15))
    
    to_encode.update({"exp": expire})
    # Use SECRET_KEY and ALGORITHM from settings
    # Ensure settings.SECRET_KEY and settings.ALGORITHM are available in your config
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

# Optional: Basic token verification stub (will be fleshed out when needed for protected routes)
# def verify_access_token(token: str, credentials_exception):
#     try:
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
#         email: str = payload.get("sub") # Assuming email is stored in "sub"
#         if email is None:
#             raise credentials_exception
#         # token_data = TokenData(email=email) # TokenData from app.schemas.token
#     except JWTError:
#         raise credentials_exception
#     # return token_data

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)
