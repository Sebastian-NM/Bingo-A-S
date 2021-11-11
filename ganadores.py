'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''


#Importar Librerías
from tkinter import *
from tkinter import ttk
import menuPrincipal as MP
import logica as logic


#Inicio variables globales
ganadoresPantalla="";
premio=""
label6=""
juegoSelecionado=""
cantarNumero=""


'''
Entradas: numero, cedulaText
Salidas: textBox (interfaz) 
Restriciones: numero (int)
              numero >= 0
'''
#Muestra los números cantados
def cantarFuncion():
   numero = logic.ultimoNumeroCantado()
   textBox.configure(state='normal')
   textBox.insert(END, str(numero)+" ")
   textBox.configure(state='disable')

        
'''
Entradas: ganadoresPantalla
Salidas: MP (interfaz) 
Restriciones: ganadoresPantalla (interfaz)
'''
#Abre la interfaz gráfica MP          
def regresarFuncion():
    global ganadoresPantalla
    ganadoresPantalla.destroy()
    MP.inicio()

    
'''
Entradas: ganadoresPantalla
Salidas: ganadoresPantalla (interfaz) 
Restriciones: ganadoresPantalla (interfaz)
'''
#Creación de la interfaz gráfica 
def inicio():
    global ganadoresPantalla
    global textBox
    global cantarNumero

    logic.copiaCartones()
    tipoJuego,premio = logic.enviarDatosJuego()
    cantidadCartones = logic.enviarTotalCartones()
    ganadoresPantalla=Tk()
    ganadoresPantalla.title("Bingo")
    ganadoresPantalla.config(bg="white")
    ganadoresPantalla.resizable(False, False)
    window_width  = 470
    window_height  = 160
    screen_width  = ganadoresPantalla.winfo_screenwidth()
    screen_height  = ganadoresPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    ganadoresPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label4=Label(ganadoresPantalla,text="Tipo de partida: "+tipoJuego, bg="white", fg="black")
    label4.place(x=5,y=5)
     
    label5=Label(ganadoresPantalla,text="Premio: "+premio, bg="white", fg="black")
    label5.place(x=320, y=5)
     
    label7=Label(ganadoresPantalla,text="Cartones ganadores:", bg="white", fg="black")
    label7.place(x=17,y=30)
      
    textBox = Text(ganadoresPantalla,width=53, height=3, borderwidth=1, relief="solid")
    textBox.place(x=20,y=55)

    lista = logic.retornarGanadores()

    logic.crearRegistro()

    indice = 0
    while(indice<len(lista)):
        if(indice ==len(lista)-1):
            textBox.insert(END, str(lista[indice]))
        else:
            textBox.insert(END, str(lista[indice])+", ")
        indice = indice + 1
    
    textBox.configure(state='disable')

    botonCerrarAplicacion = Button(ganadoresPantalla,text="Terminar Juego", command=regresarFuncion, bg="white", fg="black")
    botonCerrarAplicacion.place(x=358,y=120)

    label6=Label(ganadoresPantalla,text="Felicidades!", bg="white", fg="black")
    label6.place(x=200,y=120)

    ganadoresPantalla.mainloop()