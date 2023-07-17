from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/random", methods=["GET"])
def get_random_cafe():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = choice(all_cafes)
    return jsonify(random_cafe.to_dict())
     
## HTTP GET - Read Record
@app.route("/all", methods=["GET"])
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

## HTTP POST - Create Record
@app.route("/search", methods=["GET"])
def search_loc():
    location = request.args.get('loc').title()
    cafes = db.session.query(Cafe).filter_by(location=location).all()
    if cafes:
        return jsonify(search=[cafe.to_dict() for cafe in cafes])
    else:
        error_msg = {
            "error":"Not found: Sorry, we don't have a cafe at that location"
        }
        return error_msg

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record

if __name__ == '__main__':
    app.run(debug=True)
