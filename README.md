# TTS-Call-Sample-py

This is sample Nexmo Voice App demo how to make Voice Call and Play TTS Voice with SSML using Nexmo Voice API

This app is built using [Flask framework](http://flask.pocoo.org/) and require [Python3](https://www.python.org/)

## Prerequisite

You will need a few thins to get going with this app: 

- A [Nexmo](https://nexmo.com) Account
- A Nexmo Messages & Dispatch App [[set one up here]](https://dashboard.nexmo.com/messages/create-application)
- A Nexmo Voice App [[set one up here]](https://dashboard.nexmo.com/voice/create-application)
- To buy Phone Number for Voice App [[set one up here]](https://dashboard.nexmo.com/buy-numbers)
- A WhatsApp Business Account or SMS 2way Number

To install the Python client library using pip:

    pip install nexmo

To upgrade your installed client library using pip:

    pip install nexmo --upgrade

To rename .env-sample to .env and set parameter

## Running the demo


For demo, to run ngrok for webhook

    $ ngrok http 3000

    Forwarding                    https://xxxxxx.ngrok.io -> localhost:3000
    
Please set "https://xxxxxx.ngrok.io" to "WEBHOOK_URL" in .env file

    WEBHOOK_URL = "Your Base Webhook URL"

To run application

$ python3 tts-call-sample.py


