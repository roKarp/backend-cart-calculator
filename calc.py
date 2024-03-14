from flask import Flask, jsonify, request
from dateutil.parser import isoparse as rush
app = Flask(__name__)

#checks all needed request fields and their correct types
def err(req):

    if 'cart_value' not in req:
        return {'error': 'cart_value found or has the wrong type'}, 400

    elif not isinstance(req['cart_value'], int):
        return {'error': 'cart_value has the wrong type'}, 401

    elif 'delivery_distance' not in req:
        return {'error': 'delivery_distance not found'}, 402
    
    elif not isinstance(req['delivery_distance'], int):
        return {'error': 'delivery_distance has the wrong type'}, 403

    elif 'number_of_items' not in req:
        return {'error': 'number_of_items not found'}, 404

    elif not isinstance(req['number_of_items'], int):
        return {'error': 'number_of_items has the wrong type'}, 405   

    elif 'time' not in req:
        return {'error': 'time not found'}, 406

    elif not isinstance(req['time'], str):
        return {'error': 'time has the wrong type'}, 407  

    try:
        rush(req['time'])
        return "ok", 200

    except:
        return {'error': 'time not using ISO format'}, 408

def delivery(cart, distance, items, time):
    #surcharge
    cost = 0
    if (cart < 1000):
        cost += 1000 - cart

    #calculate the distance traveled
    dis = distance - 1000
    cost += 200
    while(dis > 0):
        dis -= 500
        cost += 100

    #check the number of items
    if (items > 4):
        cost += (items-4)*50
        if (items > 12):
            cost += 120

    #check if friday rush is happening
    datetime = rush(time)
    if datetime.isoweekday() == 5 and 15 <= datetime.hour < 19:
        cost *= 1.2
    return min(cost,15000)



@app.route('/calc', methods=['POST'])
def calculate():
    req = request.json
    mes, num = err(req)
    if ( num != 200):
        return jsonify(mes),num
    cart = req['cart_value']
    dist = req['delivery_distance']
    items = req['number_of_items']
    time = req['time']
    cost = 0
    if cart < 20000:
        cost = delivery(cart,dist,items,time)
    return jsonify({'delivery_fee': cost}), 200

@app.route('/')
def info():
    return 'Send a simple post request to "/calc" to calculate the delivery fee'
