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
def get_prediction(customer_data:CustomerInput):
    x=predict_churn(customer_data)
    if not x:
        return({
  "tenure": 3,
  "monthly_charges": 95.5,
  "total_charges": 280.0,
  "contract_type": "Month-to-month",
  "payment_method": "Electronic check"
})
    else:
        return(x)
