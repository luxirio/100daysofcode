from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def go_home():
    return render_template('index.html')

@app.route('/about')
def go_about():
    return render_template('about.html')

@app.route('/contact')
def go_contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
