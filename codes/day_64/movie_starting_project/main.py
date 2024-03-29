from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
import requests

QUERY_ENDPOINT = "https://api.themoviedb.org/3/search/movie?query="
INFO_ENDPOINT = "https://api.themoviedb.org/3/movie/"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNGMyODUwMGMzMjUwMzc1M2I2ODhhZDk5M2YwOGM1MCIsInN1YiI6IjY0YjFhOGMzMjNkMjc4MDE0NTgzZmExZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.H2ItwhmHR7tZUoihVI_wW6GIhoHbtIETsszihh4v6gY"
}

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
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=False)

class editReview(FlaskForm):
    rating = FloatField('Edit your rating', validators=[DataRequired()])
    review = StringField('Update your review about the movie', validators=[DataRequired()])
    submit = SubmitField("Done")

class addMovie(FlaskForm):
    title = StringField('Write the movie title to be added to the list', validators=[DataRequired()])
    submit = SubmitField("Add Movie")

with app.app_context():
    db.create_all()

# ADD HERE MOVIES THE FIRST TIME THE CODE IS RUN

@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = i+1
    db.session.commit()
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

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = addMovie()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(f"{QUERY_ENDPOINT}{movie_title}", headers=headers)
        movies = response.json()['results']
        return render_template('select.html', movie_list=movies)
    return render_template('add.html', form=form)

@app.route('/select', methods=['GET', 'POST'])
def select():
    return render_template('select.html')

@app.route('/fetch', methods=['GET', 'POST'])
def fetch():
    movie_id = request.args.get('movie_id')
    info_response = requests.get(f"{INFO_ENDPOINT}{movie_id}", headers=headers).json()
    movie_poster_path = info_response['poster_path']

    # Adding the movie to the database
    new_movie = Movie(
        title=info_response['title'],
        year=info_response['release_date'].split('-')[0],
        description=info_response['overview'],
        img_url=f"https://www.themoviedb.org/t/p/w600_and_h900_bestv2/{movie_poster_path}",
    )
    db.session.add(new_movie)
    db.session.commit()
    print('This is the new recently added movie id:',new_movie.id)
    return redirect(url_for('edit', id= new_movie.id))
    

if __name__ == '__main__':
    app.run(debug=True)
