from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def go_home():
    return render_template('index.html')


@app.route('/login', methods=["POST"])
def go_login():
    return f"<h1>Name: {request.form['fname']} password:{request.form['pwd']}</h1>"

if __name__ == "__main__":
    app.run(debug=True)