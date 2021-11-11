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
import generarCartones
import consultarCarton
import registrarJugador
import enviarCartones
import iniciarJuego
import graficos
import logica as logic
#Fin de Imports



#Inicio variables globales
#menuPrincipal (str)
menuPrincipal="";
#Fin variables globales



'''
Entradas:
- menuPrincipal
Salidas:
- generarCartones (interfaz) 
Restriciones:
- menuPrincipal (interfaz)
'''
#Algoritmo que abre la interfaz gráfica generarCartones
def generarCartonesMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    generarCartones.inicio()
#Fin del algoritmo generarCartonesMenu()



'''
Entradas:
- menuPrincipal
Salidas:
- consultarCarton (interfaz) 
Restriciones:
- menuPrincipal (interfaz)
'''
#Algoritmo que abre la interfaz gráfica consultarCarton
def consultarCartonMenu():
    global menuPrincipal
    #se destruye la interfaz menú principal 
    menuPrincipal.destroy()
    #se abre la interfaz consultarCarton
    consultarCarton.inicio()
#Fin del algoritmo consultarCartonMenu()



'''
Entradas:
- menuPrincipal
Salidas:
- registrarJugador (interfaz) 
Restriciones:
- menuPrincipal (interfaz)
'''
#Algoritmo que abre la interfaz gráfica registrarJugador
def registrarJugadorMenu():
    global menuPrincipal
    #se destruye la interfaz menú principal 
    menuPrincipal.destroy()
    #se abre la interfaz registrarJugador
    registrarJugador.inicio()
#Fin del algoritmo registrarJugadorMenu()




'''
Entradas:
- menuPrincipal
Salidas:
- v (interfaz) 
Restriciones:
- menuPrincipal (interfaz)
'''
#Algoritmo que abre la interfaz gráfica enviarCartones
def enviarCartonMenu():
    global menuPrincipal
    #se destruye la interfaz menú principal 
    menuPrincipal.destroy()
    #se abre la interfaz enviarCartones
    enviarCartones.inicio()
#Fin del algoritmo enviarCartonMenu()



'''
Entradas:
- menuPrincipal
Salidas:
- iniciarJuego (interfaz) 
Restriciones:
- menuPrincipal (interfaz)
'''
#Algoritmo que abre la interfaz gráfica iniciarJuego
def iniciarUnaPartidaMenu():
    global menuPrincipal
    #se destruye la interfaz menú principal 
    menuPrincipal.destroy()
    #se abre la interfaz iniciarJuego
    iniciarJuego.inicio()
#Fin del algoritmo iniciarUnaPartidaMenu()



'''
Entradas:
- menuPrincipal
Salidas:
- graficos (interfaz) 
Restriciones:
- menuPrincipal (interfaz)
'''
#Algoritmo que abre la interfaz gráfica graficos
def graficosMenu():
    global menuPrincipal
    #se destruye la interfaz menú principal 
    menuPrincipal.destroy()
    #se abre la interfaz graficos
    graficos.inicio()
#Fin del algoritmo graficosMenu()



'''
Entradas:
- menuPrincipal
Salidas:
- destrución de menu principal (interfaz)
Restriciones:
- menuPrincipal (interfaz)
'''
#Algoritmo que destruye la interfaz gráfica menuPrincipal
def cerrarAplicacionFuncion():
    global menuPrincipal
    #se destruye la interfaz menú principal 
    menuPrincipal.destroy()
#Fin del algoritmo cerrarAplicacionFuncion()



'''
Entradas:
- menuPrincipal
Salidas:
- menuPrincipal (interfaz) 
Restriciones:
- menuPrincipal (interfaz)
'''
#Algoritmo que crea la interfaz grafica 
def inicio():
    #se crea la lista de los jugadores que hay en el sistema
    logic.listaJugadores()
    
    global menuPrincipal
    #Se inicializa las caracteristicas de la gráfica
    menuPrincipal=Tk()
    #Se crea el nombre del banner
    menuPrincipal.title("Bingo")
    #Se integra el color del fondo
    menuPrincipal.config(bg="white")
    #Se establece que el usuario no puede cambiar el tamaño de la aplicacion
    menuPrincipal.resizable(False, False)
    #Se establece las caracteristicas del frame de la aplicación
    window_width  = 300
    window_height  = 400
    #Se establece los parametros para insertar el screen en el centro de la pantalla
    screen_width  = menuPrincipal.winfo_screenwidth()
    screen_height  = menuPrincipal.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    #Se crea el screen 
    menuPrincipal.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))
    
    #Se crea una etiqueta label1   
    label1=Label(menuPrincipal,text="           Bienvenido esto es el menú principal del juego.", bg="white", fg="black")
    label1.grid(row=1,column=1)
    
    #Se crea una etiqueta label2
    label2=Label(menuPrincipal,text="Por favor selecione una opción:", bg="white", fg="black")
    label2.grid(row=2,column=1)
    
    #Se crea una etiqueta label3
    label3=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label3.grid(row=3,column=1)
    
    #Se crea el boton botonIniciarSesion
    botonIniciarSesion = Button(menuPrincipal,text="Generar cartones", command=generarCartonesMenu, bg="white", fg="black")
    botonIniciarSesion.grid(row=4,column=1)
    
    #Se crea una etiqueta label4
    label4=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label4.grid(row=5,column=1)
    
    #Se crea el boton consultarCarton
    consultarCarton = Button(menuPrincipal,text="Consultar Carton", command=consultarCartonMenu, bg="white", fg="black")
    consultarCarton.grid(row=6,column=1)

    #Se crea una etiqueta label5
    label5=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label5.grid(row=7,column=1)
    
    #Se crea el boton registrarJugador
    registrarJugador = Button(menuPrincipal,text="Registrar Jugador", command=registrarJugadorMenu, bg="white", fg="black")
    registrarJugador.grid(row=8,column=1)

    #Se crea una etiqueta label6
    label6=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label6.grid(row=9,column=1)

    #Se crea el boton enviarCarton
    enviarCarton = Button(menuPrincipal,text="Enviar cartón", command=enviarCartonMenu, bg="white", fg="black")
    enviarCarton.grid(row=10,column=1)

    #Se crea una etiqueta label7
    label7=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label7.grid(row=11,column=1)
    
    #Se crea el boton iniciarPartida
    iniciarPartida = Button(menuPrincipal,text="Iniciar Juego", command=iniciarUnaPartidaMenu, bg="white", fg="black")
    iniciarPartida.grid(row=12,column=1)

    #Se crea una etiqueta label8
    label8=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label8.grid(row=13,column=1)
    
    #Se crea el boton graficos
    graficos = Button(menuPrincipal,text="Menú graficos", command=graficosMenu, bg="white", fg="black")
    graficos.grid(row=14,column=1)

    label9=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label9.grid(row=15,column=1)
    
    #Se crea el boton cerrarAplicacion
    cerrarAplicacion = Button(menuPrincipal,text="Cerrar aplicación", command=cerrarAplicacionFuncion, bg="white", fg="black")
    cerrarAplicacion.grid(row=16,column=1)

    #Se crea la pantalla
    menuPrincipal.mainloop()
#Fin del algoritmo inicio()

inicio()

