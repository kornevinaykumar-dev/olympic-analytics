import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-change-me")
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60 * 24  # 24h

    SQLALCHEMY_DATABASE_URI = os.getenv("MYSQL_URL")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

    ML_MODEL_PATH = os.getenv("ML_MODEL_PATH", "../ML/model.pkl")
    ML_ENCODERS_PATH = os.getenv("ML_ENCODERS_PATH", "../ML/encoders.pkl")
