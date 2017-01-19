from twilio import rest

account_sid = "AC3c9a371a25ea0df7407919853ae16239" # Your Account SID from www.twilio.com/console
auth_token  = "8bb20f348564ba4e26e92f1548b78fac"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+5531993885379", 
    from_="+14152003426",
    body="After some changes!")

print(message.sid)
