import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense

def train_lstm(X_train, y_train):
    model = Sequential()
    model.add(LSTM(50, input_shape=(X_train.shape[1], 1)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X_train.values.reshape(-1, 4, 1), y_train.values, epochs=50)
    return model

def predict_lstm(model, X_test):
    return model.predict(X_test.values.reshape(-1, 4, 1))