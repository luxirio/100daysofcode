from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
# It has to have a app secret key if we want to work with flask_wtf
app.secret_key = "any-string-you-want-just-keep-it-secret"

# Instance of the Bootstrapp to embelish
bootstrap = Bootstrap4(app)

# Instance of the WTF form
class loginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), validators.Length(min=6, message='A minimum of 8 characters is necessary')])
    submit = SubmitField(label='Login')

@app.route("/")
def home():
    return render_template('index.html')

# Both methods, POST and GET have to be instantiated
@app.route('/login', methods=["POST", "GET"])
def login():
    login_form = loginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "a@gmail.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else: return render_template('denied.html')
    else: 
        return render_template('login.html', form = login_form)

if __name__ == '__main__':
    app.run(debug=True)