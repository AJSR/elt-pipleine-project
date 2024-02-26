from fastapi import APIRouter, HTTPException, Depends, status, Security
from sqlalchemy.orm import Session
from typing import List
from ..schemas import TrackingOut
from ..database import get_reader_db
from ..models import Tracking
from ..oauth2 import get_current_user


router = APIRouter(
    prefix='/trackings',
    tags=['Trackings']
)

@router.get("/", response_model=List[TrackingOut])
async def get_all_trackings(current_user_id: int = Security(get_current_user, scopes=["reader"]), 
                            db: Session = Depends(get_reader_db), limit: int = 10, skip: int = 10):
    result = db.query(Tracking).limit(limit).offset(skip).all()
    return result

@router.get("/{nfl_id}", response_model=List[TrackingOut])
async def get_player_trackings(nfl_id: int, current_user_id: int = Security(get_current_user, scopes=["reader"]),
                                db: Session = Depends(get_reader_db), limit: int = 10, skip: int = 0):
    result = db.query(Tracking).filter(Tracking.nfl_id == nfl_id).limit(limit).offset(skip).all()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No trackings found for player with id {nfl_id}")
    return result

@router.get("/{game_id}/{play_id}", response_model=List[TrackingOut])
async def get_trackings_by_play(game_id: int, play_id: int, current_user_id: int = Security(get_current_user, scopes=["reader"]), 
                                limit: int = 10, skip: int = 0, db: Session = Depends(get_reader_db)):
    result = db.query(Tracking).filter(Tracking.game_id == game_id and Tracking.play_id == play_id).limit(limit).offset(skip).all()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No trackings found")
    return result
