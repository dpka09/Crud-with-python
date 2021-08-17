# Hotel Management System

## Steps to run the project:

### Using virtual environment
> 1. Use `pip install -r requirements.txt` to install all dependencies

> 2. Use `run flask` to run the flask server.

### Using docker file
> 1. Run `docker build -t hms:latest` to build the docker image

> 2. Run `docker run -it -p 4500:5000 hms` to run the server




## Endpoints and Requests
| Endpoints               | Request   |
|----------------         |-----------|
|/customers               |GET, POST  |
|/cutomer/\<id>           |GET, PUT, DELETE |
|/rooms                   |GET, POST  |
|/room/\<id>              |PATCH, DELETE|
|/room/price/\<id>/\<days>|GET  |
|/customer/detail/\<id>   |GET  |
|/rooms/available         |GET  |

## To use swagger UI to make Requests
Go to `http://localhost:5000/swagger/`

## Project Description</h2>

1. The desk officer should be able to add new customers and their personal as well as booking information. One customer can book many rooms and there can be many types of rooms (Single, Double, Deluxe, etc). The booking details should include the check in and check out date as well as cost and payment information.

2. Each room must have its specific price and payment should be calculated accordingly. There can be many rooms in a hotel and the room status should be tracked. For example whether a room is available or not.

3. User should be able to view the list of available rooms

4. Users should be able to calculate the price of stay. For example, if a customer wants to stay for 5 days in a single room that costs Rs 2000 per day. The total cost of Rs 10000 should be returned.

5. Users should be able to view customer details and their booking details.


