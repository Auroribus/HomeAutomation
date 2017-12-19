from __future__ import print_function
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.output(17,0)

mqttc = mqtt.Client()

import argparse
import os.path
import json

import google.oauth2.credentials

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file


def on_message(mqttc, obj, msg):
 print(msg.topic)
 print(msg.payload.decode())

def process_event(event):
 global mqttc
 if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
  print()
  print(event)
    
 if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED:
  print(event.args['text'])
  if event.args['text'] == 'lights on' :
   print("Turning the Lights ON")
   mqttc.publish('topic/test',payload="on", qos=0, retain=False)
  elif event.args['text'] == 'lights off':
   print("Turning the Lights OFF")
   mqttc.publish('topic/test',payload="off", qos=0, retain=False)
  elif event.args['text'] == 'lights down':
   print("Dimming the Lights")
   mqttc.publish('topic/test',payload="less", qos=0, retain=False)
  elif event.args['text'] == 'lights up':
   print("Brightening the Lights")
   mqttc.publish('topic/test',payload="more", qos=0, retain=False)
  elif event.args['text'] == 'Open Door':
   print("Opening the Door")
   mqttc.publish('topic/test',payload="open", qos=0, retain=False)
  elif event.args['text'] == 'close door':
   print("Closing the Door")
   mqttc.publish('topic/test',payload="close", qos=0, retain=False)
  elif event.args['text'] == 'show temperature':
   print("Getting Temperature from Sensor and Displaying on the Dashboard")
   mqttc.publish('topic/test',payload="show", qos=0, retain=False)
  


  

 if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            event.args and not event.args['with_follow_on_turn']):
  print()


def main():
 global mqttc
 mqttc.on_message = on_message
 mqttc.connect("raspberrypi.local",1883,60)
 mqttc.subscribe('topic/test')
 print("starting application")
 print("say: Ok, Google. To start")
 print("Commands: lights on, lights off, lights down, lights up")

# mqttc.loop_forever()

 parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
 parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
 args = parser.parse_args()
 with open(args.credentials, 'r') as f:
  credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

 with Assistant(credentials) as assistant:
  for event in assistant.start():
   process_event(event)


if __name__ == '__main__':
 main()
