from fastapi import FastAPI
from routes.device import device
app = FastAPI()
app.include_router(device)
