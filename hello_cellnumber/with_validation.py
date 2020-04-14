from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    msisdn = request.args.get('msisdn') if request.args.get('msisdn') else ''
    
    if not msisdn.startswith('258') or len(msisdn) != 12 or not msisdn.isnumeric():
        message = f"Hi {msisdn}, your cellnumber is invalid" 
    else:
        message = f"Hi {msisdn}, welcome to my WAP"
        #This validation is not in production because the operator will validate for us

    print(msisdn.startswith('258'))
    print(len(msisdn))
    print(msisdn.isnumeric())

    return f"""
<ussd>
	<sessionid>some_session</sessionid>
	<type>RESPONSE</type>
	<msg>{message}</msg>
</ussd>"""


if __name__ == '__main__':
    app.run(debug=True)