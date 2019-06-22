 4






Message List

Valarmathi [10:09 PM]
Screen Shot 2019-06-18 at 10.08.11 PM.png 

i can able to populate the tickers in dropdown

Kent Williams [10:10 PM]
:+1:

Valarmathi [10:11 PM]
:blush::+1:

Ken [5:18 PM]
Hey everyone just getting a bite to eat. Will be over a little after 5:30
Great job on the drop down, value!
Valar *

Valarmathi [5:18 PM]
Thanks Ken .. I am waiting in waiting area.. nobody came as of now..

aracelymndz [5:18 PM]
On my way,
I will be there at 15 minutes

Kent Williams [5:19 PM]
On my way.

Valarmathi [6:42 PM]
incomplete flask app
app.py 
import os
​
import pandas as pd
import numpy as np
import json
from flask import Flask
from flask import Flask, request, render_template
from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
​
#################################################
# Database Setup
#################################################
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/company_db"
mongo = PyMongo(app)
​
@app.route("/")
def index():
  """Return the homepage."""
  return render_template("index.html")
​
@app.route('/ticker', methods=['GET'])
def get_all_ticker():
 company = mongo.db.company
 ticker=[]
 for testy in company.find().distinct('ticker'):
   ticker.append(testy)
 print(ticker)
 return jsonify(ticker) 
​
@app.route("/metadata/<ticker>", methods=['GET'])
def companydata(ticker):
  """Return the MetaData for a given sample."""
  # sample_metadata = {}
  company = mongo.db.company
  # tickerdata=[]
  for data in company.find({"ticker": ticker }):
    # tickerdata.append(data)
     print(data)
  return (jsonify(data))
  
# @app.route("/ticker/<ticker>", methods=['GET'])
# def samples(ticker):
#   """Return `price`, `calenderdate`,and `ticker values`."""
  
#   # Filter the data based on the ticker and
#   # only keep rows with values above 1
#   company = mongo.db.company
#   for columns in company.find({'ticker':ticker}):
     
#   # Format the data to send as json
#       data = {
#         "price": columns.price.values.tolist(),
#         "ticker": columns[ticker].values.tolist(),
#         "calendardate": columns.calendardate.tolist(),
#       }
#   print (data)
#   return jsonify(data)
​
​
if __name__ == "__main__":
  
  app.run()
Collapse

Message Input


Message aracelymndz, Valarmathi, Kent Williams