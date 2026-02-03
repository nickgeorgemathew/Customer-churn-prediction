import os
import joblib
import pandas as pd


BASE_DIR = os.path.dirname(os.getcwd()) 
MODEL_DIR = os.path.join(BASE_DIR, "model_and_dev")
model_path = os.path.join(MODEL_DIR, "model_v1.pkl")
preprocessor_path=os.path.join(MODEL_DIR, "preprocessor.pkl")
model=joblib.load(model_path)
preprocessor=joblib.load(preprocessor_path)


def transform_payload(payload):
    
    if hasattr(payload, "dict") and callable(payload.dict):
        payload = payload.dict()
        mapping = {
         "Usage_Frequency":"Usage Frequency",
         "Support_Calls":"Support Calls",
         "Payment_Delay":"Payment Delay",
         "Subscription_Type":"Subscription Type",
         "Contract_Length":"Contract Length",
        "Total_Spend":"Total Spend",
        "Last_Interaction":"Last Interaction"
    }
        return {mapping.get(k, k): v for k, v in payload.items()}
  
def predict_churn(data):
    
    transformed=transform_payload(data)
    data_df=pd.DataFrame([transformed])
    predict=model.predict_proba(data_df)[0]
    prob=int(predict[1]>=0.5)
    return(predict,prob)

