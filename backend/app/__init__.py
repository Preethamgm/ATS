from fastapi import FastAPI
from .database import engine, Base
from .routes import router as main_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Applicant Tracking System (ATS)", version="1.0")

# Include routes
app.include_router(main_router)

@app.get("/")
def root():
    return {"message": "Welcome to the ATS API"}
