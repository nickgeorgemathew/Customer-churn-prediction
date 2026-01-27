import os
import joblib


BASE_DIR = os.path.dirname(os.getcwd())  
MODEL_DIR = os.path.join(BASE_DIR, "model_and_dev")
model_path = os.path.join(MODEL_DIR, "model_v1.pkl")
preprocessor_path=os.path.join(MODEL_DIR, "preprocessor.pkl")
model=joblib.load(model_path)
preprocessor=joblib.load(preprocessor_path)

def predict_churn(data):
    x=preprocessor.transform(data)
    predict=model.predict_proba(x)[0][1]
    return float(predict)

