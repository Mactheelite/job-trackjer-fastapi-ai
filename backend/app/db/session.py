from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings

# The engine manages the connection pool and provides the session factory
engine = create_async_engine(settings.database_url, echo=True)

session_local = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    async with session_local() as session:
        yield session