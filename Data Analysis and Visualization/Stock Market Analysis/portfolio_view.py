from flask import render_template
from app import app
from models.portfolio_model import PortfolioModel

@app.route('/portfolio')
def portfolio():
    portfolio_data = PortfolioModel().get_portfolio_data()
    return render_template('portfolio.html', portfolio_data=portfolio_data)