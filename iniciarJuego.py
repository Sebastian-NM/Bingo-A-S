'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''


# Importar Librerías
from tkinter import *
from tkinter import ttk
import menuPrincipal as MP
import funcionalidades as func
import partida as game


# Inicio variables globales
iniciarJuego = ""
premio = ""
mensaje = ""
configuracionJuego = ""


'''
Entradas: premioText, configuracionJuegoText
Salidas: game (interfaz) 
Restriciones: premioText (str)
              premioText != ""
              configuracionJuegoText (str)
              configuracionJuegoText != ""
'''
# Genera solicitud de los requerimientos necesarios para iniciar una partida


def generarJuego():
    global iniciarJuego
    global premio
    global mensaje
    global configuracionJuego

    premioText = premio.get()
    configuracionJuegoText = configuracionJuego.get()

    if(premioText != "100000" and premioText != ""):
        if(func.enviarTotalCartones() != 0):
            func.guardarDatosJuego(configuracionJuegoText, premioText)
            mensaje.destroy()
            mensaje = Label(
                iniciarJuego, text=configuracionJuegoText, bg="white", fg="black")
            mensaje.place(x=150, y=56)
            iniciarJuego.destroy()
            game.iniciarPartidaBingo()
        else:
            mensaje.destroy()
            mensaje = Label(iniciarJuego, text="No se puede iniciar el juego debido a que no existen cartones",
                            fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
            mensaje.place(x=40, y=56)
    else:
        mensaje.destroy()
        mensaje = Label(iniciarJuego, text="Complete la información solicitada",
                        fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
        mensaje.place(x=120, y=56)


'''
Entradas: iniciarJuego
Salidas: MP (interfaz) 
Restriciones: iniciarJuego (interfaz)
'''
# Abre la interfaz gráfica MP


def regresarFuncion():
    global iniciarJuego
    iniciarJuego.destroy()
    MP.inicio()


'''
Entradas: event
Salidas: se borra el contenido de premio (accion)
Restriciones: event debe tener una interaccion con premio para su uso (accion)
'''
# Eliminación del contenido de cantidadCartones


def clickpremio(event):
    premio.config(state=NORMAL)
    premio.delete(0, END)


'''
Entradas: iniciarJuego
Salidas: iniciarJuego (interfaz) 
Restriciones: iniciarJuego (interfaz)
'''
# Crea la interfaz grafica


def jugar():
    global iniciarJuego
    global premio
    global mensaje
    global configuracionJuego

    func.limpiarVariables()
    iniciarJuego = Tk()
    iniciarJuego.iconbitmap("bingo.ico")
    iniciarJuego.title("Iniciar Juego")
    iniciarJuego.config(bg="#B0E0E6")
    iniciarJuego.resizable(False, False)
    window_width = 470
    window_height = 120
    screen_width = iniciarJuego.winfo_screenwidth()
    screen_height = iniciarJuego.winfo_screenheight()
    position_top = (screen_width / 2) - (window_width / 2)
    position_right = (screen_height / 2) - (window_height / 2)
    iniciarJuego.geometry('%dx%d+%d+%d' % (window_width,
                          window_height, position_top, position_right))

    label2 = Label(iniciarJuego, text="¡Juguemos!", bg="#B0E0E6",
                   fg="black", font=("Finland", 12, 'bold'))
    label2.place(x=200, y=5)

    label4 = Label(iniciarJuego, text="Configuración:",
                   bg="#B0E0E6", fg="black", font=("Finland", 10))
    label4.place(x=15, y=30)

    choices = ['Jugar en X', 'Cuatro esquinas', 'Cartón lleno', 'Jugar en Z']
    configuracionJuego = ttk.Combobox(iniciarJuego, values=choices)
    configuracionJuego.current(0)
    configuracionJuego.place(x=100, y=30)

    label5 = Label(iniciarJuego, text="Premio:", bg="#B0E0E6", fg="black")
    label5.place(x=250, y=30)

    premio_StringVar = StringVar()
    premio = Entry(iniciarJuego, bg="white", fg="black",
                   textvariable=premio_StringVar, width="25")
    premio.insert(0, "100000")
    premio.config(state=DISABLED)
    premio.bind("<Button-1>", clickpremio)
    premio.place(x=300, y=30)

    botonIniciarSesion = Button(iniciarJuego, text="Iniciar", command=generarJuego,
                                bg="#20B2AA", fg="black", font=("Finland", 10, 'bold'))
    botonIniciarSesion.place(x=275, y=80)

    botonCerrarAplicacion = Button(iniciarJuego, text="Menú Principal", command=regresarFuncion,
                                   bg="#E00000", fg="#FFFFFF", font=("Finland", 10, 'bold'))
    botonCerrarAplicacion.place(x=130, y=80)

    mensaje = Label(iniciarJuego, text="", bg="#B0E0E6", fg="black")
    mensaje.place(x=150, y=56)

    iniciarJuego.mainloop()
