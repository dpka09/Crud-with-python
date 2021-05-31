from flask import Flask
from flask import jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS

from bson.json_util import dumps
from bson.objectid import ObjectId

from datetime import datetime


app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb+srv://Hotel:hotelms@hotelms.ueddl.mongodb.net/Hotel?retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route('/room/<id>/<days>')
def get_price_of_stay(id, days):
    price = mongo.db.room.aggregate([{"$match":{'_id': ObjectId(id)}},
                                     {"$project": {"totalAmount": { "$sum": { "$multiply": ["$room_rate", int(days) ] } }}}
                                    ])
    resp = dumps(price)
    return resp


if __name__ == '__main__':
    app.run(debug=True)


