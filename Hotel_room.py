from flask import Flask, Response, json
from flask import jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId


app = Flask(__name__)

try:

    app.secret_key = "secretkey"

    app.config['MONGO_URI'] = "mongodb+srv://Hotel:hotelms@hotelms.ueddl.mongodb.net/Hotel?retryWrites=true&w=majority"

    mongo = PyMongo(app)

except Exception as e:
    print(e)
    print('***************couldnot conncect to db************')


@app.route('/')
def index():
    return "HEYYYYYYYYYYYY"

@app.route('/room', methods=["GET"])
def Room():
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



@app.route('/room', methods=["POST"])
def Rooms():
    try:
        post_room={ 
                "room_no":request.form["room_no"],
                "room_type":request.form["room_type"],
                "room_status":request.form["room_status"],
                "room_rate":request.form["room_rate"]
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
    
@app.route('/room/<id>', methods=["PATCH"])
def update_room(id):
    try:
        _update = mongo.db.room.update_one(
            {"_id":ObjectId(id)},
            {"$set":{"room_no":request.form["room_no"],
            "room_type":request.form["room_type"],
            "room_status":request.form["room_status"],
            "room_rate":request.form["room_rate"]}}
        )
        return Response( response= json.dumps({"msg":"Room info updated successfully" },
                                                status=200,
                                                mimetype="application/json"
                                            )
                                               )
                                               
    except Exception as e:
        print(e)
        return Response(response= json.dumps({  "msg":"Couldnot update room info" },
                                                status=500,
                                                mimetype="application/json"
                                            )
                                                 )


@app.route('/room/<id>', methods=["DELETE"])
def delete_room(id):
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




if __name__ == '__main__':
    app.run(debug=True, port=3000)
