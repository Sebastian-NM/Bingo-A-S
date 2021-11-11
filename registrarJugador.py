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
#registrarJugadorPantalla (str)
registrarJugadorPantalla=""
#nombre (str)
nombre=""
#cedula (str)
cedula=""
#correo (str)
correo=""
#label6 (str)
label6=""
#Fin variables globales



'''
Entradas:
- pCorreo
Salidas:
- correo es valido (bool) 
Restriciones:
- pCorreo (str)
- pCorreo != ""
'''
#Función que genera un juegador en el sistema
def identificarCorreo(pCorreo):
    if(pCorreo.rfind("@")!=-1):
        return True
    else:
        return False
    #Fin del if
#Fin de la función identificarCorreo()



def generarFuncion():
    global registrarJugadorPantalla
    global nombre
    global cedula
    global correo
    global label6

    #Se extrae la información digitada en nombre
    #nombreText (str)
    nombreText = nombre.get()
    #Se extrae la información digitada en cedula
    #cedulaText (str)
    cedulaText = cedula.get()
    #Se extrae la información digitada en correo
    #correoText (str)
    correoText = correo.get() 

    if(nombreText!="" and cedulaText!="" and correoText!="" and nombreText!="Ejemplo: Luis Soto" and correoText!="Ejemplo: luis@gmail.com"  and cedulaText!="Ejemplo: 103250410"):
        if(len(cedulaText)==9 and cedulaText.isnumeric()):
            if(identificarCorreo(correoText)):
                if(logic.existeJugador(cedulaText)==False):
                    #Se crea un nuevo jugadpr
                    logic.crearJugador(nombreText,cedulaText,correoText)
                    #Se destruye el label6
                    label6.destroy()
                    #Se crea el label6
                    label6=Label(registrarJugadorPantalla,text="Se registro un nuevo jugador.", bg="white", fg="black")
                    label6.place(x=100,y=120)
                    
                else:
                    #Se destruye el label6
                    label6.destroy()
                    #Se crea el label6
                    label6=Label(registrarJugadorPantalla,text="El jugador que se desea guardar ya existe.", bg="white", fg="black")
                    label6.place(x=100,y=120)
                #Fin del if
            else:
                #Se destruye el label6
                label6.destroy()
                #Se crea el label6
                label6=Label(registrarJugadorPantalla,text="Se digitó un correo que no es valido.", bg="white", fg="black")
                label6.place(x=100,y=120)
            #Fin del if
        else:
            #Se destruye el label6
            label6.destroy()
            #Se crea el label6
            label6=Label(registrarJugadorPantalla,text="Se digitó una cedula que no es valida.", bg="white", fg="black")
            label6.place(x=100,y=120)
        #Fin del if
    else:
        #Se destruye el label6
        label6.destroy()
        #Se crea el label6
        label6=Label(registrarJugadorPantalla,text="Falta información por completar.", bg="white", fg="black")
        label6.place(x=100,y=120)
    #Fin del if
#Fin del algoritmo generarFuncion()



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
    global registrarJugadorPantalla
    #se destruye la interfaz enviarCartonesPantalla 
    registrarJugadorPantalla.destroy()
    #se abre la interfaz MP
    MP.inicio()
#Fin del algoritmo regresarFuncion()



'''
Entradas:
- event
Salidas:
- se borra el contenido de nombre (accion)
Restriciones:
- event debe tener una interaccion con nombre para su uso (accion)
'''
#Algoritmo que borra el contenido de nombre 
def clickNombre(event):
    nombre.config(state=NORMAL)
    nombre.delete(0,END)
#Fin del algoritmo clickNombre()



'''
Entradas:
- event
Salidas:
- se borra el contenido de cedula (accion)
Restriciones:
- event debe tener una interaccion con cedula para su uso (accion)
'''
#Algoritmo que borra el contenido de correo 
def clickCedula(event):
    cedula.config(state=NORMAL)
    cedula.delete(0,END)
#Fin del algoritmo clickCedula()



'''
Entradas:
- event
Salidas:
- se borra el contenido de correo (accion)
Restriciones:
- event debe tener una interaccion con correo para su uso (accion)
'''
#Algoritmo que borra el contenido de correo 
def clickCorreo(event):
    correo.config(state=NORMAL)
    correo.delete(0,END)
#Ffin del algoritmo clickCorreo()



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
    global registrarJugadorPantalla
    global nombre
    global cedula
    global correo
    global label6

    #Se inicializa las caracteristicas de la gráfica
    registrarJugadorPantalla=Tk()
    #Se crea el nombre del banner
    registrarJugadorPantalla.title("Bingo")
    #Se integra el color del fondo
    registrarJugadorPantalla.config(bg="white")
    #Se establece que el usuario no puede cambiar el tamaño de la aplicacion
    registrarJugadorPantalla.resizable(False, False)
    #Se establece las caracteristicas del frame de la aplicación
    window_width  = 366
    window_height  = 180
    #Se establece los parametros para insertar el screen en el centro de la pantalla
    screen_width  = registrarJugadorPantalla.winfo_screenwidth()
    screen_height  = registrarJugadorPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    #Se crea el screen 
    registrarJugadorPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    #Se crea una etiqueta label2
    label2=Label(registrarJugadorPantalla,text="Registrar jugador", bg="white", fg="black")
    label2.place(x=130,y=10)

    #Se crea una etiqueta label3
    label3=Label(registrarJugadorPantalla,text="Nombre:", bg="white", fg="black")
    label3.place(x=30,y=30)

    #Se crea la entry nombre_StringVar
    nombre_StringVar = StringVar()
    #Se crea un entry nombre
    nombre = Entry(registrarJugadorPantalla, bg="white", fg="black", textvariable=nombre_StringVar, width="38")
    nombre.insert(0,"Ejemplo: Luis Soto")
    nombre.config(state=DISABLED)
    nombre.bind("<Button-1>",clickNombre)
    nombre.place(x=100,y=32)

    #Se crea una etiqueta label4
    label4=Label(registrarJugadorPantalla,text="Cédula:", bg="white", fg="black")
    label4.place(x=30,y=60)

    #Se crea la entry cedula_StringVar
    cedula_StringVar = StringVar()
    #Se crea un entry cedula
    cedula = Entry(registrarJugadorPantalla, bg="white", fg="black", textvariable=cedula_StringVar, width="38")
    cedula.insert(0,"Ejemplo: 103250410")
    cedula.config(state=DISABLED)
    cedula.bind("<Button-1>",clickCedula)
    cedula.place(x=100,y=62)

    #Se crea una etiqueta label5   
    label5=Label(registrarJugadorPantalla,text="Correo:", bg="white", fg="black")
    label5.place(x=30,y=90)

    #Se crea la entry correo_StringVar
    correo_StringVar = StringVar()
    #Se crea un entry correo
    correo = Entry(registrarJugadorPantalla, bg="white", fg="black", textvariable=correo_StringVar, width="38")
    correo.insert(0,"Ejemplo: luis@gmail.com")
    correo.config(state=DISABLED)
    correo.bind("<Button-1>",clickCorreo)
    correo.place(x=100,y=92)

    #Se crea el boton botonIniciarSesion
    botonIniciarSesion = Button(registrarJugadorPantalla,text="Guardar", command=generarFuncion, bg="white", fg="black")
    botonIniciarSesion.place(x=100,y=150)
    
    #Se crea el boton botonCerrarAplicacion
    botonCerrarAplicacion = Button(registrarJugadorPantalla,text="Menu Principal", command=regresarFuncion, bg="white", fg="black")
    botonCerrarAplicacion.place(x=180,y=150)

    #Se crea una etiqueta label6
    label6=Label(registrarJugadorPantalla,text="", bg="white", fg="black")
    label6.place(x=100,y=120)
    
    #Se crea la pantalla
    registrarJugadorPantalla.mainloop()
#Fin del algoritmo inicio()


