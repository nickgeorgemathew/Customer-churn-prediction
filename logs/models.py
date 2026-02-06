from sqlalchemy import Column,Integer,DateTime,String,JSON,Float
from datetime import datetime
from logs.db import engine
from logs.db import Base

class Predictionlog(Base):
    __tablename__="predictionlogs"

    id=Column(Integer,primary_key=True,index=True)
    timestamp=Column(DateTime)
    model_version=Column(String,index=True)
    input_features=Column(JSON)
    prediction=Column()
    probability=Column()
    latency_ms=Column(Float)
    error=Column(String,nullable=True)


Base.metadata.create_all(bind=engine)