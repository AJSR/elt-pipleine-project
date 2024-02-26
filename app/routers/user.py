from fastapi import APIRouter, HTTPException, Depends, status, Security
from ..schemas import UserOut, UserCreate
from sqlalchemy.orm import Session
from ..database import get_god_db
from .. import utils
from ..models import User
from ..oauth2 import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: UserCreate, current_user_id: int = Security(get_current_user, scopes=["admin"]),
                 db: Session = Depends(get_god_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
