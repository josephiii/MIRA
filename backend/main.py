
from fastapi import FastAPI
from routes import router

app = FastAPI(title="MIRA")

app.include_router(router)