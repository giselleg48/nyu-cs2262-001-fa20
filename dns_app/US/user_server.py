from flask import Flask, requests, Response
from datetime import datetime
app = Flask(__name__)



@app.route('/fibonacci?hostname=fibonacci.com&fs_port=K&number=C&as_ip=Y&as_prt=Z')
def handle():
    args = requests.args
    fs_port= args.get('fs_port')
    number = args.get('number')
    as_ip = args.get('as_ip')
    as_prt = args.get('as_prt')
    if not fs_port or not number or not as_ip or not as_prt:
        return(Response("400: Bad Request", status=400))

    # query ap to get fs IP
    resp = requests.get(as_ip + ":" + as_prt, params=({"TYPE": "A", "NAME": "fibonacci.com"})
    fs_ip =resp.get("VALUE")

    # make request to FS given IP and port
    lnk = fs_ip + ":" fs_port + "'/fibonacci?number={}"
    fmt_lnk = lnk.format(number)
    resp2 = request.get(lnk)

    return(resp2)

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
