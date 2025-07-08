from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserAuth, UserAuthResponse, UserRead
from models.user import User
from utils.database import get_db
from utils.security import verify_password, get_password_hash, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/signup", response_model=UserAuthResponse, status_code=201)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = User(name=user.name, email=user.email, password_hash=hashed_password)
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    token = create_access_token({"sub": str(db_user.user_id)})
    return UserAuthResponse(userId=db_user.user_id, token=token)

@router.post("/signin", response_model=UserAuthResponse)
def signin(auth: UserAuth, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == auth.email).first()
    if not db_user or not verify_password(auth.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    token = create_access_token({"sub": str(db_user.user_id)})
    return UserAuthResponse(userId=db_user.user_id, token=token) 