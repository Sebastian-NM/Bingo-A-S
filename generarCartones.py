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
                    label3=Label(generarCartonesPantalla,text="Se creó "+str(cantidadCartonesText)+" cartón", bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
                    label3.place(x=250,y=40)                   
                else:
                    label3.destroy()
                    label3=Label(generarCartonesPantalla,text="Se crearon "+str(cantidadCartonesText)+" cartones", bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
                    label3.place(x=230,y=40)
            else:
                label3.destroy()
                label3=Label(generarCartonesPantalla,text="Debe de digitar un número entre 1 y 500.", bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
                label3.place(x=150,y=40)
        else:
            label3.destroy()
            label3=Label(generarCartonesPantalla,text="Digite un valor válido.", bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
            label3.place(x=230,y=40)
    else:
        label3.destroy()
        label3=Label(generarCartonesPantalla,text="Ingrese el número de cartones a generar.", bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
        label3.place(x=150,y=40)

         
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
    generarCartonesPantalla.iconbitmap("bingo.ico")
    generarCartonesPantalla.title("Generar Cartones de Bingo")
    generarCartonesPantalla.config(bg="#B0E0E6")
    generarCartonesPantalla.resizable(False, False)
    window_width  = 600
    window_height  = 130
    screen_width  = generarCartonesPantalla.winfo_screenwidth()
    screen_height  = generarCartonesPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    generarCartonesPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label2=Label(generarCartonesPantalla,text="", bg="#B0E0E6", fg="black", font=("Finland", 10))
    label2.place(x=10,y=10)

    label3=Label(generarCartonesPantalla,text="Ingrese la cantidad de cartones que desea generar:", bg="#B0E0E6", fg="black", font=("Finland", 10))
    label3.place(x=20,y=10)

    cantidadCartones_StringVar = StringVar()
    cantidadCartones = Entry(generarCartonesPantalla, bg="white", fg="black", textvariable=cantidadCartones_StringVar, width="25")
    cantidadCartones.insert(0,"Valor entre 1 y 500")
    cantidadCartones.config(state=DISABLED)
    cantidadCartones.bind("<Button-1>",clickCantidadCartones)
    cantidadCartones.place(x=330,y=13)

    botonIniciarSesion = Button(generarCartonesPantalla,text="Generar", command=generarFuncion, bg="#20B2AA", fg="black", font=("Finland", 10, 'bold'))
    botonIniciarSesion.place(x=350,y=80)

    botonCerrarAplicacion = Button(generarCartonesPantalla,text="Menú Principal", command=regresarFuncion, bg="#E00000", fg="#FFFFFF", font=("Finland", 10, 'bold'))
    botonCerrarAplicacion.place(x=150,y=80)

    label3=Label(generarCartonesPantalla,text="", bg="#B0E0E6", fg="black", font=("Finland", 10))
    label3.place(x=50,y=60)

    generarCartonesPantalla.mainloop()