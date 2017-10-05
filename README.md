# Internet of Things - 

## Doel van het product
Home Automation en Monitoring door middel van Speech to Text technologie.

De gebruiker moet door middel van een hoofd unit of applicatie sensoren kunnen aansturen. Dezen moeten processen automatiseren en monitoren. Bijvoorbeeld: wanneer men thuis komt en de deur opent, gaan automatisch de lichten in de hal aan. Dit wordt gerealiseerd door middel van stemherkenning en actuatoren.

## Beschrijving Project

Wij willen ervoor zorgen dat huizen geautomatiseerd en geoptimaliseerd worden, ofwel “Smart”. Dit voornamelijk door het plaatsen
van sensoren en gebruik te maken van een applicatie voor het aansturen van het systeem. Het is vervolgens de bedoeling dat 
men dit systeem kan aansturen door een Speech to Text technologie zoals Alexa.

We zullen van “domme” objecten, slimme objecten gaan maken.

Ons systeem zal bestaan uit een main unit, waarschijnlijk een Raspberry Pi, die alles zal gaan aansturen. Daarnaast zullen wij 
units ontwerpen die hiermee verbonden worden, dit netwerk zal opgezet worden door middel van de LoRa technologie. Doordat het 
systeem onderling verbonden is, kunnen de verschillende units met elkaar communiceren. Op die manier zorgen wij ervoor dat 
bepaalde processen geautomatiseerd worden en veelal ook geoptimaliseerd. De data die wij hieruit krijgen zullen wij opslaan 
en kan vervolgens gebruikt worden om het systeem te optimaliseren en te controleren.

Hieronder volgen enkele concepten die wij willen gaan uitwerken omtrent Home Automation:

### 1.	Slimme Deurbel

Concept: Men belt aan en vervolgens wordt er via de LoRa technologie een signaal gestuurd naar de hoofd unit, deze stuurt 
vervolgens een bericht naar je telefoon dat er iemand heeft aangebeld, op deze manier mis je nooit meer de bel.
Doordat de bel verbonden is met het systeem, kunnen wij data verzamelen over hoeveel bezoekers men gemiddeld krijgt, of 
hoe vaak men de bel mist wanneer je niet thuis bent. Deze data kan dan gebruikt worden in statistieken en dergelijken.

### 2.	Welkom bij binnenkomst

Concept: Wanneer je thuiskomt en de voordeur opent, zal het systeem via een speaker je welkom heten en vervolgens zullen de 
lichten in de hal aangaan. Hierdoor krijg je een warm welkom thuis, elke dag.

### 3.	Licht aansturen m.b.v. je stem

Concept: Door je stem te gebruiken, kun je het licht aansturen. Uit of aan, minder of meer licht. Wat betreft het licht
zouden wij bij kunnen houden hoe efficiënt de lampen zijn. Dit kan dan vervolgens gebruikt worden 
voor optimalisatie.

### 4.	Slim slot

Concept: Op het moment moet men de deur nog handmatig op slot doen, wij willen dit vergemakkelijken door dit op dezelfde 
manier te doen als met een auto. Op afstand je deur sluiten door op een knopje te drukken die een signaal naar het slot stuurt.
Doordat het slot op afstand geopend en gesloten kan worden, hoeft dit niet meer handmatig gedaan te worden. Dit zal een 
tijdsbesparing hebben en daardoor een optimalisatie zijn. Zoals bij de bel, kunnen wij ook bij het slimme slot bijhouden 
wanneer iemand het opent of sluit, en vervolgens een push notificatie uitsturen zodat de bewoners op de hoogte zijn. 
Hierbij moeten we vooral opletten met de veiligheid van het slot, zodat men dit niet gemakkelijk kan hacken. 

## Documentatie

## User stories en Engineering Tasks
#### 1. As a user i want to be able to control my lights with my voice.
   
   1. SSH to pi
   2. setup VNC on pi
   3. Install Alexa on pi    
   4. Configure Alexa to recognise commands
   5. Make pi give right output with right command
   6. Make light to shine brighter or softer
   7. Make control programm for light
   8. LoRaWAN for light
   9. LoRaWAN for pi
   10. Connect LoRaWAN

#### 2. As a user I want to be able to control my door-lock with a remote controller (cellphone).
   1. Make doorlock frame
   2. Make pcd for doorlock
   3. installeer bluetooth in doorlock
   4. Print Mini door with 3d print
   5. Make controller app
   6. Add bluetooth connection to app
   7. secure app with pin
   8. Connect phone with doorlock
   9. Make trusted phone system for bluetooth connection
   10. Test end system.
  
#### 3. As a user I want to be able to receive a message on my phone when someone is ringing my doorbell.
   1. Make doorbell
   2. Make pcd for doorbell
   3. Add LoRaWAN to doorbell
   4. LoRaWAN for pi
   5. Connect doorbell to pi
   6. Make database on pi
   7. Log doorbell on pi when rang in database
   8. connect pi to phone with MQTT 
   9. Send message from pi to phone through MQTT
   10. Show logs on phone  
      
#### 4. As a user I want to be able to have a responsive text to speech system and respons on actions.
   1. SSH to pi
   2. VNC for pi
   3. Instal Alexa on pi
   4. Make Amazon account
   5. Setup voice command for Alexa
   6. Setup Speaker through the house 
   7. Setup microphones through the house
   8. Connect everything with LoRaWAN
   9. Add detection system to door
   10. Make respons for detection door

#### 5. As a user I want to connect my nodes with a long range network system.
   1. 
   2.
   3.
   4.
   5.
   6.
   7.
   8.
   9.
   10.
   
## Benodigdheden

Voor het product te maken heb je natuurlijk materialen nodig. Dit kunnen COTS (Commercial of the Shelve) materialen 
en/of apparaten zijn (bv. Raspberry Pi, Arduino, ...). Voor het project moet je een elektronische module volledig zelf 
ontwikkelen probeer hiervoor al de nodige componenten te bepalen.

### Product / service vergelijkingen
Als je bepaalde off the shelve producten selecteert, staaf deze keuze dan. Je kan niet zomaar zeggen: 
"ik pak dit of dat.". Je onderbouwt de selectie. Dit doe je ook voor eventuele services die je wilt gebruiken. 
Je verkent de mogelijke product of service markten.

### Materialen lijst
Hier defineer je een simpele Bill Of Materials.

## Taakverdeling

In dit stuk van de analyse moet er duidelijk gemaakt worden hoe jullie als groep tegelijk aan het project gaan werken. 
Alle teamleden moeten een evengrote bijdrage leveren aan het project. Het word niet getolereerd dat er een student de 
verantwoordelijke is voor de documentatie. Documentatie is geen individuele taak maar een team effort. Iedereen moet een 
technische bijdrage leveren aan het project.

Dit realiseer door het afstemmen van de scope van het project. Dit kan gebeuren door een relevant uitbreiding bij op te
nemen in het project.

Als voorbeeld:

Als voorbeeld nemen we het project voor het opmeten van het energie verbruik in de campus.

Je moet een sensor node maken dat temperatuur en licht log. Dit is werk voor een persoon. Het andere teamlid maakt een
dashboard, de andere verzorgt het netwerk tussen de sensor en de backend server. Er is nog wel een student die geen taak heeft.
Deze kan dan bv een sensor node ontwikkelen die het opengaan en sluiten van een deur registreert. Deze data kan relevant 
zijn voor het vergelijken van de data afkomstig van de sensoren.

### Tijdelijke taakverdeling:

#### Steven Dijcks:
- Voice to speech op de arduino werkend krijgen

#### Tim de Nooijer:
- LoRa opbouwen en werkend krijgen 

#### Gejo Ossenblok:
-

#### Simon :
-



## Groepsleden

### Gejo Ossenblock
### Simon Broos
### Timmy de Nooijer
### Steven Dijcks
