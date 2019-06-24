import os

import pandas as pd
import numpy as np
import json
from flask import Flask
from flask import Flask, request, render_template,send_from_directory
from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo

#################################################
# Database Setup
#################################################
PEOPLE_FOLDER = os.path.join('static','js')
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.config["MONGO_URI"] = "mongodb://localhost:27017/company_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    """Return the homepage."""
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'bright-chart-data-210607.jpg')
    return render_template("index.html",user_image = full_filename)

@app.route('/charts')
def route1():
    return render_template('charts.html')

@app.route('/ticker', methods=['GET'])
def get_all_ticker():
  company = mongo.db.company
  ticker=[]
  for testy in company.find().distinct('ticker'):
     ticker.append(testy)
  print(ticker)
  return jsonify(ticker) 

@app.route("/metadata/<ticker>", methods=['GET'])
def companydata(ticker):
    """Return the MetaData for a given sample."""
    # sample_metadata = {}
    company = mongo.db.company
    tickerdata=[]
    for data in company.find({"ticker": ticker}, {'_id':0}):
        tickerdata.append(data)
    print(tickerdata)
    return jsonify(results = tickerdata)
    
@app.route("/ticker/<ticker>", methods=['GET'])
def samples(ticker):
    """Return `price`, `calenderdate`,and `ticker values`."""
    
    # Filter the data based on the ticker and
    # only keep rows with values above 1
    company = mongo.db.company
    tickerdata2=[]
    for test in company.find({"ticker": ticker}, {'_id':0, "price": 1, "calendardate": 1,}):
     tickerdata2.append(test)
    
    return jsonify(tickerdata2)
    


if __name__ == "__main__":
    
    app.run()
