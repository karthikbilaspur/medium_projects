# medium_projects
Here’s a single combined `README.md` with all 10 projects. You can use this as a portfolio monorepo or personal projects showcase:

---

# **Project Portfolio**
A collection of 10 full-stack, machine learning, and data projects built with Python, Flask, TensorFlow, and modern web technologies.

## **Table of Contents**
1. [Gaming Environment with Q-Learning](#1-gaming-environment-with-q-learning)
2. [Image Classification CNN](#2-image-classification-cnn)
3. [Sentiment Analysis on Movie Reviews](#3-sentiment-analysis-on-movie-reviews)
4. [Stock Price Predictor](#4-stock-price-predictor)
5. [Air Quality Index Monitoring System](#5-air-quality-index-monitoring-system)
6. [COVID-19 Vaccination Management System](#6-covid-19-vaccination-management-system)
7. [Indian Election Results Visualizer](#7-indian-election-results-visualizer)
8. [Stock Market Analysis & Portfolio Optimization](#8-stock-market-analysis--portfolio-optimization)
9. [Music Recommendation System](#9-music-recommendation-system)
10. [Video Streaming Platform](#10-video-streaming-platform)

---

## **1. Gaming Environment with Q-Learning**
**Reinforcement Learning Agent for Custom Gridworld**

A Python-based RL environment where an agent learns optimal navigation using Q-learning. Features custom rewards, obstacles, and OpenAI Gym-compatible interface.

**Tech Stack**: Python, NumPy, Matplotlib, OpenAI Gym  
**Key Features**: Q-table implementation, epsilon-greedy policy, training visualization, save/load models  
**Run**: `python train.py` in `gaming-environment/`

---

## **2. Image Classification CNN**
**Binary Classifier: Truck vs Car**

A foundational computer vision project implementing a CNN to distinguish between truck and car images. Demonstrates full ML pipeline from data loading to inference.

**Tech Stack**: TensorFlow 2.x, Keras, OpenCV, NumPy, Scikit-learn  
**Architecture**: Conv2D + MaxPooling → Flatten → Dense → Dropout → Softmax  
**Run**: `python train.py`, `python predict.py --image_path='data/truck/a_truck.jpeg'` in `image-classification/`

---

## **3. Sentiment Analysis on Movie Reviews**
**Multi-Model NLP Pipeline for Binary Classification**

Classifies Rotten Tomatoes reviews as positive/negative. Implements and benchmarks 5 classical ML models with standardized preprocessing and TF-IDF vectorization.

**Tech Stack**: Python 3.8+, Pandas, NLTK, Scikit-learn  
**Models**: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, SVM  
**Run**: `python main.py --train` in `sentiment-analysis/`

---

## **4. Stock Price Predictor**
**Time-Series Forecasting with Linear Regression & LSTM**

Predicts future stock prices using historical market data. Compares baseline Linear Regression with LSTM neural network to capture temporal dependencies.

**Tech Stack**: Python, TensorFlow/Keras, Pandas, Scikit-learn, Matplotlib  
**Metrics**: MSE, MAE, R-squared  
**Run**: `python main.py --ticker AAPL --model lstm` in `stock-price-predictor/`  
**Disclaimer**: Educational use only, not financial advice.

---

## **5. Air Quality Index Monitoring System**
**Real-Time AQI Tracking and Forecasting**

Ingests live air quality data from public APIs and IoT sensors, predicts future AQI levels using ML, and visualizes trends on an interactive Streamlit dashboard.

**Tech Stack**: Python, Streamlit, Plotly, Pandas, Prophet, SQLite  
**Data Sources**: WAQI, OpenWeather, CPCB India  
**Features**: Real-time monitoring, 24h/7d forecasts, sensor integration, alerts  
**Run**: `python aqi_dashboard.py` in `aqi-monitor/`

---

## **6. COVID-19 Vaccination Management System**
**Full-Stack Flask App for Appointment Scheduling**

Web application for scheduling, tracking, and managing COVID-19 vaccination appointments and patient records with email notifications.

**Tech Stack**: Flask, Flask-SQLAlchemy, Flask-Login, Flask-Mail, Bootstrap 5  
**Features**: Patient registration, appointment booking, vaccination records, email reminders  
**Database**: SQLite for dev, PostgreSQL for prod  
**Run**: `flask run` in `covid-vaccination-system/`

---

## **7. Indian Election Results Visualizer**
**Interactive Dashboard for Electoral Data**

Flask web app for exploring Indian election results with interactive Chart.js and D3.js visualizations. Filter by party and view candidate-wise vote shares.

**Tech Stack**: Flask, Pandas, Chart.js, D3.js, Bootstrap  
**Data Sources**: IndiaVotes, Trivedi Centre for Political Data  
**Features**: Party filtering, constituency search, hover tooltips, responsive UI  
**Run**: `python app.py` in `election-visualization/`

---

## **8. Stock Market Analysis & Portfolio Optimization**
**ML-Powered Investment Analysis Tool**

Flask application for stock data visualization and portfolio optimization using mean-variance analysis and linear regression forecasting.

**Tech Stack**: Flask, Pandas, NumPy, Scikit-learn, Chart.js  
**Features**: Price trend charts, Sharpe ratio, risk-return optimization, ML predictions  
**Data**: Local CSV files with OHLCV data  
**Run**: `python app.py` in `stock-analysis/`

---

## **9. Music Recommendation System**
**Hybrid Recommendation Engine with Spotify Integration**

Personalized music discovery platform using collaborative filtering and content-based models. Integrates with Spotify API for search, playback, and metadata.

**Tech Stack**: Flask, TensorFlow, Scikit-learn, Spotipy, SQLAlchemy  
**Models**: SVD collaborative filtering, content-based with audio features, hybrid ensemble  
**Features**: User auth, track search, 30s previews, playlist export to Spotify  
**Run**: `python app.py` in `music-recommendation/`

---

## **10. Video Streaming Platform**
**Flask Video Hosting with Custom HTML5 Player**

Simple video streaming platform with user authentication, uploads, and custom player controls. Foundation for learning video delivery.

**Tech Stack**: Flask, Flask-Login, SQLAlchemy, FFmpeg, Bootstrap  
**Features**: Secure uploads, thumbnail generation, play/pause/seek/download, search & filter  
**Storage**: Local filesystem, S3-compatible ready  
**Run**: `python app.py` in `video-streaming-platform/`

---

## **Monorepo Setup**
```
portfolio/
├── gaming-environment/
├── image-classification/
├── sentiment-analysis/
├── stock-price-predictor/
├── aqi-monitor/
├── covid-vaccination-system/
├── election-visualization/
├── stock-analysis/
├── music-recommendation/
├── video-streaming-platform/
├── .gitignore
└── README.md  # This file
```

### **Global Setup**
Each project has its own `requirements.txt` and virtual environment. To run any project:

```bash
cd project-name/
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py  # or main.py, train.py as specified
```

### **Common Dependencies**
Most projects use: `Python 3.8+`, `Flask`, `Pandas`, `NumPy`, `Scikit-learn`

### **Contributing**
1. Fork this repo
2. Create feature branch per project: `git checkout -b feat/project-name-feature`
3. Follow commit guidelines: imperative, present tense, <50 chars
4. Submit PR with clear description

### **License**
All projects licensed under MIT License unless noted otherwise in subdirectories.

### **Author**
[Vasudev Karthik]  
GitHub: [@asaudevkarthik ](https://github.com/karthikbilaspur)  
Email: karthikv81291@gmail.com


---

Want me to add GitHub topic badges, a `docker-compose.yml` for all services, or deployment instructions for each app?
