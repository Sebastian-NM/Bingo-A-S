'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''


#Importar Librerías
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



#Inicio variables gobales
cartones ={}
jugadores={}
jugadoresConCartones={}
cartonesJuego={}
listaIdentificadores =[]
identificadoresLibres =[]
listaNumerosCantados = []
listaGanadores=[]
tipoJuego=""
premio=""


'''
Entradas: numero
Salidas: numero (str)
Restriciones: numero (int)
              numero > 3
'''
#Crea tres números aleatorios
def crearNumero(numero=3):
    if(numero==0):
        return ""
    return str(randint(0,9))+crearNumero(numero-1)


'''
Entradas: numero
Salidas: letras (str)
Restriciones: numero (int)
              numero > 3
'''
#Crea 3 letras aleatorias para la identificación
def crearLetras(numero=3):
    abecedario=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    indice = randrange(len(abecedario))
    
    if(numero==0):
        return ""
    
    return abecedario[indice]+crearLetras(numero-1)


'''
Entradas: crearLetras, crearNumero
Salidas: identificardor (str)
Restriciones: crearLetras (función)
              crearNumero (función)
'''
#Crea el identificador de los cartones
def crearIdententificador():
    identificardor =crearLetras() + crearNumero()
    
    return identificardor


'''
Entradas: pLista, pIdentificador
Salidas: pIdentificador existe en pLista (bool)
Restriciones: pLista (lista), pIdentificador (str)
'''
#Indica si pIdentificador existe en pLista
def identificadorRepetido(pLista,pIdentificador):
    if(pLista==[]):
        return False
    elif(pLista[0]==pIdentificador):
        return True
    else:
        return identificadorRepetido(pLista[1:],pIdentificador)


'''
Entradas: pNum
Salidas: listaIdentificadores (list)
Restriciones: pNum (int)
              pNum > 0
'''
#Crea una lista de posibles identificadores
def crearListaIdentificadores(pNum):
    if(pNum==0):
        return []
    else:
        return [crearIdententificador()] + crearListaIdentificadores(pNum-1)


'''
Entradas: pNum
Salidas: lista (list)
Restriciones: pNum (int)
              pNum > 0
'''
#Crea una lista con identificadores no repetidos
def crearListaIdentificadoresNoRepetidos(pNum):
    lista = crearListaIdentificadores(pNum)
    indice = 0
    
    while(indice<len(lista)):
        
        if( identificadorRepetido(lista[indice+1:],lista[indice]) ):
            indice = 0
            lista = crearListaIdentificadores(pNum)
        indice = indice + 1

    return lista


'''
Entradas: pInicio, pFin
Salidas: listaNumeros (list)
Restriciones: pInicio (int)
              pInicio > 0
              pFin (int)
              pFin > 0
'''
#Crea 5 números aleatorios segun pInicio y pFin 
def crearNumerosRandomCarton(pInicio,pFin,Numero=5):
    if(Numero==0):
        return []
    else:
        return [randrange(pInicio,pFin)]+crearNumerosRandomCarton(pInicio,pFin,Numero-1)


'''
Entradas: pLista
Salidas: pLista tiene un elemento repetido (bool)
Restriciones: pLista (list), pLista !=[]
'''
#Indica si algun número del carton esta repetido
def recorrerElementosCarton(pLista):
    if(pLista==[]):
        return False
    elif( identificadorRepetido(pLista[1:],pLista[0])):
        return True
    else:
        return recorrerElementosCarton(pLista[1:])


'''
Entradas: pInicio, pFin
Salidas: fila (list)
Restriciones: pInicio (int)
             pInicio > 0
             pFin (int)
             pFin > 0
'''
#Crea un carton
def crearNumerosCarton(pInicio,pFin):
    fila=[]
    while(True):
        fila=crearNumerosRandomCarton(pInicio,pFin)
        if(recorrerElementosCarton(fila)==False):
            return fila

'''
Entradas: carton, vector
Salidas: carton (matriz)
Restriciones: carton (matriz)
              carton !=[]
              vector (array)
              vector !=[]
'''
#Crea y acomoda los elementos del cartón
def crearElementosCarton():
    carton=[]
    vector=[]
    fila1=crearNumerosCarton(1,15)
    fila2=crearNumerosCarton(16,30)
    fila3=crearNumerosCarton(31,45)
    fila4=crearNumerosCarton(46,60)
    fila5=crearNumerosCarton(61,75)
    indiceA=0
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

    return carton


'''
Entradas: pNum
Salidas: cartones (matriz)
Restriciones: pNum (int)
              pNum >= 0
'''
#Crea los cartones
def crearCarton(pNum):
    global cartones
    global listaIdentificadores

    indenticadores = crearListaIdentificadoresNoRepetidos(pNum)
    listaIdentificadores = indenticadores

    indice=0
    while(indice<pNum):
        cartones[indenticadores[indice]] = crearElementosCarton()
        indice = indice+1
        
    return cartones

  
'''
Entradas: cartones
Salidas: cartones (bool)
Restriciones: cartones (file)
              cartones debe de existir la carpeta
'''
#Identifica si existe la carpeta cartones
def existeCarpetaCartones():
    if os.path.isdir('cartones'):
        return True
    else:
       return False


'''
Entradas: cartones, listaIdentificadores
Salidas: eliminar carpeta de cartones (file)
Restriciones: cartones (list)
              listaIdentificadores (list)
'''
#Elimina la carpeta de cartones
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

    if(existeCarpetaCartones()==False):
        os.mkdir("cartones")


'''
Entradas: cartones, jugadores, jugadoresConCartones, identificadoresLibres, listaIdentificadores, tipoJuego, premio, listaNumerosCantados, cartonesJuego, listaGanadores
Salidas: limpieza de variables globales (función)
Restriciones: cartones (dict)
              cartones !={}
              jugadores (dict)
              jugadores !={}
              jugadoresConCartones (dict)
              jugadoresConCartones !={}
              identificadoresLibres (dict)
              identificadoresLibres !=[]
              listaIdentificadores (dict)
              listaIdentificadores !=[]
              tipoJuego (str)
              tipoJuego !=""
              premio (str)
              premio !=""
              premio (list)
              listaNumerosCantados !=[]
              cartonesJuego (dict)
              cartonesJuego !={}
              listaGanadores (list)
              listaGanadores !=[]
'''
#Limpia las variables globales
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


'''
Entradas: jugadores
Salidas: jugadores (bool)
Restriciones: jugadores (file)
              jugadores debe de existir
'''
#Identifica si existe la archivo jugadores
def existeArchivoJugadores():
    if os.path.isfile('jugadores/jugadores.csv'):
        return True
    else:
       return False

 
'''
Entradas:
- jugadores
Salidas:
- jugadores (bool)
Restriciones:
- jugadores (file)
- jugadores debe de existir
'''
#Identifica si existe la carpeta jugadores
def existeCarpetaJugadores():
    if os.path.isdir('jugadores'):
        return True
    else:
       return False


'''
Entradas: pCedula
Salidas: existe jugador (bool)
Restriciones: pCedula (str)
              pCedula !=""
'''
#Indica si existe jugador
def existeJugador(pCedula):
    if(existeCarpetaJugadores()==False):
        return False
    
    with open("jugadores/jugadores.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0]==pCedula):
                return True
        return False


'''
Entradas: pNombre, pCedula, pCorreo
Salidas: guardar 
Restriciones: pNombre (str)
              pNombre !=""
              pCedula (str)
              pCedula !=""
              pCorreo (str)
              pCorreo !=""
'''
#Crea un nuevo jugador en el archivo jugadores 
def crearJugador(pNombre,pCedula,pCorreo):
    if(existeCarpetaJugadores()==False):
        os.mkdir("jugadores")
    elif(existeArchivoJugadores()==False):
        rmtree("jugadores")
        os.mkdir("jugadores")

    archivo = open("jugadores/jugadores.csv","a")
    archivo.write(pCedula)
    archivo.write(";")
    archivo.write(pNombre)
    archivo.write(";")
    archivo.write(pCorreo+"\n")
    archivo.close()


'''
Entradas: pCedula
Salidas: correo(str)
Restriciones: pCedula (str), pCedula !=""
'''
#Función que extrae el correo del jugador
def extraerCorreoJugador(pCedula):
    with open("jugadores/jugadores.csv") as csvarchivo:
        #entrada (file)
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0]==pCedula):
                return columna[2]
            

'''
Entradas: pCedula
Salidas: jugadoresConCartones (dict)
Restriciones: pCedula (str)
'''
#Identifica si existe pCedula
def jugadorConCarton(pCedula):
    global jugadoresConCartones

    try:
        jugadoresConCartones[pCedula]
        return True
    except:
        return False


'''
Entradas: pCedula
Salidas: jugadoresConCartones (dict)
Restriciones: pCedula (str)
              pCedula !=""
'''
#Crea un jugador en el sistema
def crearJugadorConCartones(pCedula):
    global jugadoresConCartones

    jugadoresConCartones[pCedula] = []
    

'''
Entradas: pCedula
Salidas: cartones (int)
Restriciones: pCedula (str)
              pCedula !=""
'''
#Indica cuantos cartones tiene un jugador
def cantidadCartonesJugador(pCedula):
    global jugadoresConCartones
    cartones = jugadoresConCartones[pCedula]
    
    return len(cartones)


'''
Entradas: pLista, pIdentificador
Salidas: posicion de donde se encuentra el identificador (int)
Restriciones: pLista (list)
              pIdentificador
'''
#Identidica la posicion de identificador en la lista
def posicionIdentificador(pLista,pIdentificador,posicion=0):
    if(pLista==[]):
        return 0
    elif(pLista[0]==pIdentificador):
        return posicion
    else:
        return posicionIdentificador(pLista[1:],pIdentificador,posicion+1)


'''
Entradas: pIdentificadores
Salidas: identificadoresLibres (list)
Restriciones: pIdentificadores (list)
              pIdentificadores !=[]
'''
#Elimina los identificadores usados 
def eliminarIdentificadores(pIdentificadores):
    global identificadoresLibres
    indice = 0
    
    while(indice<len(pIdentificadores)):
        if(identificadorRepetido(identificadoresLibres,pIdentificadores[indice])):
            posicion = posicionIdentificador(identificadoresLibres,pIdentificadores[indice])
            identificadoresLibres.pop(posicion)
        indice = indice + 1
        

'''
Entradas: identificadoresLibres
Salidas: identificadoresLibres (int)
Restriciones: identificadoresLibres (list)
              identificadoresLibres !=[]
'''
#Indica la cantidad de identificadores libres hay en el sistema
def cantidadIdentificadoresLibres():
    global identificadoresLibres
    return len(identificadoresLibres)


'''
Entradas: jugadoresConCartones, identificadoresLibres, listaIdentificadores
Salidas: eliminar los identificadores repetidos (list)
Restriciones: jugadoresConCartones (dict)
              jugadoresConCartones !={}
              identificadoresLibres (list)
              identificadoresLibres !=[]
              listaIdentificadores (list)
              listaIdentificadores !=[]
'''
#Eliminar los identificadores asignados a los jugadores
def listaIdentificadoresLibres():
    global jugadoresConCartones
    global identificadoresLibres
    global listaIdentificadores

    identificadoresLibres = listaIdentificadores.copy()


    for jugador in jugadoresConCartones:
        eliminarIdentificadores(jugadoresConCartones[jugador])


'''
Entradas: pIdentificador
Salidas: jugador (dict)
Restriciones: pIdentificador (str)
              pIdentificador != ""
'''
def extraerIdentificadorJugadorConCarton(pIdentificador):
    global jugadoresConCartones
    global jugadores

    for jugador in jugadoresConCartones:
        for identificadores in jugadoresConCartones[jugador]:
            if(identificadores == pIdentificador):           
                return [jugador,jugadores[jugador][0]]


'''
Entradas: pIdentificador
Salidas: existe identificador asosiado con jugador(bool)
Restriciones: pIdentificador 
'''
#Identifica si identificador asosiado con jugador
def identificarJugadorConCarton(pIdentificador):
    global jugadoresConCartones

    for jugador in jugadoresConCartones:
        for identificadores in jugadoresConCartones[jugador]:
            if(identificadores == pIdentificador):
                return True
            
    return False


'''
Entradas: pCedula, pCartones
Salidas: enviar cartones a jugador (mail)
Restriciones: pCedula (str), pCartones (list)
'''
#Asigna los cartones a un jugador
def agragerCartonesAJugadores(pCedula,pCartones):
    global jugadoresConCartones
    global identificadoresLibres

    lista = jugadoresConCartones[pCedula]
    indice = 0

    if(pCartones<=len(identificadoresLibres)):
        while(indice<pCartones):
            numero = randrange(len(identificadoresLibres))
            lista.append(identificadoresLibres[numero])
            identificadoresLibres.pop(numero)
            
            
            indice = indice + 1

    jugadoresConCartones[pCedula] = lista
    enviarCartonesPorCorreo(pCedula)

 
'''
Entradas: jugadores
Salidas: jugadores (int)
Restriciones: jugadores (list)
              jugadores !=[]
'''
#Extrae la cantidad de jugadores existentes en memoria
def extraerCantidadJugadores():
    global jugadores
    return len(jugadores)


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
#Crea una lista de los jugadores
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


    with open("jugadores/jugadores.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            jugadores[columna[0]] = [columna[1],columna[2]]   
    

'''
Entradas: pIdentificador
Salidas: identificadorRepetido (bool)
Restriciones: pIdentificador (str)
              pIdentificador != ""
'''
#Recorre todos los elementos existentes de la carpeta cartones
def existeImagenEnCarpeta(pIdentificador):
    archivos = [carpeta for carpeta in os.listdir("cartones/") if os.path.isfile(os.path.join("cartones/",carpeta))]
    
    return identificadorRepetido(archivos,pIdentificador+".png")
 

'''
Entradas: pCedula
Salidas: correo (mail)
Restriciones: pCedula (str)
              pCedula != ""
'''
#Envia los cartones asignados segun pCedula
def enviarCartonesPorCorreo(pCedula):
    global jugadores
    global jugadoresConCartones

    listaCartones = jugadoresConCartones[pCedula]

    sender_email = "bingoproyecto2@gmail.com"
    receiver_email =  jugadores[pCedula][1]

    msg = MIMEMultipart()
    msg['Subject'] = 'Bingo, entrega de cartones'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('Muchas gracias '+ jugadores[pCedula][0]+ " por participar en el juego, te adjuntamos tus cartones.\n¡Mucha suerte!")
    msg.attach(msgText)

    indice = 0
    while(indice<len(listaCartones)):
        with open('cartones/'+listaCartones[indice]+'.png', 'rb') as fp:
            img = MIMEImage(fp.read())
            img.add_header('Content-Disposition', 'attachment', filename= listaCartones[indice]+".png")
            msg.attach(img)
        indice = indice + 1

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login("bingoproyecto2@gmail.com", "Tecdigital")
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)


'''
Entradas: pTipoJuego, pPremio 
Salidas: tipoJuego (str), premio (str)
Restriciones: pTipoJuego (str)
              pTipoJuego != ""
              pPremio (str)
              pPremio != ""
'''
#Conecta los datos de la interfaz grafico con la logica
def guardarDatosJuego(pTipoJuego,pPremio):
    global tipoJuego
    global premio
    
    premio = pPremio
    tipoJuego = pTipoJuego


'''
Entradas: listaNumerosCantados
Salidas: listaNumerosCantados (int)
Restriciones: listaNumerosCantados (list)
              listaNumerosCantados !=[]
'''
#Retonar el ultimo número cantado
def ultimoNumeroCantado():
    global listaNumerosCantados
    
    return listaNumerosCantados[-1]


'''
Entradas: tipoJuego, premio 
Salidas: tipoJuego (str), premio (str)
Restriciones: tipoJuego (str)
              tipoJuego != ""
              premio (str)
              premio != ""
'''
#Envia los datos de juego
def enviarDatosJuego():
    global tipoJuego
    global premio
    
    return tipoJuego,premio


'''
Entradas: cartones
Salidas: cartones (int)
Restriciones: cartones (list)
              cartones !=[]
'''
#Retorna la cantidad de cartones existentes
def enviarTotalCartones():
    global cartones
    return len(cartones)


'''
Entradas: numero
Salidas: numero (int)
Restriciones: numero (int)
              numero >=0
'''
#Crea un numero entre 0 y 75
def crearNumerosPartida():
    numero = randint(0,75)
    return numero



'''
Entradas: numero
Salidas: listaNumerosCantados (list)
Restriciones: numero (str)
'''
#Crea un nuevo cantado
def agregarNumeroASecuencia():
    global listaNumerosCantados
    numero = crearNumerosPartida()
    
    while(True):
        if(identificadorRepetido(listaNumerosCantados,numero)==False):
            listaNumerosCantados.append(numero)
            break
        else:
            numero = crearNumerosPartida()

    return listaNumerosCantados



'''
Entradas: pCarton
Salidas: matriz (matriz)
Restriciones: pCarton (matriz)
              pCarton !=[]
'''
#Marca el carton segun el número cantado
def marcarNumero(pCarton):
    global listaNumerosCantados
    matriz = [[],[],[],[],[]]
    indiceA=0
    indiceB=0
    
    while(indiceA<len(pCarton)):
        while(indiceB<len(pCarton[indiceA])):
            if(pCarton[indiceA][indiceB]==listaNumerosCantados[-1]):
                matriz[indiceA].append("X")
            else:
                matriz[indiceA].append(pCarton[indiceA][indiceB])
            indiceB = indiceB + 1
        indiceB = 0            
        indiceA = indiceA + 1

    return matriz


'''
Entradas: pCarton
Salidas: carton es un juego en X (bool)
Restriciones:pCarton (matriz)
             pCarton !=[]
'''
#Identifica si el pCarton es un juego en X
def juegoEnX(pCarton):
    identificador=len(pCarton)
    indiceA=0
    indiceB=0
    
    while(indiceA<len(pCarton)):
        identificador = identificador - 1
        while(indiceB<len(pCarton[indiceA])):
            if(indiceB==indiceA or indiceB==identificador):
                if(pCarton[indiceA][indiceB]!="X"):  
                    return False
            indiceB = indiceB + 1
        indiceB = 0

        indiceA = indiceA + 1
    return True


'''
Entradas: pCarton
Salidas: carton es un juego en esquinas (bool)
Restriciones: pCarton (matriz)
              pCarton !=[]
'''
#Identifica si el pCarton es un juego en esquinas
def juegoCuatroEsquinas(pCarton):
    identificador=len(pCarton)-1
    indiceA=0
    indiceB=0
    
    while(indiceA<len(pCarton)):
        while(indiceB<len(pCarton[indiceA])):
            if((indiceA==0 and indiceB==0) or (indiceA==0 and indiceB==identificador)):
                if(pCarton[indiceA][indiceB]!="X"):  
                    return False
            if((indiceA==4 and indiceB==0) or (indiceA==4 and indiceB==identificador)):
                if(pCarton[indiceA][indiceB]!="X"):  
                    return False
            indiceB = indiceB + 1
        indiceB = 0
        indiceA = indiceA + 1
    return True


'''
Entradas: pCarton
Salidas: carton es un juego completo (bool)
Restriciones: pCarton (matriz)
              pCarton !=[]
'''
#Identifica si el pCarton es un juego completo
def juegoCartonCompleto(pCarton):
    indiceA=0
    indiceB=0
    
    while(indiceA<len(pCarton)):
        while(indiceB<len(pCarton[indiceA])):
            if(pCarton[indiceA][indiceB]!="X"):  
                return False
            indiceB = indiceB + 1
        indiceB = 0

        indiceA = indiceA + 1
    return True


'''
Entradas: pCarton
Salidas: carton es un juego en Z (bool)
Restriciones: pCarton (matriz)
              pCarton !=[]
'''
#Identifica si el pCarton es un juego en Z 
def juegoEnZ(pCarton):
    diagonalInversa=len(pCarton)
    indiceA=0
    indiceB=0
    
    while(indiceA<len(pCarton)):
        diagonalInversa = diagonalInversa - 1
        while(indiceB<len(pCarton[indiceA])):
            if(indiceA==0 or indiceA==4):
                if(pCarton[indiceA][indiceB]!="X") :  
                    return False
            if(indiceB == diagonalInversa):
                if(pCarton[indiceA][indiceB]!="X") :  
                    return False
            indiceB = indiceB + 1
            
        indiceB = 0
        indiceA = indiceA + 1
    return True


'''
Entradas: cartones
Salidas: cartonesJuego (dict)
Restriciones: cartones (dict)
              cartones !={}
'''
#Crea una copia de cartones
def copiaCartones():
    global cartones
    global cartonesJuego

    cartonesJuego = cartones.copy()


'''
Entradas: cartonesJuego
Salidas: cartonesJuego (dict)
Restriciones: cartonesJuego (dict)
              cartonesJuego != {}
'''
#Marca a los cartones
def marcarCartones():
    global cartonesJuego
    
    for clave in cartonesJuego:
        cartonesJuego[clave]=marcarNumero(cartonesJuego[clave])


'''
Entradas: listaGanadores
Salidas: listaGanadores (list)
Restriciones: listaGanadores (list)
'''
#Retonar la cantidad de ganadores
def retornarGanadores():
    global listaGanadores
    return listaGanadores


'''
Entradas: pNombre, pCarton, pDestinatario
Salidas: correo (mail)
Restriciones: pNombre (str)
              pNombre !=""
              pCarton (str)
              pCarton !=""
              pDestinatario (str)
              pDestinatario !=""
'''
#Envia un correo a los ganadores
def enviarCorreoGanadores(pNombre,pCarton,pDestinatario):
    global tipoJuego
    global premio

    sender_email = "bingoproyecto2@gmail.com"
    receiver_email =  pDestinatario

    msg = MIMEMultipart()
    msg['Subject'] = 'Bingo, ¡felicidades eres un ganador!'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('¡Mucar felicidades '+pNombre + "!\nEres un ganador en el tipo de juego "+str(tipoJuego)+", y tu premio es: "+str(premio)+"\nPor favor ponte en contacto con nosotros para reclamar tu premio.")
    msg.attach(msgText)


    with open('cartones/'+pCarton+'.png', 'rb') as fp:
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
import matplotlib .pyplot as plt


'''
Entradas: jugadores, listaGanadores 
Salidas: correos enviados a los ganadores (mail)
Restriciones: jugadores (list)
              jugadores !=""
              listaGanadores (list)
              listaGanadores !=""
'''
#Envia un correo a los ganadores
def enviarEmailGanadores():
    global listaGanadores
    jugadoresConCartones
    global jugadores 

    indiceA = 0
    while(indiceA<len(listaGanadores)):
        if(identificarJugadorConCarton(listaGanadores[indiceA])):
            informacionJugador= extraerIdentificadorJugadorConCarton(listaGanadores[indiceA])
            enviarCorreoGanadores(jugadores[informacionJugador[0]][0],listaGanadores[indiceA],jugadores[informacionJugador[0]][1])
        indiceA = indiceA + 1

    
'''
Entradas: pModoJuego
Salidas: listaGanadores (list)
Restriciones: pModoJuego (str)
              pModoJuego !=""
'''
#Identifica si existe un ganador del juego
def identificarGanadores(pModoJuego):
    global cartonesJuego
    global listaGanadores
    
    for clave in cartonesJuego:           
        if(pModoJuego=='Jugar en X'):
            if(juegoEnX(cartonesJuego[clave])):
                listaGanadores.append(clave)
        elif(pModoJuego=='Cuatro esquinas'):
            if(juegoCuatroEsquinas(cartonesJuego[clave])):
                listaGanadores.append(clave)
        elif(pModoJuego=='Cartón lleno'):
            if(juegoCartonCompleto(cartonesJuego[clave])):
                listaGanadores.append(clave)
        elif(pModoJuego=='Jugar en Z'):
            if(juegoEnZ(cartonesJuego[clave])):
                listaGanadores.append(clave)


'''
Entradas: cartonesJuego
Salidas: cartones marcados (matriz)
Restriciones: cartonesJuego
'''
#Imprime los cartones almacenados en memoria
def imprimirCartones():
    global cartonesJuego
    matriz = cartonesJuego
    indiceA=0
    indiceB=0

    for clave in matriz:
        while(indiceA<len(matriz[clave])):
            indiceA = indiceA + 1
        indiceA = 0


'''
Entradas: pModoJuego
Salidas: listaGanadores (bool)
Restriciones: pModoJuego (str)
'''
#Ejecuta una partida dependiendo de modo de juego
def cantarNumero(pModoJuego):
    global listaGanadores
    agregarNumeroASecuencia()
    marcarCartones()
    identificarGanadores(pModoJuego)
    
    if(listaGanadores!=[]):
        return True
    else:
        return False


'''
Entradas: pCarton, pIdentificador
Salidas: imagen del carton (img)
Restriciones: pCarton (matrix)
              pCarton != []
              pIdentificador (str)
              pIdentificador != ""
'''
#Crea la imagen de los cartones
def crearImagen(pCarton,pIdentificador):
    img = Image.open('tabla.png')
    draw = ImageDraw.Draw(img)
    fuente = ImageFont.truetype("fuente\Staatliches-Regular.ttf", 60)
    draw.text((100, 55),"B",(0,2,27),font=fuente)
    draw.text((280, 55),"I",(0,2,27),font=fuente)
    draw.text((440, 55),"N",(0,2,27),font=fuente)
    draw.text((605, 55),"G",(0,2,27),font=fuente)
    draw.text((775, 55),"O",(0,2,27),font=fuente)
    draw.text((100, 140),str(pCarton[0][0]),(0,2,27),font=fuente)
    draw.text((260, 140),str(pCarton[0][1]),(0,2,27),font=fuente)
    draw.text((430, 140),str(pCarton[0][2]),(0,2,27),font=fuente)
    draw.text((595, 140),str(pCarton[0][3]),(0,2,27),font=fuente)
    draw.text((760, 140),str(pCarton[0][4]),(0,2,27),font=fuente)
    draw.text((100, 225),str(pCarton[1][0]),(0,2,27),font=fuente)
    draw.text((260, 225),str(pCarton[1][1]),(0,2,27),font=fuente)
    draw.text((430, 225),str(pCarton[1][2]),(0,2,27),font=fuente)
    draw.text((595, 225),str(pCarton[1][3]),(0,2,27),font=fuente)
    draw.text((760, 225),str(pCarton[1][4]),(0,2,27),font=fuente)
    draw.text((100, 310),str(pCarton[2][0]),(0,2,27),font=fuente)
    draw.text((260, 310),str(pCarton[2][1]),(0,2,27),font=fuente)
    draw.text((430, 310),str(pCarton[2][2]),(0,2,27),font=fuente)
    draw.text((595, 310),str(pCarton[2][3]),(0,2,27),font=fuente)
    draw.text((760, 310),str(pCarton[2][4]),(0,2,27),font=fuente)
    draw.text((100, 395),str(pCarton[3][0]),(0,2,27),font=fuente)
    draw.text((260, 395),str(pCarton[3][1]),(0,2,27),font=fuente)
    draw.text((430, 395),str(pCarton[3][2]),(0,2,27),font=fuente)
    draw.text((595, 395),str(pCarton[3][3]),(0,2,27),font=fuente)
    draw.text((760, 395),str(pCarton[3][4]),(0,2,27),font=fuente)
    draw.text((100, 480),str(pCarton[4][0]),(0,2,27),font=fuente)
    draw.text((260, 480),str(pCarton[4][1]),(0,2,27),font=fuente)
    draw.text((430, 480),str(pCarton[4][2]),(0,2,27),font=fuente)
    draw.text((595, 480),str(pCarton[4][3]),(0,2,27),font=fuente)
    draw.text((760, 480),str(pCarton[4][4]),(0,2,27),font=fuente)
    draw.text((210, 565),"Identificador: "+pIdentificador,(0,2,27),font=fuente)
    img.save('cartones/'+pIdentificador+'.png')


'''
Entradas: bitacora 
Salidas: existencia de la archivo (bool)
Restriciones: bitacora (file)
'''
#Identifica si existe la archivo bitacora
def existeArchivoBitacora():
    if os.path.isfile('bitacoraPartidas/bitacora.csv'):
        return True
    else:
       return False


'''
Entradas: bitacoraPartidas 
Salidas: existencia de la carpeta (bool)
Restriciones: bitacoraPartidas (file)
'''
#Identifica si existe la carpeta bitacoraPartidas
def existeCarpetaBitacora():
    if os.path.isdir('bitacoraPartidas'):
        return True
    else:
       return False


'''
Entradas: cartonesJuego, tipoJuego, premio, listaNumerosCantados, listaGanadores
Salidas: limpieza de las variables globales (función)
Restriciones: cartonesJuego (dict)
              tipoJuego (str)
              premio (str)
              listaNumerosCantados (list)
              listaGanadores (list)
'''
#Limpia todas las variables globales para empezar una nueva partida
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


'''
Entradas: listaNumerosCantados, tipoJuego
Salidas: bitacira (file)
Restriciones: listaNumerosCantados (list)
              listaNumerosCantados no puede estar vacía
              tipoJuego (str)
              tipoJuego no puede estar vacía
'''
#Crea un registro nuevo en bitacora
def crearRegistro():
    global listaNumerosCantados
    global tipoJuego
    listaInformacion=[]
    indice =0
    listaCedulas = []
    
    while(indice<len(listaGanadores)):
        if(identificarJugadorConCarton(listaGanadores[indice])):
            listaInformacion = extraerIdentificadorJugadorConCarton(listaGanadores[indice])
            if(identificadorRepetido(listaCedulas,str(listaInformacion[0]))==False):
                listaCedulas.append(str(listaInformacion[0]))
        indice = indice + 1 

    dia = date.today()
    hora = datetime.now()
    
    if(existeCarpetaBitacora()==False):
        os.mkdir("bitacoraPartidas")
    elif(existeArchivoBitacora()==False):
        rmtree("bitacoraPartidas")
        os.mkdir("bitacoraPartidas")

    if(tipoJuego=='Jugar en X'):
       tipoJuego="X"
    elif(tipoJuego=='Cuatro esquinas'):
        tipoJuego="E"
    elif(tipoJuego=='Cartón lleno'):
        tipoJuego="L"
    elif(tipoJuego=='Jugar en Z'):
        tipoJuego="Z"

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


'''
Entradas: matriz
Salidas: cartones (matriz)
Restriciones: matriz (matriz)
              matriz no puede estar vacio
'''
#Crea matrices
def imprimirMatriz():
    matriz = crearCarton()
    indice=0
    while(indice<len(matriz)):
        print(matriz[indice])
        indice = indice + 1


'''
Entradas: pNum
Salidas: cartones para el bingo (matrices)
Restriciones: pNum (int)
              pNum > 0
'''
#Crea los cartones segun pNum
def imprimirMatrices(pNum):
    matriz = crearCarton(pNum)
    indiceA=0
    indiceB=0

    for clave in matriz:
        crearImagen(matriz[clave],clave)
        while(indiceA<len(matriz[clave])):
            print(matriz[clave][indiceA])
            indiceA = indiceA + 1
        print(clave+"\n")
        indiceA = 0


'''
Entradas: bitacora
Salidas: tiposPartidasJugadas (list)
Restriciones: bitacora (file)
              bitacora debe de exitir
              bitacora no puede estar vacía
'''
#Extrae los tipos de juegos de las partidas en la bitacora
def extraerTiposPartidasJugadas():
    tiposPartidasJugadas=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            tiposPartidasJugadas.append(columna[0])

    return tiposPartidasJugadas


'''
Entradas: tiposPartidasJugadas
Salidas: juegos (list)
Restriciones: tiposPartidasJugadas (list)
              tiposPartidasJugadas no puede estar vacía
'''
#Clasifica las partidas segun las veces que se jugaron 
def crearDatosTiposPartidasJugadas():
    tiposPartidasJugadas = extraerTiposPartidasJugadas()
    tipoJuego = ["X","Z","E","L"]
    juegos=[]
    indice = 0
    cantidad = 0
    
    while(indice<len(tipoJuego)):
        cantidad = contarCaracter(tiposPartidasJugadas,tipoJuego[indice])
        juegos.append([tipoJuego[indice],cantidad])
        indice = indice + 1

    return juegos


'''
Entradas: pLista, pCaracter 
Salidas: cantidad (int)
Restriciones: pLista (list)
              pLista no puede estar vacía
              pCaracter (int/str)
              pCaracter no puede estar vacía
'''
#Indica cuantas veces aparece pCaracter
def contarCaracter(pLista,pCaracter):
    indice=0
    cantidad = 0
    
    while(indice<len(pLista)):
        if(pLista[indice]==pCaracter):
            cantidad = cantidad + 1
        indice = indice + 1

    return cantidad


'''
Entradas: pLista
Salidas: listaNueva (int)
Restriciones: pLista (list)
              pLista no puede estar vacó
'''
#Elimina los elementos repetidos
def eliminarElementosRepetidosBitacora(pLista):
    listaNueva = list(set(pLista))
    return listaNueva


'''
Entradas: bitacora
Salidas: numerosCantados
Restriciones: bitacora (file)
              bitacora debe de existir
              bitacora no puede estar vacío
'''
#Extrae los números cantados de la bitacora
def extraerNumerosCantados():
    numerosCantados=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            output=eval(columna[1])
            numerosCantados += output

    return numerosCantados


'''
Entradas: numerosCantados, numeros
Salidas: cantados (list)
Restriciones: numerosCantados (list)
              numerosCantados no puede estar vacío
              numeros (list)
              numeros no puede estar vacío
'''
#Une los números cantados con la cantidad de veces que fue cantado
def crearDatosNumerosContados():
    numerosCantados = extraerNumerosCantados()
    numeros = eliminarElementosRepetidosBitacora(numerosCantados)
    cantados=[]
    indice = 0
    cantidad = 0
    
    while(indice<len(numeros)):
        cantidad = contarCaracter(numerosCantados,numeros[indice])
        cantados.append([numeros[indice],cantidad])
        
        indice = indice + 1

    return cantados


'''
Entradas: lista
Salidas: [numero, mayor] (int,int)
Restriciones: lista (list)
              lista no puede estar vacía
'''
#Encuentra el número mayor
def encontrarMayor(lista):
    indice = 0
    mayor = 0
    numero = 0
    
    while(indice<len(lista)):
        if(mayor<lista[indice][1]):
            mayor=lista[indice][1]
            numero =lista[indice][0]
        indice = indice + 1

    return [numero, mayor]


'''
Entradas: lista, elemento
Salidas: listaNueva (list)
Restriciones: lista (list)
              lista no puede estar vacía
              elemento (str)
              elemento no puede estar vacío
'''
#Elimina el elemento mayor de lista segun elemento
def eliminarMayor(lista,elemento):
    indice = 0
    listaNueva = []
    
    while(indice<len(lista)):
        if(lista[indice][0]!=elemento[0]):
            listaNueva.append([lista[indice][0],lista[indice][1]])
        indice = indice + 1

    return listaNueva


'''
Entradas: lista
Salidas: elementosMayores (list)
Restriciones: lista (list)
              lista no puede estar vacía 
'''
#Une los numeros con sus apariciones
def identificarNumerosMayores():
    lista = crearDatosNumerosContados()
    elementosMayores = []
    indice = 0
    parada = 10

    while(indice<parada):
        elementoMayor = encontrarMayor(lista)
        lista = eliminarMayor(lista,elementoMayor)
        elementosMayores.append(elementoMayor)
        indice = indice + 1

    return elementosMayores


'''
Entradas: datos
Salidas: grafico de top 10 de números cantados (graph)
Restriciones: datos (list)
              datos no puede estar vacía
'''
#Crea un gráfico de top 10 de números cantados.
def graficoNumerosCantados():
    datos = identificarNumerosMayores()
    indice = 0
    numeros=[]
    porcentajes=[]
    
    while(indice<len(datos)):
        numeros.append(datos[indice][0])
        porcentajes.append(datos[indice][1])
        indice = indice + 1

    ypos = np.arange(len(numeros))

    plt.xticks(ypos,numeros)
    plt.bar(ypos,porcentajes, width=0.5)
    plt.title("Grafico de barras")
    plt.ylabel("Veces que aparecen")
    plt.xlabel("Números cantados")
    plt.show()


'''
Entradas: bitacora
Salidas: numerosCantados (list)
Restriciones: bitacora (file)
              bitacora debe de existir
              bitacora no puede estar vacía
'''
#Extrae los ganadores de la bitacora
def extraerJugadoresGanadores():
    numerosCantados=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            output=eval(columna[2])
            numerosCantados += output

    return numerosCantados


'''
Entradas: ganadores, cedulas
Salidas: cantidadGanadores (list)
Restriciones: ganadores (list)
              ganadores no puede estar vacía
              cedulas (list)
              cedulas no puede estar vacía
'''
#Integra los ganadores con la cantidad de veces que gano en una lista
def crearDatosJugadoresGanadores():
    ganadores = extraerJugadoresGanadores()
    cedulas = eliminarElementosRepetidosBitacora(ganadores)
    cantidadGanadores=[]
    indice = 0
    cantidad = 0
    
    while(indice<len(cedulas)):
        cantidad = contarCaracter(ganadores,cedulas[indice])
        cantidadGanadores.append([cedulas[indice],cantidad])
        indice = indice + 1

    return cantidadGanadores


'''
Entradas: bitacora
Salidas: fechasPartidas (list)
Restriciones: bitacora (file)
              bitacora no puede estar vacía
'''
#Extrae las fechas de la bitacora
def extraerFechaPartidas():
    fechasPartidas=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:           
            fechasPartidas.append(columna[3])

    return fechasPartidas


'''
Entradas: fechasPartidas, partidas 
Salidas: fechas (list)
Restriciones: fechasPartidas (list)
              fechasPartidas no puede estar vacía
              partidas (list)
              partidas no puede estar vacía
'''
#Clasifica las fechas segun su aparición en la bitacora
def crearDatosFechaPartidas():
    fechasPartidas = extraerFechaPartidas()
    partidas = eliminarElementosRepetidosBitacora(fechasPartidas)
    fechas=[]
    indice = 0
    cantidad = 0
    
    while(indice<len(partidas)):
        cantidad = contarCaracter(fechasPartidas,partidas[indice])
        fechas.append([partidas[indice],cantidad])
        indice = indice + 1

    return fechas


'''
Entradas: lista
Salidas: elementosMayores (list)
Restriciones: lista (list)
              lista no puede estar vacía
'''
#Identidica las fechas con mas partidas jugadas
def identificarFechasMayores():
    lista = crearDatosFechaPartidas()
    elementosMayores = []
    indice = 0
    parada = 3

    while(indice<parada):
        elementoMayor = encontrarMayor(lista)
        lista = eliminarMayor(lista,elementoMayor)
        fecha = elementoMayor[0].split('/')
        
        elementosMayores.append([datetime( int(fecha[2]), int(fecha[1]), int(fecha[0])  )  ,  elementoMayor[1]])
        indice = indice + 1

    return elementosMayores


'''
Entradas: pLista
Salidas: fechas
Restriciones: pLista (list)
              pLista no puede estra vacía
'''
#Ordena cronologicamente las fechas
def acomodarListas():
    pLista = identificarFechasMayores()
    indice = 0
    fechas = []
    
    while(indice<len(pLista)):
        fechas.append(pLista[indice][0])
        indice = indice + 1

    fechas.sort()
    
    return fechas


'''
Entradas: listaFechas, pLista
Salidas: listaOrdenada (list)
Restriciones: listaFechas (list)
              listaFechas no puede estar vacia
              pLista (list)
              pLista no puede estar vacia
'''
#Integra las fechas ordenas con su número de aparición
def integrarRepeticionFechas():
    listaFechas = identificarFechasMayores()
    pLista = acomodarListas()
    indiceA = 0
    indiceB = 0
    listaOrdenada=[]
    
    while(indiceA<len(pLista)):
        while(indiceB<len(listaFechas)):
            if(pLista[indiceA]==listaFechas[indiceB][0]):
                listaOrdenada.append([pLista[indiceA],listaFechas[indiceB][1]])
        
            indiceB = indiceB + 1
        indiceB = 0
        indiceA = indiceA + 1

    return listaOrdenada


'''
Entradas: fechas
Salidas: gráfico de top 3 de fecha en que se jugaron más partidas (graph)
Restriciones: fechas (list)
              fechas no puede estar vacía
'''
#Crea un gráfico de top 3 de fecha en que se jugaron más partidas.    
def graficoFechasConMasPartidas():
    fechas = integrarRepeticionFechas()
    plt.style.use('seaborn')
    indice = 0
    dates =[]
    indicadores = []
    
    while(indice<len(fechas)):
        dates.append(fechas[indice][0])
        indicadores.append(fechas[indice][1])
        indice = indice + 1

    plt.plot_date(dates, indicadores, linestyle='solid')
    plt.gcf().autofmt_xdate()
    date_format = mpl_dates.DateFormatter('%b, %d %y')
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.tight_layout()
    plt.show()


'''
Entradas: bitacora
Salidas: horas (list)
Restriciones: bitacora (file)
              bitacora debe de existir
              bitacora no puede estar vacio
'''
def extraerHoras():
    horas=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:           
            horas.append(columna[4])

    return horas


'''
Entradas: horas
Salidas: cantidadHoras (list)
Restriciones: horas (list)
              horas no puede estar vacía
'''
#Cuenta las horas registradas en la bitacora
def contarHoras(pLista):
    horas = eliminarElementosRepetidosBitacora(pLista)
    cantidadHoras=[]
    indice = 0
    cantidad = 0
    
    while(indice<len(horas)):
        cantidad = contarCaracter(pLista,horas[indice])
        cantidadHoras.append([horas[indice],cantidad])
        indice = indice + 1

    return cantidadHoras


'''
Entradas: horasPartidas
Salidas: listaFecha (list)
Restriciones: horasPartidas (list)
              horasPartidas no puede estar vacío
'''
def crearDatosHorasPartidas():
    horasPartidas = extraerHoras()
    indice = 0
    horas=""
    listaFecha=[]
    
    while(indice<len(horasPartidas)):
        horas = horasPartidas[indice].split(":")
        listaFecha.append(int(horas[0]))
        indice = indice + 1

    listaFecha.sort()
    listaFecha = contarHoras(listaFecha)
    
    return listaFecha


'''
Entradas: horasPartidas
Salidas: horas (list)
Restriciones: horasPartidas (list)
              horasPartidas no puede estar vacía
'''
#Clasifica las horas extraidas de bitacora
def clasificacionHorasPartidas():
    horasPartidas = crearDatosHorasPartidas()
    indice = 0
    horas = {"manana":0,"tarde":0,"noche":0}
    
    while(indice<len(horasPartidas)):
        if(horasPartidas[indice][0]>=5 and horasPartidas[indice][0]<=11):
            horas["manana"] +=  horasPartidas[indice][1]
        elif(horasPartidas[indice][0]>=12 and horasPartidas[indice][0]<=18):
            horas["tarde"] +=  horasPartidas[indice][1]
        elif( (horasPartidas[indice][0]>=19 and horasPartidas[indice][0]<=23) or (horasPartidas[indice][0]>=0 and horasPartidas[indice][0]<=4)):
            horas["noche"] +=  horasPartidas[indice][1]
        indice = indice + 1

    return horas
    

'''
Entradas: datos
Salidas: grafico de distribución de horarios donde se ha jugado (graph)
Restriciones: datos (list)
              datos no puede estar vacía
'''
#Crea un grafico segun la distribución de horarios donde se ha jugado (mañana, tarde, noche).
def graficoClasificacionHorasPartidas():
    datos = clasificacionHorasPartidas()
    indice = 0
    actividades=[]
    divisiones=[]
    
    for tiempo in datos:
        divisiones.append(datos[tiempo])
        actividades.append(tiempo)

    ypos = np.arange(len(actividades))

    plt.xticks(ypos,actividades)
    plt.bar(ypos,divisiones, width=0.5)
    plt.title("Distribución de horarios donde se ha jugado")
    plt.ylabel("Cantidad de partidas jugadas")
    plt.xlabel("Horarios")
    plt.show()


'''
Entradas: lista
Salidas: elementosMayores (list)
Restriciones: lista (list)
              lista no puede estar vacía
'''
#Crea una lista con los mejores jugadores
def identificarJugadoresGanadores():
    lista = crearDatosJugadoresGanadores()
    elementosMayores = []
    indice = 0
    parada = 5

    while(indice<parada):
        elementoMayor = encontrarMayor(lista)
        lista = eliminarMayor(lista,elementoMayor)
        elementosMayores.append(elementoMayor)
        indice = indice + 1

    return elementosMayores


'''
Entradas: datos 
Salidas: grafico de la frecuencia de configuración de partidas (graph)
Restriciones: datos (list)
              datos no puede estar vacio
'''
#Crea el grafico de top 5 de los jugadores que han ganado en más ocasiones.
def graficoJugadoresGanadores():
    datos = identificarJugadoresGanadores()
    indice = 0
    actividades=[]
    divisiones=[]
    
    while(indice<len(datos)):
        actividades.append(datos[indice][0])
        divisiones.append(datos[indice][1])
        indice = indice + 1

    plt.pie(divisiones, labels=actividades , startangle=90,autopct='%1.1f%%')
    plt.title("Top 5 de los jugadores que han ganado en más ocasiones.")
    plt.show()


'''
Entradas: datos 
Salidas: grafico de la frecuencia de configuración de partidas (graph)
Restriciones: datos (list)
              datos no puede estar vacio
'''
#Crea el grafico de la frecuencia de configuración de partidas.
def graficoFrecuenciaConfiguracion():
    datos = crearDatosTiposPartidasJugadas()
    indice = 0
    porcentajes=[]
    juegoTipos=["Juego en equis", "Juego en zeta","Cuatro esquinas","Cartón lleno"]
    
    while(indice<len(datos)):
        porcentajes.append(datos[indice][1])
        indice = indice + 1

    plt.pie(porcentajes, labels=juegoTipos , startangle=90,autopct='%1.1f%%')
    plt.title("Frecuencia de configuración de partidas.")
    plt.show()


'''
Entradas: bitacora
Salidas: numerosCantados (list)
Restriciones: bitacora (file)
              bitacora debe existir
              bitacora no puede estar vacio
'''
#Extrae los números cantados en configuración X
def extraerNumerosCantadosEnX():
    numerosCantados=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0]=='X'):
                output=eval(columna[1])
                numerosCantados += output

    return numerosCantados


'''
Entradas: ganadores, numeros
Salidas: cantidadNumeros (list)
Restriciones: ganadores (list)
              ganadores no puede estar vacio
              numeros (list)
              numeros no puede estar vacio
'''
#Acomoda los números cantados en configuración en X
def crearDatosNumerosCantadosEnX():
    ganadores = extraerNumerosCantadosEnX()
    numeros = eliminarElementosRepetidosBitacora(ganadores)
    cantidadNumeros=[]
    indice = 0
    cantidad = 0
    
    while(indice<len(numeros)):
        cantidad = contarCaracter(ganadores,numeros[indice])
        cantidadNumeros.append([numeros[indice],cantidad])
        indice = indice + 1

    return cantidadNumeros


'''
Entradas: bitacora
Salidas: numerosCantados (list)
Restriciones: bitacora (file)
              bitacora debe existir
              bitacora no puede estar vacio
'''
#Extrae los números cantados en configuración Z
def extraerNumerosCantadosEnZ():
    numerosCantados=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0]=='Z'):
                output=eval(columna[1])
                numerosCantados += output

    return numerosCantados


'''
Entradas: ganadores, numeros
Salidas: cantidadNumeros (list)
Restriciones: ganadores (list)
              ganadores no puede estar vacio
              numeros (list)
              numeros no puede estar vacio
'''
#Acomoda los números cantados en configuración en Z
def crearDatosNumerosCantadosEnZ():
    ganadores = extraerNumerosCantadosEnZ()
    numeros = eliminarElementosRepetidosBitacora(ganadores)
    cantidadNumeros=[]
    indice = 0
    cantidad = 0

    
    while(indice<len(numeros)):
        cantidad = contarCaracter(ganadores,numeros[indice])
        cantidadNumeros.append([numeros[indice],cantidad])
        indice = indice + 1

    return cantidadNumeros


'''
Entradas: bitacora
Salidas: numerosCantados (list)
Restriciones: bitacora (file)
              bitacora debe existir
              bitacora no puede estar vacio
'''
#Extrae los números cantados en configuración E
def extraerNumerosCantadosEnE():
    numerosCantados=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0]=='E'):
                output=eval(columna[1])
                numerosCantados += output

    return numerosCantados


'''
Entradas: ganadores, numeros
Salidas: cantidadNumeros (list)
Restriciones: ganadores (list)
              ganadores no puede estar vacio
              numeros (list)
              numeros no puede estar vacio
'''
#Acomoda los números cantados en configuración en E
def crearDatosNumerosCantadosEnE():
    ganadores = extraerNumerosCantadosEnE()
    numeros = eliminarElementosRepetidosBitacora(ganadores)
    cantidadNumeros=[]
    indice = 0
    cantidad = 0

    while(indice<len(numeros)):
        cantidad = contarCaracter(ganadores,numeros[indice])
        cantidadNumeros.append([numeros[indice],cantidad])
        indice = indice + 1

    return cantidadNumeros


'''
Entradas: bitacora
Salidas: numerosCantados (list)
Restriciones: bitacora (file)
              bitacora debe existir
              bitacora no puede estar vacio
'''
#Extrae los números cantados en configuración L
def extraerNumerosCantadosEnL():
    numerosCantados=[]
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0]=='L'):
                output=eval(columna[1])
                numerosCantados += output

    return numerosCantados


'''
Entradas: ganadores, numeros
Salidas: cantidadNumeros (list)
Restriciones: ganadores (list)
              ganadores no puede estar vacio
              numeros (list)
              numeros no puede estar vacio
'''
#Acomoda los números cantados en configuración en L 
def crearDatosNumerosCantadosEnL():
    ganadores = extraerNumerosCantadosEnL()
    numeros = eliminarElementosRepetidosBitacora(ganadores)
    cantidadNumeros = []
    indice = 0
    cantidad = 0

    while(indice<len(numeros)):
        cantidad = contarCaracter(ganadores,numeros[indice])
        cantidadNumeros.append([numeros[indice],cantidad])
        indice = indice + 1

    return cantidadNumeros


'''
Entradas: pLista
Salidas: listaNueva (list)
Restriciones: pLista (list)
              pLista no puede estar vacio
'''
#Extrae los números importantes cantados
def extrarNumerosMayoresImportantes(pLista):
    indiceA =0
    listaNueva=[]
    
    while(indiceA<len(pLista)):
        listaNueva.append(pLista[indiceA][0])
        indiceA = indiceA + 1
    return listaNueva


'''
Entradas: pListaA, pListaB
Salidas: listaNueva (list)
Restriciones: pListaA (list)
              pListaA no puede estar vacía
              pListaB (list)
              pListaB no puede estar vacía
'''
#Crear una lista con los números parecidos a la primera posición de pListaA
def acomadarNumerosImportantes(pListaA,pListaB):
    indiceA =0
    indiceB =0
    listaNueva=[]
    
    while(indiceA<len(pListaA)):
        while(indiceB<len(pListaB)):
            if(pListaA[indiceA][0]==pListaB[indiceB][0]):
                listaNueva.append(pListaB[indiceB][1])
            indiceB = indiceB +1
        indiceB = 0
        indiceA = indiceA + 1
    return listaNueva


'''
Entradas: listaMayores 
Salidas: grafico de top 10 números contados por configuracion (graph)
Restriciones: listaMayores (list)
              listaMayores no puede estar vacio
'''
#Crea el top 10 de números que más se han cantado por configuración de partida
def graficoTopNumerosContadosPorConfiguracion():
    listaMayores = identificarNumerosMayores()
    numerosEnX = crearDatosNumerosCantadosEnX()
    numerosEnX = acomadarNumerosImportantes(listaMayores,numerosEnX)
    numerosEnZ = crearDatosNumerosCantadosEnZ()
    numerosEnZ = acomadarNumerosImportantes(listaMayores,numerosEnZ)
    numerosEnE = crearDatosNumerosCantadosEnE()
    numerosEnE = acomadarNumerosImportantes(listaMayores,numerosEnE)
    numerosEnL = crearDatosNumerosCantadosEnL()
    numerosEnL = acomadarNumerosImportantes(listaMayores,numerosEnL)
    
    listaMayores = extrarNumerosMayoresImportantes(listaMayores)
    df = pd.DataFrame({'Juego en equis': numerosEnX,'Juego en zeta': numerosEnZ,'Juego cuatro esquinas': numerosEnE,'Juego cartón lleno': numerosEnL,}, index=listaMayores)
    ax = df.plot.bar(rot=0)
    plt.show()