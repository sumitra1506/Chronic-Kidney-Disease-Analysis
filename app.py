# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:47:00 2020

@author: Dipti Agrawal
"""
import numpy as np
from flask import Flask, request, jsonify, render_template

from joblib import load
app = Flask(__name__)
model = load(open('randomforest1.save', 'rb'))


@app.route('/')
def home(name=None):
    return render_template('index.html',name=name)



@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[(x) for x in request.form.values()]]
    prediction=model.predict(x_test)
    print(prediction)
    if prediction[0]==0:
        output="Chronic Kidney Disease"
    else:
        output="Not Chronic Kidney Disease"
    
    return render_template('index.html', prediction_text='Prediction: {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)

