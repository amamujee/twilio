from flask import Flask, request, redirect, session
import twilio.twiml

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+17574776464": "Little One",
    "+16175105178": "Aadil",
    "+12025773026": "Shafiq",
    "+13059785007": "Hanif"
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond with the number of text messages sent between two parties."""

    counter = session.get('counter', 0)

    # increment the counter
    counter += 1

    # Save the new counter value in the session
    session['counter'] = counter

    from_number = request.values.get('From')
    if from_number in callers:
        name = callers[from_number]
    else:
        name = "Big Monkey"

    if counter ==1:
        message = "".join([name, ", How could you forget me??? We had so much fun"])
    if counter ==2:
        message = "".join([name, ", Give me back my Hugo, He's mine"])
    if counter ==3:
        message = "".join([name, ", You're a smelly guy, and Hugo is my best friend"])
    if counter ==4:
        message = "I know you miss me, and when you close your eyes you dream of my smell - I dream of Hugo"
    if counter ==5:
        message = "".join([name, ", Tell me you don't miss the warmth of my breath - till next octoberfest"])
    else:
        message = "I'm done with this - Baby Monkey Out!"

    resp = twilio.twiml.Response()
    resp.sms(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)



