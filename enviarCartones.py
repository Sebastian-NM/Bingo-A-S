'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''


# Importar Librerías
from tkinter import *
import menuPrincipal as MP
import funcionalidades as func


# Inicio variables globales
enviarCartones = ""
cedJugador = ""
mensaje = ""
cantidadCartones = 0


'''
Entradas: cantidadCartonesText, cedJugadorText
Salidas: jugador (str) 
Restriciones: cantidadCartonesText (str)
              identificacionText != ""
              cedJugadorText (str)
              cedJugadorText != ""
'''
# Genera un juegador en el sistema


def generarEnvioCartones():
    global enviarCartones
    global cantidadCartones
    global cedJugador
    global mensaje

    cantidadCartonesText = cantidadCartones.get()
    cedJugadorText = cedJugador.get()

    if((cantidadCartonesText != "Valor entre 1 y 5" and cedJugadorText != "Ejemplo: 103250410") and (cantidadCartonesText != "" and cedJugadorText != "")):
        if(cantidadCartonesText.isnumeric() and (int(cantidadCartonesText) >= 1 and int(cantidadCartonesText) <= 5)):
            cantidadCartonesText = int(cantidadCartonesText)
            if(cedJugadorText.isnumeric() and len(cedJugadorText) == 9):
                if(func.existeCarpetaJugadores()):
                    identificadores = func.cantidadIdentificadoresLibres()
                    if(identificadores != 0):
                        if(func.existeJugador(cedJugadorText)):
                            if(func.jugadorConCarton(cedJugadorText) == False):
                                identificadores = func.cantidadIdentificadoresLibres()
                                if(int(cantidadCartonesText) <= identificadores):
                                    func.crearJugadorConCartones(
                                        cedJugadorText)
                                    func.agragerCartonesAJugadores(
                                        cedJugadorText, cantidadCartonesText)
                                    cantidadElementosCreados(
                                        cantidadCartonesText)
                                else:
                                    mensaje.destroy()
                                    mensaje = Label(
                                        enviarCartones, text="No existen tantos cartones para repartir", fg="black", bg="#B0E0E6", font=(
                                            "Finland", 10, 'bold'))
                                    mensaje.place(x=85, y=80)
                            else:
                                identificadores = func.cantidadIdentificadoresLibres()
                                cantidadIdentificadoresJugador = func.cantidadCartonesJugador(
                                    cedJugadorText)
                                if(cantidadIdentificadoresJugador < 5):
                                    cartonesFaltantes = 5 - cantidadIdentificadoresJugador
                                    if(cantidadCartonesText <= cartonesFaltantes):
                                        func.agragerCartonesAJugadores(
                                            cedJugadorText, cantidadCartonesText)
                                        cantidadElementosCreados(
                                            cantidadCartonesText)
                                    else:
                                        mensaje.destroy()
                                        mensaje = Label(enviarCartones, text="El jugador no puede tener la cantidad de cartones ingresada", fg="black", bg="#B0E0E6", font=(
                                            "Finland", 10, 'bold'))
                                        mensaje.place(x=85, y=80)
                                else:
                                    mensaje.destroy()
                                    mensaje = Label(enviarCartones, text="El jugador ya cuenta con 5 cartones",
                                                    fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
                                    mensaje.place(x=85, y=80)
                        else:
                            mensaje.destroy()
                            mensaje = Label(enviarCartones, text="La cédula ingresada no existe",
                                            fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
                            mensaje.place(x=85, y=80)
                    else:
                        mensaje.destroy()
                        mensaje = Label(enviarCartones, text="No existen cartones en el sistema",
                                        fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
                        mensaje.place(x=65, y=80)
                else:
                    mensaje.destroy()
                    mensaje = Label(enviarCartones, text="No existen jugadores en el sistema",
                                    fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
                    mensaje.place(x=65, y=80)
            else:
                mensaje.destroy()
                mensaje = Label(enviarCartones, text="Digite una cédula válida",
                                fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
                mensaje.place(x=88, y=80)
        else:
            mensaje.destroy()
            mensaje = Label(enviarCartones, text="Digite una cantidad válida",
                            fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
            mensaje.place(x=85, y=80)
    else:
        mensaje.destroy()
        mensaje = Label(enviarCartones, text="Ingrese la información solicitada",
                        fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
        mensaje.place(x=60, y=80)


'''
Entradas: pCantidad
Salidas: mensaje (interfaz)
Restriciones: pCantidad (int)
              pCantidad > 0
'''
# Eliminación del contenido de identificación


def cantidadElementosCreados(pCantidad):
    global mensaje

    if(pCantidad == 1):
        mensaje.destroy()
        mensaje = Label(enviarCartones, text="Se envió "+str(pCantidad) +
                        " carton al jugador", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
        mensaje.place(x=68, y=80)
    else:
        mensaje.destroy()
        mensaje = Label(enviarCartones, text="Se enviaron "+str(pCantidad) +
                        " cartones al jugador", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
        mensaje.place(x=55, y=80)


'''
Entradas: enviarCartones
Salidas: MP (interfaz) 
Restriciones: enviarCartones (interfaz)
'''
# Abre la interfaz gráfica MP


def regresarFuncion():
    global enviarCartones
    enviarCartones.destroy()
    MP.inicio()


'''
Entradas: event
Salidas: se borra el contenido de cantidadCartones (accion)
Restriciones: event debe tener una interaccion con cantidadCartones para su uso (accion)
'''
# Elimina el contenido de cantidadCartones


def clickCantidad(event):
    cantidadCartones.config(state=NORMAL)
    cantidadCartones.delete(0, END)


'''
Entradas: event
Salidas: se borra el contenido de cedJugador (accion)
Restriciones: event debe tener una interaccion con cedJugador para su uso (accion)
'''
# Elimina el contenido de cédula


def clickCedJugador(event):
    cedJugador.config(state=NORMAL)
    cedJugador.delete(0, END)


'''
Entradas: consultarCartonPantalla
Salidas: consultarCartonPantalla (interfaz) 
Restriciones: consultarCartonPantalla (interfaz)
'''
# Creación de la interfaz gráfica


def enviarCartonesJugador():
    global enviarCartones
    global cantidadCartones
    global cedJugador
    global mensaje

    func.listaIdentificadoresLibres()
    enviarCartones = Tk()
    enviarCartones.iconbitmap("bingo.ico")
    enviarCartones.title("Enviar Cartones")
    enviarCartones.config(bg="#B0E0E6")
    enviarCartones.resizable(False, False)
    window_width = 350
    window_height = 150
    screen_width = enviarCartones.winfo_screenwidth()
    screen_height = enviarCartones.winfo_screenheight()
    position_top = (screen_width / 2) - (window_width / 2)
    position_right = (screen_height / 2) - (window_height / 2)

    enviarCartones.geometry(
        '%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label4 = Label(enviarCartones, text="Cantidad a enviar:",
                   fg="black", bg="#B0E0E6", font=("Finland", 10))
    label4.place(x=30, y=20)

    cantidadCartones_StringVar = StringVar()

    cantidadCartones = Entry(enviarCartones, bg="white", fg="black",
                             textvariable=cantidadCartones_StringVar, width="25")
    cantidadCartones.insert(0, "1-5")
    cantidadCartones.config(state=DISABLED)
    cantidadCartones.bind("<Button-1>", clickCantidad)
    cantidadCartones.place(x=155, y=22)

    label5 = Label(enviarCartones, text="Cédula del jugador:",
                   fg="black", bg="#B0E0E6", font=("Finland", 10))
    label5.place(x=30, y=50)

    cedJugador_StringVar = StringVar()

    cedJugador = Entry(enviarCartones, bg="white", fg="black",
                       textvariable=cedJugador_StringVar, width="25")
    cedJugador.insert(0, "X0XXX0XXX")
    cedJugador.config(state=DISABLED)
    cedJugador.bind("<Button-1>", clickCedJugador)
    cedJugador.place(x=155, y=52)

    botonIniciarSesion = Button(enviarCartones, text="Enviar", command=generarEnvioCartones,
                                bg="#20B2AA", fg="black", font=("Finland", 10, 'bold'))
    botonIniciarSesion.place(x=230, y=112)

    botonCerrarAplicacion = Button(enviarCartones, text="Menú Principal",
                                   command=regresarFuncion, bg="#E00000", fg="#FFFFFF", font=("Finland", 10, 'bold'))
    botonCerrarAplicacion.place(x=40, y=112)

    mensaje = Label(enviarCartones, text="", fg="black",
                    bg="#B0E0E6", font=("Finland", 10))
    mensaje.place(x=30, y=85)

    enviarCartones.mainloop()
