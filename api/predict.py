import os
import joblib

model_path = os.path.join(MODEL_DIR, "model_v1.pkl")
model=joblib.load(model_path)
preprocessor=joblib.load("customer churn prediction/model_and_dev/preprocessor.pkl")

def predict_churn(data):
    x=preprocessor.transform(data)
    predict=model.predict_proba(x)[0][1]
    return float(predict)

