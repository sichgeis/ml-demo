from flask import Flask, request
from joblib import load

# vectorizer = load('fitted_vectorizer.joblib')
# clf = load('fitted_model.joblib')

app = Flask(__name__, static_folder="./dist/client", static_url_path='')

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

# @app.route('/api/veggie/predict', methods=['POST'])
# def predict_veggi():
#     return str(clf.predict(vectorizer.transform([request.json.get('phrase')]))[0])
