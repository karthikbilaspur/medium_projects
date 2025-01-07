from flask import Flask, render_template, jsonify, request
import pandas as pd
import json

app = Flask(__name__)

# Load election data
election_data = pd.read_csv('data/election_data.csv')

# Route for homepage
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Route for visualization data
@app.route('/data', methods=['GET'])
def data():
    data = election_data.to_dict(orient='records')
    return jsonify({'success': True, 'data': data})

# Route for visualizations
@app.route('/visualizations', methods=['GET'])
def visualizations():
    return render_template('visualizations.html')

# Route for filtering data
@app.route('/filter', methods=['POST'])
def filter_data():
    party = request.form['party']
    filtered_data = election_data[election_data['party'] == party].to_dict(orient='records')
    return jsonify({'success': True, 'data': filtered_data})

if __name__ == '__main__':
    app.run(debug=True, port=5000)