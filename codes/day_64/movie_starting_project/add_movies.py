# # Snippet to add some movies into the database the first time it is instanciateD

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()
import requests

url = "https://api.themoviedb.org/3/search/movie?query="
movie_title = "Matrix"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNGMyODUwMGMzMjUwMzc1M2I2ODhhZDk5M2YwOGM1MCIsInN1YiI6IjY0YjFhOGMzMjNkMjc4MDE0NTgzZmExZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.H2ItwhmHR7tZUoihVI_wW6GIhoHbtIETsszihh4v6gY"
}

response = requests.get(f"{url}{movie_title}", headers=headers)

[print(x,'\n') for x in response.json()['results']]