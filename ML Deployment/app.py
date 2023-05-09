# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:44:03 2023

@author: Sumit
"""


import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pic_in = open("model.pkl","rb")
clf=pickle.load(pic_in)

@app.get('/')
def index():
    return {'message': 'Wasssssup, World'}


@app.get('/{name}')
def get_name(name: str):
    return {'Hi': f'{name}'}

@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = clf.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

