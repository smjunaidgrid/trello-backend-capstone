from fastapi import FastAPI

from app.core.config import settings

from app.api.v1.auth import router as auth_router
from app.api.v1.boards import router as boards_router

from app.api.v1.sections import router as sections_router
from app.api.v1.tickets import router as tickets_router
from app.api.v1.invitations import router as invitations_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)


app.include_router(
    auth_router,
    prefix="/api/v1"
)
app.include_router(
    boards_router,
    prefix="/api/v1"
)

@app.get("/")
async def root():
    return {
        "message": "Trello Backend API is running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }

app.include_router(
    sections_router,
    prefix="/api/v1"
)

app.include_router(
    tickets_router,
    prefix="/api/v1"
)

app.include_router(
    invitations_router,
    prefix="/api/v1"
)

