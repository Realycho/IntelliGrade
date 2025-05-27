from passlib.context import CryptContext

# Initialize CryptContext. bcrypt is a good default.
# schemes defines the hashing algorithms to be used.
# deprecated="auto" will automatically mark older hashes as deprecated during verification.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)
