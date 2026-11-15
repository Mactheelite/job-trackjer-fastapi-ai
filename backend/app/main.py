from datetime import datetime
from typing import Annotated

from fastapi import Depends, FastAPI

from app.core.config import settings

from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from sqlalchemy import text
from fastapi import HTTPException

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)


def get_time() -> str:
    return datetime.now().strftime("%H:%M:%S")


@app.get("/")
async def home():
    return {"message": "Welcome to the Job Tracker API"}


@app.get("/health")
async def health(db: Annotated[AsyncSession, Depends(get_db)]):
    try:
        result = await db.execute(text("SELECT 1"))
        result.scalar_one()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"status": "ok","database": "connected successfully"}


@app.get("/about")
async def about():
    return {"app": "This is a job tracker API"}


@app.get("/time")
async def show_time(now: Annotated[str, Depends(get_time)]):
    return {"time": now}


@app.get("/greeting")
async def greeting(now: Annotated[str, Depends(get_time)]):
    return {"message": f"Hello, the time is {now}"}
