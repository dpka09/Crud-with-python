from controller.room_controller import RoomApi, RoomsApi

def room_routes(api):
    api.add_resource(RoomsApi, '/rooms')
    api.add_resource(RoomApi, '/room/<id>')