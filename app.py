import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=176ad949708eb8a0fb99205631a952c6'
    city = 'Amravati'
    r = requests.get(url.format(city)).json()
    print(r)

    weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

    return render_template('weather.html', weather_data=weather)

if __name__ == '__main__':
	app.run(debug=True)