from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return """
<ussd>
	<sessionid>some_session</sessionid>
	<type>response_type</type>
	<msg>message</msg>
</ussd>"""


if __name__ == '__main__':
    app.run(debug=True)