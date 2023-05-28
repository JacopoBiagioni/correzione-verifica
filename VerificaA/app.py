from flask import Flask
from flask import jsonify
from flask import request, send_file
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

# Per rispondere alle chiamate cross origin

app.config["MONGO_URI"] = "mongodb+srv://jbiagioni:M7JYoNondmtLqBJk@atlascluster.wjczksx.mongodb.net/tartarughe" #Importante qui va specificato il nome del DB
mongo = PyMongo(app)
CORS(app)
tartarughe = mongo.db.ninja
output = []
for s in tartarughe.find():
    output.append({"lat": s['lat'], "lng": s['lng']})

@app.route("/all")
def all():
    return (output)

@app.route("/raffaello")
def raffaello():
    return (output[random.randrange(0, len(output))])

@app.route("/donatello")
def donatello():
    return (output[random.randrange(0, len(output))])

@app.route("/michelangelo")
def michelangelo():
    return (output[random.randrange(0, len(output))])

@app.route("/leonardo")
def leonardo():
    return (output[random.randrange(0, len(output))])


if __name__ == "__main__":
    app.run()