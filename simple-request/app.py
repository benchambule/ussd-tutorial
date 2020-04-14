from flask import Flask, request

app = Flask(__name__)

session_storage = []
default_window = 'default'
menu_storage = [
    {
        'name':'default',
        'title':'Welcome',
        'message':'Please provide your name'
    },
    {
        'name':'show_name',
        'title':'Welcome',
        'message':'Your name is '
    }
]

def create_new_session(session_id, msisdn, menu):
    return {
        'session' : session_id,
        'msisdn'  : msisdn,
        'menu'    : menu
    }


def retrive_menu_from_storage(menu_name):
    s = None
    for menu in menu_storage:
        if menu['name'] == menu_name:
            s = menu

    return s


def retrieve_session_from_storage(session_id, msisdn):
    '''
        Retrieves a session from the session storage
        :session_id `int` - session_id
        :msisdn `msisdn`  - cell number
    '''
    s = None
    for session in session_storage:
        if session['session'] == session_id and session['msisdn'] == msisdn:
            s = session

    return s


def add_session_to_storage(session):
    session_storage.append(session)


def get_message_from_menu(menu):
    return menu['title'] + " " + menu['message']


@app.route('/', methods=['GET'])
def handle_request():
    '''
        1. Get the session data {msisdn, session_id, message_type, message}
        2. Check if the session exists in our session storage:
        2.1. If doesn't exist:
        2.1.1. Create and store our new session
        2.1.2. Show our index|initial|first|default menu
        2.1.3. Retrieve the index menu
        2.2. If session exists:
        2.2.1. Retrieve the session
        2.2.2. Get the menu property in the session
        2.2.3. Re-generate the menu (object) based on the menu of the previous step
        2.2.3. Process the message based on the menu
        3. Update our session with the new menu
        4. Convert our menu to the response know by the USSD Gateway
        5. Retrieve the menu
    '''

    msisdn = request.args.get('msisdn') 
    sessionId = request.args.get('session_id') 
    m_type = request.args.get('type') 
    msg = request.args.get('msg') 

    message = None

    session = retrieve_session_from_storage(sessionId, msisdn)

    if not session:
        session = create_new_session(sessionId, msisdn, default_window)
        menu = retrive_menu_from_storage(default_window)
        add_session_to_storage(session)
    else:
        if session['menu'] == 'default':
            session['menu'] == 'show_name'
            menu = retrive_menu_from_storage('show_name')
            menu['message'] = menu['message'] + msg

    message = get_message_from_menu(menu)

    return f"""
<ussd>
	<sessionid>some_session</sessionid>
	<type>RESPONSE</type>
	<msg>{message}</msg>
</ussd>"""


if __name__ == '__main__':
    app.run(debug=True)