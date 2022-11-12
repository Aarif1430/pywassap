<p align="center">
  <a href="https://pywassap.netlify.app"><img src="https://pywassap.netlify.app/img/logo-margin/pywassap-logo.png" alt="pywassap"></a>
</p>
<p align="center">
    <em> A simple asynchronous Python library for WhatsApp Web.</em>
</p>
<p align="center">
<a href="https://github.com/Aarif1430/pywassap/actions/workflows/test.yml" target="_blank">
    <img src="https://github.com/Aarif1430/pywassap/actions/workflows/test.yml/badge.svg" alt="Test">
</a>
<a href="https://github.com/Aarif1430/pywassap/actions/workflows/publish.yml" target="_blank">
    <img src="https://github.com/Aarif1430/pywassap/actions/workflows/publish.yml/badge.svg" alt="Publish">
</a>
<a href="https://github.com/Aarif1430/pywassap/pulse" alt="Activity">
    <img src="https://img.shields.io/github/commit-activity/m/Aarif1430/pywassap" /></a>
<a href="https://github.com/Aarif1430/pywassap/actions/workflows/smokeshow.yml" target="_blank">
    <img src="https://github.com/Aarif1430/pywassap/actions/workflows/smokeshow.yml/badge.svg" alt="Coverage">
</p>
</p>

---

**Documentation**: <a href="https://pywassap.netlify.app" target="_blank">https://pywassap.netlify.app</a>

**Source Code**: <a href="https://github.com/Aarif1430/pywassap" target="_blank">https://github.com/Aarif1430/pywassap</a>

---
**PyWassap** is a python library for sending WhatsApp messages using the WhatsApp Business API. It is a wrapper around the WhatsApp Business API. The library is built on top of the [aiohttp](https://pypi.org/project/aiohttp/) library for asynchronous HTTP requests.

**PyWassap** supports the following features:

**1. Send WhatsApp messages** - Send WhatsApp messages to a single or multiple recipients.

```Python
from pywassap import PyWassap

client = WhatsApp(number, token)
client.send_message(
    message="Hello World",
    recipient_id="919999999999"
    recipient_type="individual"
)
```

**2. Send WhatsApp messages to multiple recipients** - Send WhatsApp messages to multiple recipients.

```Python
from pywassap import WhatsApp

client = WhatsApp(number, token)
client.send_message(
    message="Hello World",
    recipient_id=["919999999999", "919999999998"]
    recipient_type="individual"
)
```


## Requirements
For development, the following requirements are needed:
```console
python
aiohttp
```

## Installation

<div class="termy">

```console
$ pip install pywassap
---> 100%
Successfully installed pywassap
```

</div>

## License

This project is licensed under the terms of the [MIT license](https://github.com/Aarif1430/pywassap/blob/main/LICENSE).
