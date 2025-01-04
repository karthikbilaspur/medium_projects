import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import GradientBoostingRegressor


# Load dataset
def load_data(file_path):
    return pd.read_csv(file_path)


# Preprocess data
def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df = df.interpolate(method='linear')
    return df


# Feature engineering
def engineer_features(df):
    df['Hour'] = df.index.hour
    df['Day'] = df.index.day
    df['Month'] = df.index.month
    df['Season'] = np.where(df['Month'].isin([12, 1, 2]), 'Winter', 
                           np.where(df['Month'].isin([3, 4, 5]), 'Spring', 
                                    np.where(df['Month'].isin([6, 7, 8]), 'Summer', 'Autumn')))
    return df


# Scale ozone values
def scale_ozone(df):
    scaler = StandardScaler()
    df[['Ozone']] = scaler.fit_transform(df[['Ozone']])
    return df


# Split data into training and testing sets
def split_data(df):
    train_size = int(len(df) * 0.8)
    train, test = df[0:train_size], df[train_size:len(df)]
    return train, test


# Define hyperparameter tuning space
def define_hyperparameters():
    param_grid = {'order': [(1,1,1), (2,1,2), (3,1,3)]}
    return param_grid


# Perform grid search for ARIMA model
def grid_search_arima(train, param_grid):
    grid_search = GridSearchCV(ARIMA(train['Ozone'], order=(1,1,1)), param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(train['Ozone'])
    return grid_search


# Forecast using best model
def forecast_best_model(grid_search, steps):
    best_model = grid_search.best_estimator_
    forecast, stderr, conf_int = best_model.forecast(steps=steps)
    return forecast


# Evaluate model
def evaluate_model(grid_search, test):
    best_model = grid_search.best_estimator_
    predictions = best_model.predict(start=len(test), end=len(test)+23)
    mse = mean_squared_error(test['Ozone'], predictions)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(test['Ozone'], predictions)
    mape = mean_absolute_percentage_error(test['Ozone'], predictions)
    return rmse, mae, mape


# Main function
# Main function
def main():
    file_path = 'air_quality_india.csv'
    df = load_data(file_path)
    df = preprocess_data(df)
    df = engineer_features(df)
    df = scale_ozone(df)
    train, test = split_data(df)
    param_grid = define_hyperparameters()
    grid_search = grid_search_arima(train, param_grid)
    forecast = forecast_best_model(grid_search, 24)
    rmse, mae, mape = evaluate_model(grid_search, test)
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"RMSE: {rmse:.2f}, MAE: {mae:.2f}, MAPE: {mape:.2f}")


    # Visualize forecast
    plt.figure(figsize=(12, 6))
    plt.plot(test.index, test['Ozone'], label='Actual')
    plt.plot(test.index, grid_search.best_estimator_.predict(start=len(train), end=len(train)+23), label='Forecast')
    plt.title('Ozone Level Forecast')
    plt.xlabel('Date')
    plt.ylabel('Ozone Level')
    plt.legend()
    plt.show()


    # Randomized search for hyperparameter tuning
    randomized_search = RandomizedSearchCV(ARIMA(train['Ozone'], order=(1,1,1)), param_grid, cv=5, scoring='neg_mean_squared_error', n_iter=10)
    randomized_search.fit(train['Ozone'])
    print(f"Best parameters (randomized search): {randomized_search.best_params_}")


    # Gradient boosting regressor
    gbr = GradientBoostingRegressor()
    gbr.fit(train[['Hour', 'Day', 'Month', 'Season']], train['Ozone'])
    gbr_predictions = gbr.predict(test[['Hour', 'Day', 'Month', 'Season']])
    gbr_mse = mean_squared_error(test['Ozone'], gbr_predictions)
    gbr_rmse = np.sqrt(gbr_mse)
    print(f"GBR RMSE: {gbr_rmse:.2f}")


if __name__ == "__main__":
    main()
