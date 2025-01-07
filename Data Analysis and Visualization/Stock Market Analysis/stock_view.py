from flask import render_template
from app import app
from models.stock_model import StockModel

@app.route('/stock-dashboard')
def stock_dashboard():
    stock_data = StockModel().get_stock_data()
    return render_template('stock_dashboard.html', stock_data=stock_data)