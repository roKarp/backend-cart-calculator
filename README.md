# backend-cart-calculator

This is the basic guide to using the backend for calculating a delivery fee of a cart order on Linux.

The backend application uses the following:

    Python 3.8 (or some other newer version)
    
    Flask - https://flask.palletsprojects.com/en/3.0.x/installation/
    
    python-dateutil - https://pypi.org/project/python-dateutil/

I have decided to use Flask as the web framework, because it's easy-to-use for small to medium-sized applications. If it would like to be expanded upon into a larger one, then using something like Django would be preferred.

## Information
The application uses an HTTP API to calculate all incoming cart order JSON posts. The request field looks as follows:

##### Field details

| Field             | Type  | Description                                                               | Example value                             |
|:---               |:---   |:---                                                                       |:---                                       |
|cart_value         |Integer|Value of the shopping cart __in cents__.                                   |__790__ (790 cents = 7.90€)                |
|delivery_distance  |Integer|The distance between the store and customer’s location __in meters__.      |__2235__ (2235 meters = 2.235 km)          |
|number_of_items    |Integer|The __number of items__ in the customer's shopping cart.                   |__4__ (customer has 4 items in the cart)   |
|time               |String |Order time in UTC in [ISO format](https://en.wikipedia.org/wiki/ISO_8601). |__2024-01-15T13:00:00Z__                   |

Example:
```json
{"cart_value": 500, "delivery_distance": 4160, "number_of_items": 4, "time": "2024-01-04T12:00:00Z"}
```

## Guide

1. Install all the needed programs (for example, in a virtual environment)

2. Go to the directory of back.py and input the following:

    `export FLASK_APP=back.py`

    `flask run`

3. The application should be running at http://127.0.0.1:5000

## Tests
Sending a post request with the needed payload (JSON) to http://127.0.0.1:5000/calc will return the calculated delivery fee in the response payload.

An easy way to see it work is by sending the post request with curl, like:


```curl
curl -X POST -H "Content-Type: application/json" -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 6, "time": "2024-01-20T19:00:00Z"}' http://127.0.0.1:5000/calc
```


it returns:


```json
{"delivery_fee":810}
```

and that's it. The response can have an error message in case there are missing fields or some fields have a wrong type.

## To do in future

Making a bash script for different API curl commands for testing purposes.


