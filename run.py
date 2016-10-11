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
    "+12025773026": "Keeg"
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
        name = "Monkey"

    if counter <2:
        message = "".join([name, ", you're a smelly monkey - Give me Hugo Back!"])
    else:
        if counter ==2:
            message = "".join([name, ", you're the #1 smelly monkey - and I'm going to get you"])
        else
            message = "".join([name, ", you know you miss me, but i miss Hugo's smell more"])

    resp = twilio.twiml.Response()
    resp.sms(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)



