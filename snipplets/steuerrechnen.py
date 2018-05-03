import locale

#locale.setlocale(locale.LC_ALL, "de_DE")
locale.setlocale(locale.LC_ALL, 'de_DE')

bruttopreise = input("- Bruttopreise? (n/Enter fuer ja)       : ")
artikelpreis = int(input("-   ArtikelPreis   (Enter = 0)   : "))
# artikelpreis = float(artikelpreis.replace(",","."))


precio1 = (artikelpreis * 0.19) + artikelpreis
precio2 = str(precio1)
print(locale.atoi(precio2))
   #  precio4 = locale.atof(precio)

