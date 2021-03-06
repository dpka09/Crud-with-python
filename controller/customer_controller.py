from flask import jsonify, request, Response
from flask_cors import CORS
from flask_expects_json import expects_json

from bson.json_util import dumps
from bson.objectid import ObjectId

from datetime import datetime
from flask_restful import Resource, abort

from app_config import mongo
from schema.customer_schema import customer_schema


class CustomersApi(Resource):

    def get(self):
        customers = list(mongo.db.customer.find())
        resp = Response(dumps(customers), mimetype='application/json', status=200)
        return resp

    @expects_json(customer_schema)
    def post(self):
        _json = request.json
        _customer_name = _json["customer_name"]
        _age = _json["age"]
        _phone = _json["phone"]
        _address = _json["address"]
        _room_id = _json["booking_info"]["room_id"]
        _check_in = _json["booking_info"]["check_in"]
        _check_in = datetime.strptime(_check_in, "%Y-%m-%d %H:%M:%S")
        _check_out = _json["booking_info"]["check_out"]
        _check_out = datetime.strptime(_check_out, "%Y-%m-%d %H:%M:%S")
        # _total_cost = _json["booking_info"]["total_cost"]
        _payment_method = _json["booking_info"]["payment_method"]


        if(not ObjectId.is_valid(_room_id)):
            return Response(dumps({"message": "Invalid room_id"}), 400)

        _room_id = ObjectId(_room_id)
        room = mongo.db.room.find_one({"_id": _room_id})
        if (room is None):
            abort(404, description="Room Not found")


        # days = mongo.db.room.aggregate([{"$project": {"_id": _room_id, "no_of_days": {"$trunc": {"$divide": [{ "$subtract": [_check_out, _check_in] }, 1000 * 60 * 60 * 24]}}}}]);
        days = (_check_out - _check_in).days
        price = mongo.db.room.aggregate([{"$match":{'_id': _room_id}},
                                        {"$project": {"totalAmount": { "$multiply": ["$room_rate", days ] } }}
                                        ])
        price = [p["totalAmount"] for p in price]
        _total_cost = price[0]


        if _customer_name and _age and _phone and _address and _room_id and _check_in and _check_out and _total_cost and _payment_method and request.method == 'POST':

            id = mongo.db.customer.insert({'customer_name': _customer_name, 'age': _age,
                    'phone': _phone, 'address': _address, 'booking_info': 
                    {'room_id': _room_id, 'check_in': _check_in, 'check_out': _check_out,
                    'total_cost': _total_cost, 'payment_method': _payment_method}})

            resp = jsonify("Customer added successfully")
            resp.status_code = 200

            return resp

        else:
            return not_found()


class CustomerApi(Resource):
    def get(self, id):
        customer = mongo.db.customer.find_one({'_id': ObjectId(id)})
        resp = Response(dumps(customer), mimetype='application/json', status=200)
        return resp

    @expects_json(customer_schema)
    def put(self, id):
        _id = id
        _json = request.json
        _customer_name = _json["customer_name"]
        _age = _json["age"]
        _phone = _json["phone"]
        _address = _json["address"]
        _room_id = _json["booking_info"]["room_id"]
        _check_in = _json["booking_info"]["check_in"]
        _check_in = datetime.strptime(_check_in, "%Y-%m-%d %H:%M:%S")
        _check_out = _json["booking_info"]["check_out"]
        _check_out = datetime.strptime(_check_out, "%Y-%m-%d %H:%M:%S")
        # _total_cost = _json["booking_info"]["total_cost"]
        _payment_method = _json["booking_info"]["payment_method"]


        if(not ObjectId.is_valid(_room_id)):
            return Response(dumps({"message": "Invalid room_id"}), 400)

        _room_id = ObjectId(_room_id)
        room = mongo.db.room.find_one({"_id": _room_id})
        if (room is None):
            abort(404, description="Room Not found")


        days = (_check_out - _check_in).days
        price = mongo.db.room.aggregate([{"$match":{'_id': _room_id}},
                                        {"$project": {"totalAmount": { "$multiply": ["$room_rate", days ] } }}
                                        ])
        price = [p["totalAmount"] for p in price]
        _total_cost = price[0]

        if _customer_name and _age and _phone and _address and _room_id and _check_in and _check_out and _total_cost and _payment_method and request.method == 'PUT':
            
            mongo.db.customer.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
                    {'$set': {'customer_name': _customer_name, 'age': _age,
                    'phone': _phone, 'address': _address, 'booking_info': 
                    {'room_id': _room_id, 'check_in': _check_in, 'check_out': _check_out,
                    'total_cost': _total_cost, 'payment_method': _payment_method}}})

            resp = jsonify("Customer updated successfully")
            resp.status_code = 200
            return resp
        
        else:
            return not_found()    


    def delete(self, id):
        mongo.db.customer.delete_one({'_id': ObjectId(id)})
        resp = jsonify("Customer deleted successfully")
        resp.status_code = 200
        return resp


def not_found(error=None):
        message = {
            'status': 404,
            'message': 'Not found' + request.url
        }
        resp = jsonify(message)
        resp.status_code = 404

        return resp


