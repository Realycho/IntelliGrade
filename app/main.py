from fastapi import FastAPI
from app.routers import auth # Import the auth router

app = FastAPI(
    title="IntelliGrade API",
    description="API for the IntelliGrade platform - AI-powered real-time learning.",
    version="0.1.0"
)

# Include the authentication router
app.include_router(auth.router, prefix="/api/v1", tags=["Authentication"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to IntelliGrade API"}

@app.get("/health", tags=["Utilities"])
async def health_check():
    return {"status": "ok"}

# Further application-specific routers will be included here
