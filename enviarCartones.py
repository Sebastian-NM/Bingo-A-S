'''
Proyecto programado 2
Tema: Gestor de Bingos
Integrantes:
-Valentina Mende Solano, 2021142085
-Jorge Arturo Guadamuz Godinez, 2021132991
-Daniel Josué Aguilar Gómez, 2020184120
'''



#Inicio de Imports
from tkinter import *
import menuPrincipal as MP
import logica as logic
#Fin de Imports



#Inicio variables globales
#consultarCartonPantalla (str)
enviarCartonesPantalla="";
#cedula (str)
cedula=""
#label6 (str)
label6=""
#cantidadCartones (int)
cantidadCartones=0
#Fin variables globales



'''
Entradas:
- cantidadCartonesText
- cedulaText
Salidas:
- jugador (str) 
Restriciones:
- cantidadCartonesText (str)
- identificacionText != ""
- cedulaText (str)
- cedulaText != ""
'''
#Algoritmo que genera un juegador en el sistema
def generarFuncion():
    global enviarCartonesPantalla
    global cantidadCartones
    global cedula
    global label6

    #Se extrae la información digitada en cantidadCartones
    #cantidadCartonesText (str)
    cantidadCartonesText = cantidadCartones.get()
    #Se extrae la información digitada en cedula
    #cedulaText (str)
    cedulaText = cedula.get()
    
    if((cantidadCartonesText!="Valor entre 1 y 5" and cedulaText!="Ejemplo: 103250410") and (cantidadCartonesText!="" and cedulaText!="")):
        if(cantidadCartonesText.isnumeric() and (int(cantidadCartonesText)>=1 and int(cantidadCartonesText)<=5)  ) :
            #cantidadCartonesText (int)
            cantidadCartonesText = int(cantidadCartonesText)
            if(cedulaText.isnumeric() and len(cedulaText)==9):
                if(logic.existeCarpetaJugadores()):
                    #identificadores (int)
                    identificadores = logic.cantidadIdentificadoresLibres()
                    if(identificadores!=0):
                        if(logic.existeJugador(cedulaText)):
                            if(logic.jugadorConCarton(cedulaText)==False):
                                #identificadores (int)
                                identificadores = logic.cantidadIdentificadoresLibres()
                                if(int(cantidadCartonesText)<=identificadores):
                                    #Se crea el jugador
                                    logic.crearJugadorConCartones(cedulaText)
                                    #Se le envia los cartones
                                    logic.agragerCartonesAJugadores(cedulaText,cantidadCartonesText)
                                    mostrarCantidadElementosCreados(cantidadCartonesText)
                                else:
                                    #Se destruye el label6
                                    label6.destroy()
                                    #Se crea el label6
                                    label6=Label(enviarCartonesPantalla,text="No existen muchos cartones para repartir.", bg="white", fg="black")
                                    label6.place(x=15,y=85)
                                #Fin del if
                            else:
                                #identificadores (int)
                                identificadores = logic.cantidadIdentificadoresLibres()
                                #cantidadIdentificadoresJugador (str)
                                cantidadIdentificadoresJugador = logic.cantidadCartonesJugador(cedulaText)
                                if(cantidadIdentificadoresJugador<5):
                                    #cartonesFaltantes (int)
                                    cartonesFaltantes = 5 - cantidadIdentificadoresJugador
                                    if( cantidadCartonesText <= cartonesFaltantes):
                                        #Se le envia los cartones
                                        logic.agragerCartonesAJugadores(cedulaText,cantidadCartonesText)
                                        mostrarCantidadElementosCreados(cantidadCartonesText)
                                    else:
                                        #Se destruye el label6
                                        label6.destroy()
                                        #Se crea el label3
                                        label6=Label(enviarCartonesPantalla,text="El jugador no puede tener esa cantidad de cartones.", bg="white", fg="black")
                                        label6.place(x=15,y=85)
                                    #Fin del if
                                else:
                                    #Se destruye el label6
                                    label6.destroy()
                                    #Se crea el label3
                                    label6=Label(enviarCartonesPantalla,text="El jugador cuenta con 5 cartones registrados.", bg="white", fg="black")
                                    label6.place(x=25,y=85)
                                #Fin del if
                        else:
                            #Se destruye el label6
                            label6.destroy()
                            #Se crea el label3
                            label6=Label(enviarCartonesPantalla,text="El jugador que se digitó no existe en el programa.", bg="white", fg="black")
                            label6.place(x=30,y=85)
                        #Fin del if
                    else:
                        #Se destruye el label6
                        label6.destroy()
                        #Se crea el label3
                        label6=Label(enviarCartonesPantalla,text="No hay cartones para repartir.", bg="white", fg="black")
                        label6.place(x=25,y=85)
                    #Fin del if
                else:
                    #Se destruye el label6
                    label6.destroy()
                    #Se crea el label3
                    label6=Label(enviarCartonesPantalla,text="No existen jugadores ingresados en el progroma.", bg="white", fg="black")
                    label6.place(x=30,y=85)
                #Fin del if
            else:
                #Se destruye el label6
                label6.destroy()
                #Se crea el label3
                label6=Label(enviarCartonesPantalla,text="Se digitó una cédula que no es valida.", bg="white", fg="black")
                label6.place(x=30,y=85)
            #Fin del if
        else:
            #Se destruye el label6
            label6.destroy()
            #Se crea el label3
            label6=Label(enviarCartonesPantalla,text="Se digitó una cantidad que no es valida.", bg="white", fg="black")
            label6.place(x=30,y=85)
        #Fin del if
    else:
        #Se destruye el label6
        label6.destroy()
        #Se crea el label3
        label6=Label(enviarCartonesPantalla,text="Falta información por completar.", bg="white", fg="black")
        label6.place(x=30,y=85)
    #Fin del if
#Fin del algoritmo generarFuncion()



'''
Entradas:
- pCantidad
Salidas:
- label6 (interfaz)
Restriciones:
- pCantidad (int)
- pCantidad > 0
'''
#Algoritmo que borra el contenido de identificacion
def mostrarCantidadElementosCreados(pCantidad):
    global label6

    if(pCantidad==1):
        #Se destruye el label6
        label6.destroy()
        #Se crea el label6
        label6=Label(enviarCartonesPantalla,text="Se envió: "+str(pCantidad)+" carton al jugador.", bg="white", fg="black")
        label6.place(x=30,y=85)
    else:
        #Se destruye el label6
        label6.destroy()
        #Se crea el label6
        label6=Label(enviarCartonesPantalla,text="Se enviaron: "+str(pCantidad)+" cartones al jugador.", bg="white", fg="black")
        label6.place(x=30,y=85)
    #Fin del if
#Fin de la función mostrarCantidadElementosCreados()
    


'''
Entradas:
- enviarCartonesPantalla
Salidas:
- MP (interfaz) 
Restriciones:
- enviarCartonesPantalla (interfaz)
'''
#Algoritmo que abre la interfaz gráfica MP         
def regresarFuncion():
    global enviarCartonesPantalla
    #se destruye la interfaz enviarCartonesPantalla 
    enviarCartonesPantalla.destroy()
    #se abre la interfaz MP
    MP.inicio()
#Fin del algoritmo regresarFuncion()



'''
Entradas:
- event
Salidas:
- se borra el contenido de cantidadCartones (accion)
Restriciones:
- event debe tener una interaccion con cantidadCartones para su uso (accion)
'''
#Algoritmo que borra el contenido de cantidadCartones
def clickCantidad(event):
    cantidadCartones.config(state=NORMAL)
    cantidadCartones.delete(0,END)
#Fin del algoritmo clickCantidad()



'''
Entradas:
- event
Salidas:
- se borra el contenido de cedula (accion)
Restriciones:
- event debe tener una interaccion con cedula para su uso (accion)
'''
#Algoritmo que borra el contenido de cedula 
def clickCedula(event):
    cedula.config(state=NORMAL)
    cedula.delete(0,END)
#Fin del algoritmo clickCedula()


  
'''
Entradas:
- consultarCartonPantalla
Salidas:
- consultarCartonPantalla (interfaz) 
Restriciones:
- consultarCartonPantalla (interfaz)
'''
#Algoritmo que crea la interfaz grafica 
def inicio():
    global enviarCartonesPantalla
    global cantidadCartones
    global cedula
    global label6
    
    #Se revisa cuales son los identificadores restantes
    logic.listaIdentificadoresLibres()
    #Se inicializa las caracteristicas de la gráfica
    enviarCartonesPantalla=Tk()
    #Se crea el nombre del banner
    enviarCartonesPantalla.title("Bingo")
    #Se integra el color del fondo
    enviarCartonesPantalla.config(bg="white")
    #Se establece que el usuario no puede cambiar el tamaño de la aplicacion
    enviarCartonesPantalla.resizable(False, False)
    #Se establece las caracteristicas del frame de la aplicación
    window_width  = 300
    window_height  = 150
    #Se establece los parametros para insertar el screen en el centro de la pantalla
    screen_width  = enviarCartonesPantalla.winfo_screenwidth()
    screen_height  = enviarCartonesPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)

    #Se crea el screen 
    enviarCartonesPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    #Se crea una etiqueta label2
    label2=Label(enviarCartonesPantalla,text="Enviar cartón a jugador registrado", bg="white", fg="black")
    label2.place(x=60,y=5)

    #Se crea una etiqueta label4   
    label4=Label(enviarCartonesPantalla,text="Cantidad:", bg="white", fg="black")
    label4.place(x=30,y=30)

    #Se crea la entry cantidadCartones_StringVar
    cantidadCartones_StringVar = StringVar()
    #Se crea un entry cantidadCartones
    cantidadCartones = Entry(enviarCartonesPantalla, bg="white", fg="black", textvariable=cantidadCartones_StringVar, width="25")
    cantidadCartones.insert(0,"Valor entre 1 y 5")
    cantidadCartones.config(state=DISABLED)
    cantidadCartones.bind("<Button-1>",clickCantidad)
    cantidadCartones.place(x=100,y=30)

    #Se crea una etiqueta label5   
    label5=Label(enviarCartonesPantalla,text="Cédula:", bg="white", fg="black")
    label5.place(x=30,y=60)

    #Se crea la entry cedula_StringVar
    cedula_StringVar = StringVar()
    #Se crea un entry cedula
    cedula = Entry(enviarCartonesPantalla, bg="white", fg="black", textvariable=cedula_StringVar, width="25")
    cedula.insert(0,"Ejemplo: 103250410")
    cedula.config(state=DISABLED)
    cedula.bind("<Button-1>",clickCedula)
    cedula.place(x=100,y=62)

    #Se crea el boton botonIniciarSesion
    botonIniciarSesion = Button(enviarCartonesPantalla,text="Enviar cartones digitales", command=generarFuncion, bg="white", fg="black")
    botonIniciarSesion.place(x=40,y=110)

    #Se crea el boton botonCerrarAplicacion
    botonCerrarAplicacion = Button(enviarCartonesPantalla,text="Regresar", command=regresarFuncion, bg="white", fg="black")
    botonCerrarAplicacion.place(x=200,y=110)

    #Se crea una etiqueta label6   
    label6=Label(enviarCartonesPantalla,text="", bg="white", fg="black")
    label6.place(x=30,y=85)  

    #Se crea la pantalla
    enviarCartonesPantalla.mainloop()
#Fin del algoritmo inicio()


