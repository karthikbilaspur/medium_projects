from sklearn.ensemble import GradientBoostingClassifier

class GradientBoostingModel:
    def __init__(self):
        self.model = GradientBoostingClassifier(n_estimators=100)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)