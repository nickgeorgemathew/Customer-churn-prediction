
# 📊 Customer Churn Prediction – End-to-End Machine Learning System

## 📌 Overview

This project implements a **complete, production-oriented Customer Churn Prediction system**, covering the full machine learning lifecycle:

* Exploratory Data Analysis (EDA)
* Feature engineering & preprocessing
* Model training, tuning, and evaluation
* Model interpretability
* Real-time inference via FastAPI
* Prediction logging with SQLAlchemy
* Monitoring dashboard with Streamlit
* Model drift detection using PSI (Population Stability Index)

The goal of this project is not just to build an accurate churn model, but to demonstrate **how ML systems are designed, deployed, and monitored in real-world settings**.

---

## 🧠 Problem Statement

Customer churn is a critical business problem where organizations aim to identify customers likely to leave their service.
This project predicts whether a customer will churn based on demographic, contractual, and usage-related features, enabling proactive retention strategies.

---

## 🗂️ Project Structure

```
customer_churn_prediction/
│
├── notebooks/
│   ├── customer_churn_model.ipynb      # EDA, feature engineering, modeling
│
├── app/
│   ├── main.py                          # FastAPI inference service
│   ├── predict.py                       # Model inference logic
│   ├── schemas.py                       # Request validation schemas
│
├── logs/
│   ├── models.py                        # SQLAlchemy ORM models
│   ├── db.py                            # Database connection
│   ├── logs.db                          # SQLite prediction logs
│   ├── dashboard.py                    # Streamlit monitoring dashboard
│             
│
├── artifacts/
│   ├── model.pkl                        # Trained model
│   ├── preprocessor.pkl                # Preprocessing pipeline
│
├── requirements.txt
└── README.md
```

---

## 📊 Exploratory Data Analysis (EDA)

The notebook begins with an extensive EDA to understand:

* Churn vs non-churn distributions
* Feature relationships with churn
* Data imbalance and skewness
* Potential data leakage risks
* Redundant and noisy features

Key insights from EDA directly informed:

* Feature selection
* Preprocessing strategy
* Model choice

> **Takeaway:** Strong models start with strong data understanding.

---

## 🧩 Feature Engineering & Preprocessing

A robust preprocessing pipeline was built using **scikit-learn’s ColumnTransformer**:

* **Categorical features**

  * OneHotEncoding
* **Numerical features**

  * QuantileTransformer (to handle skew and outliers)

All preprocessing steps are:

* Fit only on training data
* Serialized and reused during inference to prevent leakage

---

## 🤖 Model Development

Multiple models were trained and compared:

| Model               | Purpose                      |
| ------------------- | ---------------------------- |
| Logistic Regression | Baseline + interpretability  |
| Random Forest       | Non-linear interactions      |
| XGBoost             | Final high-performance model |

### Hyperparameter Tuning

* RandomizedSearchCV
* HalvingRandomSearchCV

### Evaluation Metrics

* ROC-AUC
* Precision / Recall
* F1-Score

**Final Model Performance**

* ROC-AUC ≈ **0.95**

---

## 🔎 Model Interpretability

Interpretability was treated as a first-class concern:

* Logistic Regression coefficients
* Tree-based feature importance
* **SHAP** for:

  * Global explanations
  * Local, per-prediction explanations

This ensures model decisions are **transparent and explainable**, which is critical for business adoption.

---

## ⚙️ FastAPI Inference Service

The trained model is deployed as a **FastAPI application**:

### Key Features

* Strict request validation using schemas
* Low-latency inference endpoint
* Per-request latency measurement
* Robust error handling

### Sample Endpoint

```
POST /predict
```

Returns:

* Churn probability
* Class prediction

---

## 📝 Prediction Logging (Observability)

Every inference request is logged using **SQLAlchemy ORM** into SQLite.

Each log captures:

* Timestamp
* Input features
* Predicted probability & class
* Latency (ms)
* Error (if any)
* Model version

This enables:

* Traceability
* Debugging
* Monitoring
* Auditing

---

## 📈 Monitoring Dashboard (Streamlit)

A Streamlit dashboard provides **real-time observability**:

### Metrics Tracked

* Total predictions
* Churn rate
* Latency trends
* Error rates
* High-risk customers
* Time-based comparisons

---

## 📉 Model Drift Detection

To monitor post-deployment behavior, **Population Stability Index (PSI)** is used on predicted probabilities.

### Why PSI?

* Works without immediate labels
* Industry-standard (finance, risk modeling)
* Interpretable thresholds

| PSI Value  | Interpretation                      |
| ---------- | ----------------------------------- |
| < 0.1      | No drift                            |
| 0.1 – 0.25 | Moderate drift                      |
| > 0.25     | High drift (retraining recommended) |

This provides early warning signals when model behavior changes.

---

## 🧪 Demo 

To demo the system :

```bash

streamlit run dashboard.py
streamlit run demo.py
uvicorn api.main:app --reload
```
* Run db.py and models.py to ensure the database is created and the table is available
* Run the fastapi app next with uvicorn,if using powershell ensure you are in the respective api directory before running.
* Run the dashboard and demo streamlit apps to view the logging and get prediction


---

## 🛠️ Tech Stack

* **Python**
* **pandas, NumPy**
* **scikit-learn**
* **XGBoost**
* **SHAP**
* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Streamlit**

---

## 🎯 Key Learnings

* Model accuracy alone is not sufficient
* Observability is critical for ML systems
* Drift detection is essential post-deployment
* End-to-end ownership matters more than isolated models
* Production ML requires both data science and engineering thinking

---

## 🚀 Future Improvements

* Feature-level drift detection
* Automated retraining pipelines
* Alerting for SLA breaches
* Cloud deployment
* A/B model comparison (v1 vs v2)

---

## 📬 Contact

If you’d like to discuss this project or provide feedback, feel free to reach out via LinkedIn or GitHub.

