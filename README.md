# Ever wanted to know how to program USSD applications?
You came to the right place. Here you can learn how to program USSD applications

## Main algorithm

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
