from fastapi import FastAPI
from app.routers import auth
from app.db.session import engine # Import engine
from app.models.user import Base # Import Base from where User model is defined

# This will create the tables if they don't exist.
# For production, you'd use something like Alembic for migrations.
def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="IntelliGrade API",
    description="API for the IntelliGrade platform - AI-powered real-time learning.",
    version="0.1.0"
)

@app.on_event("startup")
async def on_startup():
    create_db_and_tables() # Call the function to create tables

# Include the authentication router
app.include_router(auth.router, prefix="/api/v1", tags=["Authentication"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to IntelliGrade API"}

@app.get("/health", tags=["Utilities"])
async def health_check():
    return {"status": "ok"}

# Further application-specific routers will be included here
