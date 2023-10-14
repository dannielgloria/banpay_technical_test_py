from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.middleware.auth_middleware import check_user_has_role
from model.user import User, UserCreate, UserUpdate
from services.user_service import create_user, get_users, get_user_by_id, update_user, delete_user

router = APIRouter()

@router.post("/users/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    return create_user(db, user)

@router.get("/users/", response_model=list[User])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of users with optional pagination.
    """
    return get_users(db, skip, limit)

@router.get("/users/{user_id}", response_model=User)
def retrieve_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user by their ID.
    """
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=User)
def update_user_info(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    """
    Update a user's information.
    """
    user = update_user(db, user_id, user_update)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}", response_model=User)
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user by their ID.
    """
    user = delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/admin-resource")
def admin_resource(user: User = Depends(check_user_has_role("admin"))):
    """
    Access an admin resource.
    """
    return {"message": "This is an admin resource accessible only to users with the 'admin' role."}
