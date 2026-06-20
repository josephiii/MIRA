
from fastapi import FastAPI
from routes.AuthRoutes import router

app = FastAPI(title="MIRA")

app.include_router(router)