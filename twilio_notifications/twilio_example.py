from twilio import TwilioRestException
from twilio.rest import TwilioRestClient
import config

account_sid = config.TWILIO_ACCOUNT_SID # Your Account SID from www.twilio.com/console
auth_token = config.TWILIO_AUTH_TOKEN   # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

try:
    message = client.messages.create(
        body="Greetings from Python via Twilio API",
        to="+13212104622",           # Replace with your phone number
        from_=config.TWILIO_NUMBER)  # Replace with your Twilio number

    # return the message sid
    print(message.sid)

except TwilioRestException as e:
    print(e)
