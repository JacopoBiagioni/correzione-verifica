from flask import Flask
from flask import jsonify
from flask import request, send_file
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)

# Per rispondere alle chiamate cross origin
CORS(app)
app.config["MONGO_URI"] = "mongodb+srv://jbiagioni:M7JYoNondmtLqBJk@atlascluster.wjczksx.mongodb.net/" #Importante qui va specificato il nome del DB

mongo = PyMongo(app)

# Annotation that allows the function to be hit at the specific URL.
@app.route("/all")
# Generic Python functino that returns "Hello world!"
def all():
    return send_file('coordinate.json')

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()