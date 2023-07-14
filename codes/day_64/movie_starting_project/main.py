from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, Form
from wtforms.validators import DataRequired, Length
import requests

# Instance of the app and DB
db = SQLAlchemy()
app = Flask(__name__)

# Basic config of app and DB
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db.init_app(app)
bootstrap = Bootstrap5(app) # Setting up the bootstrap object

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False, unique=True)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)

class editReview(FlaskForm):
    rating = FloatField('Edit your rating', validators=[DataRequired()])
    review = StringField('Update your review about the movie', validators=[DataRequired()])
    submit = SubmitField("Done")

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.ranking.desc())).scalars()
    return render_template("index.html", movies=all_movies)

@app.route('/edit', methods=['POST', 'GET'])
def edit():
    form = editReview()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie = movie)

if __name__ == '__main__':
    app.run(debug=True)
