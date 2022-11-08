from os import getenv

from dotenv import load_dotenv
from hiya import WhatsApp


def test_sending_message():
    load_dotenv()

    messenger = WhatsApp(token=getenv("TOKEN"), phone_number_id=getenv("PHONE_NUMBER_ID"))

    response = messenger.send_message(
        message="https://www.youtube.com/watch?v=K4TOrB7at0Y",
        recipient_id=getenv("RECIPIENT_ID"),
    )

    assert response["contacts"][0]["input"] == getenv("RECIPIENT_ID")
    assert response["contacts"][0]["wa_id"] == getenv("RECIPIENT_ID")
    assert response["messaging_product"] == "whatsapp"
