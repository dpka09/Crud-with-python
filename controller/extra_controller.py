from flask import json, request, Response
from flask_cors import CORS

from bson.json_util import dumps
from bson.objectid import ObjectId

from flask_restful import Resource
from app_config import mongo


class AvailableRoomsApi(Resource):

    def get(self):
        search= list(mongo.db.room.find({"room_status": "vacant"}))

        for information in search:
            information["_id"]= str(information["_id"])
        return Response( 
            response = json.dumps(search),
            status=200,
            mimetype="application/json"
                                )

class CustomerDetailApi(Resource):
    
    def get(self, id):
        customers= mongo.db.customer.aggregate([{"$match":{'_id': ObjectId(id)}}, {"$lookup":{ "from" :"room", "localField": "booking_info.room_id","foreignField":"_id","as":"details" }}])

        # for attributes in customers:
        #     attributes["_id"] = str(attributes["_id"])

        return Response(
        response =dumps(customers),
        status=200,
        mimetype="application/json" )


class StayPriceApi(Resource):
    def get(self, id, days):
        price = mongo.db.room.aggregate([{"$match":{'_id': ObjectId(id)}},
                                        {"$project": {"totalAmount": { "$multiply": ["$room_rate", int(days) ] } }}
                                        ])
        # price = [p["totalAmount"] for p in price]
        # price = price[0]
        resp = Response(dumps(price), mimetype="application/json", status=200)
        return resp