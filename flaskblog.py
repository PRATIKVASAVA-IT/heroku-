# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 20:38:34 2020

@author: ADMIN
"""

import numpy as np
import pickle
from flask import Flask,request,jsonify,render_template

app=Flask(__name__)
model=pickle.load(open('model2.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Predict',methods=['POST'])
def Predict():
    int_feature=[float(x) for x in request.form.values()]
    x=int_feature[0]
    #y=request.form.values('income')
    final_result=[np.array(int_feature)]
    Prediction=model.predict(final_result)
    #Prediction=model.predict(x,y)
    output=np.round(Prediction[0],2)
    output=str(output)
    return render_template('index.html',Prediction_tax='petrol consumption Should be ${} Ltr.'.format(output),tax='currunt tax applied {} % '.format(x))
    #return render_template('index.html',)

if __name__=="__main__":
    app.run(debug=True)
