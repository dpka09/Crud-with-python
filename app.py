from werkzeug.utils import send_from_directory
from app_config import app_config

from flask import Flask
from flask_restful import Api

from routes.customer_route import customer_routes
from routes.room_route import room_routes
from routes.extra_route import extra_routes

from flask_swagger_ui import get_swaggerui_blueprint

from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = os.getenv('MONGO_URI')

app_config(app)

api = Api(app)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Hotel Management System"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

customer_routes(api)
room_routes(api)
extra_routes(api)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
