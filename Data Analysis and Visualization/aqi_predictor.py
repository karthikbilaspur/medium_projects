import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load historical data
df = pd.read_csv('aqi_data.csv')

# Preprocess data
X = df.drop(['aqi'], axis=1)  # features
y = df['aqi']  # target variable

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Make predictions
def predict_aqi(features):
    return model.predict(features)