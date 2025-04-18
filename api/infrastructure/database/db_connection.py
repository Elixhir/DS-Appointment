import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "development") 

if ENV == "production":
    DATABASE_URL = os.getenv("DATABASE_URL")
else:
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'keepalert')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'keepalert')
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'keep_alert')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5433)

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()