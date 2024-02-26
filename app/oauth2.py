from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, models
from .config import settings
from .database import get_god_db
from fastapi import Depends, status, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='authenticate',
                                     scopes={"admin": "Creates users", "reader": "Consumes endpoints that are not users"},)



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expires_minutes)
    to_encode.update({'exp': expire})

    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

    return encoded_jwt

async def get_current_user(security_scopes: SecurityScopes, 
                              token: str = Depends(oauth2_scheme), db: Session = Depends(get_god_db)):

    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"

        credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
					  detail="Could not validate credentials",
					  headers={"WWW-Authenticate": authenticate_value},)
    
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        id = payload.get("user_id")
        
        if id is None:
            raise credentials_exception
        
        token_data = schemas.TokenData(id=id)

        user = db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        for scope in security_scopes.scopes:
            if scope != user.scope:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not enough permissions.")

    except JWTError:
        raise credentials_exception

    return user.id
