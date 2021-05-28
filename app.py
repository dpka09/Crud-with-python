from flask import Flask
from flask import jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS


app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb+srv://Hotel:hotelms@hotelms.ueddl.mongodb.net/Hotel?retryWrites=true&w=majority"

mongo = PyMongo(app)

if __name__ == '__main__':
    app.run(debug=True)
