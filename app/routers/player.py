from fastapi import APIRouter, HTTPException, Depends, status, Security
from sqlalchemy.orm import Session
from typing import List
from ..schemas import PlayerOut
from ..database import get_reader_db
from ..models import Player
from ..oauth2 import get_current_user


router = APIRouter(
    prefix="/players",
    tags=["Players"]
)

@router.get("/", response_model=List[PlayerOut])
async def get_players(current_user_id: int = Security(get_current_user, scopes=["reader"]), db: Session = Depends(get_reader_db), limit: int = 10, skip: int = 0):
    result = db.query(Player).limit(limit).offset(skip).all()
    return result

@router.get("/{id}", response_model=PlayerOut)
async def get_player(id: int, current_user_id: int = Security(get_current_user, scopes=["reader"]), db: Session = Depends(get_reader_db)):
    player = db.query(Player).filter(Player.nfl_id == id).first()

    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Player with id {id} not found")
    
    return player
