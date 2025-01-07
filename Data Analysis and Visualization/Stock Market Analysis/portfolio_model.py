import pandas as pd

class PortfolioModel:
    def __init__(self):
        pass

    def get_portfolio_data(self):
        # Load portfolio data from CSV file
        data = pd.read_csv('csv/portfolio_data.csv')
        
        # Calculate portfolio metrics
        portfolio_metrics = {
            'return': data['return'].mean(),
            'risk': data['risk'].std()
        }
        return portfolio_metrics