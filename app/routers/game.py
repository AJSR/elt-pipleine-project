from fastapi import APIRouter, HTTPException, Depends, status, Security
from sqlalchemy.orm import Session
from typing import List
from ..schemas import GameOut
from ..database import get_reader_db
from ..models import Game
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/games",
    tags=["Games"]
)

@router.get("/", response_model=List[GameOut])
async def get_games(current_user_id: int = Security(get_current_user, scopes=["reader"]), 
                    db: Session = Depends(get_reader_db), limit: int=10, skip: int=0):
    result = db.query(Game).limit(limit).offset(skip).all()
    return result

@router.get("/{id}", response_model=GameOut)
async def get_game_by_id(id: int, db: Session = Depends(get_reader_db)):
    result = db.query(Game).filter(Game.game_id == id).first()

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No game found with id {id}")

    return result
