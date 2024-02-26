from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import player, game, play, tackle, tracking, user, auth

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(player.router)
app.include_router(game.router)
app.include_router(play.router)
app.include_router(tackle.router)
app.include_router(tracking.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"info": "This is the main page"}
