import pickle

import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open('C:\\Users\\MON PC\\Desktop\\qfm s3\\labs\\Nteflix stock price prediction - flask\\model.pkl', 'rb'))
#model = joblib.load('/path/to/svm-model-1.pkl')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    '''
    pour l'affichage sur html
    '''

    features = request.form.to_dict()
    features = list(features.values())
    features = list(map(int, features))
    final_features = np.array(features).reshape(1,4)
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='the price of the netflix stock is : $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)