<p align="center">
  <a href="https://pywassap.netlify.app"><img src="https://pywassap.netlify.app/img/logo-margin/pywassap-logo.png" alt="pywassap"></a>
</p>
<p align="center">
    <em> A simple FastAPI wrapper for WhatsApp Web API </em>
</p>
<p align="center">
<a href="https://github.com/Aarif1430/pywassap/actions/workflows/test.yml" target="_blank">
    <img src="https://github.com/Aarif1430/pywassap/actions/workflows/test.yml/badge.svg" alt="Test">
</a>
<a href="https://github.com/Aarif1430/pywassap/actions/workflows/publish.yml" target="_blank">
    <img src="https://github.com/Aarif1430/pywassap/actions/workflows/publish.yml/badge.svg" alt="Publish">
</a>
<a href="https://github.com/Aarif1430/pywassap/actions/workflows/smokeshow.yml" target="_blank">
    <img src="https://github.com/Aarif1430/pywassap/actions/workflows/smokeshow.yml/badge.svg" alt="Coverage">
</p>
</p>

---

**Documentation**: <a href="https://pywassap.netlify.app" target="_blank">https://pywassap.netlify.app</a>

**Source Code**: <a href="https://github.com/Aarif1430/pywassap" target="_blank">https://github.com/Aarif1430/pywassap</a>

---
**PyWassap** is a python library for sending WhatsApp messages using the WhatsApp Business API. It is a wrapper around the WhatsApp Business API. The library is built on top of the [FastAPI](https://fastapi.Aarif1.com/) framework and uses [pydantic](https://pydantic-docs.helpmanual.io/) for data validation. It is built with the developer experience in mind. It is a fully asynchronous library and uses [aiohttp](https://docs.aiohttp.org/en/stable/) for making HTTP requests.

**PyWassap** supports the following features:

**1. Send WhatsApp messages** - Send WhatsApp messages to a single or multiple recipients.

```Python
from pywassap import WhatsApp

client = WhatsApp()
client.send_message(
    message="Hello World",
    recipient_id="919999999999"
    recipient_type="individual"
)
```

The entire **PyWassap** library is built on top of the FastApI framework.
The FastAPI swagger UI is available at `http://localhost:8000/docs` and
makes it easy to test the API.

**2. Send WhatsApp messages to multiple recipients** - Send WhatsApp messages to multiple recipients.

```Python
from pywassap import WhatsApp

client = WhatsApp()
client.send_message(
    message="Hello World",
    recipient_id=["919999999999", "919999999998"]
    recipient_type="individual"
)
```


## Requirements
For development, the following requirements are needed:
```console
fastapi
uvicorn
pydantic
aiohttp
```

## Installation

<div class="termy">

```console
$ pip install pywassap
---> 100%
Successfully installed asyncer anyio
```

</div>
## License

This project is licensed under the terms of the [MIT license](https://github.com/Aarif1430/pywassap/blob/main/LICENSE).
