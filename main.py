from fastapi import FastAPI
from compus.views import router as compus_router

app = FastAPI()

app.include_router(compus_router)