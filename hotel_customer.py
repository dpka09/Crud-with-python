from flask import Flask
from flask import jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS

from bson.json_util import dumps
from bson.objectid import ObjectId


app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb+srv://Hotel:hotelms@hotelms.ueddl.mongodb.net/Hotel?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/customers')
def get_customers():
    customers = mongo.db.customer.find()
    resp = dumps(customers)
    return resp

@app.route('/customer/add', methods=['POST'])
def add_customer():
    _json = request.json
    _customer_name = _json["customer_name"]
    _age = _json["age"]
    _phone = _json["phone"]
    _address = _json["address"]
    _room_no = _json["booking_info"]["room_no"]
    _check_in = _json["booking_info"]["check_in"]
    _check_out = _json["booking_info"]["check_out"]
    _total_cost = _json["booking_info"]["total_cost"]
    _payment_method = _json["booking_info"]["payment_method"]

    if _customer_name and _age and _phone and _address and _room_no and _check_in and _check_out and _total_cost and _payment_method and request.method == 'POST':

        id = mongo.db.customer.insert({'customer_name': _customer_name, 'age': _age,
                'phone': _phone, 'address': _address, 'booking_info': 
                {'room_no': _room_no, 'check_in': _check_in, 'check_out': _check_out,
                'total_cost': _total_cost, 'payment_method': _payment_method}})

        resp = jsonify("Customer added successfully")
        resp.status_code = 200

        return resp

    else:
        return not_found()

@app.route('/customer/<id>')
def get_customer(id):
    customer = mongo.db.customer.find_one({'_id': ObjectId(id)})
    resp = dumps(customer)
    return resp

@app.route('/customer/update/<id>', methods=['PUT'])
def update_customer(id):
    _id = id
    _json = request.json
    _customer_name = _json["customer_name"]
    _age = _json["age"]
    _phone = _json["phone"]
    _address = _json["address"]
    _room_no = _json["booking_info"]["room_no"]
    _check_in = _json["booking_info"]["check_in"]
    _check_out = _json["booking_info"]["check_out"]
    _total_cost = _json["booking_info"]["total_cost"]
    _payment_method = _json["booking_info"]["payment_method"]

    if _customer_name and _age and _phone and _address and _room_no and _check_in and _check_out and _total_cost and _payment_method and request.method == 'PUT':
        
        mongo.db.customer.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
                {'$set': {'customer_name': _customer_name, 'age': _age,
                'phone': _phone, 'address': _address, 'booking_info': 
                {'room_no': _room_no, 'check_in': _check_in, 'check_out': _check_out,
                'total_cost': _total_cost, 'payment_method': _payment_method}}})

        resp = jsonify("Customer updated successfully")
        resp.status_code = 200
        return resp
    
    else:
        return not_found()    

@app.route('/customer/delete/<id>', methods=['DELETE'])
def delete_customer(id):
    mongo.db.customer.delete_one({'_id': ObjectId(id)})
    resp = jsonify("Customer deleted successfully")
    resp.status_code = 200
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not found' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == '__main__':
    app.run(debug=True)
