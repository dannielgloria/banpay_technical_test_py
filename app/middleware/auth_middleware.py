from fastapi import Request, HTTPException, Security, Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from app.database import Session, User
from services.user_services import get_user_by_username
from config.settings import Settings
from jose import JWTError, jwt
from model.user import User
from typing import Optional

# Define security schemes, in this case, we're using OAuth2 token bearer for authentication.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Verify the token and retrieve user details from it.

    Args:
        token (str): The authentication token.
        db (Session): The database session.

    Returns:
        User: The authenticated user.
    """
    settings = Settings()
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_by_username(db, token_data.username)
    if user is None:
        raise credentials_exception
    return user

def check_user_has_role(required_role: str = None, current_user: User = Security(verify_token)):
    """
    Check if the authenticated user has the required role.

    Args:
        required_role (str): The required role for accessing the endpoint.
        current_user (User): The authenticated user.

    Raises:
        HTTPException: If the user doesn't have the required role.
    """
    if required_role and required_role != current_user.role:
        raise HTTPException(status_code=403, detail="You don't have permission to access this resource")

credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)