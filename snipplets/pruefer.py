# diese script ist eine zwischenvorgang fuer list.py, Ziele sind:
#
# nur dd.mm.yyyy format fuer datum akzeptieren
# nur alfabetisch+numerisch+ unterschrift für Lieferant, Bemerkung, Artikelname
# nur € x.xxx.xxx,xx format für Preis akzeptiert
# autokonvert von datum in yyyy-mm-dd fuer datum4file
#import dateutil
#from datetime import datetime
import re

from datetime import datetime

#eingabe="12.12.2018"
#print(datetime.strptime(eingabe, '%d.%m.%Y'))

#damit ist import re noetig.
vari = input('var')
mama = bool(re.match('^[a-zA-Z0-9]+-', vari))
print(mama)

#geht gut aber muss man finden wie ich noch _ akzeptieren kann
#'123abc'.isalnum()

