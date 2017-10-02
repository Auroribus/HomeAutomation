# Korte beschrijving

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
