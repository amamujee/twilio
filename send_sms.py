# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC9cae8a357c0111ce160b7410aa7bfe2c"
auth_token = "66a1c2714748a09d057429d10e0e6346"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
	to="12025773026", 
	from_="+15104601941",
    body="I miss Hugo", 
   media_url="http://dailypicksandflicks.com/wp-content/uploads/2011/12/cute-monkey1.jpg",
    status_callback="http://requestb.in/1h18unm1"
    )
