# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:12:48 2023

@author: hemang
"""
from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import cv2
import matplotlib.pyplot as plt
import numpy as np
# flask
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
# tensoprflow
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.models import load_model





app = Flask(__name__)

model = load_model("objmodel.h5")#importing the pre-trained model.

def model_predict(img_path, model):
    classes = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.astype(np.float32) / 255.0
    image = cv2.resize(image, (32, 32))
    image = image.reshape((32, 32, 3))
    # Make predictions
    predictions = model.predict(np.expand_dims(image, axis=0))
    class_index = np.argmax(predictions)
    class_name = classes[class_index]
    return class_name

@app.route("/", methods=['GET'])
def home():
  # Main page
  return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def upload():
  if request.method == 'POST':
    # Get the file from post request
    img = request.files['file']
    # Save the file to ./uploads
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(basepath, 'uploads', secure_filename(img.filename))
    img.save(file_path)
    
    # Making predictions
    final_pred = model_predict(file_path, model)
    return final_pred
  return None

app.run(debug=True)