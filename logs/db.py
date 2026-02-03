from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL="sqlite:///./logs.db"

engine=create_engine(
    DATABASE_URL,connect_args={"check_same_thread":False}
)
session_local=sessionmaker(bind=engine)
Base=declarative_base()