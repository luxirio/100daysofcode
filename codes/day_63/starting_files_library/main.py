from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# Instance of the app
# It still lacks the bootstrap object DON'T FORGET
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)

all_books = []
# Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}'

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html', books = all_books)

@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        new_data = {
            "title": request.form['title'],
            "author": request.form['author'],
            "rating": request.form['rating']
        }
        with app.app_context():
            new_book = Book(title=new_data['title'], author=new_data['author'], rating=new_data['rating'])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


# Update rating
def update_rating(book_id, rating):
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        book_to_update.rating = rating
        db.session.commit()

@app.route("/edit/<book_id>", methods=["GET", "POST"])
def edit(book_id):
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    
    if request.method == "GET":
        print("estou aqui")
        print(book_id)
        return render_template('edit.html', book_id=book_id, books = all_books)
    else:
        new_rating = request.args.get('rating')
        print(new_rating)
        #update_rating(book_id=book_id, rating=new_rating)
        return redirect(url_for('home'))    

if __name__ == "__main__":
    app.run(debug=True)



