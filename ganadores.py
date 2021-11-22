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


# Inicio variables globales
cartonesGanadores = ""
premio = ""
mensaje = ""
cantarNumero = ""


'''
Entradas: numero, cedulaText
Salidas: textBox (interfaz) 
Restriciones: numero (int)
              numero >= 0
'''
# Muestra los números cantados


def cantarJuego():
    numero = func.ultimoNumeroCantado()
    textBox.configure(state='normal')
    textBox.insert(END, str(numero)+" ")
    textBox.configure(state='disable')


'''
Entradas: cartonesGanadores
Salidas: MP (interfaz) 
Restriciones: cartonesGanadores (interfaz)
'''
# Abre la interfaz gráfica MP


def regresarFuncion():
    global cartonesGanadores
    cartonesGanadores.destroy()
    MP.inicio()


'''
Entradas: cartonesGanadores
Salidas: cartonesGanadores (interfaz) 
Restriciones: cartonesGanadores (interfaz)
'''
# Creación de la interfaz gráfica


def ganadoresBingo():
    global cartonesGanadores
    global textBox
    global cantarNumero

    func.copiaCartones()
    tipoJuego, premio = func.enviarDatosJuego()
    cantidadCartones = func.enviarTotalCartones()
    cartonesGanadores = Tk()
    cartonesGanadores.iconbitmap("bingo.ico")
    cartonesGanadores.title("Cartones Ganadores")
    cartonesGanadores.config(bg="#B0E0E6")
    cartonesGanadores.resizable(False, False)
    window_width = 470
    window_height = 160
    screen_width = cartonesGanadores.winfo_screenwidth()
    screen_height = cartonesGanadores.winfo_screenheight()
    position_top = (screen_width / 2) - (window_width / 2)
    position_right = (screen_height / 2) - (window_height / 2)
    cartonesGanadores.geometry(
        '%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label4 = Label(cartonesGanadores, text="Configuración: " +
                   tipoJuego, bg="#B0E0E6", fg="black", font=("Finland", 10))
    label4.place(x=5, y=5)

    label5 = Label(cartonesGanadores, text="Premio: "+premio,
                   bg="#B0E0E6", fg="black", font=("Finland", 10))
    label5.place(x=350, y=5)

    label7 = Label(cartonesGanadores, text="Cartones ganadores:",
                   bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
    label7.place(x=17, y=30)

    textBox = Text(cartonesGanadores, width=53, height=3,
                   borderwidth=1, relief="solid")
    textBox.place(x=20, y=55)

    lista = func.retornarGanadores()

    func.crearRegistro()

    indice = 0
    while(indice < len(lista)):
        if(indice == len(lista)-1):
            textBox.insert(END, str(lista[indice]))
        else:
            textBox.insert(END, str(lista[indice])+", ")
        indice = indice + 1

    textBox.configure(state='disable')

    botonCerrarAplicacion = Button(cartonesGanadores, text="Terminar Juego",
                                   command=regresarFuncion, bg="#E00000", fg="#FFFFFF", font=("Finland", 10, 'bold'))
    botonCerrarAplicacion.place(x=175, y=120)

    mensaje = Label(cartonesGanadores, text="¡Felicidades!",
                    bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
    mensaje.place(x=355, y=30)

    cartonesGanadores.mainloop()
