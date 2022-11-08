from os import getenv

from src.hiya import WhatsApp


def test_sending_template_message():
    messenger = WhatsApp(token=getenv("TOKEN"), phone_number_id=getenv("PHONE_NUMBER_ID"))

    response = messenger.send_template("hello_world", getenv("RECIPIENT_ID"))

    assert response["contacts"][0]["input"] == getenv("RECIPIENT_ID")
    assert response["contacts"][0]["wa_id"] == getenv("RECIPIENT_ID")
    assert response["messaging_product"] == "whatsapp"
