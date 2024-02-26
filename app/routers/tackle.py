from fastapi import APIRouter, HTTPException, Depends, status, Security
from sqlalchemy.orm import Session
from typing import List
from ..schemas import TackleOut
from ..database import get_reader_db
from ..models import Tackle
from ..oauth2 import get_current_user

router = APIRouter(
    prefix='/tackles',
    tags=['Tackles']
)

@router.get("/", response_model=List[TackleOut])
async def get_tackles(current_user_id: int = Security(get_current_user, scopes=["reader"]), 
                      db: Session = Depends(get_reader_db), limit: int = 10, skip: int = 0):
    result = db.query(Tackle).limit(limit).offset(skip).all()
    return result

@router.get("/{nfl_id}", response_model=List[TackleOut])
async def get_player_tackles(nfl_id: int, 
                             current_user_id: int = Security(get_current_user, scopes=["reader"]),
                               db: Session = Depends(get_reader_db)):
    result = db.query(Tackle).filter(Tackle.nfl_id == nfl_id).all()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No tackles found for player with id {nfl_id}")
    return result

@router.get("/{game_id}/{play_id}", response_model=TackleOut)
async def get_tackles_in_play(game_id: int, play_id: int, current_user_id: int = Security(get_current_user, scopes=["reader"]), 
                              db: Session = Depends(get_reader_db)):
    result = db.query(Tackle).filter(Tackle.game_id == game_id and Tackle.play_id == play_id).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tackle not found")
    return result

