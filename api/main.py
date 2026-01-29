from fastapi import FastAPI
from schemas import CustomerInput
from predict import predict_churn
import pandas as pd
import csv
from datetime import datetime

app= FastAPI(title="Customer churn prediction")

@app.get('/')
def root():
    return {"message":"Welcome to Customer Churn Prediction API"}
@app.post('/predict')
def get_prediction(customer_data: CustomerInput):
    try:
        proba = predict_churn(customer_data)
        return {
            "churn_probability": {
                "will churn": float(proba[1]),
                "will not churn": float(proba[0])
            }
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}