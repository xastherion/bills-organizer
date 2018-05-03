# Reconoce errores de entrada para formato de monedas y los convierte automaticamente
# 1234567 sera convertido en 1.234.567,00
# 1234567.00 sera convertido en 1.234.567,00
# 1234567,00 sera convertido ERROR porque es cadena y la funcion float no puede conv
# 1.234.567,00 sera ERROR igual que arriba

from re import *
global precio

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


def converter():
    global precio3
    precio0 = str(precio)               #<-- convierte precio en cadena
    precio1=precio0.replace(".","#")    #<-- convierte puntos en #
    precio2=precio1.replace(",",".")    #<-- convierte comas en puntos
    precio3=precio2.replace("#",",")    #<-- convierte # en comas


entrada=input("Precio : ")
precio = currency(float(entrada))

converter()
print(precio3)


# Analyzer :
# print('E --> ', entrada, 'P --> ', precio, 'P0 --> ', precio0, 'P1 --> ', precio1,'P2 --> ', precio2, 'P3 --> ', precio3)

