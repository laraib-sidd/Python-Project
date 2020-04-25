from twilio.rest import Client

account_sid = 'ACbd79ecddce789e53625243bcc8650f7f'
auth_token = '4beb2061089249ced8543c4cd575c16a'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12162798914',
    body='How the fuck are you doing shithole. Die Motherfucker?',
    to='+918587886108'
)

print(message.sid)
