'''
Proyecto programado 2
Tema: Gestor de Bingos
Integrantes:
-Valentina Mende Solano, 2021142085
-Jorge Arturo Guadamuz Godinez, 2021132991
-Daniel Josué Aguilar Gómez, 2020184120
'''



#Inicio de Imports
from tkinter import *
from tkinter import ttk
import menuPrincipal as MP
import logica as logic
import ganadores as winners
#Fin de Imports



#Inicio variables globales
#partidaPantalla (str)
partidaPantalla="";
#premio (str)
premio=""
#label6 (str)
label6=""
#juegoSelecionado (str)
juegoSelecionado=""
#cantarNumero (str)
cantarNumero=""
#primero (bool)
primero=bool
#Fin variables globales



'''
Entradas:
- partidaPantalla
Salidas:
- winners (interfaz) 
Restriciones:
- partidaPantalla (interfaz)
'''
#Algoritmo que abre la interfaz gráfica winners   
def ganadoresFuncion():
    global partidaPantalla
    partidaPantalla.destroy()
    winners.inicio()
#Fin del algoritmo regresarFuncion()


'''
Entradas:
- numero
Salidas:
- jugador (str) 
Restriciones:
- numero (int)
- numero >= 0
'''
#Algoritmo que genera un número nuevo
def cantarFuncion():
    global partidaPantalla
    global textBox
    global cantarNumero
    global primero

    #tipoJuego (str)
    #premio (str)
    tipoJuego,premio = logic.enviarDatosJuego()
    
    if( logic.cantarNumero(tipoJuego)==False):
        #numero (str)
        numero = logic.ultimoNumeroCantado()
        textBox.configure(state='normal')
        if(primero==True):
            primero=False
            #Se inserta un nuevo número
            textBox.insert(END, str(numero))
            textBox.configure(state='disable')
        else:
            #Se inserta un nuevo número
            textBox.insert(END, ","+str(numero))
            textBox.configure(state='disable')
        #Fin if
    else:
        #Se envia un correo a los ganadores
        logic.enviarEmailGanadores()
        cantarNumero.configure(state='disable')
        textBox.configure(state='normal')

        #Se crea el label6
        label6=Label(partidaPantalla,text="Ganador", bg="white", fg="black")
        label6.place(x=203,y=218)
        
        #Se crea el boton botonGanadores
        botonGanadores = Button(partidaPantalla,text="Ver los ganadores", command=ganadoresFuncion, bg="white", fg="black")
        botonGanadores.place(x=174,y=190)
    #Fin if
#Fin del algoritmo cantarFuncion()
    
    
           
    

'''
Entradas:
- event
Salidas:
- se borra el contenido de premio (accion)
Restriciones:
- event debe tener una interaccion con premio para su uso (accion)
'''
#Algoritmo que borra el contenido de premio
def clickpremio(event):
    premio.config(state=NORMAL)
    premio.delete(0,END)
#Ffin del algoritmo clickpremio()

    
'''
Entradas:
- partidaPantalla
Salidas:
- partidaPantalla (interfaz) 
Restriciones:
- partidaPantalla (interfaz)
'''
#Algoritmo que crea la interfaz grafica 
def inicio():
    global partidaPantalla
    global textBox
    global cantarNumero
    global primero

    #primero (bool)
    primero = True
    #Se hace una copia de los cartones originales
    logic.copiaCartones()
    #tipoJuego (str)
    #premio (str)
    tipoJuego,premio = logic.enviarDatosJuego()
    #cantidadCartones (int)
    cantidadCartones = logic.enviarTotalCartones()
    #Se inicializa las caracteristicas de la gráfica
    partidaPantalla=Tk()
    #Se crea el nombre del banner
    partidaPantalla.title("Bingo")
    #Se integra el color del fondo
    partidaPantalla.config(bg="white")
    #Se establece que el usuario no puede cambiar el tamaño de la aplicacion
    partidaPantalla.resizable(False, False)
    #Se establece las caracteristicas del frame de la aplicación
    window_width  = 470
    window_height  = 240
    #Se establece los parametros para insertar el screen en el centro de la pantalla
    screen_width  = partidaPantalla.winfo_screenwidth()
    screen_height  = partidaPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)

    #Se crea el screen 
    partidaPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    #Se crea una etiqueta label4
    label4=Label(partidaPantalla,text="Tipo de cartida: "+tipoJuego, bg="white", fg="black")
    label4.place(x=5,y=5)

    #Se crea una etiqueta label5
    label5=Label(partidaPantalla,text="Premio: "+premio, bg="white", fg="black")
    label5.place(x=320, y=5)

    #Se crea una etiqueta label7
    label7=Label(partidaPantalla,text="Números cantados: ", bg="white", fg="black")
    label7.place(x=10,y=60)

    #Se crea el boton cantarNumero
    cantarNumero = Button(partidaPantalla,text="Cantar número", command=cantarFuncion, bg="white", fg="black")
    cantarNumero.place(x=180,y=30)

    #Se crea un text textBox
    textBox = Text(partidaPantalla,width=53, height=6, borderwidth=1, relief="solid")
    textBox.place(x=20,y=85)
    textBox.configure(state='disabled')

    #Se crea una etiqueta label8
    label8=Label(partidaPantalla,text="Total de cartones: "+str(cantidadCartones), bg="white", fg="black")
    label8.place(x=5, y=218)

    #Se crea una etiqueta label9
    label9=Label(partidaPantalla,text="Total de jugadores: "+str(logic.extraerCantidadJugadores()), bg="white", fg="black")
    label9.place(x=340, y=218)
    
    #Se crea la pantalla
    partidaPantalla.mainloop()
#Fin del algoritmo inicio()

    
