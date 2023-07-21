from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired,URL
import csv

# secret key
import secrets
key = secrets.token_urlsafe(16)

app = Flask(__name__)
app.config['SECRET_KEY'] = key
boostrap = Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Location URL', validators=[DataRequired(), URL(message="A Valid URL must be input")])
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],validators=[DataRequired()])
    wifi_rating = SelectField('Wifi strength',choices=['💻','💻💻', '💻💻💻', '💻💻💻💻', '💻💻💻💻💻'], validators=[DataRequired()])
    power = SelectField('Power availability', choices=['🔌','🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods = ["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a') as csv_file:
            csv_file.write(f"\n{form.data['cafe']},{form.data['location_url']},{form.data['open_time']}, {form.data['close_time']}, {form.data['coffee_rating']},{form.data['wifi_rating']},{form.data['power']}")
            return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True)
