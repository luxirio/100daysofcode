from flask import Flask, render_template
import datetime
import requests

# Endpoints
AGE_ENDPOINT = "https://api.agify.io?name="
GENDER_ENDPOINT = "https://api.genderize.io?name="

# Time for the footer
NOW = datetime.datetime.now()
CURRENT_YEAR = NOW.strftime("%Y")

# Instantiating the page
app = Flask(__name__)

@app.route('/<name>')
def home(name):
    # API Fetch
    age_response = requests.get(AGE_ENDPOINT+str(name))
    gender_response = requests.get(GENDER_ENDPOINT+str(name))
    age = age_response.json()['age']
    gender = gender_response.json()['gender']

    return render_template("index.html", year= CURRENT_YEAR, name=name, age=age, gender=gender)


@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/c7fecc37a5a8ef85eae7"
    all_posts = requests.get(blog_url).json()
    return render_template("blog.html", posts = all_posts)

if __name__ == "__main__":
    app.run(debug=True)