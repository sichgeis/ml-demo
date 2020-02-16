import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB

recipies = pd.read_csv('tensorflow-jupyterlab/work/RAW_recipes.csv')
recipies['isVegi'] = (recipies['tags'].str.find('vegetarian') > -1)
recipies = recipies[['name', 'steps', 'isVegi']]
recipies['steps'] = recipies["steps"].str \
    .replace(r'([\[\]\'\"])', '', regex=True) \
    .replace('  ', ' ', regex=False)

pd.set_option("display.max_colwidth", -1)


vectorizer = CountVectorizer()

X = vectorizer.fit_transform(recipies['steps'])
y = recipies['isVegi']

#clf = MultinomialNB(alpha=.01).fit(X,y)
clf = BernoulliNB(alpha=.01).fit(X[:-1000],y[:-1000])

# flask server
from flask import Flask, request

app = Flask(__name__, static_folder="./build", static_url_path='')

@app.route('/', methods=['POST'])
def index():
    return str(clf.predict(vectorizer.transform([request.json.get('phrase')]))[0])

@app.route('/api/isvegi', methods=['POST'])
def isvegi():
    return 'banana'
