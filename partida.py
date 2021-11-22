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
import logica as logic
import ganadores as winners


# Inicio variables globales
iniciarPartida = ""
premio = ""
cantarNumeros = ""
primero = bool


'''
Entradas: iniciarPartida
Salidas: winners (interfaz) 
Restriciones: iniciarPartida (interfaz)
'''
# Abre la interfaz gráfica winners


def cartonesGanadores():
    global iniciarPartida
    iniciarPartida.destroy()
    winners.ganadoresBingo()


'''
Entradas: numero
Salidas: jugador (str) 
Restriciones: numero (int)
              numero >= 0
'''
# Genera un número nuevo


def cantarJuego():
    global iniciarPartida
    global textBox
    global cantarNumeros
    global primero

    tipoJuego, premio = logic.enviarDatosJuego()

    if(logic.cantarNumeros(tipoJuego) == False):
        numero = logic.ultimoNumeroCantado()
        textBox.configure(state='normal')
        if(primero == True):
            primero = False
            textBox.insert(END, str(numero))
            textBox.configure(state='disable')
        else:
            textBox.insert(END, ","+str(numero))
            textBox.configure(state='disable')
    else:
        logic.enviarEmailGanadores()
        cantarNumeros.configure(state='disable')
        textBox.configure(state='normal')

        botonGanadores = Button(iniciarPartida, text="Ver los ganadores",
                                command=cartonesGanadores, bg="#E00000", fg="#FFFFFF", font=("Finland", 10, 'bold'))
        botonGanadores.place(x=174, y=158)


'''
Entradas: event
Salidas: se borra el contenido de premio (accion)
Restriciones: event debe tener una interaccion con premio para su uso (accion)
'''
# Borra el contenido de premio


def clickpremio(event):
    premio.config(state=NORMAL)
    premio.delete(0, END)


'''
Entradas: iniciarPartida
Salidas: iniciarPartida (interfaz) 
Restriciones: iniciarPartida (interfaz)
'''
# Crea la interfaz grafica


def iniciarPartidaBingo():
    global iniciarPartida
    global textBox
    global cantarNumeros
    global primero

    primero = True
    logic.copiaCartones()
    tipoJuego, premio = logic.enviarDatosJuego()
    cantidadCartones = logic.enviarTotalCartones()
    iniciarPartida = Tk()
    iniciarPartida.iconbitmap("bingo.ico")
    iniciarPartida.title("Partida en Proceso")
    iniciarPartida.config(bg="#B0E0E6")
    iniciarPartida.resizable(False, False)
    window_width = 470
    window_height = 240
    screen_width = iniciarPartida.winfo_screenwidth()
    screen_height = iniciarPartida.winfo_screenheight()
    position_top = (screen_width / 2) - (window_width / 2)
    position_right = (screen_height / 2) - (window_height / 2)

    iniciarPartida.geometry(
        '%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label4 = Label(iniciarPartida, text="Configuración: "+tipoJuego,
                   fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
    label4.place(x=5, y=185)

    label5 = Label(iniciarPartida, text="Premio: "+premio,
                   fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
    label5.place(x=5, y=210)

    label7 = Label(iniciarPartida, text="Números cantados: ",
                   fg="black", bg="#B0E0E6", font=("Finland", 10))
    label7.place(x=10, y=10)

    cantarNumeros = Button(iniciarPartida, text="Cantar número", command=cantarJuego,
                           bg="#20B2AA", fg="black", font=("Finland", 10, 'bold'))
    cantarNumeros.place(x=350, y=8)

    textBox = Text(iniciarPartida, width=53, height=6,
                   borderwidth=1, relief="solid")
    textBox.place(x=20, y=50)
    textBox.configure(state='disabled')

    label8 = Label(iniciarPartida, text="Total de cartones: " +
                   str(cantidadCartones), fg="black", bg="#B0E0E6", font=("Finland", 10))
    label8.place(x=320, y=210)

    label9 = Label(iniciarPartida, text="Total de jugadores: "+str(
        logic.extraerCantidadJugadores()), fg="black", bg="#B0E0E6", font=("Finland", 10))
    label9.place(x=320, y=185)

    iniciarPartida.mainloop()
