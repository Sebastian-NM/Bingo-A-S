'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''

# Importar Librerías
from tkinter import *
from PIL import Image, ImageTk
import menuPrincipal as MP
import funcionalidades as func


# Inicio variables globales
consultarCarton = ""
idCarton = ""
imagenCarton = ""
mensajesError = ""
mensajeExito = ""


'''
Entradas: idCartonText
Salidas: carton (img) 
Restriciones: idCartonText (str)
              idCartonText !=""
'''
# Muestra el carton solicitado


def mostrarCarton():
    global consultarCarton
    global idCarton
    global imagenCarton
    global mensajesError
    global mensajeExito

    idCartonText = idCarton.get()

    if(idCartonText != "" and idCartonText != "NCC004"):
        if(len(idCartonText) == 6):
            if(func.existeCarpetaCartones()):
                if(func.existeImagenEnCarpeta(idCartonText)):
                    if(func.identificarJugadorConCarton(idCartonText)):
                        cartonJugador = func.extraerIdentificadorJugadorConCarton(
                            idCartonText)
                        mensajeExito.destroy()
                        mensajeExito = Label(consultarCarton, text="Dueño del cartón: "+str(cartonJugador[1])+" , cédula: "+str(
                            cartonJugador[0])+".", bg="#B0E0E6", fg="black", font=("Finland", 10))
                        mensajeExito.place(x=40, y=350)
                    else:
                        mensajeExito.destroy()
                        mensajeExito = Label(
                            consultarCarton, text="", bg="#B0E0E6", fg="black", font=("Finland", 10))
                        mensajeExito.place(x=40, y=350)

                    mensajesError.destroy()
                    mensajesError = Label(consultarCarton, text="¡Cartón encontrado!.",
                                          bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
                    mensajesError.place(x=150, y=50)

                    imagenCarton.destroy()

                    imagenCarton = Frame(
                        consultarCarton, width=350, height=260)
                    imagenCarton.place(x="40", y="80")

                    img = Image.open('cartones/'+idCartonText+'.png')
                    img = img.resize((354, 270), Image.BICUBIC)
                    tkimage = ImageTk.PhotoImage(img)
                    labelImage = Label(
                        imagenCarton, image=tkimage, width=350, height=260).pack()
                    consultarCarton.mainloop()
                else:
                    mensajesError.destroy()
                    mensajesError = Label(consultarCarton, text="El número de cartón es incorrecto.",
                                          bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
                    mensajesError.place(x=120, y=50)
            else:
                mensajesError.destroy()
                mensajesError = Label(consultarCarton, text="No existen cartones creados en el sistema.",
                                      bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
                mensajesError.place(x=65, y=50)
        else:
            mensajesError.destroy()
            mensajesError = Label(consultarCarton, text="Ingrese un número de cartón válido.",
                                  bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
            mensajesError.place(x=105, y=50)
    else:
        mensajesError.destroy()
        mensajesError = Label(consultarCarton, text="Por favor ingrese el número de cartón a consultar.",
                              bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
        mensajesError.place(x=65, y=50)


'''
Entradas: menuPrincipal
Salidas: MP (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
# Abre la interfaz gráfica MP


def regresarFuncion():
    global consultarCarton
    consultarCarton.destroy()
    MP.inicio()


'''
Entradas: event
Salidas: se borra el contenido de idCarton (accion)
Restriciones: event debe tener una interaccion con identificación para su uso (accion)
'''
# Borra el contenido de identificación


def clickIdentificar(event):
    idCarton.config(state=NORMAL)
    idCarton.delete(0, END)


'''
Entradas: consultarCarton
Salidas: consultarCarton (interfaz) 
Restriciones: consultarCarton (interfaz)
'''
# Creación de la interfaz grafica de consultar cartón


def buscarCarton():
    global consultarCarton
    global idCarton
    global imagenCarton
    global mensajesError
    global mensajeExito

    consultarCarton = Tk()
    consultarCarton.iconbitmap("bingo.ico")
    consultarCarton.title("Consultar Cartones")
    consultarCarton.config(bg="#B0E0E6")
    consultarCarton.resizable(False, False)
    window_width = 450
    window_height = 405
    screen_width = consultarCarton.winfo_screenwidth()
    screen_height = consultarCarton.winfo_screenheight()
    position_top = (screen_width / 2) - (window_width / 2)
    position_right = (screen_height / 2) - (window_height / 2)
    consultarCarton.geometry(
        '%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label4 = Label(consultarCarton, text="Ingrese el número de cartón:",
                   fg="black", bg="#B0E0E6", font=("Finland", 10))
    label4.place(x=30, y=20)

    idCartonCartones_StringVar = StringVar()

    idCarton = Entry(consultarCarton, bg="white", fg="black",
                     textvariable=idCartonCartones_StringVar, width="25")
    idCarton.insert(0, "ENCC004")
    idCarton.config(state=DISABLED)
    idCarton.bind("<Button-1>", clickIdentificar)
    idCarton.place(x=205, y=22)

    botonIniciarSesion = Button(consultarCarton, text="Buscar", command=mostrarCarton,
                                bg="#20B2AA", fg="black", font=("Finland", 10, 'bold'))
    botonIniciarSesion.place(x=380, y=17)

    botonCerrarAplicacion = Button(consultarCarton, text="Menú Principal",
                                   command=regresarFuncion, bg="#E00000", fg="#FFFFFF", font=("Finland", 10, 'bold'))
    botonCerrarAplicacion.place(x=176, y=370)

    imagenCarton = Frame(consultarCarton, width=370, height=260)
    imagenCarton.place(x="40", y="80")

    mensajesError = Label(consultarCarton, text="",
                          bg="#B0E0E6", fg="black", font=("Finland", 10))
    mensajesError.place(x=40, y=45)

    mensajeExito = Label(consultarCarton, text="",
                         bg="#B0E0E6", fg="black", font=("Finland", 10))
    mensajeExito.place(x=40, y=350)

    consultarCarton.mainloop()
