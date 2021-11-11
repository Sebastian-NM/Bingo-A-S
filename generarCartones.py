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
#generarCartonesPantalla (str)
generarCartonesPantalla=""
#label3 (str)
label3=""
#cantidadCartones (int)
cantidadCartones=0
#Fin variables globales



'''
Entradas:
- cantidadCartonesText
Salidas:
- catones (matriz) 
Restriciones:
- cantidadCartonesText (str)
- identificacionText != ""
'''
#Algoritmo que genera los cartones para la partida
def generarFuncion():
    global generarCartonesPantalla
    global cantidadCartones
    global label3

    #Se extrae la información digitada en cantidadCartones
    #cantidadCartonesText (str)
    cantidadCartonesText = cantidadCartones.get();

    if(cantidadCartonesText!="" and cantidadCartonesText!="Valor entre 1 y 500"):
        if(cantidadCartonesText.isnumeric()):
            #cantidadCartonesText (int)
            cantidadCartonesText = int(cantidadCartonesText)
            if(cantidadCartonesText>=1 and cantidadCartonesText<=500 ):
                #Se crea los cartones
                logic.imprimirMatrices(cantidadCartonesText)
                
                if(cantidadCartonesText==1):
                    #Se destruye el label3
                    label3.destroy()
                    #Se crea el label3
                    label3=Label(generarCartonesPantalla,text="Se creo: "+str(cantidadCartonesText)+" tabla.", bg="white", fg="black")
                    label3.place(x=50,y=60)                   
                else:
                    #Se destruye el label3
                    label3.destroy()
                    #Se crea el label3
                    label3=Label(generarCartonesPantalla,text="Se crearon: "+str(cantidadCartonesText)+" tablas.", bg="white", fg="black")
                    label3.place(x=50,y=60)
                #Fin del if
            else:
                #Se destruye el label3
                label3.destroy()
                #Se crea el label3
                label3=Label(generarCartonesPantalla,text="Debes de digitar un número entre 1 a 500.", bg="white", fg="black")
                label3.place(x=50,y=60)
            #Fin del if
        else:
            #Se destruye el label3
            label3.destroy()
            #Se crea el label3
            label3=Label(generarCartonesPantalla,text="Digitaste un valor que no esta permitido.", bg="white", fg="black")
            label3.place(x=50,y=60)
        #Fin del if
    else:
        #Se destruye el label3
        label3.destroy()
        #Se crea el label3
        label3=Label(generarCartonesPantalla,text="No se digitó nada, por favor intentelo de nuevo.", bg="white", fg="black")
        label3.place(x=50,y=60)
    #Fin del if
#Fin de la función generarFuncion()


         
'''
Entradas:
- event
Salidas:
- se borra el contenido de cantidadCartones (accion)
Restriciones:
- event debe tener una interaccion con cantidadCartones para su uso (accion)
'''
#Algoritmo que borra el contenido de cantidadCartones
def clickCantidadCartones(event):
    cantidadCartones.config(state=NORMAL)
    cantidadCartones.delete(0,END)
#Ffin del algoritmo clickCantidadCartones


    
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
    global generarCartonesPantalla
    #se destruye la interfaz enviarCartonesPantalla 
    generarCartonesPantalla.destroy()
    #se abre la interfaz MP
    MP.inicio()
#Fin del algoritmo regresarFuncion()
   


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
    global generarCartonesPantalla
    global cantidadCartones
    global label3

    #Se elimina los registro anteriores 
    logic.eliminarRegistros()
    #Se elimina la carpeta cartones junto con los cartones dentro de ella
    logic.eliminarCarpetaCartones()
    #Se inicializa las caracteristicas de la gráfica
    generarCartonesPantalla=Tk()
    #Se crea el nombre del banner
    generarCartonesPantalla.title("Bingo")
    #Se integra el color del fondo
    generarCartonesPantalla.config(bg="white")
    #Se establece que el usuario no puede cambiar el tamaño de la aplicacion
    generarCartonesPantalla.resizable(False, False)
    #Se establece las caracteristicas del frame de la aplicación
    window_width  = 400
    window_height  = 100
    #Se establece los parametros para insertar el screen en el centro de la pantalla
    screen_width  = generarCartonesPantalla.winfo_screenwidth()
    screen_height  = generarCartonesPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    #Se crea el screen 
    generarCartonesPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    #Se crea una etiqueta label2
    label2=Label(generarCartonesPantalla,text="Generar Los cartones de Bingo", bg="white", fg="black")
    label2.place(x=10,y=10)

    #Se crea una etiqueta label3
    label3=Label(generarCartonesPantalla,text="Cantidad:", bg="white", fg="black")
    label3.place(x=30,y=30)

    #Se crea la entry cantidadCartones_StringVar
    cantidadCartones_StringVar = StringVar()
    #Se crea un entry cantidadCartones
    cantidadCartones = Entry(generarCartonesPantalla, bg="white", fg="black", textvariable=cantidadCartones_StringVar, width="25")
    cantidadCartones.insert(0,"Valor entre 1 y 500")
    cantidadCartones.config(state=DISABLED)
    cantidadCartones.bind("<Button-1>",clickCantidadCartones)
    cantidadCartones.place(x=100,y=32)

    #Se crea el boton botonIniciarSesion
    botonIniciarSesion = Button(generarCartonesPantalla,text="Generar", command=generarFuncion, bg="white", fg="black")
    botonIniciarSesion.place(x=340,y=28)

    #Se crea el boton botonCerrarAplicacion
    botonCerrarAplicacion = Button(generarCartonesPantalla,text="Regresar", command=regresarFuncion, bg="white", fg="black")
    botonCerrarAplicacion.place(x=337,y=60)

    #Se crea una etiqueta label3
    label3=Label(generarCartonesPantalla,text="", bg="white", fg="black")
    label3.place(x=50,y=60)

    #Se crea la pantalla
    generarCartonesPantalla.mainloop()
#Fin del algoritmo inicio()


