import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "cambia_esto_por_una_clave_segura")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "cambia_esto_por_una_clave_segura")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///ecommerce.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = os.getenv("DEBUG", "False") == "True"
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")