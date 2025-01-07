import pandas as pd
from models.linear_regression import train_linear_regression, predict_linear_regression
from models.lstm import train_lstm, predict_lstm
from utils.data_utils import load_data, preprocess_data, split_data, scale_data
from utils.metrics import calculate_metrics

def main():
    # Load data
    data = load_data('data/apple_stock_price.csv')

    # Preprocess data
    data = preprocess_data(data)

    # Split data
    train_data, test_data = split_data(data)

    # Scale data
    train_data = scale_data(train_data)
    test_data = scale_data(test_data)

    # Define features and target
    X_train = train_data[['Open', 'High', 'Low', 'Volume']]
    y_train = train_data['Close']
    X_test = test_data[['Open', 'High', 'Low', 'Volume']]
    y_test = test_data['Close']

    # Train linear regression model
    lr_model = train_linear_regression(X_train, y_train)
    lr_pred = predict_linear_regression(lr_model, X_test)

    # Train LSTM model
    lstm_model = train_lstm(X_train, y_train)
    lstm_pred = predict_lstm(lstm_model, X_test)

    # Calculate metrics
    lr_mse, lr_mae, lr_r2 = calculate_metrics(y_test.values, lr_pred)
    lstm_mse, lstm_mae, lstm_r2 = calculate_metrics(y_test.values, lstm_pred)

    # Print metrics
    print(f'Linear Regression MSE: {lr_mse:.2f}, MAE: {lr_mae:.2f}, R2: {lr_r2:.2f}')
    print(f'LSTM MSE: {lstm_mse:.2f}, MAE: {lstm_mae:.2f}, R2: {lstm_r2:.2f}')

if __name__ == '__main__':
    main()