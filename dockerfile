FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /model_and_dev /model_and_dev
COPY /log /log
COPY /api /api

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
