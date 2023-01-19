from fastapi import FastAPI
from src.mail_sender import routers

app = FastAPI()

#Routes
app.include_router(routers.router)

@app.get("/ping")
async def root():
    return "pong!"
