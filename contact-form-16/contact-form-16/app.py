#Import libraries
from flask import Flask, request, render_template
from datetime import datetime
from dateutil.relativedelta import relativedelta

import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

import os

app = Flask(__name__)

# route
@app.route('/')
def home():
    # print(os.listdir("./"))
    return render_template('./contact-form-16/contact-form-16/index.html')


def get_model():
    '''
    Loading model for the server-side
    '''
    # model = load_model('./Trained Model/881.h5')
    # return model


@app.route('/predict', methods=['POST'])
def predict():
    '''
    A view for rendering results on HTML GUI with the prediction
    '''
    return render_template('./contact-form-16/contact-form-16/index.html')
 
def preprocess_data(inputs):
    '''
    Takes the input generator of html elements,
    Converts the data into 3 groups,
    pass the dataframe back to predict fucntion 
    '''
    # convert generator to list
    inputs = list(inputs)

    go

    return array



if __name__ == "__main__":
    app.run(debug=True) #debug=True means you won't have to run the server again & again, it'll update directly for you
