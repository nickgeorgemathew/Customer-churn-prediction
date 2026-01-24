from fastapi import FastAPI
from schemas import CustomerInput
# from predict import predict_churn
import pandas as pd
import csv
from datetime import datetime

app= FastAPI(title="Customer churn prediction")

@app.post('/predict')
def get_prediction(customer_data:CustomerInput):
    return(220102)
    
