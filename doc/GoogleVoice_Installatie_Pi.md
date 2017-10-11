## Google voice assistant SDK on the Raspberry Pi 3
#### Source: https://developers.google.com/assistant/sdk/develop/python/hardware/setup
### Benodigdheden:
-	Raspberry Pi, aangeraden model 3 met OS Raspbian
-	USB microfoon en speaker (mag ook een headset zijn)
-	SSH: VNC viewer om te kunnen SSH met grafische weergave
-	Anders een scherm, toetsenbord en muis

### 1.	Configureren van een Google Developer project:
	1. Om toegang te krijgen tot de Google Assistant API, moet je een aantal stappen uitvoeren, dit zijn de volgenden:
	i.	Op de projects page, selecteer een bestaand project of maak een nieuwe aan
	ii.	Zet de Google Assistant API aan in je project
	iii.	Creëer een OAUTH Client ID
	iv.	Download de client ID file, via het pijltje naar beneden aan de rechterkant van het scherm
	v.	Wanneer je deze stappen niet hebt uitgevoerd op de raspberry pi: 
deze file MOET gekopieerd worden naar de Raspberry Pi onder /home/pi 
dit kan gedaan worden met bijvoorbeeld WinSCP
	2. Om gebruik te kunnen maken van de Google Assistant, moet je bepaalde data delen met Google
		i.	Open de Activity Controls Page voor je Google Account
		ii.	Deel de volgende onderdelen: 
			1.	Web & App activity
			2.	Device Information
			3.	Voice & Audio Activity
	3. Vervolgens gaan we de library downloaden en testen op de Pi

### 2.	Library downloaden en testen:
	1. Allereerst gaan we een Python virtuele omgeving opzetten (dit kun je overslaan als dit al geinstalleerd is op je Pi)
		i. Python 3:
			1. sudo apt-get update
			2. sudo apt-get install python3-dev python3-venv
			3. python3 -m venv env
			4. env/bin/python -m pip install --upgrade pip 
			5. source env/bin/activate   (sla deze commando op, hiermee start je de virtual environment)

		ii. Python 2:
			1. sudo apt-get update
			2. sudo apt-get install python-dev python-virtualenv
			3. virtualenv env --no-site-packages env/bin/python -m pip install --upgrade pip setuptools 
			4. source env/bin/activate
	2. Vervolgens in de virtual Environment via source env/bin/activate:
		i. Python -m pip install --upgrade google-assistant-library 
	3. Open op je raspberry pi een browser en log in op je Google account (hierdoor heb je dus of een scherm nodig, of een programma zoals VNC viewer)
	4. Nu gaan we de Google Assistant SDK toegang geven tot je account, hierdoor ga je de json file met het client ID nodig hebben dat we eerder hebben opgeslagen onder /home/pi
	5. Installeren van de authorization tool:
	6. Python -m pip install --upgrade google-auth-oauthlib[tool]
	7. Uitvoeren van de tool, wanneer je deze commando runt via de terminal op de Pi zelf, dus niet via een SHH sessie, kun je de headless flag weglaten:
	8. google-oatuhlib-tool --client-secrets [/path/to/client_secret.json file] --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless 
	9.	Start de Google Assistant SDK sample op je Pi:
	10.	(env) google-assistant-demo
	11.	Om te testen zeg: “Ok Google”, en stel een vraag

### 3.	Wanneer alles werkt en je kunt met Google Voice spreken, kun je vervolgens alles kopiëren naar een eigen project met de volgende commando’s:
	1. Git clone https://github.com/googlesamples/assistant-sdk-python
	2. cp -r assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/library [directory name project]

### 4.	Nu kunnen we speech to voice gaan gebruiken om GPIO pinnen aan te sturen op de Pi
	1. Allereerst, omdat we in een virtuele omgeving werken, moet je de RPi.GPIO library installeren:
	2. pip install RPi.GPIO (pip3 voor python3)
	3. Vervolgens kun je in je eigen project directory, de file: hotword.py zodanig aanpassen dat je de GPIO pinnen kunt aansturen
	4. Voorbeeld script om via de commando’s: “lights on” en “lights off” een ledje op pin 17 aan en uit te zetten met je stem:


from __future__ import print_function
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.output(17,0)

import argparse
import os.path
import json

import google.oauth2.credentials

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file


def process_event(event):
    
    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        print()

    print(event)
    
    if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED:
        print(event.args['text'])
        if event.args['text'] == 'lights on' :
            print("light on")
            GPIO.output(17,1)
        if event.args['text'] == 'lights off':
            print("light off")
            GPIO.output(17,0)        
    
    if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            event.args and not event.args['with_follow_on_turn']):
        print()


def main():
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


 
 
 


