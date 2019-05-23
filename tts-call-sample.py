from flask import Flask,request, Response,session
from pprint import pprint
import requests
import json
import nexmo
from base64 import urlsafe_b64encode
import os
import calendar
import jwt # https://github.com/jpadilla/pyjwt -- pip3 install PyJWT
import coloredlogs, logging

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_key = os.environ.get("API_KEY") 
api_secret = os.environ.get("API_SECRET")
application_id = os.environ.get("APPLICATION_ID")

keyfile = os.environ.get("KEYFILE")
webhookurl = os.environ.get("WEBHOOK_URL")
virtual_number = os.environ.get("LVN")
target_phone = os.environ.get("TARGET_PHONE")

session={}

# https://github.com/Nexmo/nexmo-python#voice-api

client = nexmo.Client(application_id=application_id, private_key=keyfile)
                      
app = Flask(__name__) 

response = client.create_call({'to': [{'type': 'phone', 'number': target_phone}],'from': {'type': 'phone', 'number': virtual_number},'answer_url': [webhookurl+'/answer']})
        
@app.route("/answer", methods = ['GET', 'POST']) 
def tts():
    
    arg_to = request.args['to']
    arg_from = request.args['from']
    session['to'] = arg_to
    session['from'] = arg_from
    
    ncco = [
        {
            "action": "talk",
            "text": "<speak>こんにちは。テキストツースピーチのテストコールです。発信先の電話番号は、<prosody rate='slow'><say-as interpret-as='digits'>"+ session['to'] + "</say-as></prosody> です。ではさようなら。</speak>",
            "voiceName": "Mizuki",
            "eventURL": webhookurl+"/event"
        }
    ]
    js = json.dumps(ncco)
    resp = Response(js, status=200, mimetype='application/json')
    print(resp)
    return resp

@app.route('/event', methods=['GET', 'POST', 'OPTIONS'])
def event():
    r = request.json
    print(r)
    return "OK"

if __name__ == "__main__":
    app.run(port="3000")