from flask import Flask
from flask import send_file
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_cors import CORS
import random

import geojson
import shapely.wkt

# pip install Flask-PyMongo
# pip install Flask
# pip install dnspython
# npm install -g --force nodemon
# pip install flask-cors
# pip install geojson
# pip install shapely
# pip install jsonify
# npm i -g nodemon
# pip install random

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://jbiagioni:M7JYoNondmtLqBJk@atlascluster.wjczksx.mongodb.net/pokemon" #Importante qui va specificato il nome del DB
mongo = PyMongo(app)
CORS(app)
tane = mongo.db.tane # crea una variabile collegata al mongo db

@app.route("/all")
def all():
    return send_file('coordinate.json')

if __name__ == "__main__":
    app.run()