from fastapi import APIRouter, HTTPException, Depends, status, Security
from sqlalchemy.orm import Session
from typing import List
from ..schemas import PlayOut
from ..database import get_reader_db
from ..models import Play
from ..oauth2 import get_current_user

router = APIRouter(
    prefix='/plays',
    tags=['Plays']
)

@router.get("/", response_model=List[PlayOut])
async def get_plays(current_user_id: int = Security(get_current_user, scopes=["reader"]), db: Session = Depends(get_reader_db), limit: int = 10, skip: int = 0):
    result = db.query(Play).limit(limit).offset(skip).all()
    return result

@router.get("/{game_id}/{play_id}", response_model=PlayOut)
async def get_play(game_id: int, play_id: int, db: Session = Depends(get_reader_db)):
    result = db.query(Play).filter(Play.game_id == game_id and Play.play_id == play_id).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No plays found")
    return result
