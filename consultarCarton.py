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
from PIL  import Image, ImageTk
import menuPrincipal as MP
import logica as logic
#Fin de Imports



#Inicio variables globales
#consultarCartonPantalla (str)
consultarCartonPantalla="";
#identificacion (str)
identificacion=""
#imagenCarton (str)
imagenCarton=""
#frameImagen (str)
frameImagen=""
#label3 (str)
label3=""
#label7 (str)
label7=""
#Fin variables globales


'''
Entradas:
- identificacionText
Salidas:
- carton (img) 
Restriciones:
- identificacionText (str)
- identificacionText !=""
'''
#Algoritmo que muestra el carton solicitado
def mostrarCarton():
    global consultarCartonPantalla
    global identificacion
    global frameImagen
    global label3
    global label7
    
    #Se extrae la información digitada en identificacion
    #identificacionText (str)
    identificacionText = identificacion.get()    
    
    if(identificacionText!="" and identificacionText!="Ejemplo: NCC004" ):
        if(len(identificacionText)==6):
            if(logic.existeCarpetaCartones()):
                if(logic.existeImagenEnCarpeta(identificacionText)):
                    if(logic.identificarJugadorConCarton(identificacionText)):
                        #cartonJugador (list)
                        cartonJugador = logic.extraerIdentificadorJugadorConCarton(identificacionText)
                        #Se destruye el label7
                        label7.destroy()
                        #Se crea el label3
                        label7=Label(consultarCartonPantalla,text="Dueño del carton: "+str(cartonJugador[1])+" ,cedula: "+str(cartonJugador[0])+".", bg="white", fg="black")
                        label7.place(x=40,y=350)
                    else:
                        #Se destruye el label7
                        label7.destroy()
                        #Se crea el label7
                        label7=Label(consultarCartonPantalla,text="", bg="white", fg="black")
                        label7.place(x=40,y=350)
                    #Fin del if
                    
                    label3.destroy()
                    #Se crea el label3
                    label3=Label(consultarCartonPantalla,text="Se encontró la imagen.", bg="white", fg="black")
                    label3.place(x=50,y=60)

                    #Se destruye frameImagen
                    frameImagen.destroy()

                    #Se crea frameImagen
                    frameImagen = Frame(consultarCartonPantalla, width = 350, height=260)
                    frameImagen.place(x="40", y="80")

                    #Se abre la imagen img
                    img = Image.open('cartones/'+identificacionText+'.png')
                    img = img.resize((354, 270), Image.BICUBIC)
                    #Se integra la imagen a la interfaz
                    tkimage = ImageTk.PhotoImage(img)
                    #Se muestra la imagen en la interfaz
                    labelImage= Label(frameImagen, image=tkimage, width=350, height=260).pack()
                    #Se crea la pantalla
                    consultarCartonPantalla.mainloop()
                else:
                    #Se destruye el label3
                    label3.destroy()
                    #Se crea el label3
                    label3=Label(consultarCartonPantalla,text="El cartón que desea consultar no existe.", bg="white", fg="black")
                    label3.place(x=50,y=60)
                #Fin del if
            else:
                #Se destruye el label3
                label3.destroy()
                #Se crea el label3
                label3=Label(consultarCartonPantalla,text="No es posible enontrar el carton debido a que no se an creado cartones.", bg="white", fg="black")
                label3.place(x=50,y=60)
            #Fin del if
        else:
            #Se destruye el label3
            label3.destroy()
            #Se crea el label3
            label3=Label(consultarCartonPantalla,text="Se ingreso una identificación que no es valida.", bg="white", fg="black")
            label3.place(x=50,y=60)
        #Fin del if
    else:
        #Se destruye el label3
        label3.destroy()
        #Se crea el label3
        label3=Label(consultarCartonPantalla,text="No se digitó nada, por favor intentelo de nuevo.", bg="white", fg="black")
        label3.place(x=50,y=60)
    #Fin del if
#Fin del algoritmo mostrarCarton()
        


'''
Entradas:
- menuPrincipal
Salidas:
- MP (interfaz) 
Restriciones:
- menuPrincipal (interfaz)
'''
#Algoritmo que abre la interfaz gráfica MP
def regresarFuncion():
    global consultarCartonPantalla
    #se destruye la interfaz consultarCartonPantalla 
    consultarCartonPantalla.destroy()
    #se abre la interfaz MP
    MP.inicio()
#Fin del algoritmo regresarFuncion()



'''
Entradas:
- event
Salidas:
- se borra el contenido de identificacion (accion)
Restriciones:
- event debe tener una interaccion con identificación para su uso (accion)
'''
#Algoritmo que borra el contenido de identificacion
def clickIdentificar(event):
    identificacion.config(state=NORMAL)
    identificacion.delete(0,END)
#Fin del algoritmo clickIdentificar


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
    global consultarCartonPantalla
    global identificacion
    global frameImagen
    global label3
    global label7

    #Se inicializa las caracteristicas de la gráfica
    consultarCartonPantalla=Tk()
    #Se crea el nombre del banner
    consultarCartonPantalla.title("Bingo")
    #Se integra el color del fondo
    consultarCartonPantalla.config(bg="white")
    #Se establece que el usuario no puede cambiar el tamaño de la aplicacion
    consultarCartonPantalla.resizable(False, False)
    #Se establece las caracteristicas del frame de la aplicación
    window_width  = 450
    window_height  = 405
    #Se establece los parametros para insertar el screen en el centro de la pantalla
    screen_width  = consultarCartonPantalla.winfo_screenwidth()
    screen_height  = consultarCartonPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    #Se crea el screen 
    consultarCartonPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    #Se crea una etiqueta label2
    label2=Label(consultarCartonPantalla,text="Consultar Cartones", bg="white", fg="black")
    label2.place(x=20,y=5)

    #Se crea una etiqueta label4   
    label4=Label(consultarCartonPantalla,text="Identificación:", bg="white", fg="black")
    label4.place(x=30,y=30)

    #Se crea el stringVar identificacionCartones_StringVar
    identificacionCartones_StringVar = StringVar()
    
    #Se crea la entry identificacion
    identificacion = Entry(consultarCartonPantalla, bg="white", fg="black", textvariable=identificacionCartones_StringVar, width="25")
    identificacion.insert(0,"Ejemplo: NCC004")
    identificacion.config(state=DISABLED)
    identificacion.bind("<Button-1>",clickIdentificar)
    identificacion.place(x=120,y=32)

    #Se crea el boton botonIniciarSesion
    botonIniciarSesion = Button(consultarCartonPantalla,text="Mostrar", command=mostrarCarton, bg="white", fg="black")
    botonIniciarSesion.place(x=380,y=30)

    #Se crea el boton botonCerrarAplicacion
    botonCerrarAplicacion = Button(consultarCartonPantalla,text="Regresar", command=regresarFuncion, bg="white", fg="black")
    botonCerrarAplicacion.place(x=376,y=370)

    #Se crea una cuadra frameImagen  
    frameImagen = Frame(consultarCartonPantalla, width = 370, height=260);
    frameImagen.place(x="40", y="80");

    #Se crea una etiqueta label3  
    label3=Label(consultarCartonPantalla,text="", bg="white", fg="black")
    label3.place(x=50,y=60)

    #Se crea una etiqueta label7  
    label7=Label(consultarCartonPantalla,text="", bg="white", fg="black")
    label7.place(x=40,y=350)

    #Se crea la pantalla
    consultarCartonPantalla.mainloop()
#Fin del algoritmo inicio()
