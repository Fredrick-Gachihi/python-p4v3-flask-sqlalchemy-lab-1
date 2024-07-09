# app.py
from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    
    quakes_list = []
    for quake in earthquakes:
        quake_data = {
            'id': quake.id,
            'location': quake.location,
            'magnitude': quake.magnitude,
            'year': quake.year
        }
        quakes_list.append(quake_data)
    
    response = {
        'count': len(quakes_list),
        'quakes': quakes_list
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
