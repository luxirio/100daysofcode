from flask import Flask
from random import randint

app = Flask(__name__)

# Random number
random_num = randint(0,9)

def lower():
    return '<h1 style="color: red">Too low, try again!</h1>'\
    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
def higher():
    return '<h1 style="color: purple"> Too high, try again!</h1>'\
    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
def found_number():
    return '<h1 style="color: darkgreen"> Found it!</h1>'\
    '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjA4YzIwYmU5ODFhNDM4Y2E1MTJlYThiOTgyZGU4OGUxZTA5YTI1NCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/4T7e4DmcrP9du/giphy.gif">'

def check_number_decorator(func):
    def wrapper(**kw):
        if kw['number'] < random_num:
            return lower()
        elif kw['number'] > random_num:
            return higher()
        else:
            return found_number()
    return wrapper

@app.route('/')
def welcome():
    return '<h1>Guess the number between 0 and 9</h1>'\
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:number>')
@check_number_decorator
def high_or_low(number):
    return None

if __name__ == "__main__":
    app.run(debug=True)