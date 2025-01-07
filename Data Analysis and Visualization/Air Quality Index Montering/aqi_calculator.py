def calculate_aqi(pm25_value):
    if pm25_value <= 50:
        aqi = pm25_value * 50 / 50
        category = "Good"
    elif pm25_value <= 100:
        aqi = (pm25_value - 50) * 50 / 50 + 50
        category = "Moderate"
    # ... implement remaining categories
    return aqi, category