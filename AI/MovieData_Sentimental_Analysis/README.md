Sentiment Analysis Project
Overview
This project performs sentiment analysis on movie reviews using various machine learning models. The goal is to classify reviews as positive or negative.
Project Structure
sentiment_analysis/
|---- data/
|       |---- rotten_tomatoes_movie_reviews.csv
|       |---- rotten_tomatoes_movies.csv
|---- models/
|       |---- logistic_regression.py
|       |---- decision_tree.py
|       |---- random_forest.py
|       |---- gradient_boosting.py
|       |---- svm.py
|---- utils/
|       |---- preprocessing.py
|       |---- vectorization.py
|---- main.py
|---- config.py
|---- requirements.txt
|---- README.md
Requirements
Python 3.8+
NumPy
Pandas
NLTK
Scikit-learn
TensorFlow (optional)
Installation
Clone the repository: git clone https://github.com/your-username/sentiment-analysis.git
Install requirements: pip install -r requirements.txt
Download required NLTK data: python -m nltk.downloader stopwords wordnet
Usage
Run the project: python main.py
Train and evaluate models: python main.py --train
Make predictions: python main.py --predict
Models
Logistic Regression
Decision Tree
Random Forest
Gradient Boosting
Support Vector Machine (SVM)
Datasets
Rotten Tomatoes Movie Reviews
Rotten Tomatoes Movies
License
MIT License
Contributors
Acknowledgments
Rotten Tomatoes for providing the datasets.
Please note that you should replace your-username with your actual GitHub username. Also, make sure to update the requirements and installation instructions according to your project's specific needs.

