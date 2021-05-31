from flask import Flask, Response, json
from flask import jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId
from bson.json_util import dumps


app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb+srv://Hotel:hotelms@hotelms.ueddl.mongodb.net/Hotel?retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route('/room/available', methods=["GET"])
def available_room():
    
    search= list(mongo.db.room.find({"room_status": "vacant"}))

    for information in search:
        information["_id"]= str(information["_id"])
    return Response( 
        response = json.dumps(search),
        status=200,
        mimetype="application/json"
                             )


@app.route('/customer/<id>', methods=["GET"])
def customer(id):
    

    customers= list(mongo.db.customer.aggregate([{"$match":{'_id': ObjectId(id)}}, {"$lookup":{ "from" :"room", "localField": "booking_info.room_id","foreignField":"_id","as":"details" }}]))
    print(id)

    for attributes in customers:
        attributes["_id"] = str(attributes["_id"])

        return Response(
        response =json.dumps(str(customers)),
        status=200,
        mimetype="application/json" )




if __name__=="__main__":
    app.run(debug=True)


