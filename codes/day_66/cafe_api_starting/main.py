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

## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
    name=request.args.get('name'), 
    map_url=request.args.get('map_url'), 
    img_url=request.args.get('img_url'), 
    location=request.args.get('location'),
    seats=request.args.get('seats'),
    has_sockets=bool(request.args.get('has_sockets')),
    has_toilet=bool(request.args.get('has_toilet')),
    has_wifi=bool(request.args.get('has_wifi')),
    can_take_calls=bool(request.args.get('can_take_calls')),
    coffee_price=request.args.get('coffee_price'),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"sucess": "Successfully added the new cafe"})

## HTTP PUT/PATCH - Update Record
@app.route("/update-patch/<cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    cafe_to_update = db.get_or_404(Cafe, cafe_id)
    new_price = request.args.get('new_price')
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response=
                       {"success": 
                        "Successfully updated the price"}), 200
    else:
        return jsonify(response={
            "error":
            "Not found the cafe!"}), 404
## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = "secret_key"
    
    if request.args.get('api-key') == api_key:
        cafe_to_delete = db.get_or_404(Cafe, cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={
                "Success": "Cafe successfully deleted from the database"
            })
        else:
            return jsonify(response={
                "Error":"ID not found on the database"
            })
    else:
        return jsonify(response={
            "error": "Not authorized. Make sure to provide the correct API key as an argument (apk-key)"
        })
    
if __name__ == '__main__':
    app.run(debug=True)
