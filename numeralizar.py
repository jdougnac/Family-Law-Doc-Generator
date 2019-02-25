import random

def numeralizar(string):
    """Toma un número y lo convierte en palabras"""
    string=str(string)
    string=string.replace('.','')
    string=string.replace(' ','')
    remanente='f'
    if string[0] == '0':
        string = string[1:]
    if '-' in string:
        remanente=string[-1:]
        string=string[:-2]

    def unDigito(numero):   
        if numero=='1':
            return('un')
        elif numero == '2':
            return('dos')
        elif numero == '3':
            return('tres')
        elif numero == '4':
            return('cuatro')
        elif numero == '5':
            return('cinco')
        elif numero == '6':
            return('seis')
        elif numero == '7':
            return('siete')
        elif numero == '8':
            return('ocho')
        elif numero == '9':
            return('nueve')
        elif numero == '0':
            return('cero')

    def dosDigitos(numero):
        if numero ==  '10' :
            return('diez')
        if numero ==  '11' :
            return('once')
        if numero ==  '12' :
            return('doce')
        if numero ==  '13' :
            return('trece')
        if numero ==  '14' :
            return('catorce')
        if numero ==  '15' :
            return('quince')
        if numero ==  '16' :
            return('dieciséis')
        if numero ==  '17' :
            return('diecisiete')
        if numero ==  '18' :
            return('dieciocho')
        if numero ==  '19' :
            return('diecinueve')
        if numero ==  '20' :
            return('veinte')
        if numero ==  '21' :
            return('veintiuno')
        if numero ==  '22' :
            return('veintidós')
        if numero ==  '23' :
            return('veintitrés')
        if numero ==  '24' :
            return('veinticuatro')
        if numero ==  '25' :
            return('veinticinco')
        if numero ==  '26' :
            return('veintiséis')
        if numero ==  '27' :
            return('veintisiete')
        if numero ==  '28' :
            return('veintiocho')
        if numero ==  '29' :
            return('veintinueve')
        if numero[0] ==  '0' :
            return(unDigito(numero[1]))
        elif numero[0] ==  '3' :
            if numero[1] == '0':
                return('treinta')
            elif numero[1] != '0':
                return('treinta y ' + unDigito(numero[1]))                
                return(unDigito(numero[1]))
        elif numero[0] ==  '4' :
            if numero[1] == '0':
                return('cuarenta')
            elif numero[1] != '0':
                return('cuarenta y ' + unDigito(numero[1]))
                return(unDigito(numero[1]))
        elif numero[0] ==  '5' :
            if numero[1] == '0':
                return('cincuenta')
            elif numero[1] != '0':
                return('cincuenta y ' + unDigito(numero[1]))             
                return(unDigito(numero[1]))
        elif numero[0] ==  '6' :
            if numero[1] == '0':
                return('sesenta')
            elif numero[1] != '0':
                return('sesenta y ' + unDigito(numero[1]))                
                return(unDigito(numero[1]))
        elif numero[0] ==  '7' :
            if numero[1] == '0':
                return('setenta')
            elif numero[1] != '0':
                return('setenta y ' + unDigito(numero[1]))               
                return(unDigito(numero[1]))
        elif numero[0] ==  '8' :
            if numero[1] == '0':
                return('ochenta')
            elif numero[1] != 0:
                return('ochenta y ' + unDigito(numero[1]))
                return(unDigito(numero[1]))
        elif numero[0] ==  '9' :
            if numero[1] == '0':
                return('noventa')
            elif numero[1] != '0':
                return('noventa y ' + unDigito(numero[1]))                
                return(unDigito(numero[1]))
            
    def tresDigitos(numero):
        if numero[0] == '0':
            return(dosDigitos(numero[1:]))
        
        elif numero[0] == '1':
            if numero[1] == '0':
                if numero[2] == '0':
                    return('cien')
                else:
                    return('ciento ' + unDigito(numero[2]))
            else:
                return('ciento ' + dosDigitos(numero[1:]))
            
        elif numero[0] == '2':
            if numero[1] == '0':
                if numero[2] == '0':
                    return('doscientos')
                else:
                    return('doscientos ' + unDigito(numero[2]))
            else:
                return('doscientos ' + dosDigitos(numero[1:]))
            
        elif numero[0] == '3':
            if numero[1] == '0':
                if numero[2] == '0':
                    return('trescientos')
                else:
                    return('trescientos ' + unDigito(numero[2]))
            else:
                return('trescientos ' + dosDigitos(numero[1:]))
            
        elif numero[0] == '4':
            if numero[1] == '0':
                if numero[2] == '0':
                    return('cuatrocientos')
                else:
                    return('cuatrocientos ' + unDigito(numero[2]))
            else:
                return('cuatrocientos ' + dosDigitos(numero[1:]))

        elif numero[0] == '5':
            if numero[1] == '0':
                if numero[2] == '0':
                    return('quinientos')
                else:
                    return('quinientos ' + unDigito(numero[2]))
            else:
                return('quinientos ' + dosDigitos(numero[1:]))

        elif numero[0] == '6':
            if numero[1] == '0':
                if numero[2] == '0':
                    return('seiscientos')
                else:
                    return('seiscientos ' + unDigito(numero[2]))
            else:
                return('seiscientos ' + dosDigitos(numero[1:]))

        elif numero[0] == '7':
            if numero[1] == '0':
                if numero[2] == '0':
                    return('setecientos')
                else:
                    return('setecientos ' + unDigito(numero[2]))
            else:
                return('setecientos ' + dosDigitos(numero[1:]))

        elif numero[0] == '8':
            if numero[1] == '0':
                if numero[2] == '0':
                    return('ochocientos')
                else:
                    return('ochocientos ' + unDigito(numero[2]))
            else:
                return('ochocientos ' + dosDigitos(numero[1:]))

        elif numero[0] == '9':
            if numero[1] == '0':
                if numero[2] == '0':
                    return('novecientos')
                else:
                    return('novecientos ' + unDigito(numero[2]))
            else:
                return('novecientos ' + dosDigitos(numero[1:]))


    def cuatroDigitos(numero):
        if numero[0] == '0':
            return (tresDigitos(numero[1:]))

        elif numero[0] == '1':
            if numero[1] == '0' and numero[2] == '0' and numero[3] == '0':
                return('mil')
            else:
                return('mil ' + tresDigitos(numero[1:]))

        elif numero[0] == '2':
            if numero[1] == '0' and numero[2] == '0' and numero[3] == '0':
                return('dos mil')
            else:
                return('dos mil ' + tresDigitos(numero[1:]))

        elif numero[0] == '3':
            if numero[1] == '0' and numero[2] == '0' and numero[3] == '0':
                return('tres mil')
            else:
                return('tres mil ' + tresDigitos(numero[1:]))

        elif numero[0] == '4':
            if numero[1] == '0' and numero[2] == '0' and numero[3] == '0':
                return('cuatro mil')
            else:
                return('cuatro mil ' + tresDigitos(numero[1:]))            

        elif numero[0] == '5':
            if numero[1] == '0' and numero[2] == '0' and numero[3] == '0':
                return('cinco mil')
            else:
                return('cinco mil ' + tresDigitos(numero[1:]))

        elif numero[0] == '6':
            if numero[1] == '0' and numero[2] == '0' and numero[3] == '0':
                return('seis mil')
            else:
                return('seis mil ' + tresDigitos(numero[1:]))

        elif numero[0] == '7':
            if numero[1] == '0' and numero[2] == '0' and numero[3] == '0':
                return('siete mil')
            else:
                return('siete mil ' + tresDigitos(numero[1:]))

        elif numero[0] == '8':
            if numero[1] == '0' and numero[2] == '0' and numero[3] == '0':
                return('ocho mil')
            else:
                return('ocho mil ' + tresDigitos(numero[1:]))

        elif numero[0] == '9':
            if numero[1] == '0' and numero[2] == '0' and numero[3] == '0':
                return('nueve mil')
            else:
                return('nueve mil ' + tresDigitos(numero[1:]))            

    def cincoDigitos(numero):
        if numero[0] == '0':
            return cuatroDigitos(numero[1:])
        elif numero[2] == '0' and numero[3] == '0' and numero[4] == '0':
            return (dosDigitos(numero[0:2]) + ' mil')
        else:
            return (dosDigitos(numero[0:2]) + ' mil ' + tresDigitos(numero[2:]))

    def seisDigitos(numero):
        if numero[0] == '0':
            return cincoDigitos(numero[1:])
        elif numero[3] == '0' and numero[4] == '0' and numero[5] == '0':
            return (tresDigitos(numero[0:3]) + ' mil')
        else:
            return (tresDigitos(numero[0:3]) + ' mil ' + tresDigitos(numero[3:]))

    def sieteDigitos(numero):
        if numero[0] == '0':
            return seisDigitos(numero[1:])

        elif numero[0] == '1':
            if numero[1] == '0' and numero[2] == '0' and numero[3] == '0' and numero[4] == '0' and numero[5] == '0':
                return('un millón')
            else:
                return('un millón ' + seisDigitos(numero[1:]))

        else: 
            if numero[1] == '0' and numero[2] == '0' and numero[3] == '0' and numero[4] == '0' and numero[5] == '0' and numero[6] == '0':
                return(unDigito(numero[0]) + ' millones')
            else:
                return(unDigito(numero[0]) + ' millones ' + seisDigitos(numero[1:]))

    def ochoDigitos(numero):
        if numero[0] == '0':
            return sieteDigitos(numero[1:])
        elif numero[2] == '0' and numero[3] == '0' and numero[4] == '0' and numero[5] == '0' and numero[6] == '0' and numero[7] == '0':
            return(dosDigitos(numero[0:2]) + ' millones ')            
        else: 
            return(dosDigitos(numero[0:2]) + ' millones ' + seisDigitos(numero[2:]))

    def nueveDigitos(numero):
        if numero[0] == '0':
            return ochoDigitos(numero[1:])
        elif numero[3] == '0' and numero[4] == '0' and numero[5] == '0' and numero[6] == '0' and numero[7] == '0' and numero[8] == '0':
            return(tresDigitos(numero[0:3]) + ' millones ')            
        else: 
            return(tresDigitos(numero[0:3]) + ' millones ' + seisDigitos(numero[3:]))


    def diezDigitos(numero):
        if numero[0] == '0':
            return nueveDigitos(numero[1:])
        elif numero[4] == '0' and numero[5] == '0' and numero[6] == '0' and numero[7] == '0' and numero[8] == '0' and numero[9] == '0' :
            return(cuatroDigitos(numero[0:4]) + ' millones ')            
        else: 
            return(cuatroDigitos(numero[0:4]) + ' millones ' + seisDigitos(numero[4:]))

    def onceDigitos(numero):
        if numero[0] == '0':
            return diezDigitos(numero[1:])
        elif numero[5] == '0' and numero[6] == '0' and numero[7] == '0' and numero[8] == '0' and numero[9] == '0' and numero[10] == '0':
            return(cincoDigitos(numero[0:5]) + ' millones ')            
        else: 
            return(cincoDigitos(numero[0:5]) + ' millones ' + seisDigitos(numero[5:]))        

    def doceDigitos(numero):
        if numero[6] == '0' and numero[7] == '0' and numero[8] == '0' and numero[9] == '0' and numero[10] == '0' and numero[11] == '0':
            return(seisDigitos(numero[0:6]) + ' millones ')            
        else: 
            return(seisDigitos(numero[0:6]) + ' millones ' + seisDigitos(numero[6:]))  

    def getRemanente(numero):
        if 'k' in numero or 'K' in numero:
            return(' guión K')
        else:
            return(' guión ' + unDigito(numero))

    if len(string) == 1:
        if remanente == 'f':        
            return(unDigito(string))
        else:
            return(unDigito(string) + getRemanente(remanente))
    if len(string) == 2:
        if remanente == 'f':
            return(dosDigitos(string))
        else:
            return(dosDigitos(string) + getRemanente(remanente))
            
    if len(string) == 3:
        if remanente == 'f':
            return(tresDigitos(string))
        else:
            return(tresDigitos(string) + getRemanente(remanente))
    if len(string) == 4:
        if remanente == 'f':
            return(cuatroDigitos(string))
        else:
            return(cuatroDigitos(string) + getRemanente(remanente))
    if len(string) == 5:
        if remanente == 'f':
            return(cincoDigitos(string))
        else:
            return(cincoDigitos(string) + getRemanente(remanente))
    if len(string) == 6:
        if remanente == 'f':
            return(seisDigitos(string))
        else:
            return(seisDigitos(string) + getRemanente(remanente))
    if len(string) == 7:
        if remanente == 'f':
            return(sieteDigitos(string))
        else:
            return(sieteDigitos(string) + getRemanente(remanente))
    if len(string) == 8:
        if remanente == 'f':
            return(ochoDigitos(string))
        else:
            return(ochoDigitos(string) + getRemanente(remanente))
    if len(string) == 9:
        if remanente == 'f':
            return(nueveDigitos(string))
        else:
            return(nueveDigitos(string) + getRemanente(remanente))
    if len(string) == 10:
        if remanente == 'f':
            return(diezDigitos(string))
        else:
            return(diezDigitos(string) + getRemanente(remanente))
    if len(string) == 11:
        if remanente == 'f':
            return(onceDigitos(string))
        else:
            return(onceDigitos(string) + getRemanente(remanente))
    if len(string) == 12:
        if remanente == 'f':
            return(doceDigitos(string))
        else:
            return(doceDigitos(string) + getRemanente(remanente))


def getRut(numero):
    '''Esta función se usa cuando lo que se quiere pasar a palabras es un RUT'''
    rut = numeralizar(numero)
    if rut[-2:] == 'un':
        return (rut + 'o')
    else:
        return(rut)

                
def tenerNumero(string):
    numeros=['0','1','2','3','4','5','6','7','8','9']
    lista=string.split(' ')
    listaFinal=[]
    for item in lista:
        if item[0] in numeros:
            listaFinal.append(numeralizar(item))
        else:
            listaFinal.append(item)
    listaFinal=' '.join(listaFinal)
    return(listaFinal)


def tenerRIT(string):
    numeros=['0','1','2','3','4','5','6','7','8','9']
    lista=string.split('-')
    listaFinal=[]
    for item in lista:
        if item[0] in numeros:
            listaFinal.append(numeralizar(item))
        else:
            listaFinal.append(item)
    listaFinal=' guión '.join(listaFinal)
    return(listaFinal)

