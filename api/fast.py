from fastapi import FastAPI
import pandas as pd
# from zoologist.predict import load_model, predict

app = FastAPI()
# Load the model in the global scope
# only load once when the api starts
# model_path = ''
# app.state.model = load_model(model_path)

@app.get("/")
def root():
    return {"message": "API is running!"}

@app.get("/dummy")
def dummy():
    return {"status": "ok", "data": "This is a dummy endpoint"}

# --- Prediction Endpoint ---

# Predict endpoint
@app.get('/predict')
def predict_endpoint(
    pickup_datetime: str,
    pickup_longitude: float,
    pickup_latitude: float,
    dropoff_longitude: float,
    dropoff_latitude: float,
    passenger_count: int
):
    """
    Returns a taxi fare prediction based on the input features.
    """
    # 1. Construct the dataframe from the inputs
    X_pred = pd.DataFrame([{
        'pickup_datetime': pickup_datetime,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }])

    # 2. Get the prediction using the loaded model
    # For now, return a placeholder: passenger_count * 2.5
    y_pred = passenger_count * 2.5

    # 3. Returns the required dictionary format
    return {
        "prediction": y_pred,
    }
