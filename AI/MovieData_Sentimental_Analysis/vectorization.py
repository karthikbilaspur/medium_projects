from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_text(text_data):
    vectorizer = TfidfVectorizer()
    return vectorizer.fit_transform(text_data)