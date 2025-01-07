import pandas as pd
from models.logistic_regression import LogisticRegressionModel
from models.decision_tree import DecisionTreeModel
from models.random_forest import RandomForestModel
from models.gradient_boosting import GradientBoostingModel
from models.svm import SVMModel
from utils.preprocessing import preprocess_text
from utils.vectorization import vectorize_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def load_datasets():
    reviews_df = pd.read_csv('data/rotten_tomatoes_movie_reviews.csv')
    movies_df = pd.read_csv('data/rotten_tomatoes_movies.csv')
    return reviews_df, movies_df

def merge_datasets(reviews_df, movies_df):
    merged_df = pd.merge(reviews_df, movies_df, on='movie_id')
    return merged_df

def main():
    reviews_df, movies_df = load_datasets()
    merged_df = merge_datasets(reviews_df, movies_df)

    # Preprocess text data
    merged_df['text'] = merged_df['text'].apply(preprocess_text)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(merged_df['text'], merged_df['label'], test_size=0.2, random_state=42)

    # Vectorize text data
    X_train_tf = vectorize_text(X_train)
    X_test_tf = vectorize_text(X_test)

    # Initialize models
    models = [
        LogisticRegressionModel(),
        DecisionTreeModel(),
        RandomForestModel(),
        GradientBoostingModel(),
        SVMModel()
    ]

    # Train and evaluate models
    for model in models:
        model.fit(X_train_tf, y_train)
        y_pred = model.predict(X_test_tf)
        print(f"{model.__class__.__name__} Accuracy: {accuracy_score(y_test, y_pred)}")
        print(f"{model.__class__.__name__} Classification Report:\n{classification_report(y_test, y_pred)}")
        print(f"{model.__class__.__name__} Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")

if __name__ == '__main__':
    main()