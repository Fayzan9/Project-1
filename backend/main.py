import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from apis.notes import router as notes_router

app = FastAPI(title="Notes Backend API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],
)




# Initialize DB file
init_db()

# Register routers
app.include_router(notes_router)



if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="localhost",
        port=8000
    )