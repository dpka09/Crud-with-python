from flask_pymongo import PyMongo

mongo = PyMongo()

def app_config(app):
    mongo.init_app(app)