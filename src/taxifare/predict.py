import joblib
import pandas as pd

from sklearn import set_config
set_config(transform_output="pandas")


MODEL_PATH = 'models/linreg_pipeline.joblib'

def load_model(MODEL_PATH):
    """
    load the trained model
    """


    model = joblib.load(open(MODEL_PATH, 'rb'))
    return model



def predict(model, X): #: pd.DataFrame
    """
    make a prediction
    """
    prediction = model.predict(X)

    return prediction


if __name__ == "__main__":
    X_dummy = pd.DataFrame([{
          'pickup_datetime': '2013-07-06 17:18:00 UTC',
          'pickup_longitude': -73.950655,
          'pickup_latitude': 40.783282,
          'dropoff_longitude': -73.984365,
          'dropoff_latitude': 40.769802,
          'passenger_count': 1
    }])

    model = load_model("models/linreg_pipeline.joblib")

    print(predict(model, X_dummy))
