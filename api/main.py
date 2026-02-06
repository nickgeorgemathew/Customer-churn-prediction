from fastapi import FastAPI
from api.schemas import CustomerInput
from api.predict import predict_churn
import pandas as pd
import csv
from logs.models import Predictionlog
from logs.db import Sessionlocal
import time
from datetime import datetime,timezone


app= FastAPI(title="Customer churn prediction")

@app.get('/')
def root():
    return {"message":"Welcome to Customer Churn Prediction API"}
@app.post('/predict')
def get_prediction(customer_data: CustomerInput):
    start_time=time.perf_counter()
    db=Sessionlocal()
    
    try:
        proba,pred = predict_churn(customer_data)
        latency=(time.perf_counter()-start_time)*1000
        log=Predictionlog(
            model_version="v1.0",
            timestamp=datetime.now(timezone.utc),
            input_features=customer_data.model_dump(),
            prediction=pred,
            probability=proba,
            latency_ms=latency

        )
        db.add(log)
        db.commit()
        return {
            "churn_probability": {
                "will churn": float(proba[1]),
                "will not churn": float(proba[0])
            }
        }
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        latency=(time.perf_counter()-start_time)*1000
        log=Predictionlog(
            model_version="v1.0",
            timestamp=datetime.now(timezone.utc),
            input_features=customer_data.model_dump(),
            error=str(e),
            latency_ms=latency

        )
        db.add(log)
        db.commit()
        
        return {"error": str(e)}