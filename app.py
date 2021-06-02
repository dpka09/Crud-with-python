from app_config import app_config

from flask import Flask
from flask_restful import Api

from routes.customer_route import customer_routes
from routes.room_route import room_routes
from routes.extra_route import extra_routes

from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = os.getenv('MONGO_URI')

app_config(app)

api = Api(app)


customer_routes(api)
room_routes(api)
extra_routes(api)


if __name__ == '__main__':
    app.run(debug=True)
