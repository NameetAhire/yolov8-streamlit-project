import os
from twilio.rest import Client

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM")
TWILIO_TO = os.getenv("TWILIO_TO")

def make_phone_call():
    if not TWILIO_SID or not TWILIO_TOKEN:
        raise ValueError("Twilio credentials not set")

    client = Client(TWILIO_SID, TWILIO_TOKEN)
    call = client.calls.create(
        to=TWILIO_TO,
        from_=TWILIO_FROM,
        url="http://demo.twilio.com/docs/voice.xml"
    )
    print(f"Call SID: {call.sid}")
