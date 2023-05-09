# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:34:38 2023

@author: Sumit
"""
# Importing necessary libraries.
import uvicorn
from fastapi import FastAPI

# Creating the app object
app=FastAPI()

# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'messsage':'Hello, World'}

# get_name route with single parameter, returns the parameter 
# within a message located at 
# http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name:str):
    return {'Wass up! ':f'{name}'}

# Run the api with uvicorn
if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
    