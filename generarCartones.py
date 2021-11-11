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
generarCartonesPantalla=""
label3=""
cantidadCartones=0


'''
Entradas: cantidadCartonesText
Salidas: catones (matriz) 
Restriciones: cantidadCartonesText (str)
              identificacionText != ""
'''
#genera los cartones para la partida
def generarFuncion():
    global generarCartonesPantalla
    global cantidadCartones
    global label3

    cantidadCartonesText = cantidadCartones.get();

    if(cantidadCartonesText!="" and cantidadCartonesText!="Valor entre 1 y 500"):
        if(cantidadCartonesText.isnumeric()):
            cantidadCartonesText = int(cantidadCartonesText)
            if(cantidadCartonesText>=1 and cantidadCartonesText<=500 ):
                logic.imprimirMatrices(cantidadCartonesText)
                
                if(cantidadCartonesText==1):
                    label3.destroy()
                    label3=Label(generarCartonesPantalla,text="Se creo: "+str(cantidadCartonesText)+" tabla.", bg="white", fg="black")
                    label3.place(x=50,y=60)                   
                else:
                    label3.destroy()
                    label3=Label(generarCartonesPantalla,text="Se crearon: "+str(cantidadCartonesText)+" tablas.", bg="white", fg="black")
                    label3.place(x=50,y=60)
            else:
                label3.destroy()
                label3=Label(generarCartonesPantalla,text="Debes de digitar un número entre 1 a 500.", bg="white", fg="black")
                label3.place(x=50,y=60)
        else:
            label3.destroy()
            label3=Label(generarCartonesPantalla,text="Digitaste un valor que no esta permitido.", bg="white", fg="black")
            label3.place(x=50,y=60)
    else:
        label3.destroy()
        label3=Label(generarCartonesPantalla,text="No se digitó nada, por favor intentelo de nuevo.", bg="white", fg="black")
        label3.place(x=50,y=60)

         
'''
Entradas: event
Salidas: se borra el contenido de cantidadCartones (accion)
Restriciones: event debe tener una interaccion con cantidadCartones para su uso (accion)
'''
#Eliminación del contenido de cantidadCartones
def clickCantidadCartones(event):
    cantidadCartones.config(state=NORMAL)
    cantidadCartones.delete(0,END)

    
'''
Entradas: enviarCartonesPantalla
Salidas: MP (interfaz) 
Restriciones: enviarCartonesPantalla (interfaz)
'''
#Abre la interfaz gráfica MP  
def regresarFuncion():
    global generarCartonesPantalla
    generarCartonesPantalla.destroy()
    MP.inicio()
   

'''
Entradas: consultarCartonPantalla
Salidas: consultarCartonPantalla (interfaz) 
Restriciones: consultarCartonPantalla (interfaz)
'''
#Crea la interfaz gráfica 
def inicio():
    global generarCartonesPantalla
    global cantidadCartones
    global label3

    logic.eliminarRegistros()
    logic.eliminarCarpetaCartones()
    generarCartonesPantalla=Tk()
    generarCartonesPantalla.title("Bingo")
    generarCartonesPantalla.config(bg="white")
    generarCartonesPantalla.resizable(False, False)
    window_width  = 400
    window_height  = 100
    screen_width  = generarCartonesPantalla.winfo_screenwidth()
    screen_height  = generarCartonesPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    generarCartonesPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label2=Label(generarCartonesPantalla,text="Generar Los cartones de Bingo", bg="white", fg="black")
    label2.place(x=10,y=10)

    label3=Label(generarCartonesPantalla,text="Cantidad:", bg="white", fg="black")
    label3.place(x=30,y=30)

    cantidadCartones_StringVar = StringVar()
    cantidadCartones = Entry(generarCartonesPantalla, bg="white", fg="black", textvariable=cantidadCartones_StringVar, width="25")
    cantidadCartones.insert(0,"Valor entre 1 y 500")
    cantidadCartones.config(state=DISABLED)
    cantidadCartones.bind("<Button-1>",clickCantidadCartones)
    cantidadCartones.place(x=100,y=32)

    botonIniciarSesion = Button(generarCartonesPantalla,text="Generar", command=generarFuncion, bg="white", fg="black")
    botonIniciarSesion.place(x=340,y=28)

    botonCerrarAplicacion = Button(generarCartonesPantalla,text="Regresar", command=regresarFuncion, bg="white", fg="black")
    botonCerrarAplicacion.place(x=337,y=60)

    label3=Label(generarCartonesPantalla,text="", bg="white", fg="black")
    label3.place(x=50,y=60)

    generarCartonesPantalla.mainloop()