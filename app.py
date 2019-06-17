# import necessary libraries
from sqlalchemy import func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# @TODO: Setup your database here
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/pets.sqlite"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')

db = SQLAlchemy(app)
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64))
    calendardate = db.Column(db.String(64))
    age = db.Column(db.)

    def __repr__(self):
        return '<Pet %r>' % (self.name)

@app.route("/")
def home():
    return render_template("index.html")


# @TODO: Create a route "/send" that handles both GET and POST requests
# If the request method is POST, save the form data to the database
# Otherwise, return "form.html"

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        name = request.form["petName"]
        pettype = request.form["petType"]
        petage = request.form["petAge"]
        print(name)
        pet = Pet(name=name, type=pettype, age=petage)
        db.session.add(pet)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")

# @TODO: Create an API route "/api/pals" to return data to plot
@app.route("/api/pals")
def pals():
    results = db.session.query(Pet.name, Pet.type, Pet.age).all()

    hover_text = [result[0] for result in results]
    pettype = [result[1] for result in results]
    petage = [result[2] for result in results]

    pet_data = [{
        "type": pettype,
        "age":petage,
        "text": hover_text,
        "hoverinfo": "text",
        "marker": {
            "size": 50,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(pet_data)

   

   

    

if __name__ == "__main__":
    app.run()

