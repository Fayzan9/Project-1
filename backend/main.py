import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apis.notes import router as notes_router
from apis.tags import router as tags_router
from database import init_db
import logging
from core.logging_config import setup_logging
from fastapi.responses import JSONResponse
setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI(title="Notes Backend API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")

    try:
        response = await call_next(request)
        logger.info(f"Response status: {response.status_code}")
        return response

    except Exception as e:
        logger.exception(f"Unhandled error: {e}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"}
        )



@app.on_event("startup")
def startup():
    init_db()

# Register routers
app.include_router(notes_router)
app.include_router(tags_router)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="localhost",
        port=8000
    )