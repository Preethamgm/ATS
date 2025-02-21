import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ------------------- Database Config -------------------

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/ats")

# ------------------- JWT Authentication Config -------------------

SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# ------------------- Other Configurations -------------------

DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1"]
