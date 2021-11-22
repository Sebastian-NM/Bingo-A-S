'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''

import matplotlib .pyplot as plt
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


# Variables gobales
cartones = {}
jugadores = {}
jugadoresConCartones = {}
cartonesJuego = {}
listaIdentificadores = []
identificadoresLibres = []
listaNumerosCantados = []
listaGanadores = []
tipoJuego = ""
premio = ""


# CREACIÓN DE IDENTIFICADORES PARA LOS CARTONES Y SUS VALIDACIONES

# FUNCIÓN RECURSIVA ENCARGADA DE CREAR TRES NÚMEROS ALEATORIOS
def crearNumero(numero=3):
    if(numero == 0):
        return ""
    return str(randint(0, 9))+crearNumero(numero-1)


# FUNCIÓN RECURSIVA ENCARGADA DE CREAR TRES LETRAS ALEATORIAS
def crearLetras(numero=3):
    abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    indice = randrange(len(abecedario))

    if(numero == 0):
        return ""

    return abecedario[indice]+crearLetras(numero-1)


# FUNCIÓN ENCARGADA DE FORMAR EL IDENTIFICADOR
def crearIdententificador():
    identificardor = crearLetras() + crearNumero()
    return identificardor


# FUNCIÓN RECURSIVA ENCARGADA DE CREAR UNA LISTA DE POSIBLES IDENTIFICADORES
def crearListaIdentificadores(pNum):
    if(pNum == 0):
        return []
    else:
        return [crearIdententificador()] + crearListaIdentificadores(pNum-1)


# FUNCIÓN RECURSIVA ENCARGADA DE INDICAR SI UN IDENTIFICADOR YA EXISTE
def identificadorRepetido(pLista, pIdentificador):
    if(pLista == []):
        return False
    elif(pLista[0] == pIdentificador):
        return True
    else:
        return identificadorRepetido(pLista[1:], pIdentificador)


# FUNCIÓN RECURSIVA ENCARGADA DE CREAR UNA LISTA CON IDENTIFICADORES NO REPETIDOS
def crearListaIdentificadoresNoRepetidos(pNum):
    lista = crearListaIdentificadores(pNum)
    indice = 0

    while(indice < len(lista)):
        if(identificadorRepetido(lista[indice+1:], lista[indice])):
            indice = 0
            lista = crearListaIdentificadores(pNum)
        indice = indice + 1

    return lista


# FUNCIONES PARA PARA LA CREACIÓN DEL CARTÓN DE BINGO Y SU ALMACENAMIENTO

# FUNCIÓN RECURSIVA ENCARGADA DE CREAR NÚMEROS ALEATORIOS EN EL CARTÓN
def crearNumerosRandomCarton(pInicio, pFin, Numero=5):
    if(Numero == 0):
        return []
    else:
        return [randrange(pInicio, pFin)]+crearNumerosRandomCarton(pInicio, pFin, Numero-1)


# FUNCIÓN RECURSIVA ENCARGADA DE INDICAR SI ALGÚN NÚMERO DEL CARTÓN ESTÁ REPETIDO
def recorrerElementosCarton(pLista):
    if(pLista == []):
        return False
    elif(identificadorRepetido(pLista[1:], pLista[0])):
        return True
    else:
        return recorrerElementosCarton(pLista[1:])


# FUNCIÓN RECURSIVA ENCARGADA DE CREAR LOS NÚMEROS DEL CARTÓN DE BINGO
def crearNumerosCarton(pInicio, pFin):
    fila = []
    while(True):
        fila = crearNumerosRandomCarton(pInicio, pFin)
        if(recorrerElementosCarton(fila) == False):
            return fila


# FUNCIÓN  ENCARGADA DE CREAR Y ACOMODAR LOS ELEMENTOS DEL CARTÓN
def crearElementosCarton():
    carton = []
    vector = []
    fila1 = crearNumerosCarton(1, 15)
    fila2 = crearNumerosCarton(16, 30)
    fila3 = crearNumerosCarton(31, 45)
    fila4 = crearNumerosCarton(46, 60)
    fila5 = crearNumerosCarton(61, 75)
    indiceA = 0
    indiceB = 0

    while(indiceA < 5):
        vector.append(fila1[indiceA])
        vector.append(fila2[indiceA])
        vector.append(fila3[indiceA])
        vector.append(fila4[indiceA])
        vector.append(fila5[indiceA])
        carton.append(vector)
        vector = []
        indiceA = indiceA+1

    return carton


# FUNCIÓN ENCARGADA DE CREAR EL CARTÓN DE BINGO
def crearCarton(pNum):
    global cartones
    global listaIdentificadores

    indenticadores = crearListaIdentificadoresNoRepetidos(pNum)
    listaIdentificadores = indenticadores

    indice = 0
    while(indice < pNum):
        cartones[indenticadores[indice]] = crearElementosCarton()
        indice = indice+1

    return cartones


# FUNCIÓN ENCARGADA DE VERIFICAR SI LA CARPETA DONDE SE ALMACENAN EXISTE
def existeCarpetaCartones():
    if os.path.isdir('cartones'):
        return True
    else:
        return False


# FUNCIÓN ENCARGADA DE ELIMINAR LOS CARTONES DE LA CARPETA DONDE SE ALMACENAN
def eliminarCarpetaCartones():
    global cartones
    global listaIdentificadores

    try:
        rmtree("cartones")
        os.mkdir("cartones")
        listaIdentificadores = []
        cartones = {}
    except:
        pass

    if(existeCarpetaCartones() == False):
        os.mkdir("cartones")


# FUNCIÓN ENCARGADA DE ELIMINAR LOS IDENTIFICADORES DE CARTONES YA USADOS
def eliminarIdentificadores(pIdentificadores):
    global identificadoresLibres
    indice = 0

    while(indice < len(pIdentificadores)):
        if(identificadorRepetido(identificadoresLibres, pIdentificadores[indice])):
            posicion = posicionIdentificador(
                identificadoresLibres, pIdentificadores[indice])
            identificadoresLibres.pop(posicion)
        indice = indice + 1


# FUNCIÓN ENCARGADA DE INDICAR LA CANTIDAD DE IDENTIFICADORES DISPONIBLES EN EL SISTEMA
def cantidadIdentificadoresLibres():
    global identificadoresLibres
    return len(identificadoresLibres)


# FUNCIÓN ENCARGADA DE ELIMINAR LOS IDENTIFICADORES ASIGNADOS A LOS JUGADORES
def listaIdentificadoresLibres():
    global jugadoresConCartones
    global identificadoresLibres
    global listaIdentificadores

    identificadoresLibres = listaIdentificadores.copy()

    for jugador in jugadoresConCartones:
        eliminarIdentificadores(jugadoresConCartones[jugador])


# FUNCIÓN ENCARGADA DE IMPRIMIR LOS CARTONES ALMACENADOS EN MEMORIA
def imprimirCartones():
    global cartonesJuego
    matriz = cartonesJuego
    indiceA = 0
    indiceB = 0

    for clave in matriz:
        while(indiceA < len(matriz[clave])):
            indiceA = indiceA + 1
        indiceA = 0


# FUNCIÓN ENCARGADA DE CREAR LA IMAGEN DEL CARTÓN
def crearImagen(pCarton, pIdentificador):
    img = Image.open('tabla.png')
    draw = ImageDraw.Draw(img)
    fuente = ImageFont.truetype("fuente\Staatliches-Regular.ttf", 60)
    draw.text((100, 55), "B", (0, 2, 27), font=fuente)
    draw.text((280, 55), "I", (0, 2, 27), font=fuente)
    draw.text((440, 55), "N", (0, 2, 27), font=fuente)
    draw.text((605, 55), "G", (0, 2, 27), font=fuente)
    draw.text((775, 55), "O", (0, 2, 27), font=fuente)
    draw.text((100, 140), str(pCarton[0][0]), (0, 2, 27), font=fuente)
    draw.text((260, 140), str(pCarton[0][1]), (0, 2, 27), font=fuente)
    draw.text((430, 140), str(pCarton[0][2]), (0, 2, 27), font=fuente)
    draw.text((595, 140), str(pCarton[0][3]), (0, 2, 27), font=fuente)
    draw.text((760, 140), str(pCarton[0][4]), (0, 2, 27), font=fuente)
    draw.text((100, 225), str(pCarton[1][0]), (0, 2, 27), font=fuente)
    draw.text((260, 225), str(pCarton[1][1]), (0, 2, 27), font=fuente)
    draw.text((430, 225), str(pCarton[1][2]), (0, 2, 27), font=fuente)
    draw.text((595, 225), str(pCarton[1][3]), (0, 2, 27), font=fuente)
    draw.text((760, 225), str(pCarton[1][4]), (0, 2, 27), font=fuente)
    draw.text((100, 310), str(pCarton[2][0]), (0, 2, 27), font=fuente)
    draw.text((260, 310), str(pCarton[2][1]), (0, 2, 27), font=fuente)
    draw.text((430, 310), str(pCarton[2][2]), (0, 2, 27), font=fuente)
    draw.text((595, 310), str(pCarton[2][3]), (0, 2, 27), font=fuente)
    draw.text((760, 310), str(pCarton[2][4]), (0, 2, 27), font=fuente)
    draw.text((100, 395), str(pCarton[3][0]), (0, 2, 27), font=fuente)
    draw.text((260, 395), str(pCarton[3][1]), (0, 2, 27), font=fuente)
    draw.text((430, 395), str(pCarton[3][2]), (0, 2, 27), font=fuente)
    draw.text((595, 395), str(pCarton[3][3]), (0, 2, 27), font=fuente)
    draw.text((760, 395), str(pCarton[3][4]), (0, 2, 27), font=fuente)
    draw.text((100, 480), str(pCarton[4][0]), (0, 2, 27), font=fuente)
    draw.text((260, 480), str(pCarton[4][1]), (0, 2, 27), font=fuente)
    draw.text((430, 480), str(pCarton[4][2]), (0, 2, 27), font=fuente)
    draw.text((595, 480), str(pCarton[4][3]), (0, 2, 27), font=fuente)
    draw.text((760, 480), str(pCarton[4][4]), (0, 2, 27), font=fuente)
    draw.text((210, 565), "Identificador: " +
              pIdentificador, (0, 2, 27), font=fuente)
    img.save('cartones/'+pIdentificador+'.png')


# FUNCIÓN ENCARGADA DE LIMPIAR LAS VARIABLES GLOBALES
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

    cartones = {}
    jugadores = {}
    jugadoresConCartones = {}
    identificadoresLibres = []
    listaIdentificadores = []
    tipoJuego = ""
    premio = ""
    listaNumerosCantados = []
    cartonesJuego = {}
    listaGanadores = []


# CREACIÓN DE JUEGADORES Y SUS VALIDACIONES

# FUNCIÓN ENCARGADA DE IDENTIFICAR SI LA CARPETA JUGADORES EXISTE
def existeCarpetaJugadores():
    if os.path.isdir('jugadores'):
        return True
    else:
        return False


# FUNCIÓN ENCARGADA DE IDENTIFICAR SI EXISTE EL ARCHIVO DONDE SE ALMACENAN LOS JUGADORES
def existeArchivoJugadores():
    if os.path.isfile('jugadores/jugadores.csv'):
        return True
    else:
        return False


# FUNCIÓN ENCARGADA DE IDENTIFICAR SI LA CÉDULA DEL JUGADOR YA EXISTE
def existeJugador(pCedula):
    if(existeCarpetaJugadores() == False):
        return False

    with open("jugadores/jugadores.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0] == pCedula):
                return True
        return False


# FUNCIÓN ENCARGADA DE AGREGAR EL NUEVO JUGADOR EN EL ARCHIVO JUGADORES
def crearJugador(pNombre, pCedula, pCorreo):
    if(existeCarpetaJugadores() == False):
        os.mkdir("jugadores")
    elif(existeArchivoJugadores() == False):
        rmtree("jugadores")
        os.mkdir("jugadores")

    archivo = open("jugadores/jugadores.csv", "a")
    archivo.write(pCedula)
    archivo.write(";")
    archivo.write(pNombre)
    archivo.write(";")
    archivo.write(pCorreo+"\n")
    archivo.close()


# FUNCIÓN ENCARGADA DE EXTRAER EL CORREO DEL JUGADOR
def extraerCorreoJugador(pCedula):
    with open("jugadores/jugadores.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            if(columna[0] == pCedula):
                return columna[2]


# FUNCIÓN ENCARGADA DE IDENTIFICAR SI EXISTE LA CÉDULA DEL JUGADOR PARA ASIGNARLE UN CARTÓN
def jugadorConCarton(pCedula):
    global jugadoresConCartones

    try:
        jugadoresConCartones[pCedula]
        return True
    except:
        return False


# FUNCIÓN ENCARGADA DE ASOCIAR UN JUGADOR CON CARTONES
def crearJugadorConCartones(pCedula):
    global jugadoresConCartones
    jugadoresConCartones[pCedula] = []


# FUNCIÓN ENCARGADA DE INDICAR LA CANTIDAD DE CARTONES QUE POSEE UN JUGADOR
def cantidadCartonesJugador(pCedula):
    global jugadoresConCartones
    cartones = jugadoresConCartones[pCedula]
    return len(cartones)


# FUNCIÓN RECURSIVA ENCARGADA DE IDENTIFICAR LA POSICIÓN DEL IDENTIFICADOR EN LA LISTA
def posicionIdentificador(pLista, pIdentificador, posicion=0):
    if(pLista == []):
        return 0
    elif(pLista[0] == pIdentificador):
        return posicion
    else:
        return posicionIdentificador(pLista[1:], pIdentificador, posicion+1)


# FUNCIÓN ENCARGADA DE EXTRAER EL IDENTIFICADOR DEL JUGADOR ASIGNADO A UN CARTÓN
def extraerIdentificadorJugadorConCarton(pIdentificador):
    global jugadoresConCartones
    global jugadores
    for jugador in jugadoresConCartones:
        for identificadores in jugadoresConCartones[jugador]:
            if(identificadores == pIdentificador):
                return [jugador, jugadores[jugador][0]]


# FUNCIÓN ENCARGADA DE INDENTIFICAR SI EL IDENTIFICADOR ESTÁ ASOCIADO CON UN JUGADOR
def identificarJugadorConCarton(pIdentificador):
    global jugadoresConCartones

    for jugador in jugadoresConCartones:
        for identificadores in jugadoresConCartones[jugador]:
            if(identificadores == pIdentificador):
                return True

    return False


# FUNCIÓN ENCARGADA DE ASIGNAR LOS CARTONES A UN JUGADOR
def agragerCartonesAJugadores(pCedula, pCartones):
    global jugadoresConCartones
    global identificadoresLibres

    lista = jugadoresConCartones[pCedula]
    indice = 0

    if(pCartones <= len(identificadoresLibres)):
        while(indice < pCartones):
            numero = randrange(len(identificadoresLibres))
            lista.append(identificadoresLibres[numero])
            identificadoresLibres.pop(numero)

            indice = indice + 1

    jugadoresConCartones[pCedula] = lista
    enviarCartonesPorCorreo(pCedula)


# FUNCIÓN ENCARGADA DE EXTRAER LA CANTIDAD DE JUGADORES EXISTENTES EN MEMORIA
def extraerCantidadJugadores():
    global jugadores
    return len(jugadores)


# FUNCIÓN ENCARGADA DE CREAR UNA LISTA DE LOS JUGADORES
def listaJugadores():
    global jugadores
    if(existeCarpetaJugadores() == False):
        os.mkdir("jugadores")
        archivo = open("jugadores/jugadores.csv", "a")
        archivo.close()
    elif(existeArchivoJugadores() == False):
        rmtree("jugadores")
        os.mkdir("jugadores")
        archivo = open("jugadores/jugadores.csv", "a")
        archivo.close()

    with open("jugadores/jugadores.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            jugadores[columna[0]] = [columna[1], columna[2]]


# FUNCIÓN ENCARGADA DE RECORRER LOS ELEMENTOS EXISTENTES DE LA CARPETA CARTONES
def existeImagenEnCarpeta(pIdentificador):
    archivos = [carpeta for carpeta in os.listdir(
        "cartones/") if os.path.isfile(os.path.join("cartones/", carpeta))]

    return identificadorRepetido(archivos, pIdentificador+".png")


# ENVÍO DE CORREOS ELECTRÓNICOS Y SUS VALIDACIONES

# FUNCIÓN ENCARGADA DE ENVIAR LOS CARTONES ASIGNADOS SEGÚN LA CÉDULA DEL JUGADOR
def enviarCartonesPorCorreo(pCedula):
    global jugadores
    global jugadoresConCartones

    listaCartones = jugadoresConCartones[pCedula]

    sender_email = "bingoitcr.as01@gmail.com"
    receiver_email = jugadores[pCedula][1]

    msg = MIMEMultipart()
    msg['Subject'] = 'Bingo, entrega de cartones'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('Hola estimado(a) ' + jugadores[pCedula][0] +
                       " ¡se te han asignado los siguientes cartones!")
    msg.attach(msgText)

    indice = 0
    while(indice < len(listaCartones)):
        with open('cartones/'+listaCartones[indice]+'.png', 'rb') as fp:
            img = MIMEImage(fp.read())
            img.add_header('Content-Disposition', 'attachment',
                           filename=listaCartones[indice]+".png")
            msg.attach(img)
        indice = indice + 1

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login("bingoitcr.as01@gmail.com", "Chocofresa526")
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)


# FUNCIÓN ENCARGADA DE IDENTIFICAR LOS JUGADORES GANADORES Y ENVIAR EL CORREO
def enviarEmailGanadores():
    global listaGanadores
    jugadoresConCartones
    global jugadores

    indiceA = 0
    while(indiceA < len(listaGanadores)):
        if(identificarJugadorConCarton(listaGanadores[indiceA])):
            informacionJugador = extraerIdentificadorJugadorConCarton(
                listaGanadores[indiceA])
            enviarCorreoGanadores(jugadores[informacionJugador[0]][0],
                                  listaGanadores[indiceA], jugadores[informacionJugador[0]][1])
        indiceA = indiceA + 1


# FUNCIÓN ENCARGADA DE ENVIAR EL CORREO AL JUGADOR GANADOR
def enviarCorreoGanadores(pNombre, pCarton, pDestinatario):
    global tipoJuego
    global premio

    sender_email = "bingoitcr.as01@gmail.com"
    receiver_email = pDestinatario

    msg = MIMEMultipart()
    msg['Subject'] = 'Bingo, ¡felicidades eres un ganador!'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('¡Hola '+pNombre + "!\n has ganado la partida de bingo en la modalidad de "+str(tipoJuego) +
                       ". Tu premio corresponde a: "+str(premio) + "\n¡Felicidades!")
    msg.attach(msgText)

    with open('cartones/'+pCarton+'.png', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment',
                       filename=pCarton+".png")
        msg.attach(img)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login("bingoitcr.as01@gmail.com", "Chocofresa526")
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)


# ESTADÍSTICAS Y GRÁFICOS

# FUNCIÓN ENCARGADA DE CONECTAR LOS DATOS DE LA INTERFAZ DEL GRÁFICO CON LA LÓGICA
def guardarDatosJuego(pTipoJuego, pPremio):
    global tipoJuego
    global premio

    premio = pPremio
    tipoJuego = pTipoJuego


# FUNCIÓN ENCARGADA DE CREAR UN GRÁFICO DE TOP 10 DE NÚMEROS CANTADOS
def graficoNumerosCantados():
    datos = identificarNumerosMayores()
    indice = 0
    numeros = []
    porcentajes = []

    while(indice < len(datos)):
        numeros.append(datos[indice][0])
        porcentajes.append(datos[indice][1])
        indice = indice + 1

    ypos = np.arange(len(numeros))

    plt.xticks(ypos, numeros)
    plt.bar(ypos, porcentajes, width=0.5)
    plt.title("Grafico de barras")
    plt.ylabel("Veces que aparecen")
    plt.xlabel("Números cantados")
    plt.show()


# FUNCIÓN ENCARGADA DE CLASIFICAR LAS PARTIDAS SEGÚN LAS VECES QUE SE JUGARON
def crearDatosTiposPartidasJugadas():
    tiposPartidasJugadas = extraerTiposPartidasJugadas()
    tipoJuego = ["X", "Z", "E", "L"]
    juegos = []
    indice = 0
    cantidad = 0

    while(indice < len(tipoJuego)):
        cantidad = contarCaracter(tiposPartidasJugadas, tipoJuego[indice])
        juegos.append([tipoJuego[indice], cantidad])
        indice = indice + 1

    return juegos


# FUNCIÓN ENCARGADA DE CREAR EL GRÁFICO DE LA FRECUENCIA DE LA CONFIGURACIÓN DE PARTIDAS
def graficoFrecuenciaConfiguracion():
    datos = crearDatosTiposPartidasJugadas()
    indice = 0
    porcentajes = []
    juegoTipos = ["Juego en equis", "Juego en zeta",
                  "Cuatro esquinas", "Cartón lleno"]

    while(indice < len(datos)):
        porcentajes.append(datos[indice][1])
        indice = indice + 1

    plt.pie(porcentajes, labels=juegoTipos, startangle=90, autopct='%1.1f%%')
    plt.title("Frecuencia de configuración de partidas.")
    plt.show()


# JUGAR BINGO

# FUNCIÓN ENCARGADA DE RETORNAR EL ÚLTIMO NÚMERO CANTADO
def ultimoNumeroCantado():
    global listaNumerosCantados

    return listaNumerosCantados[-1]


# FUNCIÓN ENCARGADA DE ENVIAR LOS DATOS DEL JUEGO
def enviarDatosJuego():
    global tipoJuego
    global premio

    return tipoJuego, premio


# FUNCIÓN ENCARGADA DE ENVIAR LA CANTIDAD DE CARTONES EXISTENTES
def enviarTotalCartones():
    global cartones
    return len(cartones)


# FUNCIÓN ENCARGADA DE CREAR UN NÚMERO ENTRE 0 Y 75
def crearNumerosPartida():
    numero = randint(0, 75)
    return numero


# FUNCIÓN ENCARGADA DE CREAR UN NUEVO NÚMERO PARA CANTARLO
def agregarNumeroASecuencia():
    global listaNumerosCantados
    numero = crearNumerosPartida()

    while(True):
        if(identificadorRepetido(listaNumerosCantados, numero) == False):
            listaNumerosCantados.append(numero)
            break
        else:
            numero = crearNumerosPartida()

    return listaNumerosCantados


# FUNCIÓN ENCARGADA DE MARCAR EL CARTÓN SEGÚN EL NÚMERO CANTADO
def marcarNumero(pCarton):
    global listaNumerosCantados
    matriz = [[], [], [], [], []]
    indiceA = 0
    indiceB = 0

    while(indiceA < len(pCarton)):
        while(indiceB < len(pCarton[indiceA])):
            if(pCarton[indiceA][indiceB] == listaNumerosCantados[-1]):
                matriz[indiceA].append("X")
            else:
                matriz[indiceA].append(pCarton[indiceA][indiceB])
            indiceB = indiceB + 1
        indiceB = 0
        indiceA = indiceA + 1

    return matriz


# FUNCIÓN ENCARGADA DE IDENTIFICAR SI EL CARTÓN ES UN JUEGO EN X
def juegoEnX(pCarton):
    identificador = len(pCarton)
    indiceA = 0
    indiceB = 0

    while(indiceA < len(pCarton)):
        identificador = identificador - 1
        while(indiceB < len(pCarton[indiceA])):
            if(indiceB == indiceA or indiceB == identificador):
                if(pCarton[indiceA][indiceB] != "X"):
                    return False
            indiceB = indiceB + 1
        indiceB = 0

        indiceA = indiceA + 1
    return True


# FUNCIÓN ENCARGADA DE IDENTIFICAR SI EL CARTÓN ES UN JUEGO EN CUATRO ESQUINAS
def juegoCuatroEsquinas(pCarton):
    identificador = len(pCarton)-1
    indiceA = 0
    indiceB = 0

    while(indiceA < len(pCarton)):
        while(indiceB < len(pCarton[indiceA])):
            if((indiceA == 0 and indiceB == 0) or (indiceA == 0 and indiceB == identificador)):
                if(pCarton[indiceA][indiceB] != "X"):
                    return False
            if((indiceA == 4 and indiceB == 0) or (indiceA == 4 and indiceB == identificador)):
                if(pCarton[indiceA][indiceB] != "X"):
                    return False
            indiceB = indiceB + 1
        indiceB = 0
        indiceA = indiceA + 1
    return True


# FUNCIÓN ENCARGADA DE IDENTIFICAR SI EL CARTÓN ES UN JUEGO COMPLETO
def juegoCartonCompleto(pCarton):
    indiceA = 0
    indiceB = 0

    while(indiceA < len(pCarton)):
        while(indiceB < len(pCarton[indiceA])):
            if(pCarton[indiceA][indiceB] != "X"):
                return False
            indiceB = indiceB + 1
        indiceB = 0

        indiceA = indiceA + 1
    return True


# FUNCIÓN ENCARGADA DE IDENTIFICAR SI EL CARTÓN ES UN JUEGO EN Z
def juegoEnZ(pCarton):
    diagonalInversa = len(pCarton)
    indiceA = 0
    indiceB = 0

    while(indiceA < len(pCarton)):
        diagonalInversa = diagonalInversa - 1
        while(indiceB < len(pCarton[indiceA])):
            if(indiceA == 0 or indiceA == 4):
                if(pCarton[indiceA][indiceB] != "X"):
                    return False
            if(indiceB == diagonalInversa):
                if(pCarton[indiceA][indiceB] != "X"):
                    return False
            indiceB = indiceB + 1

        indiceB = 0
        indiceA = indiceA + 1
    return True


# FUNCIÓN ENCARGADA DE CREAR UNA COPIA DE CARTONES
def copiaCartones():
    global cartones
    global cartonesJuego

    cartonesJuego = cartones.copy()


# FUNCIÓN ENCARGADA DE MARCAR LOS CARTONES
def marcarCartones():
    global cartonesJuego

    for clave in cartonesJuego:
        cartonesJuego[clave] = marcarNumero(cartonesJuego[clave])


# FUNCIÓN ENCARGADA DE RETORNAR LA CANTIDAD DE GANADORES
def retornarGanadores():
    global listaGanadores
    return listaGanadores


# FUNCIÓN ENCARGADA DE IDENTIFICAR LOS JUGADORES DEL JUEGO
def identificarGanadores(pModoJuego):
    global cartonesJuego
    global listaGanadores

    for clave in cartonesJuego:
        if(pModoJuego == 'Jugar en X'):
            if(juegoEnX(cartonesJuego[clave])):
                listaGanadores.append(clave)
        elif(pModoJuego == 'Cuatro esquinas'):
            if(juegoCuatroEsquinas(cartonesJuego[clave])):
                listaGanadores.append(clave)
        elif(pModoJuego == 'Cartón lleno'):
            if(juegoCartonCompleto(cartonesJuego[clave])):
                listaGanadores.append(clave)
        elif(pModoJuego == 'Jugar en Z'):
            if(juegoEnZ(cartonesJuego[clave])):
                listaGanadores.append(clave)


# FUNCIÓN ENCARGADA DE EJECUTAR UNA PARTIDA SEGÚN EL MODO DE JUEGO
def cantarNumeros(pModoJuego):
    global listaGanadores
    agregarNumeroASecuencia()
    marcarCartones()
    identificarGanadores(pModoJuego)

    if(listaGanadores != []):
        return True
    else:
        return False


# FUNCIÓN ENCARGADA DE LIMPIAR LAS VARIABLES PARA INICIAR UN NUEVO JUEGO
def limpiarVariables():
    global cartonesJuego
    global tipoJuego
    global premio
    global listaNumerosCantados
    global listaGanadores

    cartonesJuego = {}
    tipoJuego = ""
    premio = ""
    listaNumerosCantados = []
    listaGanadores = []


# BITÁCORA

# FUNCIÓN ENCARGADA DE IDENTIFICAR SI LA CARPETA DONDE SE ALMACENA LA BITÁCORA EXISTE
def existeCarpetaBitacora():
    if os.path.isdir('bitacoraPartidas'):
        return True
    else:
        return False


# FUNCIÓN ENCARGADA DE IDENTIFICAR SI EXISTE EL ARCHIVO BITÁCORA
def existeArchivoBitacora():
    if os.path.isfile('bitacoraPartidas/bitacora.csv'):
        return True
    else:
        return False


# FUNCIÓN ENCARGADA PARA CREAR UN REGISTRO EN LA BITÁCORA
def crearRegistro():
    global listaNumerosCantados
    global tipoJuego
    listaInformacion = []
    indice = 0
    listaCedulas = []

    while(indice < len(listaGanadores)):
        if(identificarJugadorConCarton(listaGanadores[indice])):
            listaInformacion = extraerIdentificadorJugadorConCarton(
                listaGanadores[indice])
            if(identificadorRepetido(listaCedulas, str(listaInformacion[0])) == False):
                listaCedulas.append(str(listaInformacion[0]))
        indice = indice + 1

    dia = date.today()
    hora = datetime.now()

    if(existeCarpetaBitacora() == False):
        os.mkdir("bitacoraPartidas")
    elif(existeArchivoBitacora() == False):
        rmtree("bitacoraPartidas")
        os.mkdir("bitacoraPartidas")

    if(tipoJuego == 'Jugar en X'):
        tipoJuego = "X"
    elif(tipoJuego == 'Cuatro esquinas'):
        tipoJuego = "E"
    elif(tipoJuego == 'Cartón lleno'):
        tipoJuego = "L"
    elif(tipoJuego == 'Jugar en Z'):
        tipoJuego = "Z"

    archivo = open("bitacoraPartidas/bitacora.csv", "a")
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


# FUNCIÓN ENCARGADA DE EXTRAER LOS TIPOS DE JUEGOS DE LAS PARTIDAS EN LA BITÁCORA
def extraerTiposPartidasJugadas():
    tiposPartidasJugadas = []
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            tiposPartidasJugadas.append(columna[0])

    return tiposPartidasJugadas


# FUNCIÓN ENCARGADA DE ELIMINAR LOS ELEMENTOS REPETIDOS DE LA BITÁCORA
def eliminarElementosRepetidosBitacora(pLista):
    listaNueva = list(set(pLista))
    return listaNueva


# FUNCIÓN ENCARGADA DE EXTRAER LOS NÚMEROS CANTADOS DE LA BITÁCORA
def extraerNumerosCantados():
    numerosCantados = []
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            output = eval(columna[1])
            numerosCantados += output

    return numerosCantados


# FUNCIÓN ENCARGADA DE EXTRAER LOS GANADORES DE LA BITÁCORA
def extraerJugadoresGanadores():
    numerosCantados = []
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            output = eval(columna[2])
            numerosCantados += output

    return numerosCantados


# FUNCIÓN ENCARGADA DE UNIR LOS NÚMEROS CANTADOS CON LA CANTIDAD DE VECES QUE FUE ENCONTRADO
def crearDatosNumerosContados():
    numerosCantados = extraerNumerosCantados()
    numeros = eliminarElementosRepetidosBitacora(numerosCantados)
    cantados = []
    indice = 0
    cantidad = 0

    while(indice < len(numeros)):
        cantidad = contarCaracter(numerosCantados, numeros[indice])
        cantados.append([numeros[indice], cantidad])

        indice = indice + 1

    return cantados


# FUNCIÓN ENCARGADA DE ENCONTRAR EL NÚMERO MAYOR
def encontrarMayor(lista):
    indice = 0
    mayor = 0
    numero = 0

    while(indice < len(lista)):
        if(mayor < lista[indice][1]):
            mayor = lista[indice][1]
            numero = lista[indice][0]
        indice = indice + 1

    return [numero, mayor]


# FUNCIÓN ENCARGADA DE ELIMINAR EL ELEMENTO MAYOR DE LA LISTA SEGÚN UN ELEMENTO
def eliminarMayor(lista, elemento):
    indice = 0
    listaNueva = []

    while(indice < len(lista)):
        if(lista[indice][0] != elemento[0]):
            listaNueva.append([lista[indice][0], lista[indice][1]])
        indice = indice + 1

    return listaNueva


# FUNCIÓN ENCARGADA DE UNIR LOS NÚMEROS CON SUS APARICIONES
def identificarNumerosMayores():
    lista = crearDatosNumerosContados()
    elementosMayores = []
    indice = 0
    parada = 10

    while(indice < parada):
        elementoMayor = encontrarMayor(lista)
        lista = eliminarMayor(lista, elementoMayor)
        elementosMayores.append(elementoMayor)
        indice = indice + 1

    return elementosMayores


# FUNCIÓN ENCARGADA DE INTEGRAR LOS GANADORES CON LA CANTIDAD DE VECES QUE GANÓ EN UNA LISTA
def crearDatosJugadoresGanadores():
    ganadores = extraerJugadoresGanadores()
    cedulas = eliminarElementosRepetidosBitacora(ganadores)
    cantidadGanadores = []
    indice = 0
    cantidad = 0

    while(indice < len(cedulas)):
        cantidad = contarCaracter(ganadores, cedulas[indice])
        cantidadGanadores.append([cedulas[indice], cantidad])
        indice = indice + 1

    return cantidadGanadores


# FUNCIÓN ENCARGADA DE EXTRAER FECHAS DE LA BITÁCORA
def extraerFechaPartidas():
    fechasPartidas = []
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            fechasPartidas.append(columna[3])

    return fechasPartidas


# FUNCIÓN ENCARGADA DE CLASIFICAR LAS FECHAS SEGÚN SU APARICIÓN EN LA BITÁCORA
def crearDatosFechaPartidas():
    fechasPartidas = extraerFechaPartidas()
    partidas = eliminarElementosRepetidosBitacora(fechasPartidas)
    fechas = []
    indice = 0
    cantidad = 0

    while(indice < len(partidas)):
        cantidad = contarCaracter(fechasPartidas, partidas[indice])
        fechas.append([partidas[indice], cantidad])
        indice = indice + 1

    return fechas


# FUNCIÓN ENCARGADA DE IDENTIFICAR LAS FECHAS CON MÁS PARTIDAS JUGADAS
def identificarFechasMayores():
    lista = crearDatosFechaPartidas()
    elementosMayores = []
    indice = 0
    parada = 3

    while(indice < parada):
        elementoMayor = encontrarMayor(lista)
        lista = eliminarMayor(lista, elementoMayor)
        fecha = elementoMayor[0].split('/')

        elementosMayores.append(
            [datetime(int(fecha[2]), int(fecha[1]), int(fecha[0])),  elementoMayor[1]])
        indice = indice + 1

    return elementosMayores


# FUNCIÓN ENCARGADA DE ORDENAR CRONOLÓGICAMENTE LAS FECHAS
def acomodarListas():
    pLista = identificarFechasMayores()
    indice = 0
    fechas = []

    while(indice < len(pLista)):
        fechas.append(pLista[indice][0])
        indice = indice + 1

    fechas.sort()

    return fechas


# FUNCIÓN ENCARGADA DE INTEGRAR LAS FECHAS ORDENADAS CON SU NÚMERO DE APARICIÓN
def integrarRepeticionFechas():
    listaFechas = identificarFechasMayores()
    pLista = acomodarListas()
    indiceA = 0
    indiceB = 0
    listaOrdenada = []

    while(indiceA < len(pLista)):
        while(indiceB < len(listaFechas)):
            if(pLista[indiceA] == listaFechas[indiceB][0]):
                listaOrdenada.append(
                    [pLista[indiceA], listaFechas[indiceB][1]])

            indiceB = indiceB + 1
        indiceB = 0
        indiceA = indiceA + 1

    return listaOrdenada


# FUNCIÓN ENCARGADA DE EXTRAER LAS HORAS DE LA BITÁCORA
def extraerHoras():
    horas = []
    with open("bitacoraPartidas/bitacora.csv") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=";")
        for columna in entrada:
            horas.append(columna[4])

    return horas


# FUNCIÓN ENCARGADA DE CONTAR LA CANTIDAD DE HORAS REGISTRADAS EN LA BITÁCORA
def contarHoras(pLista):
    horas = eliminarElementosRepetidosBitacora(pLista)
    cantidadHoras = []
    indice = 0
    cantidad = 0

    while(indice < len(horas)):
        cantidad = contarCaracter(pLista, horas[indice])
        cantidadHoras.append([horas[indice], cantidad])
        indice = indice + 1

    return cantidadHoras


# FUNCIÓN ENCARGADA DE CREAR DATOS SOBRE LAS HORAS DE PARTIDAS
def crearDatosHorasPartidas():
    horasPartidas = extraerHoras()
    indice = 0
    horas = ""
    listaFecha = []

    while(indice < len(horasPartidas)):
        horas = horasPartidas[indice].split(":")
        listaFecha.append(int(horas[0]))
        indice = indice + 1

    listaFecha.sort()
    listaFecha = contarHoras(listaFecha)

    return listaFecha

# MATRICES

# FUNCIÓN ENCARGADA DE CREAR UNA MATRIZ


def imprimirMatriz():
    matriz = crearCarton()
    indice = 0
    while(indice < len(matriz)):
        print(matriz[indice])
        indice = indice + 1


# FUNCIÓN ENCARGADA DE CREAR UNA MATRIZ SEGÚN EL NÚMERO
def imprimirMatrices(pNum):
    matriz = crearCarton(pNum)
    indiceA = 0
    indiceB = 0

    for clave in matriz:
        crearImagen(matriz[clave], clave)
        while(indiceA < len(matriz[clave])):
            print(matriz[clave][indiceA])
            indiceA = indiceA + 1
        print(clave+"\n")
        indiceA = 0


# FUNCIÓN ENCARGADA DE INDICAR CUANTAS VECES APARECE UN CARACTER
def contarCaracter(pLista, pCaracter):
    indice = 0
    cantidad = 0

    while(indice < len(pLista)):
        if(pLista[indice] == pCaracter):
            cantidad = cantidad + 1
        indice = indice + 1

    return cantidad
