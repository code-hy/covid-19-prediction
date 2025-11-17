import pandas as pd
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def train_model():
    """
    Loads data, performs feature engineering, trains a model,
    and saves it to a file.
    """
    print("Starting model training process...")
    
    # Load data
    df = pd.read_csv('data/covid_19_clean_complete.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Aggregate to country level
    country_df = df.groupby(['Country/Region', 'Date']).agg({
        'Confirmed': 'sum',
        'Lat': 'first',
        'Long': 'first'
    }).reset_index()
    print(country_df.head())
    print(country_df.tail)
    print(country_df)
    # Feature Engineering
    country_df.sort_values(['Country/Region', 'Date'], inplace=True)
    country_df['days_since_first_case'] = country_df.groupby('Country/Region').cumcount()

    # Define features and target
    features = ['days_since_first_case', 'Lat', 'Long']
    target = 'Confirmed'
    
    X = country_df[features]
    y = country_df[target]
    print(X.head())
    print(y.head(50))
    # Initialize and train the model
    print("Training RandomForestRegressor model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X, y)
    
    # Save the trained model to a file
    model_filename = 'model.pkl'
    with open(model_filename, 'wb') as f:
        pickle.dump(model, f)
        
    print(f"Model training complete. Model saved as '{model_filename}'")
    
    # Store country data for lookup in the API
    country_coords = country_df[['Country/Region', 'Lat', 'Long']].drop_duplicates().set_index('Country/Region')
    with open('country_coords.pkl', 'wb') as f:
        pickle.dump(country_coords, f)
    print("Country coordinates data saved as 'country_coords.pkl'")


if __name__ == "__main__":
    train_model()