from flask import Flask, render_template, url_for
import requests

blog_posts_raw = requests.get('https://api.npoint.io/d5c45435d89d793b69d2')
blog_posts_dict = blog_posts_raw.json()

app = Flask(__name__)

@app.route('/')
def go_home():
    return render_template('index.html', posts = blog_posts_dict)

@app.route('/about')
def go_about():
    return render_template('about.html')

@app.route('/contact')
def go_contact():
    return render_template('contact.html')

@app.route('/posts/<int:number>')
def go_posts(number):
    return render_template('post.html', post_id = number, posts = blog_posts_dict)

if __name__ == "__main__":
    app.run(debug=True)
