from flask import Flask

# Instantiating the object
app = Flask(__name__)

def make_bold(func):
    def wrapper():
        func()
        return '<b>' + func() + '</b>' 
    return wrapper

def make_italic(func):
    def wrapper():
        func()
        return '<em>' + func() + '</em>'
    return wrapper

# The @object.route decorator is how flask works
@app.route('/')
def hello():
    return '<h1 style="text-align: center">Hello World!</h1>'\
        '<p>This is a text</p>'\
        '<img src="https://media3.giphy.com/media/l4KibK3JwaVo0CjDO/giphy.gif?cid=ecf05e47iw5q94zpccie1qj9qx7gtq4qkbonmkfiy10mbhfx&ep=v1_gifs_search&rid=giphy.gif&ct=g" width=200>'

@app.route('/bye')
@make_bold
@make_italic
def bye():
    return 'Bye!'

@app.route('/username/<name>')
def greeting(name):
    return f'Hello {name}!'

# if we run the file directly
if __name__== '__main__':
    app.run(debug=True)
