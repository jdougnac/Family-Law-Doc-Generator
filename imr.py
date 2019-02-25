from decimal import *

def ingresoMinimo(alimentos, IMR):
    '''Esta función toma el valor de los alimentos menores que serán pagados, y
        da su equivalente en decimales o cantidad de ingresos mínimos'''

    g=Decimal((int(alimentos)/int(IMR))*100)
    if g < 100:
        final = int(g)
        return('l '+str(final)+'% de un Ingreso Mínimo Remuneracional')
    elif g == 100:
        final = 1
        return(' un Ingreso Mínimo Remuneracional')
    elif g > 100:
        final = str(round(g/100,1))
        if final[-2:] == '.0':
            final = int(final)
            return(str(final)+ ' Ingresos Mínimos Remuneracionales')  
        else:
            return(str(final)+ ' Ingresos Mínimos Remuneracionales')

         