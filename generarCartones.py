'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''

# Librería
from tkinter import *
import menuPrincipal as MP
import logica as logic


# Variables globales
winGenerarCartones = ""
lblInfoError = ""
ntryCantidadCartones = 0


'''
Entradas: cantidadCartonesText
Salidas: catones (matriz) 
Restriciones: cantidadCartonesText (str)
              identificacionText != ""
'''
# genera los cartones para la partida


def generarFuncion():
    global winGenerarCartones
    global ntryCantidadCartones
    global lblInfoError

    ntryCantidadCartonesGetter = ntryCantidadCartones.get()

    if(ntryCantidadCartonesGetter != ""):
        if(ntryCantidadCartonesGetter.isnumeric()):
            ntryCantidadCartonesGetter = int(ntryCantidadCartonesGetter)
            if(ntryCantidadCartonesGetter >= 1 and ntryCantidadCartonesGetter <= 500):
                logic.imprimirMatrices(ntryCantidadCartonesGetter)

                if(ntryCantidadCartonesGetter == 1):
                    lblInfoError.destroy()
                    lblInfoError = Label(winGenerarCartones, text="Se creó "+str(
                        ntryCantidadCartonesGetter)+" cartón", bg="#B0E0E6", font=("Finland", 10, 'bold'), fg="black")
                    lblInfoError.place(x=200, y=120)
                else:
                    lblInfoError.destroy()
                    lblInfoError = Label(winGenerarCartones, text="Se crearon "+str(
                        ntryCantidadCartonesGetter)+" cartones", bg="#B0E0E6", font=("Finland", 10, 'bold'), fg="black")
                    lblInfoError.place(x=180, y=120)
            else:
                lblInfoError.destroy()
                lblInfoError = Label(winGenerarCartones, text="El rango aceptado es de 1 a 500 cartones", bg="#B0E0E6", font=(
                    "Finland", 10, 'bold'), fg="black")
                lblInfoError.place(x=110, y=120)
        else:
            lblInfoError.destroy()
            lblInfoError = Label(winGenerarCartones, text="Valor inválido", bg="#B0E0E6", font=(
                "Finland", 10, 'bold'), fg="black")
            lblInfoError.place(x=200, y=120)
    else:
        lblInfoError.destroy()
        lblInfoError = Label(winGenerarCartones, text="Ingrese un valor para continuar",
                             bg="#B0E0E6", font=("Finland", 10, 'bold'), fg="black")
        lblInfoError.place(x=150, y=120)


'''
Entradas: event
Salidas: se borra el contenido de cantidadCartones (accion)
Restriciones: event debe tener una interaccion con cantidadCartones para su uso (accion)
'''
# Eliminación del contenido de cantidadCartones
# def clickCantidadCartones(event):
# ntryCantidadCartones.config(state=NORMAL)
# ntryCantidadCartones.delete(0,END)


'''
Entradas: enviarCartonesPantalla
Salidas: MP (interfaz) 
Restriciones: enviarCartonesPantalla (interfaz)
'''
# Abre la interfaz gráfica MP


def goBackButton():
    global winGenerarCartones
    winGenerarCartones.destroy()
    MP.inicio()


'''
Entradas: consultarCartonPantalla
Salidas: consultarCartonPantalla (interfaz) 
Restriciones: consultarCartonPantalla (interfaz)
'''
# Crea la interfaz gráfica


def interfaz():
    global winGenerarCartones
    global ntryCantidadCartones
    global lblInfoError

    logic.eliminarRegistros()
    logic.eliminarCarpetaCartones()
    winGenerarCartones = Tk()
    winGenerarCartones.iconbitmap("bingo.ico")
    winGenerarCartones.title("Generar Cartones")
    winGenerarCartones.config(bg="#B0E0E6")
    winGenerarCartones.resizable(False, False)
    window_width = 500
    window_height = 150

    # Centrar interfaz en el centro de la botella
    screen_width = winGenerarCartones.winfo_screenwidth()
    screen_height = winGenerarCartones.winfo_screenheight()
    position_top = (screen_width / 2) - (window_width / 2)
    position_right = (screen_height / 2) - (window_height / 2)
    winGenerarCartones.geometry(
        '%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label2 = Label(winGenerarCartones, text="", bg="#B0E0E6",
                   fg="black", font=("Finland", 10))
    label2.place(x=10, y=10)

    lblTitle = Label(winGenerarCartones, text="Ingrese la cantidad de cartones que desea generar",
                     bg="#B0E0E6", fg="black", font=("Finland", 13))
    lblTitle.place(x=45, y=10)

    cantidadCartones_StringVar = StringVar()

    ntryCantidadCartones = Entry(winGenerarCartones, bg="white",
                                 fg="black", textvariable=cantidadCartones_StringVar, width="25")
    ntryCantidadCartones.config(width=65)
    ntryCantidadCartones.place(x=50, y=45)

    btnGenerar = Button(winGenerarCartones, text="         Generar         ",
                        command=generarFuncion, bg="#20B2AA", fg="black", font=("Finland", 11, 'bold'))
    btnGenerar.place(x=80, y=80)

    btnVolver = Button(winGenerarCartones, text="    Menú Principal    ",
                       command=goBackButton, bg="#E00000", fg="#FFFFFF", font=("Finland", 11, 'bold'))
    btnVolver.place(x=270, y=80)

    lblInfoError = Label(winGenerarCartones, text="",
                         bg="#B0E0E6", fg="black", font=("Finland", 10))
    lblInfoError.place(x=50, y=100)

    winGenerarCartones.mainloop()
