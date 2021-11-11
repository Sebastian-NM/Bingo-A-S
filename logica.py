'''
Proyecto programado 2
Tema: Gestor de Bingos
Integrantes:
-Valentina Mende Solano, 2021142085
-Jorge Arturo Guadamuz Godinez, 2021132991
-Daniel Josué Aguilar Gómez, 2020184120
'''

#Inicio de Imports
import os
import menuPrincipal as MP
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
from random import *
from shutil import rmtree
from PIL import Image
from PIL import ImageFont 
from PIL import ImageDraw
from datetime import date
from datetime import datetime
#Fin de Imports



#Inicio variables gobales
#cartone (dict)
cartones ={}
#jugadores (dict)
jugadores={}
#jugadoresConCartones (dict)
jugadoresConCartones={}
#cartonesJuego (dict)
cartonesJuego={}
#listaIdentificadores (list)
listaIdentificadores =[]
#identificadoresLibres (list)
identificadoresLibres =[]
#listaNumerosCantados (list)
listaNumerosCantados = []
#listaGanadores (list)
listaGanadores=[]
#tipoJuego (str)
tipoJuego=""
#premio (str)
premio=""
#Fin variables gobales



'''
Entradas:
- numero
Salidas:
- numero (str)
Restriciones:
- numero (int)
- numero > 3
'''
#Función que crea 3 números random
def crearNumero(numero=3):
    if(numero==0):
        return ""
    #fin del if
    return str(randint(0,9))+crearNumero(numero-1)
#Fin de la función 



'''
Entradas:
- numero
Salidas:
- letras (str)
Restriciones:
- numero (int)
- numero > 3
'''
#Función que crea 3 letras aleatorias para la identificación
def crearLetras(numero=3):
    #abecedario (list)
    abecedario=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    #indice (int)
    indice = randrange(len(abecedario))
    
    if(numero==0):
        return ""
    #fin del if
    
    return abecedario[indice]+crearLetras(numero-1)
#Fin de la función crearLetras()



'''
Entradas:
- crearLetras
- crearNumero
Salidas:
- identificardor (str)
Restriciones:
- crearLetras (función)
- crearNumero (función)
'''
#Función que crea el identificador de los cartones
def crearIdententificador():
    #identificardor (str)
    identificardor =crearLetras() + crearNumero()
    
    return identificardor
#Fin de la función crearIdententificador()



'''
Entradas:
- pLista
- pIdentificador
Salidas:
- pIdentificador existe en pLista (bool)
Restriciones:
- pLista (lista)
- pIdentificador (str)
'''
#Función que indica si pIdentificador existe en pLista
def identificadorRepetido(pLista,pIdentificador):
    if(pLista==[]):
        return False
    elif(pLista[0]==pIdentificador):
        return True
    else:
        return identificadorRepetido(pLista[1:],pIdentificador)
    #Fin del if
#Fin de la función identificadorRepetido()



'''
Entradas:
- pNum
Salidas:
- listaIdentificadores (list)
Restriciones:
- pNum (int)
- pNum > 0
'''
#Función que crea una lista de posibles identificadores
def crearListaIdentificadores(pNum):
    if(pNum==0):
        return []
    else:
        return [crearIdententificador()] + crearListaIdentificadores(pNum-1)
    #Fin del if
#Fin de la función crearListaIdentificadores()



'''
Entradas:
- pNum
Salidas:
- lista (list)
Restriciones:
- pNum (int)
- pNum > 0
'''
#Función que crea una lista con identificadores no repetidos
def crearListaIdentificadoresNoRepetidos(pNum):
    #lista (list)
    lista = crearListaIdentificadores(pNum)
    #indice (int)
    indice = 0
    
    while(indice<len(lista)):
        
        if( identificadorRepetido(lista[indice+1:],lista[indice]) ):
            indice = 0
            lista = crearListaIdentificadores(pNum)
        #Fin del if
        indice = indice + 1
    #Fin del while

    return lista
#Fin de la función crearListaIdentificadoresNoRepetidos()



'''
Entradas:
- pInicio
- pFin
Salidas:
- listaNumeros (list)
Restriciones:
- pInicio (int)
- pInicio > 0
- pFin (int)
- pFin > 0
'''
#Función que crea 5 números random segun pInicio y pFin 
def crearNumerosRandomCarton(pInicio,pFin,Numero=5):
    if(Numero==0):
        return []
    else:
        return [randrange(pInicio,pFin)]+crearNumerosRandomCarton(pInicio,pFin,Numero-1)
    #Fin del if
#Fin de la función crearNumerosRandomCarton()




'''
Entradas:
- pLista
Salidas:
- pLista tiene un elemento repetido (bool)
Restriciones:
- pLista (list)
- pLista !=[]
'''
#Función que indica si algun número del carton esta repetido
def recorrerElementosCarton(pLista):
    if(pLista==[]):
        return False
    elif( identificadorRepetido(pLista[1:],pLista[0])):
        return True
    else:
        return recorrerElementosCarton(pLista[1:])
    #Fin del if
#Fin del función recorrerElementosCarton()
    



'''
Entradas:
- pInicio
- pFin
Salidas:
- fila (list)
Restriciones:
- pInicio (int)
- pInicio > 0
- pFin (int)
- pFin > 0
'''
#Función que crea un carton
def crearNumerosCarton(pInicio,pFin):
    #fila (list)
    fila=[]
    while(True):
        fila=crearNumerosRandomCarton(pInicio,pFin)
        if(recorrerElementosCarton(fila)==False):
            return fila
        #Fin if
    #Fin while
#Fin de la función crearNumerosCarton()

'''
Entradas:
- carton
- vector
Salidas:
- carton (matriz)
Restriciones:
- carton (matriz)
- carton !=[]
- vector (array)
- vector !=[]
'''
#Función que crea y acomoda los elementos del cartón
def crearElementosCarton():
    #carton (list)
    carton=[]
    #vector (list)
    vector=[]
    #fila1 (list)
    fila1=crearNumerosCarton(1,15)
    #fila2 (list)
    fila2=crearNumerosCarton(16,30)
    #fila3 (list)
    fila3=crearNumerosCarton(31,45)
    #fila4 (list)
    fila4=crearNumerosCarton(46,60)
    #fila5 (list)
    fila5=crearNumerosCarton(61,75)
    #indiceA (list)
    indiceA=0
    #indiceA (list)
    indiceB=0
 
    while(indiceA<5):
        vector.append(fila1[indiceA])
        vector.append(fila2[indiceA])
        vector.append(fila3[indiceA])
        vector.append(fila4[indiceA])
        vector.append(fila5[indiceA])
        carton.append(vector)
        vector=[]
        indiceA=indiceA+1
    #Fin del while

    return carton
#Fin del algoritmo crearElementosCarton()





'''
Entradas:
- pNum
Salidas:
- cartones (matriz)
Restriciones:
- pNum (int)
- pNum >= 0
'''
#Función que crea los cartones
def crearCarton(pNum):
    global cartones
    global listaIdentificadores

    #indentificadores (list)
    indenticadores = crearListaIdentificadoresNoRepetidos(pNum)
    listaIdentificadores = indenticadores

    #indice (int)
    indice=0
    while(indice<pNum):
        cartones[indenticadores[indice]] = crearElementosCarton()
        indice = indice+1
    #fin del while
        
    return cartones
#Fin de la función crearCarton()


  
'''
Entradas:
- cartones
Salidas:
- cartones (bool)
Restriciones:
- cartones (file)
- cartones debe de existir la carpeta
'''
#Algoritmo que identifica si existe la carpeta cartones
def existeCarpetaCartones():
    if os.path.isdir('cartones'):
        return True
    else:
       return False
    #Fin del if
#Fin del algoritmo existeCarpetaCartones()


'''
Entradas:
- cartones
- listaIdentificadores
Salidas:
- eliminar carpeta de cartones (file)
Restriciones:
- cartones (list)
- listaIdentificadores (list)
'''
#Algoritmo que elimina la carpeta de cartones
def eliminarCarpetaCartones():
    global cartones
    global listaIdentificadores
    
    try:
        rmtree("cartones")
        os.mkdir("cartones")
        listaIdentificadores=[]
        cartones={}
    except:
        pass
    #Fin del try

    if(existeCarpetaCartones()==False):
        os.mkdir("cartones")
    #Fin del if
#Fin del algoritmo eliminarCarpetaCartones()



'''
Entradas:
- cartones 
- jugadores
- jugadoresConCartones
- identificadoresLibres 
- listaIdentificadores 
- tipoJuego
- premio
- listaNumerosCantados 
- cartonesJuego
- listaGanadores
Salidas:
- limpieza de variables globales (función)
Restriciones:
- cartones (dict)
- cartones !={}
- jugadores (dict)
- jugadores !={}
- jugadoresConCartones (dict)
- jugadoresConCartones !={}
- identificadoresLibres (dict)
- identificadoresLibres !=[]
- listaIdentificadores (dict)
- listaIdentificadores !=[]
- tipoJuego (str)
- tipoJuego !=""
- premio (str)
- premio !=""
- premio (list)
- listaNumerosCantados !=[]
- cartonesJuego (dict)
- cartonesJuego !={}
- listaGanadores (list)
- listaGanadores !=[]
'''
#Algoritmo que limpia las variables globales
def eliminarRegistros():
    global cartones 
    global jugadores
    global jugadoresConCartones
    global identificadoresLibres 
    global listaIdentificadores 
    global tipoJuego
    global premio
    global listaNumerosCantados 
    global cartonesJuego
    global listaGanadores

    cartones ={}
    jugadores={}
    jugadoresConCartones={}
    identificadoresLibres =[]
    listaIdentificadores =[]
    tipoJuego=""
    premio=""
    listaNumerosCantados = []
    cartonesJuego={}
    listaGanadores=[]
#Fin del Algoritmo eliminarRegistros()




'''
Entradas:
- jugadores
Salidas:
- jugadores (bool)
Restriciones:
- jugadores (file)
- jugadores debe de existir
'''
#Algoritmo que identifica si existe la archivo jugadores
def existeArchivoJugadores():
    if os.path.isfile('jugadores/jugadores.csv'):
        return True
    else:
       return False
#Fin del algoritmo existeArchivoJugadores()



 
'''
Entradas:
- jugadores
Salidas:
- jugadores (bool)
Restriciones:
- jugadores (file)
- jugadores debe de existir
'''
#Algoritmo que identifica si existe la carpeta jugadores
def existeCarpetaJugadores():
    if os.path.isdir('jugadores'):
        return True
    else:
       return False
    #Fin del if
#Fin del algoritmo existeCarpetaJugadores()


'''
Entradas:
- pCedula
Salidas:
- existe jugador (bool)
Restriciones:
- pCedula (str)
- pCedula !=""
'''
#Función que indica si existe jugador
def existeJugador(pCedula):
    if(existeCarpetaJugadores()==False):
        return False
    #Fin del if
    
    with open("jugadores/jugadores.csv") as csvarchivo:
        #entrada (list)
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0]==pCedula):
                return True
            #Fin del if
        #Fin del for
        return False
#Fin de la función existeJugador()




'''
Entradas:
- pNombre
- pCedula
- pCorreo
Salidas:
- guardar 
Restriciones:
- pNombre (str)
- pNombre !=""
- pCedula (str)
- pCedula !=""
- pCorreo (str)
- pCorreo !=""
'''

#Función que crea un nuevo jugador en el archivo jugadores 
def crearJugador(pNombre,pCedula,pCorreo):
    if(existeCarpetaJugadores()==False):
        os.mkdir("jugadores")
    elif(existeArchivoJugadores()==False):
        rmtree("jugadores")
        os.mkdir("jugadores")
    #Fin if

    #archivo (file)
    archivo = open("jugadores/jugadores.csv","a")
    archivo.write(pCedula)
    archivo.write(";")
    archivo.write(pNombre)
    archivo.write(";")
    archivo.write(pCorreo+"\n")
    archivo.close()
#Fin de la funcion crearJugador


'''
Entradas:
- pCedula
Salidas:
- correo(str)
Restriciones:
- pCedula (str)
- pCedula !=""
'''
#Función que extrae el correo del jugador
def extraerCorreoJugador(pCedula):
    with open("jugadores/jugadores.csv") as csvarchivo:
        #entrada (file)
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0]==pCedula):
                return columna[2]
            #fin if
        #fin for
#Fin del función extraerCorreoJugador()
            




'''
Entradas:
- pCedula
Salidas:
- jugadoresConCartones (dict)
Restriciones:
- pCedula (str)
'''
#Funcion que identifica si existe pCedula
def jugadorConCarton(pCedula):
    global jugadoresConCartones

    try:
        jugadoresConCartones[pCedula]
        return True
    except:
        return False
#Fin de la función jugadorConCarton()



'''
Entradas:
- pCedula
Salidas:
- jugadoresConCartones (dict)
Restriciones:
- pCedula (str)
- pCedula !=""
'''
#Funcion que crea un jugador en el sistema
def crearJugadorConCartones(pCedula):
    global jugadoresConCartones

    jugadoresConCartones[pCedula] = []
#Fin de la función 
    


'''
Entradas:
- pCedula
Salidas:
- cartones (int)
Restriciones:
- pCedula (str)
- pCedula !=""
'''
#Función indica cuantos cartones tiene un jugador
def cantidadCartonesJugador(pCedula):
    global jugadoresConCartones
    #cartones (list)
    cartones = jugadoresConCartones[pCedula]
    
    return len(cartones)
#Fin de la función cantidadCartonesJugador()



'''
Entradas:
- pLista
- pIdentificador
Salidas:
- posicion de donde se encuentra el identificador (int)
Restriciones:
- pLista (list)
- pIdentificador
'''
#Función que identidica la posicion de identificador en la lista
def posicionIdentificador(pLista,pIdentificador,posicion=0):
    if(pLista==[]):
        return 0
    elif(pLista[0]==pIdentificador):
        return posicion
    #fin elif
    else:
        return posicionIdentificador(pLista[1:],pIdentificador,posicion+1)
    #fin if
#Fin de la función posicionIdentificador()



'''
Entradas:
- pIdentificadores
Salidas:
- identificadoresLibres (list)
Restriciones:
- pIdentificadores (list)
- pIdentificadores !=[]
'''
# Función que elimina los identificadores usados 
def eliminarIdentificadores(pIdentificadores):
    global identificadoresLibres
    #indice (int)
    indice = 0
    
    while(indice<len(pIdentificadores)):
        if(identificadorRepetido(identificadoresLibres,pIdentificadores[indice])):
            posicion = posicionIdentificador(identificadoresLibres,pIdentificadores[indice])
            identificadoresLibres.pop(posicion)
        #Fin if
        indice = indice + 1
    #Fin while
#Fin de la función 
        

    

'''
Entradas:
- identificadoresLibres
Salidas:
- identificadoresLibres (int)
Restriciones:
- identificadoresLibres (list)
- identificadoresLibres !=[]
'''
#Algoritmo que dice la cantidad de identificadores libres hay en el sistema
def cantidadIdentificadoresLibres():
    global identificadoresLibres
    return len(identificadoresLibres)
#Fin del algoritmo cantidadIdentificadoresLibres()



'''
Entradas:
- jugadoresConCartones
- identificadoresLibres
- listaIdentificadores
Salidas:
- eliminar los identificadores repetidos (list)
Restriciones:
- jugadoresConCartones (dict)
- jugadoresConCartones !={}
- identificadoresLibres (list)
- identificadoresLibres !=[]
- listaIdentificadores (list)
- listaIdentificadores !=[]
'''
#Función que eliminar los identificadores asignados a los jugadores
def listaIdentificadoresLibres():
    global jugadoresConCartones
    global identificadoresLibres
    global listaIdentificadores

    identificadoresLibres = listaIdentificadores.copy()


    for jugador in jugadoresConCartones:
        eliminarIdentificadores(jugadoresConCartones[jugador])
    #Fin del for
        
#Fin de la función listaIdentificadoresLibres()

        

'''
Entradas:
- pIdentificador
Salidas:
- jugador (dict)
Restriciones:
- pIdentificador (str)
- pIdentificador != ""
'''
#Función que 
def extraerIdentificadorJugadorConCarton(pIdentificador):
    global jugadoresConCartones
    global jugadores

    for jugador in jugadoresConCartones:
        for identificadores in jugadoresConCartones[jugador]:
            if(identificadores == pIdentificador):           
                return [jugador,jugadores[jugador][0]]
            #Fin if
        #Fin for
    #Fin for
#Fin de la función extraerIdentificadorJugadorConCarton()

            

'''
Entradas:
- pIdentificador
Salidas:
- existe identificador asosiado con jugador(bool)
Restriciones:
- pIdentificador 
'''
#Función que identifica si identificador asosiado con jugador
def identificarJugadorConCarton(pIdentificador):
    global jugadoresConCartones

    for jugador in jugadoresConCartones:
        for identificadores in jugadoresConCartones[jugador]:
            if(identificadores == pIdentificador):
                return True
            #Fin del if
        #Fin del for
    #Fin del for
            
    return False
#Fin de la función identificarJugadorConCarton()



'''
Entradas:
- pCedula
- pCartones
Salidas:
- enviar cartones a jugador (mail)
Restriciones:
- pCedula (str)
- pCartones (list)
'''
#Algoritmo que asigna los cartones a un jugador
def agragerCartonesAJugadores(pCedula,pCartones):
    global jugadoresConCartones
    global identificadoresLibres

    #lista (list)
    lista = jugadoresConCartones[pCedula]
    #indice (int)
    indice = 0

    if(pCartones<=len(identificadoresLibres)):
        while(indice<pCartones):
            #numero (str)
            numero = randrange(len(identificadoresLibres))
            lista.append(identificadoresLibres[numero])
            identificadoresLibres.pop(numero)
        #Fin while
    #Fin if
            
            
            indice = indice + 1

    jugadoresConCartones[pCedula] = lista
    enviarCartonesPorCorreo(pCedula)
#Fin de la función agragerCartonesAJugadores()


 
'''
Entradas:
- jugadores
Salidas:
- jugadores (int)
Restriciones:
- jugadores (list)
- jugadores !=[]
'''
#Algoritmo que extrae la cantidad de jugadores existentes en memoria
def extraerCantidadJugadores():
    global jugadores
    return len(jugadores)
#Fin del algoritmo extraerCantidadJugadores()



'''
Entradas:
- jugadores
Salidas:
- jugadores (list)
Restriciones:
- jugadores (file)
- jugadores debe de existir
- jugadores no puede estar vacio
'''
#Algortimo que crea una lista de los jugadores
def listaJugadores():
    global jugadores

    if(existeCarpetaJugadores()==False):
        os.mkdir("jugadores")
        archivo = open("jugadores/jugadores.csv","a")
        archivo.close()
    elif(existeArchivoJugadores()==False):
        rmtree("jugadores")
        os.mkdir("jugadores")
        archivo = open("jugadores/jugadores.csv","a")
        archivo.close()
    #Fin del if 


    with open("jugadores/jugadores.csv") as csvarchivo:
        #entrada (file)
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            jugadores[columna[0]] = [columna[1],columna[2]]
        #fin del for
#Fin del algoritmo listaJugadores()
                
    

'''
Entradas:
- pIdentificador
Salidas:
- identificadorRepetido (bool)
Restriciones:
- pIdentificador (str)
- pIdentificador != ""
'''
#Algoritmo que recorre todos los elementos existentes de la carpeta cartones
def existeImagenEnCarpeta(pIdentificador):
    archivos = [carpeta for carpeta in os.listdir("cartones/") if os.path.isfile(os.path.join("cartones/",carpeta))]
    
    return identificadorRepetido(archivos,pIdentificador+".png")
#Fin del algoritmo existeImagenEnCarpeta()

 

'''
Entradas:
- pCedula
Salidas:
- correo (mail)
Restriciones:
- pCedula (str)
- pCedula != ""
'''
#Función que envia los cartones asignados segun pCedula
def enviarCartonesPorCorreo(pCedula):
    global jugadores
    global jugadoresConCartones

    #listaCartones (list)
    listaCartones = jugadoresConCartones[pCedula]

    #sender_email (str)
    sender_email = "bingoproyecto2@gmail.com"
    #receiver_email (str)
    receiver_email =  jugadores[pCedula][1]

    #Se agregan la información necesaria para enviar el correo
    msg = MIMEMultipart()
    msg['Subject'] = 'Bingo, entrega de cartones'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #msgText = (str)
    msgText = MIMEText('Muchas gracias '+ jugadores[pCedula][0]+ " por participar en el juego, te adjuntamos tus cartones.\n¡Mucha suerte!")
    msg.attach(msgText)

    #indice (int)
    indice = 0
    while(indice<len(listaCartones)):
        with open('cartones/'+listaCartones[indice]+'.png', 'rb') as fp:
            #img (file)
            img = MIMEImage(fp.read())
            img.add_header('Content-Disposition', 'attachment', filename= listaCartones[indice]+".png")
            msg.attach(img)
        indice = indice + 1
    #Fin del while

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login("bingoproyecto2@gmail.com", "Tecdigital")
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)
#Fin de la función enviarCartonesPorCorreo()



'''
Entradas:
- pTipoJuego
- pPremio 
Salidas:
- tipoJuego (str)
- premio (str)
Restriciones:
- pTipoJuego (str)
- pTipoJuego != ""
- pPremio (str)
- pPremio != ""
'''
#Función que conecta los datos de la interfaz grafico con la logica
def guardarDatosJuego(pTipoJuego,pPremio):
    global tipoJuego
    global premio
    
    premio = pPremio
    tipoJuego = pTipoJuego
#Fin de la funcion guardarDatosJuego()



'''
Entradas:
- listaNumerosCantados
Salidas:
- listaNumerosCantados (int)
Restriciones:
- listaNumerosCantados (list)
- listaNumerosCantados !=[]
'''
#Algoritmo que retonar el ultimo número cantado
def ultimoNumeroCantado():
    global listaNumerosCantados
    
    return listaNumerosCantados[-1]
#Fin del algoritmo ultimoNumeroCantado()



'''
Entradas:
- tipoJuego 
- premio 
Salidas:
- tipoJuego (str)
- premio (str)
Restriciones:
- tipoJuego (str)
- tipoJuego != ""
- premio (str)
- premio != ""
'''
#Algoritmo que envia los datos de juego
def enviarDatosJuego():
    global tipoJuego
    global premio
    
    return tipoJuego,premio
#Fin del algoritmo enviarDatosJuego()



'''
Entradas:
- cartones
Salidas:
- cartones (int)
Restriciones:
- cartones (list)
- cartones !=[]
'''
#Algoritmo que retorna la cantidad de cartones existentes
def enviarTotalCartones():
    global cartones
    return len(cartones)
#Fin del algoritmo enviarTotalCartones()



'''
Entradas:
- numero
Salidas:
- numero (int)
Restriciones:
- numero (int)
- numero >=0
'''
#Funcion que crea un numero entre 0 y 75
def crearNumerosPartida():
    #numero (int)
    numero = randint(0,75)
    return numero
#Fin de la funcón crearNumerosPartida()



'''
Entradas:
- numero
Salidas:
- listaNumerosCantados (list)
Restriciones:
- numero (str)
'''
#Algoritmo que crea un nuevo cantado
def agregarNumeroASecuencia():
    global listaNumerosCantados
    #numero (int)
    numero = crearNumerosPartida()
    
    while(True):
        if(identificadorRepetido(listaNumerosCantados,numero)==False):
            listaNumerosCantados.append(numero)
            break
        else:
            numero = crearNumerosPartida()
        #Fin del if
    #Fin del while

    return listaNumerosCantados
#Fin algortimo agregarNumeroASecuencia()



'''
Entradas:
- pCarton
Salidas:
- matriz (matriz)
Restriciones:
- pCarton (matriz)
- pCarton !=[]
'''
#Función que marca el carton segun el número cantado
def marcarNumero(pCarton):
    global listaNumerosCantados
    #matriz (matriz)
    matriz = [[],[],[],[],[]]
    #indiceA (int)
    indiceA=0
    #indiceB (int)
    indiceB=0
    
    while(indiceA<len(pCarton)):
        while(indiceB<len(pCarton[indiceA])):
            if(pCarton[indiceA][indiceB]==listaNumerosCantados[-1]):
                matriz[indiceA].append("X")
            else:
                matriz[indiceA].append(pCarton[indiceA][indiceB])
            indiceB = indiceB + 1
            #Fin del if
        #Fin del while
        indiceB = 0            
        indiceA = indiceA + 1
    #Fin del while

    return matriz
#Fin de la función  marcarNumero()



'''
Entradas:
- pCarton
Salidas:
- carton es un juego en X (bool)
Restriciones:
- pCarton (matriz)
- pCarton !=[]
'''
#Algoritmo que identifica si el pCarton es un juego en X
def juegoEnX(pCarton):
    #identificador (int)
    identificador=len(pCarton)
    #indiceA (int)
    indiceA=0
    #indiceB (int)
    indiceB=0
    
    while(indiceA<len(pCarton)):
        identificador = identificador - 1
        while(indiceB<len(pCarton[indiceA])):
            if(indiceB==indiceA or indiceB==identificador):
                if(pCarton[indiceA][indiceB]!="X"):  
                    return False
                #Fin del if
            #Fin del if
            indiceB = indiceB + 1
        indiceB = 0

        indiceA = indiceA + 1
        #Fin del while
    #Fin del while
    return True
#Fin de la función juegoEnX()



'''
Entradas:
- pCarton
Salidas:
- carton es un juego en esquinas (bool)
Restriciones:
- pCarton (matriz)
- pCarton !=[]
'''
#Algoritmo que identifica si el pCarton es un juego en esquinas
def juegoCuatroEsquinas(pCarton):
    #identificador (int)
    identificador=len(pCarton)-1
    #indiceA (int)
    indiceA=0
    #indiceB (int)
    indiceB=0
    
    while(indiceA<len(pCarton)):
        while(indiceB<len(pCarton[indiceA])):
            if((indiceA==0 and indiceB==0) or (indiceA==0 and indiceB==identificador)):
                if(pCarton[indiceA][indiceB]!="X"):  
                    return False
                #Fin del if
            #Fin del if
            if((indiceA==4 and indiceB==0) or (indiceA==4 and indiceB==identificador)):
                if(pCarton[indiceA][indiceB]!="X"):  
                    return False
                #Fin del if
            #Fin del if
            indiceB = indiceB + 1
        #Fin del while
        indiceB = 0
        indiceA = indiceA + 1
    #Fin del while
    return True
#Fin de la función juegoCuatroEsquinas()



'''
Entradas:
- pCarton
Salidas:
- carton es un juego completo (bool)
Restriciones:
- pCarton (matriz)
- pCarton !=[]
'''
#Algoritmo que identifica si el pCarton es un juego completo
def juegoCartonCompleto(pCarton):
    #indiceA (int)
    indiceA=0
    #indiceB (int)
    indiceB=0
    
    while(indiceA<len(pCarton)):
        while(indiceB<len(pCarton[indiceA])):
            if(pCarton[indiceA][indiceB]!="X"):  
                return False
            #Fin del if
            indiceB = indiceB + 1
        #Fin del while
        indiceB = 0

        indiceA = indiceA + 1
    #Fin del while
    return True

#Fin de la función juegoCartonCompleto()



'''
Entradas:
- pCarton
Salidas:
- carton es un juego en Z (bool)
Restriciones:
- pCarton (matriz)
- pCarton !=[]
'''
#Algoritmo que identifica si el pCarton es un juego en Z 
def juegoEnZ(pCarton):
    #diagonalInversa (int)
    diagonalInversa=len(pCarton)
    #indiceA (int)
    indiceA=0
    #indiceB (int)
    indiceB=0
    
    while(indiceA<len(pCarton)):
        diagonalInversa = diagonalInversa - 1
        while(indiceB<len(pCarton[indiceA])):
            if(indiceA==0 or indiceA==4):
                if(pCarton[indiceA][indiceB]!="X") :  
                    return False
                #Fin del if
            #Fin del if
            if(indiceB == diagonalInversa):
                if(pCarton[indiceA][indiceB]!="X") :  
                    return False
                #Fin del if
            #Fin del if
            indiceB = indiceB + 1
            
        indiceB = 0
        indiceA = indiceA + 1
    return True
#Fin de la función juegoEnZ()



'''
Entradas:
- cartones
Salidas:
- cartonesJuego (dict)
Restriciones:
- cartones (dict)
- cartones !={}
'''
#Algoritmo que crea una copia de cartones
def copiaCartones():
    global cartones
    global cartonesJuego

    cartonesJuego = cartones.copy()
#Fin del algortimo copiaCartones()



'''
Entradas:
- cartonesJuego
Salidas:
- cartonesJuego (dict)
Restriciones:
- cartonesJuego (dict)
- cartonesJuego != {}
'''
#Algoritmo que marca a los cartones
def marcarCartones():
    global cartonesJuego
    
    for clave in cartonesJuego:
        cartonesJuego[clave]=marcarNumero(cartonesJuego[clave])
    #fin del for
#Fin del algoritmo marcarCartones()



'''
Entradas:
- listaGanadores
Salidas:
- listaGanadores (list)
Restriciones:
- listaGanadores (list)
'''
#Algoritmo que retonar la cantidad de ganadores
def retornarGanadores():
    global listaGanadores
    return listaGanadores
#Fin del algoritmo retornarGanadores()



'''
Entradas:
- pNombre
- pCarton
- pDestinatario
Salidas:
- correo (mail)
Restriciones:
- pNombre (str)
- pNombre !=""
- pCarton (str)
- pCarton !=""
- pDestinatario (str)
- pDestinatario !=""
'''
#Función que envia un correo a los ganadores
def enviarCorreoGanadores(pNombre,pCarton,pDestinatario):
    global tipoJuego
    global premio

    #sender_email (str)
    sender_email = "bingoproyecto2@gmail.com"
    #receiver_email (str)
    receiver_email =  pDestinatario

    #se prepara el correo para ser enviado
    msg = MIMEMultipart()
    msg['Subject'] = 'Bingo, ¡felicidades eres un ganador!'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #msgText (str)
    msgText = MIMEText('¡Mucar felicidades '+pNombre + "!\nEres un ganador en el tipo de juego "+str(tipoJuego)+", y tu premio es: "+str(premio)+"\nPor favor ponte en contacto con nosotros para reclamar tu premio.")
    msg.attach(msgText)


    with open('cartones/'+pCarton+'.png', 'rb') as fp:
        #img (file)
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename= pCarton+".png")
        msg.attach(img)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login("bingoproyecto2@gmail.com", "Tecdigital")
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)
    #Fin del try
        
#Fin de la función enviarCorreoGanadores()
import matplotlib .pyplot as plt



'''
Entradas:
- jugadores
- listaGanadores 
Salidas:
- Correos enviados a los ganadores (mail)
Restriciones:
- jugadores (list)
- jugadores !=""
- listaGanadores (list)
- listaGanadores !=""
'''
#Algoritmo que envia un correo a los ganadores
def enviarEmailGanadores():
    global listaGanadores
    jugadoresConCartones
    global jugadores 

    indiceA = 0
    while(indiceA<len(listaGanadores)):
        if(identificarJugadorConCarton(listaGanadores[indiceA])):
            informacionJugador= extraerIdentificadorJugadorConCarton(listaGanadores[indiceA])
            enviarCorreoGanadores(jugadores[informacionJugador[0]][0],listaGanadores[indiceA],jugadores[informacionJugador[0]][1])
        #Fin del if
        indiceA = indiceA + 1
    #Fin del while
        
#Fin del algortimo enviarEmailGanadores()


    
'''
Entradas:
- pModoJuego
Salidas:
- listaGanadores (list)
Restriciones:
- pModoJuego (str)
- pModoJuego !=""
'''
#Función que identifica si existe un ganador del juego
def identificarGanadores(pModoJuego):
    global cartonesJuego
    global listaGanadores
    
    for clave in cartonesJuego:           
        if(pModoJuego=='Jugar en X'):
            if(juegoEnX(cartonesJuego[clave])):
                listaGanadores.append(clave)
            #Fin del if
        #Fin del if    
        elif(pModoJuego=='Cuatro esquinas'):
            if(juegoCuatroEsquinas(cartonesJuego[clave])):
                listaGanadores.append(clave)
            #Fin del if
        #Fin del elif    
        elif(pModoJuego=='Cartón lleno'):
            if(juegoCartonCompleto(cartonesJuego[clave])):
                listaGanadores.append(clave)
            #Fin del if
        #Fin del elif
        elif(pModoJuego=='Jugar en Z'):
            if(juegoEnZ(cartonesJuego[clave])):
                listaGanadores.append(clave)
            #Fin del if
        #Fin del elif
    #Fin del for
#Fin del algoritmo identificarGanadores()



'''
Entradas:
- cartonesJuego
Salidas:
- cartones marcados (matriz)
Restriciones:
- cartonesJuego
'''
#Algoritmo que imprime los cartones almacenados en memoria
def imprimirCartones():
    global cartonesJuego
    #matriz (matriz)
    matriz = cartonesJuego
    #indiceA (int)
    indiceA=0
    #indiceB (int)
    indiceB=0

    for clave in matriz:
        while(indiceA<len(matriz[clave])):
            indiceA = indiceA + 1
        #fin while
        indiceA = 0
    #fin del for
        
#Fin del algortimo imprimirCartones()



'''
Entradas:
- pModoJuego
Salidas:
- listaGanadores (bool)
Restriciones:
- pModoJuego (str)
'''
#Funcion que ejecuta una partida dependiendo de modo de juego
def cantarNumero(pModoJuego):
    global listaGanadores
    agregarNumeroASecuencia()
    marcarCartones()
    identificarGanadores(pModoJuego)
    
    if(listaGanadores!=[]):
        return True
    else:
        return False
    #Fin del if
#Fin de la función



'''
Entradas:
- pCarton
- pIdentificador
Salidas:
- imagen del carton (img)
Restriciones:
- pCarton (matrix)
- pCarton != []
- pIdentificador (str)
- pIdentificador != ""
'''
#Función que crea la imagen de los cartones
def crearImagen(pCarton,pIdentificador):
    #img (file)
    img = Image.open('tabla.png')
    #Se usa la función draw para dibujar encima de la imafen
    draw = ImageDraw.Draw(img)
    #Se establece el tipo de fuente a utilizar
    fuente = ImageFont.truetype("fuente\Staatliches-Regular.ttf", 60)
    #Se dibuja la primera linea
    draw.text((100, 55),"B",(0,2,27),font=fuente)
    draw.text((280, 55),"I",(0,2,27),font=fuente)
    draw.text((440, 55),"N",(0,2,27),font=fuente)
    draw.text((605, 55),"G",(0,2,27),font=fuente)
    draw.text((775, 55),"O",(0,2,27),font=fuente)
    #Se dibuja la segunda linea
    draw.text((100, 140),str(pCarton[0][0]),(0,2,27),font=fuente)
    draw.text((260, 140),str(pCarton[0][1]),(0,2,27),font=fuente)
    draw.text((430, 140),str(pCarton[0][2]),(0,2,27),font=fuente)
    draw.text((595, 140),str(pCarton[0][3]),(0,2,27),font=fuente)
    draw.text((760, 140),str(pCarton[0][4]),(0,2,27),font=fuente)
    #Se dibuja la tercera linea
    draw.text((100, 225),str(pCarton[1][0]),(0,2,27),font=fuente)
    draw.text((260, 225),str(pCarton[1][1]),(0,2,27),font=fuente)
    draw.text((430, 225),str(pCarton[1][2]),(0,2,27),font=fuente)
    draw.text((595, 225),str(pCarton[1][3]),(0,2,27),font=fuente)
    draw.text((760, 225),str(pCarton[1][4]),(0,2,27),font=fuente)
    #Se dibuja la cuarta linea
    draw.text((100, 310),str(pCarton[2][0]),(0,2,27),font=fuente)
    draw.text((260, 310),str(pCarton[2][1]),(0,2,27),font=fuente)
    draw.text((430, 310),str(pCarton[2][2]),(0,2,27),font=fuente)
    draw.text((595, 310),str(pCarton[2][3]),(0,2,27),font=fuente)
    draw.text((760, 310),str(pCarton[2][4]),(0,2,27),font=fuente)
    #Se dibuja la quinta linea
    draw.text((100, 395),str(pCarton[3][0]),(0,2,27),font=fuente)
    draw.text((260, 395),str(pCarton[3][1]),(0,2,27),font=fuente)
    draw.text((430, 395),str(pCarton[3][2]),(0,2,27),font=fuente)
    draw.text((595, 395),str(pCarton[3][3]),(0,2,27),font=fuente)
    draw.text((760, 395),str(pCarton[3][4]),(0,2,27),font=fuente)
    #Se dibuja la sexta linea
    draw.text((100, 480),str(pCarton[4][0]),(0,2,27),font=fuente)
    draw.text((260, 480),str(pCarton[4][1]),(0,2,27),font=fuente)
    draw.text((430, 480),str(pCarton[4][2]),(0,2,27),font=fuente)
    draw.text((595, 480),str(pCarton[4][3]),(0,2,27),font=fuente)
    draw.text((760, 480),str(pCarton[4][4]),(0,2,27),font=fuente)
    #Se dibuja la la ultima linea
    draw.text((210, 565),"Identificador: "+pIdentificador,(0,2,27),font=fuente)
    #Se crea la imagen
    img.save('cartones/'+pIdentificador+'.png')
#Fin de la función crearImagen()



'''
Entradas:
- bitacora 
Salidas:
- existencia de la archivo (bool)
Restriciones:
- bitacora (file)
'''
#Algoritmo que identifica si existe la archivo bitacora
def existeArchivoBitacora():
    if os.path.isfile('bitacoraPartidas/bitacora.csv'):
        return True
    else:
       return False
#Fin del algoritmo existeArchivoBitacora()



'''
Entradas:
- bitacoraPartidas 
Salidas:
- existencia de la carpeta (bool)
Restriciones:
- bitacoraPartidas (file)
'''
#Algoritmo que identifica si existe la carpeta bitacoraPartidas
def existeCarpetaBitacora():
    if os.path.isdir('bitacoraPartidas'):
        return True
    else:
       return False
#Fin del algoritmo existeCarpetaBitacora()



'''
Entradas:
- cartonesJuego
- tipoJuego
- premio
- listaNumerosCantados 
- listaGanadores
Salidas:
- limpieza de las variables globales (función)
Restriciones:
- cartonesJuego (dict)
- tipoJuego (str)
- premio (str)
- listaNumerosCantados (list)
- listaGanadores (list)
'''
#Algortimo que limpia todas las variables globales para empezar una nueva partida
def limpiarVariables():
    global cartonesJuego
    global tipoJuego
    global premio
    global listaNumerosCantados 
    global listaGanadores

    cartonesJuego={}
    tipoJuego=""
    premio=""
    listaNumerosCantados = []
    listaGanadores=[]
#Fin del algortimo



'''
Entradas:
- listaNumerosCantados
- tipoJuego
Salidas:
- bitacira (file)
Restriciones:
- listaNumerosCantados (list)
- listaNumerosCantados no puede estar vacía
- tipoJuego (str)
- tipoJuego no puede estar vacía
'''
#Algortimo que crea un registro nuevo en bitacora
def crearRegistro():
    global listaNumerosCantados
    global tipoJuego
    #listaInformacion (list)
    listaInformacion=[]
    #indice (int)
    indice =0
    #listaCedulas (list)
    listaCedulas = []
    
    while(indice<len(listaGanadores)):
        if(identificarJugadorConCarton(listaGanadores[indice])):
            listaInformacion = extraerIdentificadorJugadorConCarton(listaGanadores[indice])
            if(identificadorRepetido(listaCedulas,str(listaInformacion[0]))==False):
                listaCedulas.append(str(listaInformacion[0]))
            #fin del if
        #fin del if
        indice = indice + 1 
    #fin del while

    #dia (date)
    dia = date.today()
    #hora (date)
    hora = datetime.now()
    
    if(existeCarpetaBitacora()==False):
        os.mkdir("bitacoraPartidas")
    #fin del if
    elif(existeArchivoBitacora()==False):
        rmtree("bitacoraPartidas")
        os.mkdir("bitacoraPartidas")
    #fin del elif

    if(tipoJuego=='Jugar en X'):
       tipoJuego="X"
    #fin del if
    elif(tipoJuego=='Cuatro esquinas'):
        tipoJuego="E"
    #fin del elif
    elif(tipoJuego=='Cartón lleno'):
        tipoJuego="L"
    #fin del elif
    elif(tipoJuego=='Jugar en Z'):
        tipoJuego="Z"
    #fin del elif

    #archivo (file)
    archivo = open("bitacoraPartidas/bitacora.csv","a")
    archivo.write(tipoJuego)
    archivo.write(";")
    archivo.write(str(listaNumerosCantados))
    archivo.write(";")
    archivo.write(str(listaCedulas))
    archivo.write(";")
    archivo.write(str(dia.day)+"/"+str(dia.month)+"/"+str(dia.year))
    archivo.write(";")
    archivo.write(str(hora.hour)+":"+str(hora.minute)+"\n")
    archivo.close()
#Fin del algortimo crearRegistro()



'''
Entradas:
- matriz
Salidas:
- cartones (matriz)
Restriciones:
- matriz (matriz)
- matriz no puede estar vacio
'''
#Función que crea matrices
def imprimirMatriz():
    #matriz (matriz)
    matriz = crearCarton()
    #indice (int)
    indice=0
    while(indice<len(matriz)):
        print(matriz[indice])
        indice = indice + 1
    #fin while
#Algoritmo imprimirMatriz()



'''
Entradas:
- pNum
Salidas:
- cartones para el bingo (matrices)
Restriciones:
- pNum (int)
- pNum > 0
'''
#Función que crea los cartones segun pNum
def imprimirMatrices(pNum):
    #matriz (matriz)
    matriz = crearCarton(pNum)
    #indiceA (int)
    indiceA=0
    #indiceB (int)
    indiceB=0

    for clave in matriz:
        crearImagen(matriz[clave],clave)
        while(indiceA<len(matriz[clave])):
            print(matriz[clave][indiceA])
            indiceA = indiceA + 1
        #fin del while
        print(clave+"\n")
        indiceA = 0
    #fin del for
#Fin de la función imprimirMatrices()



'''
Entradas:
- bitacora
Salidas:
- tiposPartidasJugadas (list)
Restriciones:
- bitacora (file)
- bitacora debe de exitir
- bitacora no puede estar vacía
'''
#Algoritmo que extrae los tipos de juegos de las partidas en la bitacora
def extraerTiposPartidasJugadas():
    #tiposPartidasJugadas (list)
    tiposPartidasJugadas=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            tiposPartidasJugadas.append(columna[0])
        #fin del for

    return tiposPartidasJugadas
#Fin del algoritmo extraerTiposPartidasJugadas()



'''
Entradas:
- tiposPartidasJugadas
Salidas:
- juegos (list)
Restriciones:
- tiposPartidasJugadas (list)
- tiposPartidasJugadas no puede estar vacía
'''
#Algoritmo que clasifica las partidas segun las veces que se jugaron 
def crearDatosTiposPartidasJugadas():
    #tiposPartidasJugadas (list)
    tiposPartidasJugadas = extraerTiposPartidasJugadas()
    #tipoJuego (list)
    tipoJuego = ["X","Z","E","L"]
    #juegos (list)
    juegos=[]
    #indice (int)
    indice = 0
    #cantidad (int)
    cantidad = 0
    
    while(indice<len(tipoJuego)):
        cantidad = contarCaracter(tiposPartidasJugadas,tipoJuego[indice])
        juegos.append([tipoJuego[indice],cantidad])
        indice = indice + 1
    #fin del while

    return juegos
#Fin del algoritmo



'''
Entradas:
- pLista 
- pCaracter 
Salidas:
- cantidad (int)
Restriciones:
- pLista (list)
- pLista no puede estar vacía
- pCaracter (int/str)
- pCaracter no puede estar vacía
'''
#Función que indica cuantas veces aparece pCaracter
def contarCaracter(pLista,pCaracter):
    #indice (int)
    indice=0
    #cantidad (int)
    cantidad = 0
    
    while(indice<len(pLista)):
        if(pLista[indice]==pCaracter):
            cantidad = cantidad + 1
        #fin del if
        indice = indice + 1
    #fin del while

    return cantidad
#Fin de la función contarCaracter()



'''
Entradas:
- pLista
Salidas:
- listaNueva (int)
Restriciones:
- pLista (list)
- pLista no puede estar vacó
'''
#Algoritmo que elimina los elementos repetidos
def eliminarElementosRepetidosBitacora(pLista):
    #listaNueva (list)
    listaNueva = list(set(pLista))
    return listaNueva
#Fin de la función eliminarElementosRepetidosBitacora()



'''
Entradas:
- bitacora
Salidas:
- numerosCantados
Restriciones:
- bitacora (file)
- bitacora debe de existir
- bitacora no puede estar vacío
'''
#Algortimo que extrae los números cantados de la bitacora
def extraerNumerosCantados():
    #numerosCantados (list)
    numerosCantados=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            output=eval(columna[1])
            numerosCantados += output
        #fin del for

    return numerosCantados
#Fin del algoritmo extraerNumerosCantados()



'''
Entradas:
- numerosCantados
- numeros
Salidas:
- cantados (list)
Restriciones:
- numerosCantados (list)
- numerosCantados no puede estar vacío
- numeros (list)
- numeros no puede estar vacío
'''
#Algoritmo que une los números cantados con la cantidad de veces que fue cantado
def crearDatosNumerosContados():
    #numerosCantados (list)
    numerosCantados = extraerNumerosCantados()
    #numeros (list)
    numeros = eliminarElementosRepetidosBitacora(numerosCantados)
    #cantados (list)
    cantados=[]
    #indice (int)
    indice = 0
    #cantidad (int)
    cantidad = 0
    
    while(indice<len(numeros)):
        cantidad = contarCaracter(numerosCantados,numeros[indice])
        cantados.append([numeros[indice],cantidad])
        
        indice = indice + 1
    #Fin del while

    return cantados
#Fin del algortimo crearDatosNumerosContados()



'''
Entradas:
- lista
Salidas:
- [numero, mayor] (int,int)
Restriciones:
- lista (list)
- lista no puede estar vacía
'''
#Función que encuentra el número mayor
def encontrarMayor(lista):
    #indice (int)
    indice = 0
    #mayor (int)
    mayor = 0
    #numero (int)
    numero = 0
    
    while(indice<len(lista)):
        if(mayor<lista[indice][1]):
            mayor=lista[indice][1]
            numero =lista[indice][0]
        #fin del if
        indice = indice + 1
    #fin del while

    return [numero, mayor]
#Fin de la función encontrarMayor()



'''
Entradas:
- lista
- elemento
Salidas:
- listaNueva (list)
Restriciones:
- lista (list)
- lista no puede estar vacía
- elemento (str)
- elemento no puede estar vacío
'''
#Función que elimina el elemento mayor de lista segun elemento
def eliminarMayor(lista,elemento):
    #indice (int)
    indice = 0
    #listaNueva (list)
    listaNueva = []
    
    while(indice<len(lista)):
        if(lista[indice][0]!=elemento[0]):
            listaNueva.append([lista[indice][0],lista[indice][1]])
        #fin del if 
        indice = indice + 1
    #fin del while
            

    return listaNueva
#Fin de la funcion eliminarMayor()



'''
Entradas:
- lista
Salidas:
- elementosMayores (list)
Restriciones:
- lista (list)
- lista no puede estar vacía 
'''
#Algoritmo une los numeros con sus apariciones
def identificarNumerosMayores():
    #lista (list)
    lista = crearDatosNumerosContados()
    #elementosMayores (list)
    elementosMayores = []
    #indice (list)
    indice = 0
    #parada (list)
    parada = 10

    while(indice<parada):
        elementoMayor = encontrarMayor(lista)
        lista = eliminarMayor(lista,elementoMayor)
        elementosMayores.append(elementoMayor)
        indice = indice + 1
    #fin del while

    return elementosMayores
#Fin del algoritmo identificarNumerosMayores()



'''
Entradas:
- datos
Salidas:
- grafico de top 10 de números cantados (graph)
Restriciones:
- datos (list)
- datos no puede estar vacía
'''
#Algoritmo que crea un gráfico de top 10 de números cantados.
def graficoNumerosCantados():
    #datos (list)
    datos = identificarNumerosMayores()
    #indice (int)
    indice = 0
    #numeros (list)
    numeros=[]
    #porcentajes (list)
    porcentajes=[]
    
    while(indice<len(datos)):
        numeros.append(datos[indice][0])
        porcentajes.append(datos[indice][1])
        indice = indice + 1
    #fin del while

    ypos = np.arange(len(numeros))

    plt.xticks(ypos,numeros)
    #Se crea el gráfico de barras
    plt.bar(ypos,porcentajes, width=0.5)
    plt.title("Grafico de barras")
    plt.ylabel("Veces que aparecen")
    plt.xlabel("Números cantados")
    #Se muestra el gráfico
    plt.show()
#Fin del algoritmo graficoNumerosCantados()



'''
Entradas:
- bitacora
Salidas:
- numerosCantados (list)
Restriciones:
- bitacora (file)
- bitacora debe de existir
- bitacora no puede estar vacía
'''
#Funcion que extrae los ganadores de la bitacora
def extraerJugadoresGanadores():
    #numerosCantados (list)
    numerosCantados=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            output=eval(columna[2])
            numerosCantados += output
        #fin del for

    return numerosCantados
#Fin del algoritmo extraerJugadoresGanadores()



'''
Entradas:
- ganadores
- cedulas
Salidas:
- cantidadGanadores (list)
Restriciones:
- ganadores (list)
- ganadores no puede estar vacía
- cedulas (list)
- cedulas no puede estar vacía
'''
#Algortimo que intega los ganadores con la cantidad de veces que gano en una lista
def crearDatosJugadoresGanadores():
    #ganadores (list)
    ganadores = extraerJugadoresGanadores()
    #cedulas (list)
    cedulas = eliminarElementosRepetidosBitacora(ganadores)
    #cantidadGanadores (list)
    cantidadGanadores=[]
    #indice (int)
    indice = 0
    #cantidad (int)
    cantidad = 0

    
    while(indice<len(cedulas)):
        cantidad = contarCaracter(ganadores,cedulas[indice])
        cantidadGanadores.append([cedulas[indice],cantidad])
        indice = indice + 1
    #fin del while

    return cantidadGanadores
#Fin del algortimo crearDatosJugadoresGanadores()



'''
Entradas:
- bitacora
Salidas:
- fechasPartidas (list)
Restriciones:
- bitacora (file)
- bitacora no puede estar vacía
'''
#Algortimo que extrae las fechas de la bitacora
def extraerFechaPartidas():
    #fechasPartidas (list)
    fechasPartidas=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:           
            fechasPartidas.append(columna[3])
        #fin del for

    return fechasPartidas
#Fin del algoritmo extraerFechaPartidas()



'''
Entradas:
- fechasPartidas
- partidas 
Salidas:
- fechas (list)
Restriciones:
- fechasPartidas (list)
- fechasPartidas no puede estar vacía
- partidas (list)
- partidas no puede estar vacía
'''
#Algortimo que clasifica las fechas segun su aparición en la bitacora
def crearDatosFechaPartidas():
    #fechasPartidas (list)
    fechasPartidas = extraerFechaPartidas()
    #partidas (list)
    partidas = eliminarElementosRepetidosBitacora(fechasPartidas)
    #fechas (list)
    fechas=[]
    #indice (int)
    indice = 0
    #cantidad (int)
    cantidad = 0
    
    while(indice<len(partidas)):
        cantidad = contarCaracter(fechasPartidas,partidas[indice])
        fechas.append([partidas[indice],cantidad])
        indice = indice + 1
    #fin del while

    return fechas
#Fin del algoritmo crearDatosFechaPartidas()


'''
Entradas:
- lista
Salidas:
- elementosMayores (list)
Restriciones:
- lista (list)
- lista no puede estar vacía
'''
#Algoritmo que identidica las fechas con mas partidas jugadas
def identificarFechasMayores():
    #lista (list)
    lista = crearDatosFechaPartidas()
    #elementosMayores (list)
    elementosMayores = []
    #indice (list)
    indice = 0
    #parada (list)
    parada = 3

    while(indice<parada):
        elementoMayor = encontrarMayor(lista)
        lista = eliminarMayor(lista,elementoMayor)
        fecha = elementoMayor[0].split('/')
        
        elementosMayores.append([datetime( int(fecha[2]), int(fecha[1]), int(fecha[0])  )  ,  elementoMayor[1]])
        indice = indice + 1
    #fin del while

    return elementosMayores
#Fin del algoritmo identificarFechasMayores()



'''
Entradas:
- pLista
Salidas:
- fechas
Restriciones:
- pLista (list)
- pLista no puede estra vacía
'''
#Algortimo que ordena cronologicamente las fechas
def acomodarListas():
    #pLista (list)
    pLista = identificarFechasMayores()
    #indice (int)
    indice = 0
    #fechas (list)
    fechas = []
    
    while(indice<len(pLista)):
        fechas.append(pLista[indice][0])
        indice = indice + 1
    #fin del while

    fechas.sort()
    
    return fechas
#fin del algoritmo acomodarListas()



'''
Entradas:
- listaFechas
- pLista
Salidas:
- listaOrdenada (list)
Restriciones:
- listaFechas (list)
- listaFechas no puede estar vacia
- pLista (list)
- pLista no puede estar vacia
'''
#Algortimo que integra las fechas ordenas con su número de aparición
def integrarRepeticionFechas():
    #listaFechas (list)
    listaFechas = identificarFechasMayores()
    #pLista (list)
    pLista = acomodarListas()
    #indiceA (int)
    indiceA = 0
    #indiceB (int)
    indiceB = 0
    #listaOrdenada (list)
    listaOrdenada=[]
    
    while(indiceA<len(pLista)):
        while(indiceB<len(listaFechas)):
            if(pLista[indiceA]==listaFechas[indiceB][0]):
                listaOrdenada.append([pLista[indiceA],listaFechas[indiceB][1]])
            #fin if
        #fin del while
    #fin del while
        
            indiceB = indiceB + 1
        indiceB = 0
        indiceA = indiceA + 1

    return listaOrdenada
#Fin de la funcion integrarRepeticionFechas()



'''
Entradas:
- fechas
Salidas:
- gráfico de top 3 de fecha en que se jugaron más partidas (graph)
Restriciones:
- fechas (list)
- fechas no puede estar vacía
'''
#Algoritmo que crea un gráfico de top 3 de fecha en que se jugaron más partidas.    
def graficoFechasConMasPartidas():
    #fechas (list)
    fechas = integrarRepeticionFechas()
    #Se llama a un estilo especifico
    plt.style.use('seaborn')
    #indice (int)
    indice = 0
    #dates (list)
    dates =[]
    #indicadores (list)
    indicadores = []
    
    while(indice<len(fechas)):
        dates.append(fechas[indice][0])
        indicadores.append(fechas[indice][1])
        indice = indice + 1
    #fin del while

    #Se crea gráfico
    plt.plot_date(dates, indicadores, linestyle='solid')
    plt.gcf().autofmt_xdate()
    date_format = mpl_dates.DateFormatter('%b, %d %y')
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.tight_layout()
    #Se muestra el gráfico
    plt.show()
#Fin del algoritmo graficoFechasConMasPartidas()



'''
Entradas:
- bitacora
Salidas:
- horas (list)
Restriciones:
- bitacora (file)
- bitacora debe de existir
- bitacora no puede estar vacio
'''
def extraerHoras():
    #horas (list)
    horas=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        #entrada (file)
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:           
            horas.append(columna[4])

    return horas
#Fin del algortimo extraerHoras()



'''
Entradas:
- horas
Salidas:
- cantidadHoras (list)
Restriciones:
- horas (list)
- horas no puede estar vacía
'''
#Funcion que cuenta las horas registradas en la bitacora
def contarHoras(pLista):
    #horas (list)
    horas = eliminarElementosRepetidosBitacora(pLista)
    #cantidadHoras (list)
    cantidadHoras=[]
    #indice (int)
    indice = 0
    #cantidad (int)
    cantidad = 0

    
    while(indice<len(horas)):
        cantidad = contarCaracter(pLista,horas[indice])
        cantidadHoras.append([horas[indice],cantidad])
        indice = indice + 1
    #fin del while

    return cantidadHoras
#Fin de la función contarHoras()



'''
Entradas:
- horasPartidas
Salidas:
- listaFecha (list)
Restriciones:
- horasPartidas (list)
- horasPartidas no puede estar vacío
'''
#Algoritmo 
def crearDatosHorasPartidas():
    #horasPartidas (list)
    horasPartidas = extraerHoras()
    #indice (int)
    indice = 0
    #horas (str)
    horas=""
    #listaFecha (list)
    listaFecha=[]
    
    while(indice<len(horasPartidas)):
        horas = horasPartidas[indice].split(":")
        listaFecha.append(int(horas[0]))
        indice = indice + 1
    #fin del while

    #listaFecha (Se ordena la lista en orden cronologico)
    listaFecha.sort()
    listaFecha = contarHoras(listaFecha)
    
    return listaFecha
#Fin del algoritmo crearDatosHorasPartidas()

      

'''
Entradas:
- horasPartidas
Salidas:
- horas (list)
Restriciones:
- horasPartidas (list)
- horasPartidas no puede estar vacía
'''
#Algoritmo que clasifica las horas extraidas de bitacora
def clasificacionHorasPartidas():
    #horasPartidas (list)
    horasPartidas = crearDatosHorasPartidas()
    #indice (int)
    indice = 0
    #horas (dict)
    horas = {"manana":0,"tarde":0,"noche":0}
    
    while(indice<len(horasPartidas)):
        if(horasPartidas[indice][0]>=5 and horasPartidas[indice][0]<=11):
            horas["manana"] +=  horasPartidas[indice][1]
        #fin del if
        elif(horasPartidas[indice][0]>=12 and horasPartidas[indice][0]<=18):
            horas["tarde"] +=  horasPartidas[indice][1]
        #fin del elif
        elif( (horasPartidas[indice][0]>=19 and horasPartidas[indice][0]<=23) or (horasPartidas[indice][0]>=0 and horasPartidas[indice][0]<=4)):
            horas["noche"] +=  horasPartidas[indice][1]
        #fin del elif
        indice = indice + 1
    #fin del while

    return horas
#Fin del algoritmo clasificacionHorasPartidas()

    

'''
Entradas:
- datos
Salidas:
- grafico de distribución de horarios donde se ha jugado (graph)
Restriciones:
- datos (list)
- datos no puede estar vacía
'''
#Algoritmo que crea un grafico segun la distribución de horarios donde se ha jugado (mañana, tarde, noche).
def graficoClasificacionHorasPartidas():
    #datos (list)
    datos = clasificacionHorasPartidas()
    #indice (int)
    indice = 0
    #actividades (list)
    actividades=[]
    #divisiones (list)
    divisiones=[]
    
    for tiempo in datos:
        divisiones.append(datos[tiempo])
        actividades.append(tiempo)
    #fin del for

    ypos = np.arange(len(actividades))

    plt.xticks(ypos,actividades)
    #Se crea el gráfico
    plt.bar(ypos,divisiones, width=0.5)
    plt.title("Distribución de horarios donde se ha jugado")
    plt.ylabel("Cantidad de partidas jugadas")
    plt.xlabel("Horarios")
    #Se muestra el gráfico
    plt.show()
#Fin del algoritmo graficoClasificacionHorasPartidas()



'''
Entradas:
- lista
Salidas:
- elementosMayores (list)
Restriciones:
- lista (list)
- lista no puede estar vacía
'''
#Algoritmo que crea una lista con los mejores jugadores
def identificarJugadoresGanadores():
    #lista (list)
    lista = crearDatosJugadoresGanadores()
    #elementosMayores (list)
    elementosMayores = []
    #indice (list)
    indice = 0
    #parada (list)
    parada = 5

    while(indice<parada):
        elementoMayor = encontrarMayor(lista)
        lista = eliminarMayor(lista,elementoMayor)
        elementosMayores.append(elementoMayor)
        indice = indice + 1

    return elementosMayores
#Fin del algoritmo identificarJugadoresGanadores()



'''
Entradas:
- datos 
Salidas:
- grafico de la frecuencia de configuración de partidas (graph)
Restriciones:
- datos (list)
- datos no puede estar vacio
'''
#Algoritmo que crea el grafico de top 5 de los jugadores que han ganado en más ocasiones.
def graficoJugadoresGanadores():
    #datos (list)
    datos = identificarJugadoresGanadores()
    #indice (list)
    indice = 0
    #actividades (list)
    actividades=[]
    #divisiones (list)
    divisiones=[]
    
    while(indice<len(datos)):
        actividades.append(datos[indice][0])
        divisiones.append(datos[indice][1])
        indice = indice + 1
    #fin del while

    #Se crea el gráfico
    plt.pie(divisiones, labels=actividades , startangle=90,autopct='%1.1f%%')
    plt.title("Top 5 de los jugadores que han ganado en más ocasiones.")
    #Se muestra el gráfico
    plt.show()
#Fin del algoritmo graficoJugadoresGanadores()



'''
Entradas:
- datos 
Salidas:
- grafico de la frecuencia de configuración de partidas (graph)
Restriciones:
- datos (list)
- datos no puede estar vacio
'''
#Algoritmo que crea el grafico de la frecuencia de configuración de partidas.
def graficoFrecuenciaConfiguracion():
    #datos (list)
    datos = crearDatosTiposPartidasJugadas()
    #indice (int)
    indice = 0
    #porcentajes (list) 
    porcentajes=[]
    #juegoTipos (list) 
    juegoTipos=["Juego en equis", "Juego en zeta","Cuatro esquinas","Cartón lleno"]
    
    while(indice<len(datos)):
        porcentajes.append(datos[indice][1])
        indice = indice + 1
    #fin del while

    #Se crea el gráfico
    plt.pie(porcentajes, labels=juegoTipos , startangle=90,autopct='%1.1f%%')
    plt.title("Frecuencia de configuración de partidas.")
    #Se muestra el gráfico
    plt.show()
#Fin del algoritmo graficoFrecuenciaConfiguracion()



'''
Entradas:
- bitacora
Salidas:
- numerosCantados (list)
Restriciones:
- bitacora (file)
- bitacora debe existir
- bitacora no puede estar vacio
'''
#Algortimo que extrae los números cantados en configuración X
def extraerNumerosCantadosEnX():
    #numerosCantados (list)
    numerosCantados=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        #entrada (file)
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0]=='X'):
                output=eval(columna[1])
                numerosCantados += output
            #fin del if
        #fin del for

    return numerosCantados
#Fin del algoritmo extraerNumerosCantadosEnX()



'''
Entradas:
- ganadores
- numeros
Salidas:
- cantidadNumeros (list)
Restriciones:
- ganadores (list)
- ganadores no puede estar vacio
- numeros (list)
- numeros no puede estar vacio
'''
#Algoritmo que acomoda los números cantados en configuración en X
def crearDatosNumerosCantadosEnX():
    #ganadores (list)
    ganadores = extraerNumerosCantadosEnX()
    #numeros (list)
    numeros = eliminarElementosRepetidosBitacora(ganadores)
    #cantidadNumeros (list)
    cantidadNumeros=[]
    #indice (int)
    indice = 0
    #cantidad (int)
    cantidad = 0

    
    while(indice<len(numeros)):
        cantidad = contarCaracter(ganadores,numeros[indice])
        cantidadNumeros.append([numeros[indice],cantidad])
        indice = indice + 1
    #fin del while

    return cantidadNumeros
#Find del algoritmo crearDatosNumerosCantadosEnX()



'''
Entradas:
- bitacora
Salidas:
- numerosCantados (list)
Restriciones:
- bitacora (file)
- bitacora debe existir
- bitacora no puede estar vacio
'''
#Algortimo que extrae los números cantados en configuración Z
def extraerNumerosCantadosEnZ():
    #numerosCantados (list)
    numerosCantados=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        #entrada (file)
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0]=='Z'):
                output=eval(columna[1])
                numerosCantados += output
            #fin del if
        #fin del for 

    return numerosCantados
#Fin del algoritmo extraerNumerosCantadosEnZ()



'''
Entradas:
- ganadores
- numeros
Salidas:
- cantidadNumeros (list)
Restriciones:
- ganadores (list)
- ganadores no puede estar vacio
- numeros (list)
- numeros no puede estar vacio
'''
#Algoritmo que acomoda los números cantados en configuración en Z
def crearDatosNumerosCantadosEnZ():
    #ganadores (list)
    ganadores = extraerNumerosCantadosEnZ()
    #numeros (list)
    numeros = eliminarElementosRepetidosBitacora(ganadores)
    #cantidadNumeros (list)
    cantidadNumeros=[]
    #indice (int)
    indice = 0
    #cantidad (int)
    cantidad = 0

    
    while(indice<len(numeros)):
        cantidad = contarCaracter(ganadores,numeros[indice])
        cantidadNumeros.append([numeros[indice],cantidad])
        indice = indice + 1
    #fin while

    return cantidadNumeros
#Fin del algoritmo crearDatosNumerosCantadosEnZ()



'''
Entradas:
- bitacora
Salidas:
- numerosCantados (list)
Restriciones:
- bitacora (file)
- bitacora debe existir
- bitacora no puede estar vacio
'''
#Algortimo que extrae los números cantados en configuración E
def extraerNumerosCantadosEnE():
    #numerosCantados (list)
    numerosCantados=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        #entrada (file)
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0]=='E'):
                output=eval(columna[1])
                numerosCantados += output
            #fin if
        #fin del for

    return numerosCantados
#Fin del algoritmo extraerNumerosCantadosEnE()



'''
Entradas:
- ganadores
- numeros
Salidas:
- cantidadNumeros (list)
Restriciones:
- ganadores (list)
- ganadores no puede estar vacio
- numeros (list)
- numeros no puede estar vacio
'''
#Algoritmo que acomoda los números cantados en configuración en E
def crearDatosNumerosCantadosEnE():
    #ganadores (list)
    ganadores = extraerNumerosCantadosEnE()
    #numeros (list)
    numeros = eliminarElementosRepetidosBitacora(ganadores)
    #cantidadNumeros (list)
    cantidadNumeros=[]
    #indice (list)
    indice = 0
    #cantidad (int)
    cantidad = 0

    
    while(indice<len(numeros)):
        cantidad = contarCaracter(ganadores,numeros[indice])
        cantidadNumeros.append([numeros[indice],cantidad])
        indice = indice + 1
    #fin del while

    return cantidadNumeros
#Fin del algoritmo crearDatosNumerosCantadosEnE()



'''
Entradas:
- bitacora
Salidas:
- numerosCantados (list)
Restriciones:
- bitacora (file)
- bitacora debe existir
- bitacora no puede estar vacio
'''
#Algortimo que extrae los números cantados en configuración L
def extraerNumerosCantadosEnL():
    #numerosCantados (list)
    numerosCantados=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0]=='L'):
                output=eval(columna[1])
                numerosCantados += output
            #fin del if
        #fin del for

    return numerosCantados
#Fin del algoritmo extraerNumerosCantadosEnL()



'''
Entradas:
- ganadores
- numeros
Salidas:
- cantidadNumeros (list)
Restriciones:
- ganadores (list)
- ganadores no puede estar vacio
- numeros (list)
- numeros no puede estar vacio
'''
#Algoritmo que acomoda los números cantados en configuración en L 
def crearDatosNumerosCantadosEnL():
    #ganadores (list)
    ganadores = extraerNumerosCantadosEnL()
    #numeros (list)
    numeros = eliminarElementosRepetidosBitacora(ganadores)
    #cantidadNumeros (list)
    cantidadNumeros = []
    #indice (list)
    indice = 0
    #cantidad (int)
    cantidad = 0

    
    while(indice<len(numeros)):
        cantidad = contarCaracter(ganadores,numeros[indice])
        cantidadNumeros.append([numeros[indice],cantidad])
        indice = indice + 1
    #fin del while

    return cantidadNumeros
#Fin de la algoritmo crearDatosNumerosCantadosEnL()



'''
Entradas:
- pLista
Salidas:
- listaNueva (list)
Restriciones:
- pLista (list)
- pLista no puede estar vacio
'''
#Función que extrae los números importantes cantados
def extrarNumerosMayoresImportantes(pLista):
    #indiceA (int)
    indiceA =0
    #listaNueva (list)
    listaNueva=[]
    
    while(indiceA<len(pLista)):
        listaNueva.append(pLista[indiceA][0])
        indiceA = indiceA + 1
    #Fin del while
    return listaNueva
#Fin de la función extrarNumerosMayoresImportantes()



'''
Entradas:
- pListaA
- pListaB
Salidas:
- listaNueva (list)
Restriciones:
- pListaA (list)
- pListaA no puede estar vacía 
- pListaB (lsit)
- pListaB no puede estar vacía
'''
#Función que crear una lista con los números parecidos a la primera posición de pListaA
def acomadarNumerosImportantes(pListaA,pListaB):
    #indiceA (int)
    indiceA =0
    #indiceB (int)
    indiceB =0
    #listaNueva (list)
    listaNueva=[]
    
    while(indiceA<len(pListaA)):
        while(indiceB<len(pListaB)):
            if(pListaA[indiceA][0]==pListaB[indiceB][0]):
                listaNueva.append(pListaB[indiceB][1])
            #Fin del if
            indiceB = indiceB +1
        #Fin del while
        indiceB = 0
        indiceA = indiceA + 1
    #Fin del while
    return listaNueva
#Fin de la Función acomadarNumerosImportantes()



'''
Entradas:
- listaMayores 
Salidas:
- grafico de top 10 números contados por configuracion (graph)
Restriciones:
- listaMayores (list)
- listaMayores no puede estar vacio
'''
#Algoritmo que crea el top 10 de números que más se han cantado por configuración de partida
def graficoTopNumerosContadosPorConfiguracion():
    #listaMayores (list)
    listaMayores = identificarNumerosMayores()
    #numerosEnX (list)
    numerosEnX = crearDatosNumerosCantadosEnX()
    numerosEnX = acomadarNumerosImportantes(listaMayores,numerosEnX)
    #numerosEnZ (list)
    numerosEnZ = crearDatosNumerosCantadosEnZ()
    numerosEnZ = acomadarNumerosImportantes(listaMayores,numerosEnZ)
    #numerosEnE (list)
    numerosEnE = crearDatosNumerosCantadosEnE()
    numerosEnE = acomadarNumerosImportantes(listaMayores,numerosEnE)
    #numerosEnL (list)
    numerosEnL = crearDatosNumerosCantadosEnL()
    numerosEnL = acomadarNumerosImportantes(listaMayores,numerosEnL)
    
    listaMayores = extrarNumerosMayoresImportantes(listaMayores)
    #se crea el grafico
    df = pd.DataFrame({'Juego en equis': numerosEnX,'Juego en zeta': numerosEnZ,'Juego cuatro esquinas': numerosEnE,'Juego cartón lleno': numerosEnL,}, index=listaMayores)
    ax = df.plot.bar(rot=0)
    #Se muestra el grafico
    plt.show()
#Fin del algoritmo graficoTopNumerosContadosPorConfiguracion()


