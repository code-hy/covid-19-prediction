from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd

# Initialize FastAPI app
app = FastAPI(
    title="COVID-19 Prediction API",
    description="An API to predict cumulative COVID-19 cases for a country.",
    version="1.0.0",
)

# Define the input data model using Pydantic for validation
class PredictionRequest(BaseModel):
    country_region: str
    days_since_first_case: int

# Load the trained model and country coordinates at startup
try:
    model = pickle.load(open("model.pkl", "rb"))
    country_coords = pickle.load(open("country_coords.pkl", "rb"))
    print("Model and data loaded successfully.")
except FileNotFoundError:
    print("Error: Model or data files not found. Please run train.py first.")
    model = None
    country_coords = None


@app.get("/", tags=["General"])
def read_root():
    """
    Root endpoint to welcome users.
    """
    return {"message": "Welcome to the COVID-19 Prediction API. Go to /docs for more information."}


@app.post("/predict", tags=["Prediction"])
def predict_cases(request: PredictionRequest):
    """
    Predicts the cumulative confirmed cases for a given country and day.
    - **country_region**: The name of the country/region.
    - **days_since_first_case**: The number of days since the first case in that country.
    """
    if model is None or country_coords is None:
        raise HTTPException(status_code=500, detail="Model is not loaded.")

    # Check if the country exists in our data
    if request.country_region not in country_coords.index:
        raise HTTPException(status_code=404, detail=f"Country '{request.country_region}' not found in the dataset.")

    # Get coordinates for the country
    coords = country_coords.loc[request.country_region]
    lat = coords['Lat']
    long = coords['Long']

    # Prepare the feature vector for prediction
    features_df = pd.DataFrame([{
        'days_since_first_case': request.days_since_first_case,
        'Lat': lat,
        'Long': long
    }])

    # Make prediction
    prediction = model.predict(features_df)[0]

    # Return the result
    return {
        "country_region": request.country_region,
        "days_since_first_case": request.days_since_first_case,
        "predicted_confirmed_cases": int(prediction)
    }


if __name__ == "__main__":
    # When invoked as a script, start a development server so
    # `python predict.py` behaves like `uvicorn predict:app`.
    import uvicorn

    uvicorn.run("predict:app", host="127.0.0.1", port=8000, reload=True)
