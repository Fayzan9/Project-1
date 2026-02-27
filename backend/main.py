import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

count = 0  # global counter

@app.post("/increment")
def increment_count():
    global count
    count += 1
    return {
        "message": "Count increased",
        "count": count
    }

@app.get("/count")
def get_count():
    return {"count": count}

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="localhost",
        port=8000
    )