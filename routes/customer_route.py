from controller.customer_controller import CustomerApi, CustomersApi

def customer_routes(api):
    api.add_resource(CustomersApi, '/customers')
    api.add_resource(CustomerApi, '/customer/<id>')