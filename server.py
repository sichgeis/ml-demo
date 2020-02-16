from flask import Flask, request
from joblib import load

vectorizer = load('fitted_vectorizer.joblib')
clf = load('fitted_model.joblib')

app = Flask(__name__, static_folder="./build", static_url_path='')

@app.route('/', methods=['POST'])
def index():
    return str(clf.predict(vectorizer.transform([request.json.get('phrase')]))[0])
