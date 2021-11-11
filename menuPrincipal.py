'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''


#Importar Librerías
from tkinter import *
import generarCartones
import consultarCarton
import registrarJugador
import enviarCartones
import iniciarJuego
import graficos
import logica as logic



#Inicio variables globales
menuPrincipal="";


'''
Entradas: menuPrincipal
Salidas: generarCartones (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
#Abre la interfaz gráfica generarCartones
def generarCartonesMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    generarCartones.inicio()


'''
Entradas: menuPrincipal
Salidas: consultarCarton (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
#Abre la interfaz gráfica consultarCarton
def consultarCartonMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    consultarCarton.inicio()


'''
Entradas: menuPrincipal
Salidas: registrarJugador (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
#Abre la interfaz gráfica registrarJugador
def registrarJugadorMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    registrarJugador.inicio()


'''
Entradas: menuPrincipal
Salidas: v (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
#Abre la interfaz gráfica enviarCartones
def enviarCartonMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    enviarCartones.inicio()


'''
Entradas: menuPrincipal
Salidas: iniciarJuego (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
#Abre la interfaz gráfica iniciarJuego
def iniciarUnaPartidaMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    iniciarJuego.inicio()


'''
Entradas: menuPrincipal
Salidas: graficos (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
#Abre la interfaz gráfica graficos
def graficosMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    graficos.inicio()


'''
Entradas: menuPrincipal
Salidas: destrución de menu principal (interfaz)
Restriciones: menuPrincipal (interfaz)
'''
#Destruye la interfaz gráfica menuPrincipal
def cerrarAplicacionFuncion():
    global menuPrincipal 
    menuPrincipal.destroy()


'''
Entradas: menuPrincipal
Salidas: menuPrincipal (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
#Crea la interfaz grafica 
def inicio():
    logic.listaJugadores()
    
    global menuPrincipal
    menuPrincipal=Tk()
    menuPrincipal.title("Bingo")
    menuPrincipal.config(bg="white")
    menuPrincipal.resizable(False, False)
    window_width  = 300
    window_height  = 400
    screen_width  = menuPrincipal.winfo_screenwidth()
    screen_height  = menuPrincipal.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    menuPrincipal.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))
    
    label1=Label(menuPrincipal,text="           Bienvenido esto es el menú principal del juego.", bg="white", fg="black")
    label1.grid(row=1,column=1)
    
    label2=Label(menuPrincipal,text="Por favor selecione una opción:", bg="white", fg="black")
    label2.grid(row=2,column=1)
    
    label3=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label3.grid(row=3,column=1)
    
    botonIniciarSesion = Button(menuPrincipal,text="Generar cartones", command=generarCartonesMenu, bg="white", fg="black")
    botonIniciarSesion.grid(row=4,column=1)
    
    label4=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label4.grid(row=5,column=1)
    
    consultarCarton = Button(menuPrincipal,text="Consultar Carton", command=consultarCartonMenu, bg="white", fg="black")
    consultarCarton.grid(row=6,column=1)

    label5=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label5.grid(row=7,column=1)
    
    registrarJugador = Button(menuPrincipal,text="Registrar Jugador", command=registrarJugadorMenu, bg="white", fg="black")
    registrarJugador.grid(row=8,column=1)

    label6=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label6.grid(row=9,column=1)

    enviarCarton = Button(menuPrincipal,text="Enviar cartón", command=enviarCartonMenu, bg="white", fg="black")
    enviarCarton.grid(row=10,column=1)

    label7=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label7.grid(row=11,column=1)
    
    iniciarPartida = Button(menuPrincipal,text="Iniciar Juego", command=iniciarUnaPartidaMenu, bg="white", fg="black")
    iniciarPartida.grid(row=12,column=1)

    label8=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label8.grid(row=13,column=1)
    
    graficos = Button(menuPrincipal,text="Menú graficos", command=graficosMenu, bg="white", fg="black")
    graficos.grid(row=14,column=1)

    label9=Label(menuPrincipal,text="   ", bg="white", fg="black")
    label9.grid(row=15,column=1)
    
    cerrarAplicacion = Button(menuPrincipal,text="Cerrar aplicación", command=cerrarAplicacionFuncion, bg="white", fg="black")
    cerrarAplicacion.grid(row=16,column=1)

    menuPrincipal.mainloop()

inicio()