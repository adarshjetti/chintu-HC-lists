from twilio.rest import Client
from ChintuCourt.config import *

def send_chintu_sms(text):
    account_sid=chintu_sid
    auth_token=chintu_auth

    client=Client(account_sid,auth_token)

    client.messages.create(
        to=chintu_twilio_linked_phone_num,
        from_=chintu_twilio_num,
        body="\n"+text
    )

#test method
#send_ponni_sms("test sms chintu")

def send_ponni_sms(text):
    account_sid=ponni_sid
    auth_token=ponni_auth

    client=Client(account_sid,auth_token)

    client.messages.create(
        to=ponni_twilio_linked_phone_num,
        from_=ponni_twilio_num,
        body="\n"+text
    )

#test method
#send_ponni_sms("test sms ponni")