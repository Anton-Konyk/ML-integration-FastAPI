import joblib


model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


def predict_priority(text: str) -> str:
    x = vectorizer.transform([text])
    prediction = model.predict(x)[0]

    return prediction
