import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/company_db.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
company = Base.classes.company
ticker = Base.classes.ticker


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(ticker).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


@app.route("/metadata/<sample>")
def company(sample):
    """Return the MetaData for a given sample."""
    sel = [
        company.,
        company.ticker,
        company.calendardate,
        company.assetturnover,
        company.currentratio,
        company.de,
        company.epsusd,
        company.grossmargin,
        company.netmargin,
        company.pe,
        company.price
    ]

    results = db.session.query(*sel).filter(company.sample == sample).all()

    # Create a dictionary entry for each row of metadata information
    company = {}
    for result in results:
        company["sample"] = result[0]
        company["ETHNICITY"] = result[1]
        company["GENDER"] = result[2]
        company["AGE"] = result[3]
        company["LOCATION"] = result[4]
        company["BBTYPE"] = result[5]
        company["WFREQ"] = result[6]

    print(company)
    return jsonify(company)


@app.route("/ticker/<sample>")
def ticker(sample):
    """Return `otu_ids`, `otu_labels`,and `sample_values`."""
    stmt = db.session.query(ticker).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Filter the data based on the sample number and
    # only keep rows with values above 1
    sample_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]
    # Format the data to send as json
    data = {
        "otu_ids": sample_data.otu_id.values.tolist(),
        "sample_values": sample_data[sample].values.tolist(),
        "otu_labels": sample_data.otu_label.tolist(),
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()
