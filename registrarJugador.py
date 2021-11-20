'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''


# Importar Librerías
from tkinter import *
import menuPrincipal as MP
import logica as logic
import re


# Inicio variables globales
registrarJugador = ""
nomJugador = ""
cedJugador = ""
emailJugador = ""
mensaje = ""


'''
Entradas: pEmailJugador
Salidas: emailJugador es valido (bool)
Restriciones: pEmailJugador (str)
              pEmailJugador != ""
'''
# Genera un juegador en el sistema


def identificarEmailJugador(pEmailJugador):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', pEmailJugador.lower()):
        return True
    else:
        return False


def generarFuncion():
    global registrarJugador
    global nomJugador
    global cedJugador
    global emailJugador
    global mensaje

    nomJugadorText = nomJugador.get()
    cedJugadorText = cedJugador.get()
    emailJugadorText = emailJugador.get()

    if(nomJugadorText != "" and cedJugadorText != "" and emailJugadorText != "" and nomJugadorText != "Luis Soto" and emailJugadorText != "luis@gmail.com" and cedJugadorText != "103250410"):
        if(len(cedJugadorText) == 9 and cedJugadorText.isnumeric()):
            if(identificarEmailJugador(emailJugadorText)):
                if(logic.existeJugador(cedJugadorText) == False):
                    logic.crearJugador(
                        nomJugadorText, cedJugadorText, emailJugadorText)
                    mensaje.destroy()
                    mensaje = Label(registrarJugador, text="¡Registro existoso!",
                                    bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
                    mensaje.place(x=110, y=112)

                else:
                    mensaje.destroy()
                    mensaje = Label(registrarJugador, text="El jugador ingresado ya existe",
                                    bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
                    mensaje.place(x=80, y=112)
            else:
                mensaje.destroy()
                mensaje = Label(registrarJugador, text="Ingrese un email válido",
                                bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
                mensaje.place(x=100, y=112)
        else:
            mensaje.destroy()
            mensaje = Label(registrarJugador, text="Ingrese un número de cédula válido",
                            bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
            mensaje.place(x=50, y=112)
    else:
        mensaje.destroy()
        mensaje = Label(registrarJugador, text="Ingrese la información correspondiente",
                        bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
        mensaje.place(x=50, y=112)


'''
Entradas: enviarCartonesPantalla
Salidas: MP (interfaz) 
Restriciones: enviarCartonesPantalla (interfaz)
'''
# Abre la interfaz gráfica MP


def regresarFuncion():
    global registrarJugador
    registrarJugador.destroy()
    MP.inicio()


'''
Entradas: event
Salidas: se borra el contenido de nomJugador (accion)
Restriciones: event debe tener una interaccion con nomJugador para su uso (accion)
'''
# Borra el contenido de nomJugador


def clickNomJugador(event):
    nomJugador.config(state=NORMAL)
    nomJugador.delete(0, END)


'''
Entradas: event
Salidas: se borra el contenido de cedJugador (accion)
Restriciones: event debe tener una interaccion con cedJugador para su uso (accion)
'''
# Borra el contenido de emailJugador


def clickCedJugador(event):
    cedJugador.config(state=NORMAL)
    cedJugador.delete(0, END)


'''
Entradas: event
Salidas: se borra el contenido de emailJugador (accion)
Restriciones: event debe tener una interaccion con emailJugador para su uso (accion)
'''
# Borra el contenido de emailJugador


def clickEmailJugador(event):
    emailJugador.config(state=NORMAL)
    emailJugador.delete(0, END)


'''
Entradas: consultarCartonPantalla
Salidas: consultarCartonPantalla (interfaz) 
Restriciones: consultarCartonPantalla (interfaz)
'''
# Crea la interfaz grafica


def inicio():
    global registrarJugador
    global nomJugador
    global cedJugador
    global emailJugador
    global mensaje

    registrarJugador = Tk()
    registrarJugador.iconbitmap("bingo.ico")
    registrarJugador.title("Registrar Jugadores")
    registrarJugador.config(bg="#B0E0E6")
    registrarJugador.resizable(False, False)
    window_width = 366
    window_height = 180
    screen_width = registrarJugador.winfo_screenwidth()
    screen_height = registrarJugador.winfo_screenheight()
    position_top = (screen_width / 2) - (window_width / 2)
    position_right = (screen_height / 2) - (window_height / 2)
    registrarJugador.geometry(
        '%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label3 = Label(registrarJugador, text="Nombre:",
                   bg="#B0E0E6", fg="black", font=("Finland", 10))
    label3.place(x=30, y=20)

    nomJugador_StringVar = StringVar()
    nomJugador = Entry(registrarJugador, bg="white", fg="black",
                       textvariable=nomJugador_StringVar, width="38")
    nomJugador.insert(0, "Luis Soto")
    nomJugador.config(state=DISABLED)
    nomJugador.bind("<Button-1>", clickNomJugador)
    nomJugador.place(x=100, y=22)

    label4 = Label(registrarJugador, text="Cédula:",
                   bg="#B0E0E6", fg="black", font=("Finland", 10))
    label4.place(x=30, y=50)

    cedJugador_StringVar = StringVar()
    cedJugador = Entry(registrarJugador, bg="white", fg="black",
                       textvariable=cedJugador_StringVar, width="38")
    cedJugador.insert(0, "103250410")
    cedJugador.config(state=DISABLED)
    cedJugador.bind("<Button-1>", clickCedJugador)
    cedJugador.place(x=100, y=52)

    label5 = Label(registrarJugador, text="Email:",
                   bg="#B0E0E6", fg="black", font=("Finland", 10))
    label5.place(x=30, y=80)

    emailJugador_StringVar = StringVar()
    emailJugador = Entry(registrarJugador, bg="white", fg="black",
                         textvariable=emailJugador_StringVar, width="38")
    emailJugador.insert(0, "luis@gmail.com")
    emailJugador.config(state=DISABLED)
    emailJugador.bind("<Button-1>", clickEmailJugador)
    emailJugador.place(x=100, y=82)

    botonIniciarSesion = Button(registrarJugador, text="Guardar", command=generarFuncion,
                                bg="#20B2AA", fg="black", font=("Finland", 10, 'bold'))
    botonIniciarSesion.place(x=230, y=150)

    botonCerrarAplicacion = Button(registrarJugador, text="Menú Principal",
                                   command=regresarFuncion, bg="#E00000", fg="#FFFFFF", font=("Finland", 10, 'bold'))
    botonCerrarAplicacion.place(x=60, y=150)

    mensaje = Label(registrarJugador, text="", bg="#B0E0E6", fg="black")
    mensaje.place(x=30, y=120)

    registrarJugador.mainloop()
