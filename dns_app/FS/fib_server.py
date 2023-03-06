from flask import Flask, requests, Response
from datetime import datetime
app = Flask(__name__)

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@app.route('/register')
def handle_register():
    req = requests.form
    hostname = req.get('hostname')
    ip = req.get('ip')
    as_ip = req.get('as_ip')
    as_port = req.get('as_port')


    resp = requests.get(as_ip + ":" + as_port, params=({"TYPE": "A", "NAME": hostname, "VALUE": ip, "TTL":10}))
    return(resp)

@app.route('/fibonacci?number=X')
def handle_fib():
    
    args = requests.args
    number = args.get("number")

    if not isinstance(number, int):
        return(Response("400: Bad Request", status=400))

    else: 
         ret = str(fib(number))
         r ="{'result': {}}".format(ret)
         return(Response(r, status=200))
        

app.run(host='0.0.0.1',
        port=9090,
        debug=True)
