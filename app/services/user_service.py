from sqlalchemy.orm import Session
from app.database import User
from model.user import UserCreate, UserUpdate

def create_user(db: Session, user: UserCreate) -> User:
    """
    Create a new user.

    Args:
        db (Session): The database session.
        user (UserCreate): User creation data.

    Returns:
        User: The created user.
    """
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10) -> list[User]:
    """
    Get a list of users with optional pagination.

    Args:
        db (Session): The database session.
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to retrieve.

    Returns:
        list[User]: List of users.
    """
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int) -> User:
    """
    Get a user by their ID.

    Args:
        db (Session): The database session.
        user_id (int): User ID.

    Returns:
        User: The user with the specified ID.
    """
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, user_update: UserUpdate) -> User:
    """
    Update a user's information.

    Args:
        db (Session): The database session.
        user_id (int): User ID.
        user_update (UserUpdate): User update data.

    Returns:
        User: The updated user.
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for field, value in user_update.dict(exclude_unset=True).items():
            setattr(db_user, field, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int) -> User:
    """
    Delete a user by their ID.

    Args:
        db (Session): The database session.
        user_id (int): User ID.

    Returns:
        User: The deleted user.
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user

def get_user_by_username(db: Session, username: str):
    """
    Get a user by their username.

    Args:
        db (Session): The database session.
        username (str): User's username.

    Returns:
        User: The user with the specified username.
    """
    return db.query(User).filter(User.username == username).first()
