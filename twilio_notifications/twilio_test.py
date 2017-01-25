from middleware import MessageClient

to = 3212104622
body = 'this msg is from twilio-python via API'

txt = MessageClient()
txt.send_message(body, to)
