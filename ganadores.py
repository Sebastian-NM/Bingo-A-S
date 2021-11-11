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
#Fin de Imports



#Inicio variables globales
#ganadoresPantalla (str)
ganadoresPantalla="";
#premio (str)
premio=""
#label6 (str)
label6=""
#juegoSelecionado (str)
juegoSelecionado=""
#cantarNumero (str)
cantarNumero=""
#Fin variables globales



'''
Entradas:
- numero
- cedulaText
Salidas:
- textBox (interfaz) 
Restriciones:
- numero (int)
- numero >= 0
'''
#Algoritmo que muestra los números cantados
def cantarFuncion():
   #numero (str)
   numero = logic.ultimoNumeroCantado()
   #Se habilita textBox para escribir en el
   textBox.configure(state='normal')
   #Se escribe en el textBox
   textBox.insert(END, str(numero)+" ")
   #Se desactiva el  textBox para escribir en el
   textBox.configure(state='disable')
#Fin de la función cantarFuncion() 


        
'''
Entradas:
- ganadoresPantalla
Salidas:
- MP (interfaz) 
Restriciones:
- ganadoresPantalla (interfaz)
'''
#Algoritmo que abre la interfaz gráfica MP          
def regresarFuncion():
    global ganadoresPantalla
    #se destruye la interfaz enviarCartonesPantalla 
    ganadoresPantalla.destroy()
    #se abre la interfaz MP
    MP.inicio()
#Fin del algoritmo regresarFuncion()


    
'''
Entradas:
- ganadoresPantalla
Salidas:
- ganadoresPantalla (interfaz) 
Restriciones:
- ganadoresPantalla (interfaz)
'''
#Algoritmo que crea la interfaz grafica 
def inicio():
    global ganadoresPantalla
    global textBox
    global cantarNumero

    #Se hace una copia de los cartones originales
    logic.copiaCartones()
    #tipoJuego (str)
    #premio (str)
    tipoJuego,premio = logic.enviarDatosJuego()
    #cantidadCartones (int)
    cantidadCartones = logic.enviarTotalCartones()
    #Se inicializa las caracteristicas de la gráfica
    ganadoresPantalla=Tk()
    #Se crea el nombre del banner
    ganadoresPantalla.title("Bingo")
    #Se integra el color del fondo
    ganadoresPantalla.config(bg="white")
    #Se establece que el usuario no puede cambiar el tamaño de la aplicacion
    ganadoresPantalla.resizable(False, False)
    #Se establece las caracteristicas del frame de la aplicación
    window_width  = 470
    window_height  = 160
    #Se establece los parametros para insertar el screen en el centro de la pantalla
    screen_width  = ganadoresPantalla.winfo_screenwidth()
    screen_height  = ganadoresPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    #Se crea el screen 
    ganadoresPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    #Se crea una etiqueta label4   
    label4=Label(ganadoresPantalla,text="Tipo de partida: "+tipoJuego, bg="white", fg="black")
    label4.place(x=5,y=5)
    
    #Se crea una etiqueta label5  
    label5=Label(ganadoresPantalla,text="Premio: "+premio, bg="white", fg="black")
    label5.place(x=320, y=5)
    
    #Se crea una etiqueta label7  
    label7=Label(ganadoresPantalla,text="Cartones ganadores:", bg="white", fg="black")
    label7.place(x=17,y=30)
    
    #Se crea un Text textBox   
    textBox = Text(ganadoresPantalla,width=53, height=3, borderwidth=1, relief="solid")
    textBox.place(x=20,y=55)

    #lista (list)
    lista = logic.retornarGanadores()
    #Se crea el registro de la partida
    logic.crearRegistro()

    #indice (int)
    indice = 0
    while(indice<len(lista)):
        if(indice ==len(lista)-1):
            textBox.insert(END, str(lista[indice]))
        else:
            textBox.insert(END, str(lista[indice])+", ")
        #Fin if
        indice = indice + 1
    #Fin del while
    
    #Se desabilita la edición del textBoxv
    textBox.configure(state='disable')

    #Se crea el boton botonCerrarAplicacion
    botonCerrarAplicacion = Button(ganadoresPantalla,text="Terminar Juego", command=regresarFuncion, bg="white", fg="black")
    botonCerrarAplicacion.place(x=358,y=120)

    #Se crea una etiqueta label6  
    label6=Label(ganadoresPantalla,text="Felicidades!", bg="white", fg="black")
    label6.place(x=200,y=120)

    #Se crea la pantalla
    ganadoresPantalla.mainloop()
#Fin del algoritmo inicio()


