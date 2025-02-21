from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Applicant
from .schemas import ApplicantCreate

# Secret key for signing JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 password bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------- Password Hashing -------------------

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# ------------------- JWT Token Handling -------------------

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return email
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# ------------------- User Authentication -------------------

def authenticate_applicant(email: str, password: str, db: Session):
    applicant = db.query(Applicant).filter(Applicant.email == email).first()
    if not applicant or not verify_password(password, applicant.resume):  # Assuming 'resume' stores hashed password
        return None
    return applicant

# ------------------- Token Endpoint -------------------

from fastapi import APIRouter

router = APIRouter()

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    applicant = authenticate_applicant(form_data.username, form_data.password, db)
    if not applicant:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": applicant.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
def register_applicant(applicant_data: ApplicantCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(applicant_data.resume)  # Hash the password
    applicant = Applicant(
        name=applicant_data.name,
        email=applicant_data.email,
        phone=applicant_data.phone,
        resume=hashed_password  # Store the hashed password
    )
    db.add(applicant)
    db.commit()
    db.refresh(applicant)
    return {"message": "User registered successfully"}
