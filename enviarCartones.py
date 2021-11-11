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
                                    label6=Label(enviarCartonesPantalla,text="No existen muchos cartones para repartir.", bg="white", fg="black")
                                    label6.place(x=15,y=85)
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
                                        label6=Label(enviarCartonesPantalla,text="El jugador no puede tener esa cantidad de cartones.", bg="white", fg="black")
                                        label6.place(x=15,y=85)
                                else:
                                    label6.destroy()
                                    label6=Label(enviarCartonesPantalla,text="El jugador cuenta con 5 cartones registrados.", bg="white", fg="black")
                                    label6.place(x=25,y=85)
                        else:
                            label6.destroy()
                            label6=Label(enviarCartonesPantalla,text="El jugador que se digitó no existe en el programa.", bg="white", fg="black")
                            label6.place(x=30,y=85)
                    else:
                        label6.destroy()
                        label6=Label(enviarCartonesPantalla,text="No hay cartones para repartir.", bg="white", fg="black")
                        label6.place(x=25,y=85)
                else:
                    label6.destroy()
                    label6=Label(enviarCartonesPantalla,text="No existen jugadores ingresados en el progroma.", bg="white", fg="black")
                    label6.place(x=30,y=85)
            else:
                label6.destroy()
                label6=Label(enviarCartonesPantalla,text="Se digitó una cédula que no es valida.", bg="white", fg="black")
                label6.place(x=30,y=85)
        else:
            label6.destroy()
            label6=Label(enviarCartonesPantalla,text="Se digitó una cantidad que no es valida.", bg="white", fg="black")
            label6.place(x=30,y=85)
    else:
        label6.destroy()
        label6=Label(enviarCartonesPantalla,text="Falta información por completar.", bg="white", fg="black")
        label6.place(x=30,y=85)


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
        label6=Label(enviarCartonesPantalla,text="Se envió: "+str(pCantidad)+" carton al jugador.", bg="white", fg="black")
        label6.place(x=30,y=85)
    else:
        label6.destroy()
        label6=Label(enviarCartonesPantalla,text="Se enviaron: "+str(pCantidad)+" cartones al jugador.", bg="white", fg="black")
        label6.place(x=30,y=85)
    

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
    enviarCartonesPantalla.title("Bingo")
    enviarCartonesPantalla.config(bg="white")
    enviarCartonesPantalla.resizable(False, False)
    window_width  = 300
    window_height  = 150
    screen_width  = enviarCartonesPantalla.winfo_screenwidth()
    screen_height  = enviarCartonesPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)

    enviarCartonesPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label2=Label(enviarCartonesPantalla,text="Enviar cartón a jugador registrado", bg="white", fg="black")
    label2.place(x=60,y=5)
  
    label4=Label(enviarCartonesPantalla,text="Cantidad:", bg="white", fg="black")
    label4.place(x=30,y=30)

    cantidadCartones_StringVar = StringVar()

    cantidadCartones = Entry(enviarCartonesPantalla, bg="white", fg="black", textvariable=cantidadCartones_StringVar, width="25")
    cantidadCartones.insert(0,"Valor entre 1 y 5")
    cantidadCartones.config(state=DISABLED)
    cantidadCartones.bind("<Button-1>",clickCantidad)
    cantidadCartones.place(x=100,y=30)
 
    label5=Label(enviarCartonesPantalla,text="Cédula:", bg="white", fg="black")
    label5.place(x=30,y=60)

    cedula_StringVar = StringVar()

    cedula = Entry(enviarCartonesPantalla, bg="white", fg="black", textvariable=cedula_StringVar, width="25")
    cedula.insert(0,"Ejemplo: 103250410")
    cedula.config(state=DISABLED)
    cedula.bind("<Button-1>",clickCedula)
    cedula.place(x=100,y=62)

    botonIniciarSesion = Button(enviarCartonesPantalla,text="Enviar cartones digitales", command=generarFuncion, bg="white", fg="black")
    botonIniciarSesion.place(x=40,y=110)

    botonCerrarAplicacion = Button(enviarCartonesPantalla,text="Regresar", command=regresarFuncion, bg="white", fg="black")
    botonCerrarAplicacion.place(x=200,y=110)

    label6=Label(enviarCartonesPantalla,text="", bg="white", fg="black")
    label6.place(x=30,y=85)  

    enviarCartonesPantalla.mainloop()