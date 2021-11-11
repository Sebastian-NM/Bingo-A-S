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
from tkinter import ttk
import menuPrincipal as MP
import logica as logic
import partida as game
#Fin de Imports



#Inicio variables globales
#iniciarJuegoPantalla (str)
iniciarJuegoPantalla="";
#premio (str)
premio=""
#label6 (str)
label6=""
#juegoSelecionado (str)
juegoSelecionado=""
#Fin variables globales




'''
Entradas:
- premioText
- juegoSeleccionadoText
Salidas:
- game (interfaz) 
Restriciones:
- premioText (str)
- premioText != ""
- juegoSeleccionadoText (str)
- juegoSeleccionadoText != ""
'''
#Algoritmo que genera solicita los requerimientos necesarios para iniciar una partida
def generarFuncion():
    global iniciarJuegoPantalla
    global premio
    global label6
    global juegoSelecionado

    #Se extrae la información digitada en premio
    #premioText (str)
    premioText = premio.get()
    #Se extrae la información digitada en juegoSelecionado
    #juegoSeleccionadoText (str)
    juegoSeleccionadoText = juegoSelecionado.get()
    
    if(premioText!="50.000 colones" and premioText!=""):
        if(logic.enviarTotalCartones()!=0):
            logic.guardarDatosJuego(juegoSeleccionadoText,premioText)
            #Se destruye el label6
            label6.destroy()
            #Se crea el label6
            label6=Label(iniciarJuegoPantalla,text=juegoSeleccionadoText, bg="white", fg="black")
            label6.place(x=150,y=56)
            #Se destruye el la interfaz iniciarJuegoPantalla
            iniciarJuegoPantalla.destroy()
            #Se inicia la interfaz game
            game.inicio()
        else:
            #Se destruye el label6
            label6.destroy()
            #Se crea el label6
            label6=Label(iniciarJuegoPantalla,text="No se puede iniciar el juego ya que no existen cartones.", bg="white", fg="black")
            label6.place(x=90,y=56)
        #Fin del if
    else:
        #Se destruye el label6
        label6.destroy()
        #Se crea el label6
        label6=Label(iniciarJuegoPantalla,text="Falta información por completar.", bg="white", fg="black")
        label6.place(x=150,y=56)
    #Fin del if
#Fin del algpritmo generarFuncion()
        


'''
Entradas:
- iniciarJuegoPantalla
Salidas:
- MP (interfaz) 
Restriciones:
- iniciarJuegoPantalla (interfaz)
'''
#Algoritmo que abre la interfaz gráfica MP         
def regresarFuncion():
    global iniciarJuegoPantalla
    iniciarJuegoPantalla.destroy()
    MP.inicio()
#Fin del algoritmo regresarFuncion()



'''
Entradas:
- event
Salidas:
- se borra el contenido de premio (accion)
Restriciones:
- event debe tener una interaccion con premio para su uso (accion)
'''
#Algoritmo que borra el contenido de cantidadCartones
def clickpremio(event):
    premio.config(state=NORMAL)
    premio.delete(0,END)
#Ffin del algoritmo clickpremio()

  
    
'''
Entradas:
- iniciarJuegoPantalla
Salidas:
- iniciarJuegoPantalla (interfaz) 
Restriciones:
- iniciarJuegoPantalla (interfaz)
'''
#Algoritmo que crea la interfaz grafica 
def inicio():
    global iniciarJuegoPantalla
    global premio
    global label6
    global juegoSelecionado

    #Se limpian las variables para iniciar un nuevo juego
    logic.limpiarVariables()
    #Se inicializa las caracteristicas de la gráfica
    iniciarJuegoPantalla=Tk()
    #Se crea el nombre del banner
    iniciarJuegoPantalla.title("Bingo")
    #Se integra el color del fondo
    iniciarJuegoPantalla.config(bg="white")
    #Se establece que el usuario no puede cambiar el tamaño de la aplicacion
    iniciarJuegoPantalla.resizable(False, False)
    #Se establece las caracteristicas del frame de la aplicación
    window_width  = 470
    window_height  = 120
    #Se establece los parametros para insertar el screen en el centro de la pantalla
    screen_width  = iniciarJuegoPantalla.winfo_screenwidth()
    screen_height  = iniciarJuegoPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    #Se crea el screen 
    iniciarJuegoPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    #Se crea una etiqueta label2
    label2=Label(iniciarJuegoPantalla,text="Iniciar juego de Bingo", bg="white", fg="black")
    label2.place(x=180,y=5)

    #Se crea una etiqueta label4
    label4=Label(iniciarJuegoPantalla,text="Configuración:", bg="white", fg="black")
    label4.place(x=15,y=30)

    #choices (list)
    choices = ['Jugar en X', 'Cuatro esquinas', 'Cartón lleno','Jugar en Z']
    #Se crea un Combobox juegoSelecionado
    juegoSelecionado = ttk.Combobox(iniciarJuegoPantalla, values = choices)
    juegoSelecionado.current(0)
    juegoSelecionado.place(x=100,y=30)

    #Se crea una etiqueta label5   
    label5=Label(iniciarJuegoPantalla,text="Premio:", bg="white", fg="black")
    label5.place(x=250, y=30)

    #Se crea la entry premio_StringVar
    premio_StringVar = StringVar()
    #Se crea un entry premio
    premio = Entry(iniciarJuegoPantalla, bg="white", fg="black", textvariable=premio_StringVar, width="25")
    premio.insert(0,"50.000 colones")
    premio.config(state=DISABLED)
    premio.bind("<Button-1>",clickpremio)
    premio.place(x=300,y=30)

    #Se crea el boton botonIniciarSesion
    botonIniciarSesion = Button(iniciarJuegoPantalla,text="Iniciar", command=generarFuncion, bg="white", fg="black")
    botonIniciarSesion.place(x=180,y=80)

    #Se crea el boton botonCerrarAplicacion
    botonCerrarAplicacion = Button(iniciarJuegoPantalla,text="Regresar", command=regresarFuncion, bg="white", fg="black")
    botonCerrarAplicacion.place(x=240,y=80)

    #Se crea una etiqueta label6   
    label6=Label(iniciarJuegoPantalla,text="", bg="white", fg="black")
    label6.place(x=150,y=56)  

    #Se crea la pantalla
    iniciarJuegoPantalla.mainloop()
#Fin del algoritmo inicio()


