# COVID-19 Case Prediction API

This project builds a simple machine learning model to predict the cumulative number of confirmed COVID-19 cases for a given country. The predictions are based on the number of days since the country's first case and its geographical coordinates. 
The trained model is served via a REST API built with FastAPI.

## 🧰 Tech Stack

-   **Language**: Python
-   **ML Library**: Scikit-learn
-   **API Framework**: FastAPI
-   **Package Manager**: uv
-   **Containerization**: Docker

## 📊 Dataset

The project uses the "COVID-19 Dataset" by Devakumar K. P. on Kaggle, which is a cleaned version of the JHU CSSE data.

### Why this dataset is used
 The COVID-19 pandemic (which is still ongoing) presented a global challenge where understanding the trajectory of the virus spread was crucial for public health response and resource allocation.
 Goal of this project is to build a simple machine learning model to predict the cumulative number of COVID-19 cases for a given country based on two primary factors:
 1.  Time Progression:  How many days have passed since the country's first confirmed case?
 2.  Geographical Location:  Country's geographical location helps act as proxies for climate, population densiry, and other socio economic factors
    

### How to Get the Data

1.  Go to the [Kaggle Dataset Page](https://www.kaggle.com/datasets/imdevskp/corona-virus-report).
2.  Download the `covid_19_clean_complete.csv` file.
3.  Create a `data/` directory in the root of this project.
4.  Place the downloaded CSV file inside the `data/` directory.

The final path should be: `data/covid_19_clean_complete.csv`

## 🚀 Setup and Running Instructions

### Prerequisites

-   Python 3.11+
-   `uv` package manager ([Install `uv`](https://docs.astral.sh/uv/getting-started/installation/))

### Local Setup

1.  **Clone the repository and navigate into it:**
    ```bash
    git clone <your-repo-url>
    cd covid-19-prediction-api
    ```

2.  **Create and activate a virtual environment using `uv`:**
    ```bash
    uv venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install the project dependencies:**
    ```bash
    uv pip install -e .
    ```

4.  **Train the machine learning model:**
    This script will process the data, train a `RandomForestRegressor`, and save the model as `model.pkl`.
    ```bash
    python train.py
    ```
    You should see an output like: `Starting model training process...Training RandomForestRegressormodel...Model Training complete. Model saved as model.pkl Country coordinates data saved as country_coords.pkl`
    

   

5.  **Run the FastAPI web service:**
    ```bash
    python predict.py
    ```
    The server will start, typically on `localhost:8000/docs`.
    <img width="673" height="239" alt="image" src="https://github.com/user-attachments/assets/51bea8e4-5b5d-499f-bca6-f04ef98c1632" />

## 🌐 Accessing the API

Once the server is running, you can access the interactive API documentation in your browser:

-   **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or http://localhost:8000/docs
-   **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) or http://localhost:8000/redoc

### Example API Request

You can send a `POST` request to the `/predict` endpoint to get a prediction. Here's an example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "country_region": "Italy",
  "days_since_first_case": 100
}'
```

### Example Screenshot of Swagger UI

<img width="1492" height="919" alt="example_screen1" src="https://github.com/user-attachments/assets/8f5a71c2-11dd-4bc2-900f-16048cf32eeb" />



<img width="1611" height="956" alt="image" src="https://github.com/user-attachments/assets/71e562c0-34f8-4fd7-97c2-4a1bb7dbc0cf" />

