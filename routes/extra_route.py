from controller.extra_controller import CustomerDetailApi, StayPriceApi, AvailableRoomsApi

def extra_routes(api):
    api.add_resource(AvailableRoomsApi, '/rooms/available')
    api.add_resource(StayPriceApi, '/room/price/<id>/<days>')
    api.add_resource(CustomerDetailApi, '/customer/detail/<id>')