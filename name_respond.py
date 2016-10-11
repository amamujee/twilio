from flask import Flask, request, redirect, session
import twilio.twiml

from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+17574776464": "Little One",
    "+16175105178": "Aadil",
    "+12025773026": "Keeg",
    "+18483918456": "Sajid"
}

@app.route("/", methods=['GET', 'POST'])

def hello_monkey():
    """Respond and greet the caller by name."""

    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", You're a smelly bro!"
    else:
        message = "Rando Bro, thanks for the message!"


    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

