from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


BASE_DIR=Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "logs.db"
DATABASE_URL="sqlite:///./logs.db"

engine=create_engine(
    f"sqlite:///{DB_PATH}",connect_args={"check_same_thread":False}
)
Sessionlocal=sessionmaker(bind=engine)
Base=declarative_base()

print("FASTAPI DB PATH:", engine.url)