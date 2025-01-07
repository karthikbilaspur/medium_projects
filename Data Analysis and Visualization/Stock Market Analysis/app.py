from flask import Flask, render_template
from models.stock_model import StockModel
from models.portfolio_model import PortfolioModel

app = Flask(__name__)

# Route for homepage
@app.route('/')
def index():
 return render_template('index.html')

# Route for stock dashboard
@app.route('/stock-dashboard')
def stock_dashboard():
 stock_data = StockModel().get_stock_data()
 return render_template('stock_dashboard.html', stock_data=stock_data)

# Route for portfolio
@app.route('/portfolio')
def portfolio():
 portfolio_data = PortfolioModel().get_portfolio_data()
 return render_template('portfolio.html', portfolio_data=portfolio_data)

if __name__ == '__main__':
 app.run(debug=True)