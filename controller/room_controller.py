from flask import json, request, Response
from flask_cors import CORS

from bson.json_util import dumps
from bson.objectid import ObjectId

from flask_restful import Resource
from app_config import mongo

class RoomsApi(Resource):

    def get(self):
        try:
            get_room=list(mongo.db.room.find())
        
            for information in get_room:
                information["_id"]= str(information["_id"])
            return Response( 
                response = json.dumps(get_room),
                status=200,
                mimetype="application/json"
            )
            
        except Exception as e:
            print (e)
            return Response( response= json.dumps({ "msg":"couldnot retrieve user info"}),
            status=500,
            mimetype="application/json"
            )


    def post(self):
        try:
            post_room={ 
                    "room_no":request.form["room_no"],
                    "room_type":request.form["room_type"],
                    "room_status":request.form["room_status"],
                    "room_rate":float(request.form["room_rate"])
                }
            _post= mongo.db.room.insert_one(post_room)

            return Response(
                    response = json.dumps({ "msg":"room info created"}),
                    status=200,
                    mimetype="application/json"

                                )
        except Exception as ex:
            print(ex)
            return Response( response= json.dumps({ "msg":"Didnot create room info"}),
            status=500,
            mimetype="application/json"
            )
        
class RoomApi(Resource):

    def patch(self, id):
        try:
            _update = mongo.db.room.update_one(
                {"_id":ObjectId(id)},
                {"$set":{"room_no":request.form["room_no"],
                "room_type":request.form["room_type"],
                "room_status":request.form["room_status"],
                "room_rate":float(request.form["room_rate"])}}
            )
            return Response( response= json.dumps({"msg":"Room info updated successfully" }),
                                                    status=200,
                                                    mimetype="application/json"
                                                )
                                                
        except Exception as e:
            print(e)
            return Response(response= json.dumps({  "msg":"Couldnot update room info" }),
                                                    status=500,
                                                    mimetype="application/json"
                                                    )


    def delete(self, id):
        try:
            _delete= mongo.db.room.delete_one({ "_id": ObjectId(id) })

            return Response( 
                response = json.dumps({"msg": "Room info has been deleted"}),
                status=200,
                mimetype="application/json"
            )

        except Exception as e:
            print (e)

            return Response( 
                response = json.dumps({"msg": "Room info didnot get deleted"}),
                status=500,
                mimetype="application/json"
            )