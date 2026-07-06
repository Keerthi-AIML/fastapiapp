from fastapi import FastAPI
from database import Base, engine

# Import routers
from routers import auth, company, job,chat,rag

# Create FastAPI app
app = FastAPI(
    title="FastAPI Job Portal API",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(company.router)
app.include_router(job.router)
app.include_router(chat.router)
app.include_router(rag.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "FastAPI is running successfully!"}