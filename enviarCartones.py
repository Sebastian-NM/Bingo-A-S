'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''


#Importar Librerías
from tkinter import *
import menuPrincipal as MP
import logica as logic


#Inicio variables globales
enviarCartonesPantalla="";
cedula=""
label6=""
cantidadCartones=0


'''
Entradas: cantidadCartonesText, cedulaText
Salidas: jugador (str) 
Restriciones: cantidadCartonesText (str)
              identificacionText != ""
              cedulaText (str)
              cedulaText != ""
'''
#Genera un juegador en el sistema
def generarFuncion():
    global enviarCartonesPantalla
    global cantidadCartones
    global cedula
    global label6

    cantidadCartonesText = cantidadCartones.get()
    cedulaText = cedula.get()
    
    if((cantidadCartonesText!="Valor entre 1 y 5" and cedulaText!="Ejemplo: 103250410") and (cantidadCartonesText!="" and cedulaText!="")):
        if(cantidadCartonesText.isnumeric() and (int(cantidadCartonesText)>=1 and int(cantidadCartonesText)<=5)  ) :
            cantidadCartonesText = int(cantidadCartonesText)
            if(cedulaText.isnumeric() and len(cedulaText)==9):
                if(logic.existeCarpetaJugadores()):
                    identificadores = logic.cantidadIdentificadoresLibres()
                    if(identificadores!=0):
                        if(logic.existeJugador(cedulaText)):
                            if(logic.jugadorConCarton(cedulaText)==False):
                                identificadores = logic.cantidadIdentificadoresLibres()
                                if(int(cantidadCartonesText)<=identificadores):
                                    logic.crearJugadorConCartones(cedulaText)
                                    logic.agragerCartonesAJugadores(cedulaText,cantidadCartonesText)
                                    mostrarCantidadElementosCreados(cantidadCartonesText)
                                else:
                                    label6.destroy()
                                    label6=Label(enviarCartonesPantalla,text="No existen tantos cartones para repartir", bg="white", fg="black")
                                    label6.place(x=85,y=65)
                            else:
                                identificadores = logic.cantidadIdentificadoresLibres()
                                cantidadIdentificadoresJugador = logic.cantidadCartonesJugador(cedulaText)
                                if(cantidadIdentificadoresJugador<5):
                                    cartonesFaltantes = 5 - cantidadIdentificadoresJugador
                                    if( cantidadCartonesText <= cartonesFaltantes):
                                        logic.agragerCartonesAJugadores(cedulaText,cantidadCartonesText)
                                        mostrarCantidadElementosCreados(cantidadCartonesText)
                                    else:
                                        label6.destroy()
                                        label6=Label(enviarCartonesPantalla,text="El jugador no puede tener la cantidad de cartones ingresada", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
                                        label6.place(x=85,y=80)
                                else:
                                    label6.destroy()
                                    label6=Label(enviarCartonesPantalla,text="El jugador ya cuenta con 5 cartones", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
                                    label6.place(x=85,y=80)
                        else:
                            label6.destroy()
                            label6=Label(enviarCartonesPantalla,text="La cédula ingresada no existe", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
                            label6.place(x=85,y=80)
                    else:
                        label6.destroy()
                        label6=Label(enviarCartonesPantalla,text="No existen cartones en el sistema", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
                        label6.place(x=65,y=80)
                else:
                    label6.destroy()
                    label6=Label(enviarCartonesPantalla,text="No existen jugadores en el sistema", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
                    label6.place(x=65,y=80)
            else:
                label6.destroy()
                label6=Label(enviarCartonesPantalla,text="Digite una cédula válida", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
                label6.place(x=88,y=80)
        else:
            label6.destroy()
            label6=Label(enviarCartonesPantalla,text="Digite una cantidad válida", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
            label6.place(x=85,y=80)
    else:
        label6.destroy()
        label6=Label(enviarCartonesPantalla,text="Ingrese la información solicitada", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
        label6.place(x=60,y=80)


'''
Entradas: pCantidad
Salidas: label6 (interfaz)
Restriciones: pCantidad (int)
              pCantidad > 0
'''
#Eliminación del contenido de identificación
def mostrarCantidadElementosCreados(pCantidad):
    global label6

    if(pCantidad==1):
        label6.destroy()
        label6=Label(enviarCartonesPantalla,text="Se envió "+str(pCantidad)+" carton al jugador", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
        label6.place(x=68,y=80)
    else:
        label6.destroy()
        label6=Label(enviarCartonesPantalla,text="Se enviaron "+str(pCantidad)+" cartones al jugador", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
        label6.place(x=55,y=80)
    

'''
Entradas: enviarCartonesPantalla
Salidas: MP (interfaz) 
Restriciones: enviarCartonesPantalla (interfaz)
'''
#Abre la interfaz gráfica MP         
def regresarFuncion():
    global enviarCartonesPantalla
    enviarCartonesPantalla.destroy()
    MP.inicio()


'''
Entradas: event
Salidas: se borra el contenido de cantidadCartones (accion)
Restriciones: event debe tener una interaccion con cantidadCartones para su uso (accion)
'''
#Elimina el contenido de cantidadCartones
def clickCantidad(event):
    cantidadCartones.config(state=NORMAL)
    cantidadCartones.delete(0,END)


'''
Entradas: event
Salidas: se borra el contenido de cedula (accion)
Restriciones: event debe tener una interaccion con cedula para su uso (accion)
'''
#Elimina el contenido de cédula 
def clickCedula(event):
    cedula.config(state=NORMAL)
    cedula.delete(0,END)

  
'''
Entradas: consultarCartonPantalla
Salidas: consultarCartonPantalla (interfaz) 
Restriciones: consultarCartonPantalla (interfaz)
'''
#Creación de la interfaz gráfica 
def inicio():
    global enviarCartonesPantalla
    global cantidadCartones
    global cedula
    global label6
    
    logic.listaIdentificadoresLibres()
    enviarCartonesPantalla=Tk()
    enviarCartonesPantalla.iconbitmap("bingo.ico")
    enviarCartonesPantalla.title("Enviar Cartones")
    enviarCartonesPantalla.config(bg="#B0E0E6")
    enviarCartonesPantalla.resizable(False, False)
    window_width  = 350
    window_height  = 150
    screen_width  = enviarCartonesPantalla.winfo_screenwidth()
    screen_height  = enviarCartonesPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)

    enviarCartonesPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))
  
    label4=Label(enviarCartonesPantalla,text="Cantidad a enviar:", fg="black", bg="#B0E0E6", font=("Finland", 10))
    label4.place(x=30,y=20)

    cantidadCartones_StringVar = StringVar()

    cantidadCartones = Entry(enviarCartonesPantalla, bg="white", fg="black", textvariable=cantidadCartones_StringVar, width="25")
    cantidadCartones.insert(0,"Valor entre 1 y 5")
    cantidadCartones.config(state=DISABLED)
    cantidadCartones.bind("<Button-1>",clickCantidad)
    cantidadCartones.place(x=155,y=22)
 
    label5=Label(enviarCartonesPantalla,text="Cédula del jugador:", fg="black", bg="#B0E0E6", font=("Finland", 10))
    label5.place(x=30,y=50)

    cedula_StringVar = StringVar()

    cedula = Entry(enviarCartonesPantalla, bg="white", fg="black", textvariable=cedula_StringVar, width="25")
    cedula.insert(0,"Ejemplo: 103250410")
    cedula.config(state=DISABLED)
    cedula.bind("<Button-1>",clickCedula)
    cedula.place(x=155,y=52)

    botonIniciarSesion = Button(enviarCartonesPantalla,text="Enviar", command=generarFuncion, bg="#20B2AA", fg="black", font=("Finland", 10, 'bold'))
    botonIniciarSesion.place(x=230,y=112)

    botonCerrarAplicacion = Button(enviarCartonesPantalla,text="Menú Principal", command=regresarFuncion, bg="#E00000", fg="#FFFFFF", font=("Finland", 10,'bold'))
    botonCerrarAplicacion.place(x=40,y=112)

    label6=Label(enviarCartonesPantalla,text="", fg="black", bg="#B0E0E6", font=("Finland", 10))
    label6.place(x=30,y=85)  

    enviarCartonesPantalla.mainloop()