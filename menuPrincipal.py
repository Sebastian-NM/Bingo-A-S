'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''


# Importar Librerías
from tkinter import *
import tkinter.font as tkFont
import tkinter
import generarCartones
import consultarCarton
import registrarJugador
import enviarCartones
import iniciarJuego
import graficos
import logica as logic


# Inicio variables globales
menuPrincipal = ""


'''
Entradas: menuPrincipal
Salidas: generarCartones (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
# Abre la interfaz gráfica generarCartones


def generarCartonesMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    generarCartones.interfaz()


'''
Entradas: menuPrincipal
Salidas: consultarCarton (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
# Abre la interfaz gráfica consultarCarton


def consultarCartonMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    consultarCarton.buscarCarton()


'''
Entradas: menuPrincipal
Salidas: registrarJugador (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
# Abre la interfaz gráfica registrarJugador


def registrarJugadorMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    registrarJugador.registroJugador()


'''
Entradas: menuPrincipal
Salidas: v (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
# Abre la interfaz gráfica enviarCartones


def enviarCartonMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    enviarCartones.enviarCartonesJugador()


'''
Entradas: menuPrincipal
Salidas: iniciarJuego (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
# Abre la interfaz gráfica iniciarJuego


def iniciarUnaPartidaMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    iniciarJuego.jugar()


'''
Entradas: menuPrincipal
Salidas: graficos (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
# Abre la interfaz gráfica graficos


def graficosMenu():
    global menuPrincipal
    menuPrincipal.destroy()
    graficos.inicio()


'''
Entradas: menuPrincipal
Salidas: destrución de menu principal (interfaz)
Restriciones: menuPrincipal (interfaz)
'''
# Destruye la interfaz gráfica menuPrincipal


def cerrarAplicacionFuncion():
    global menuPrincipal
    menuPrincipal.destroy()


'''
Entradas: menuPrincipal
Salidas: menuPrincipal (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
# Crea la interfaz grafica


def inicio():
    logic.listaJugadores()

    global menuPrincipal
    menuPrincipal = Tk()
    menuPrincipal.iconbitmap("bingo.ico")
    menuPrincipal.title("Bingo")
    menuPrincipal.config(bg="white")
    menuPrincipal.resizable(False, False)
    window_width = 510
    window_height = 600
    screen_width = menuPrincipal.winfo_screenwidth()
    screen_height = menuPrincipal.winfo_screenheight()
    position_top = (screen_width / 2) - (window_width / 2)
    position_right = (screen_height / 2) - (window_height / 2)
    menuPrincipal.geometry(
        '%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    imgTitle = tkinter.PhotoImage(file="bingoImage.png")
    imgTitle.configure()

    lblTitulo = tkinter.Label(menuPrincipal, image=imgTitle)
    lblTitulo.place(x=120, y=20)

    theFont = tkFont.Font(family="Tahoma", size=16, weight="bold")
    theFont2 = tkFont.Font(family="Segoe UI", size=12, weight="bold")
    theFont3 = tkFont.Font(family="Segoe UI", size=11, weight="bold")
    theFont4 = tkFont.Font(family="Segoe UI", size=13, weight="bold")

    label1 = Label(menuPrincipal, text="MENU PRINCIPAL",
                   bg="white", fg="black")
    label1.configure(font=theFont, fg="#e51c22")
    label1.place(x=145, y=300)

    botonIniciarSesion = Button(menuPrincipal, text="CREAR CARTONES!",
                                command=generarCartonesMenu, bg="#f0e823", fg="#d42158", font=theFont2)
    botonIniciarSesion.place(x=70, y=350)

    consultarCarton = Button(menuPrincipal, text="BUSCAR CARTÓN!",
                             command=consultarCartonMenu, bg="#f0e823", fg="#d42158", font=theFont2)
    consultarCarton.place(x=275, y=350)
    print("")

    registrarJugador = Button(menuPrincipal, text=" AÑADIR JUGADOR!",
                              command=registrarJugadorMenu, bg="#f0e823", fg="#d42158", font=theFont3)
    registrarJugador.place(x=70, y=400)

    enviarCarton = Button(menuPrincipal, text="ENVIAR CARTÓN!",
                          command=enviarCartonMenu, bg="#f0e823", fg="#d42158", font=theFont2)
    enviarCarton.place(x=275, y=400)

    iniciarPartida = Button(menuPrincipal, text="   INICIAR BINGO!   ",
                            command=iniciarUnaPartidaMenu, bg="#E06D00", fg="#FFFFFF", font=theFont2)
    iniciarPartida.place(x=70, y=450)

    graficos = Button(menuPrincipal, text="   ESTADÍSTICAS!  ",
                      command=graficosMenu, bg="#f0e823", fg="#d42158", font=theFont2)
    graficos.place(x=275, y=450)

    cerrarAplicacion = Button(menuPrincipal, text="                              SALIR                              ",
                              command=cerrarAplicacionFuncion, bg="#E00000", fg="#FFFFFF", font=theFont4)
    cerrarAplicacion.place(x=70, y=530)

    menuPrincipal.mainloop()


inicio()
