from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    msisdn = request.args.get('msisdn')
    message = f"Hi {msisdn}, welcome to my WAP"

    return f"""
<ussd>
	<sessionid>some_session</sessionid>
	<type>RESPONSE</type>
	<msg>{message}</msg>
</ussd>"""


if __name__ == '__main__':
    app.run(debug=True)