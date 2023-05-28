from flask import Flask
from flask import jsonify
from flask import request, send_file
from flask_pymongo import PyMongo
from flask_cors import CORS
import random 

import geojson
import shapely.wkt


app = Flask(__name__)

# Per rispondere alle chiamate cross origin

app.config["MONGO_URI"] = "mongodb+srv://jbiagioni:M7JYoNondmtLqBJk@atlascluster.wjczksx.mongodb.net/tartarughe" #Importante qui va specificato il nome del DB
mongo = PyMongo(app)
CORS(app)
tane = mongo.db.tane
#output = []
#for s in tane.find():
#    output.append({"lat": s['lat'], "lng": s['lng']})

@app.route("/all")
def all():
    return send_file('coordinate.json')


if __name__ == "__main__":
    app.run()