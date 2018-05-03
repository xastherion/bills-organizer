# BILLS-ORGANIZER :
# a VERY simple little program to organize invoices and bills
# This little Python script allow you to organize your PDF bills in a folder with a standard name system
# and put many registers likes items in a simple text file easy to export to your favorite spreedsheet
# software over comma separated values files (.csv)
# carlos-gonzalez 2018

import shutil
import time
import os
from re import *
from datetime import datetime
from pathlib import Path


# ###################################################### KLASSEN-BLOCK #
class currency(float):

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        temp = "%.2f" % self.amount
        profile = compile(r"(\d)(\d\d\d[.,])")
        while 1:
            temp, count = subn(profile, r"\1,\2", temp) # <-- aqui esta el punto separador de miles
            if not count:
                break
        return temp

# ###################################################### FUNKTIONEN-BLOCK #

def rechnung_angaben():  # Akzept Rechnung
    global rechnungsnr, einkaufdatum, lieferant, bemerkung, jahro, if_brutto
    rechnungsnr = input("- Rechnungsnummer  (A1312X-00l usw.)      : ")
    einkaufdatum = input("- Einkaufdatum (yyyy-mm-dd) [Enter=heute] : ")  # Akzept EKD
    if einkaufdatum == "" :         # pruef ob EKD ist gleich h, wenn ja nehmt Heute, wenn nicht nihmt die Eingabe - FUNKNICHT !!!
        einkaufdatum = time.strftime("%Y-%m-%d")
        print ('       ###  Einkaufdatum : ', einkaufdatum)
    else:
        einkaufdatum = (str(datetime.strptime(einkaufdatum, '%Y-%m-%d'))).replace(" 00:00:00", '')
    jahro = einkaufdatum[0:4]
    lieferant = (input("- Lieferant (z.B. SuperMac_GmbH)          : ")).replace(' ','_')
    bemerkung = (input("- Bemerkung  (z.B.  Fuer_Casino)          : ")).replace(' ','_')
    if_brutto = input("- Bruttopreise (n/Enter=ja)               : ")
    print('---------------------------------------------------------------- Artikel Input :')

def artikel_angaben():  # Akzept artikel
    global artikelname, precio, artikelmenge
    artikelname = (input("-   Artikelname (z.B. Mause_USB) : ")).replace(' ','_')
    artikelpreis = (input("-   ArtikelPreis   (Enter = 0)   : ")).replace(',','.')
    if artikelpreis == '': artikelpreis = 0
    precio = currency(float(artikelpreis))
    if if_brutto == 'n':
        precio = currency((precio * 0.19) + precio)
    converter()
    print("       ###  Bruttopreis    : ", precio)
    artikelmenge = (input("-   Menge (Enter = 1)   : "))
    if artikelmenge == '': artikelmenge = '1'

def namepdf():  # Aendert die Rechnung zum gegebene Ordner mit angepasste Name
    global pdfrechungsfile, ziel
    pdfrechnungsname = (einkaufdatum + "-" + lieferant + "-" + bemerkung).replace('\t', '')
    # print('Standard: legen Sie die Rechnung in .PDF format in gleiche Ordner dieses Script mit der Name "file.pdf" ')
    # pdfrechungsfile = input("- Pfad + Name zur PDF-File z.B. /Users/john/file.pdf oder 'n' für keine PDF oder 's' fuer Standard Pfad) : ")
    pdfrechungsfile = input("- PDF-Rechnung importieren? [n=nein, s=standard:file.pdf, pfad+filename]\n")
    if not os.path.exists(zielverzeichnis2):
        os.makedirs(zielverzeichnis2)
    if not os.path.exists(zielverzeichnis3) and pdfrechungsfile != 'n': # <-- damit keine Ordner anliegt wenn keine Datei es gibt
        os.makedirs(zielverzeichnis3)
    ziel = Path(zielverzeichnis3 + pdfrechnungsname + ".pdf")
    #print(ziel)

def pdfrechnungsfile_import():
# pdfrechnungsfile kann ein path+filename, s oder n sein.
# s ist standard, also file.pdf in billorganizer Ordner und ist automatisch gelöscht
# n tut nicht, also keine pdf zu importieren auch keine Ordner anliegen
# path+filename import das pdf von dort aber lasst dort (muss manuel gelöscht werden)
    global pdfrechungsfile
    if pdfrechungsfile == 's':
        pdfrechungsfile = str(Path(((os.getcwd()) + '/file.pdf')))  # <-- beachtet auf Linux / Windows slash/backslash
        shutil.copyfile(pdfrechungsfile, ziel) # kopiert von Ziel
        os.remove(pdfrechungsfile) # lösch der Ziel
        print('### file.pdf importiert, Quell-Datei ist gelöscht! ###')
    elif pdfrechungsfile == 'n':
        print("### für diese Rechnung wurde keine PDF-Datei importiert! ###")
    else:
        shutil.copyfile(pdfrechungsfile, ziel)
        print('### PDF-Datei importiert, Quelle NICHT gelöscht! ###')

def reg_writter(): # Schreibt eine neue Linie in Datei CSV
    global endedesinput
    lista = [rechnungsnr, einkaufdatum, lieferant, artikelname, str(precio), bemerkung, artikelmenge, '\n']
    archivo.write("\t".join(lista))
    endedesinput = input("---------------------------------------------------------------- weitere Artikel? (j/n) : ")

def converter():  # korrigiert ein paar mögliche eingabefehler in der Preis OJO PARECE QUE NO SIRVE PARA NADA !!!
    global precio
    precio = (((str(precio)).replace(".","#")).replace(",",".")).replace("#",",")

def doppel_linie():
    print('===========================================================================================')
# ###################################################### PROGRAMM-BLOCK #

os.system('clear')
doppel_linie(); print('###                       Bills-Organizer - 2018                                        ###'); doppel_linie()
zielverzeichnis = str(Path(os.getcwd()))  # <-- findet aktive verzeichniss
zielverzeichnis2 = zielverzeichnis + '/RechnungenX/' # <--  baut ordner fuer Rechnungen

file='rechnungen_v2.csv'
csv_ziel = os.path.join(os.getcwd(), file)

archivo = open(csv_ziel, "a")

rechnung_angaben()  # --> rufmal die Eingabe von Rechnung-Info
zielverzeichnis3 = zielverzeichnis2 + '/' + jahro + '/'  # <-- baut Ordner für Rechnungen nach Jahr

while True:
    artikel_angaben()  # --> rufmal die Eingabe von Artikel-Name und Preis
    reg_writter()      # --> rufmal die Writter ein Register in CSV Datei bis noetig (esc=n)
    if endedesinput == 'n':
        break

namepdf()   # --> Eingabe, Uebertraegung und Nameanpassung der Rechnungsfile wenn noetig
pdfrechnungsfile_import()
doppel_linie(); print("###                                 S c h u s s !                                      ### "); doppel_linie()


archivo.closed
exit()
