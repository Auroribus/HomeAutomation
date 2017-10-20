# Documentatie Node-Red op de Raspberry Pi
#### -	Let Op!: Security, default heeft de node-red server geen beveiliging en kan iedereen die het IP heeft erop connecteren en berichten versturen

## Installeren node-red op de Pi in een virtual environment:


### Commando’s: 
```python
Start Virtual Environment:
Source env/bin/activate

Update bestaande Nodejs en Nodered:
update-nodejs-and-nodered

Start Node-Red:
node-red-start
Let Op!: sluiten van de window stopt de server niet met runnen, gebruik: node-red-stop om de server te stoppen

Optioneel:
Run node-red bij startup van de Pi:
sudo systemctl enable nodered.service

Starten van de Node-Red:
Commando’s:

Starten van de server:
node --max-old-space-size=256 red.js

Toevoegen van security met een wachtwoord en username:
-	Aanpassen van de: settings.js file
-	in cli via: --settings|-s 
Genereren van een hashed password
Plaint-test wachtwoorden kunnen niet gebruikt worden in de settings.js file, daardoor moeten we het paswoord dus eerst hashen met het volgende commando:
Node-red-admin hash-pw

```
