def calculate_aqi(pm25_value):
    if pm25_value <= 50:
        aqi = pm25_value * 50 / 50
        category = "Good"
    elif pm25_value <= 100:
        aqi = (pm25_value - 50) * 50 / 50 + 50
        category = "Moderate"
    elif pm25_value <= 150:
        aqi = (pm25_value - 100) * 50 / 50 + 100
        category = "Unhealthy for sensitive groups"
    elif pm25_value <= 200:
        aqi = (pm25_value - 150) * 50 / 50 + 150
        category = "Unhealthy"
    elif pm25_value <= 300:
        aqi = (pm25_value - 200) * 100 / 100 + 200
        category = "Very unhealthy"
    else:
        aqi = (pm25_value - 300) * 100 / 100 + 300
        category = "Hazardous"
    
    return aqi, category