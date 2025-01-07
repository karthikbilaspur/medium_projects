import pandas as pd
from sklearn.linear_model import LinearRegression

class StockModel:
    def __init__(self):
        self.model = LinearRegression()

    def get_stock_data(self):
        # Load historical stock data from CSV file
        data = pd.read_csv('csv/stock_data.csv')
        
        # Train model
        self.model.fit(data[['open', 'high', 'low']], data['close'])
        
        # Predict stock prices
        predicted_prices = self.model.predict(data[['open', 'high', 'low']])
        return predicted_prices