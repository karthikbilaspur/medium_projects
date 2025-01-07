import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from aqi_monitor import monitor_aqi
from aqi_predictor import predict_aqi

app = dash.Dash(__name__)

# Cities and countries for dropdown
cities = ["Delhi", "Mumbai", "Bangalore"]
countries = ["India", "India", "India"]

app.layout = html.Div([
    html.H1('Air Quality Index Dashboard'),
    
    # City selection dropdown
    html.Div([
        html.H4('Select City:'),
        dcc.Dropdown(
            id='city-dropdown',
            options=[{'label': city, 'value': city} for city in cities]
        )
    ]),
    
    # Real-time AQI display
    html.Div(id='real-time-aqi'),
    
    # Predicted AQI display
    html.Div([
        html.H4('Predicted AQI:'),
        html.Div(id='predicted-aqi')
    ]),
    
    # AQI trends graph
    html.Div([
        html.H4('AQI Trends:'),
        dcc.Graph(id='aqi-trends')
    ]),
    
    # Temperature and humidity inputs for prediction
    html.Div([
        html.H4('Temperature (°C):'),
        dcc.Input(id='temperature', type='number'),
        html.H4('Humidity (%):'),
        dcc.Input(id='humidity', type='number')
    ])
])

# Update real-time AQI display
@app.callback(
    Output('real-time-aqi', 'children'),
    Input('city-dropdown', 'value')
)
def update_real_time_aqi(city):
    aqi, category = monitor_aqi(city, countries[cities.index(city)])
    return f"AQI: {aqi}, Category: {category}"

# Update predicted AQI display
@app.callback(
    Output('predicted-aqi', 'children'),
    Input('temperature', 'value'),
    Input('humidity', 'value'),
    Input('city-dropdown', 'value')
)
def update_predicted_aqi(temp, humidity, city):
    predicted_aqi = predict_aqi(temp, humidity)
    return f"Predicted AQI: {predicted_aqi}"

# Update AQI trends graph
@app.callback(
    Output('aqi-trends', 'figure'),
    Input('city-dropdown', 'value')
)
def update_aqi_trends(city):
    # Replace with actual historical data
    data = pd.DataFrame({'AQI': [50, 70, 90, 110, 130], 'Time': ['9:00', '10:00', '11:00', '12:00', '13:00']})
    fig = px.line(data, x='Time', y='AQI', title='AQI Trends')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)