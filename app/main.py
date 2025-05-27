from fastapi import FastAPI

app = FastAPI(
    title="IntelliGrade API",
    description="API for the IntelliGrade platform - AI-powered real-time learning.",
    version="0.1.0"
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to IntelliGrade API"}

@app.get("/health", tags=["Utilities"])
async def health_check():
    return {"status": "ok"}

# Further routers will be included here later
