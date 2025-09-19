from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
import settings
settings = settings.settings

# db_url = 'postgresql+asyncpg://fast_lms_user:1234@localhost:5432/fast_lms'

async_engine = create_async_engine(settings.database.url)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
