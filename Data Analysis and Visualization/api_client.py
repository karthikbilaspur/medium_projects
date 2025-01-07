import requests

def get_aqi_data(city, country):
    url = f"https://api.openaq.org/v1/latest?city={city}&country={country}"
    response = requests.get(url)
    return response.json()