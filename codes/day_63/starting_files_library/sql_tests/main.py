from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)

# Command to create the table
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, \
#                title varchar (250) NOT NULL UNIQUE, \
#                author varchar(250) NOT NULL, \
#                rating FLOAT NOT NULL)")

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique = True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}'
    
with app.app_context():
    db.create_all()

# ADD
with app.app_context():
    new_book = Book(title='sdfs', author='Esmo', rating=5.0)
    db.session.add(new_book)
    db.session.commit()

# Read all records
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    

# Update
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Alo")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()