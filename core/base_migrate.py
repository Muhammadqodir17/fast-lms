# import asyncio
# from compus.models import *
# from core.base import Base
# from core.database import async_engine
#
#
# async def init_db():
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all())
#
#
# if __name__ == '__main__':
#     asyncio.run(init_db())
