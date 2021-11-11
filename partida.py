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
import ganadores as winners



#Inicio variables globales
partidaPantalla="";
premio=""
label6=""
juegoSelecionado=""
cantarNumero=""
primero=bool


'''
Entradas: partidaPantalla
Salidas: winners (interfaz) 
Restriciones: partidaPantalla (interfaz)
'''
#Abre la interfaz gráfica winners   
def ganadoresFuncion():
    global partidaPantalla
    partidaPantalla.destroy()
    winners.inicio()


'''
Entradas: numero
Salidas: jugador (str) 
Restriciones: numero (int)
              numero >= 0
'''
#Genera un número nuevo
def cantarFuncion():
    global partidaPantalla
    global textBox
    global cantarNumero
    global primero

    tipoJuego,premio = logic.enviarDatosJuego()
    
    if( logic.cantarNumero(tipoJuego)==False):
        numero = logic.ultimoNumeroCantado()
        textBox.configure(state='normal')
        if(primero==True):
            primero=False
            textBox.insert(END, str(numero))
            textBox.configure(state='disable')
        else:
            textBox.insert(END, ","+str(numero))
            textBox.configure(state='disable')
    else:
        logic.enviarEmailGanadores()
        cantarNumero.configure(state='disable')
        textBox.configure(state='normal')

        label6=Label(partidaPantalla,text="Ganador", bg="white", fg="black")
        label6.place(x=203,y=218)
        
        botonGanadores = Button(partidaPantalla,text="Ver los ganadores", command=ganadoresFuncion, bg="white", fg="black")
        botonGanadores.place(x=174,y=190)
    

'''
Entradas: event
Salidas: se borra el contenido de premio (accion)
Restriciones: event debe tener una interaccion con premio para su uso (accion)
'''
#Borra el contenido de premio
def clickpremio(event):
    premio.config(state=NORMAL)
    premio.delete(0,END)

    
'''
Entradas: partidaPantalla
Salidas: partidaPantalla (interfaz) 
Restriciones: partidaPantalla (interfaz)
'''
#Crea la interfaz grafica 
def inicio():
    global partidaPantalla
    global textBox
    global cantarNumero
    global primero

    primero = True
    logic.copiaCartones()
    tipoJuego,premio = logic.enviarDatosJuego()
    cantidadCartones = logic.enviarTotalCartones()
    partidaPantalla=Tk()
    partidaPantalla.title("Bingo")
    partidaPantalla.config(bg="white")
    partidaPantalla.resizable(False, False)
    window_width  = 470
    window_height  = 240
    screen_width  = partidaPantalla.winfo_screenwidth()
    screen_height  = partidaPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)

    partidaPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label4=Label(partidaPantalla,text="Tipo de cartida: "+tipoJuego, bg="white", fg="black")
    label4.place(x=5,y=5)

    label5=Label(partidaPantalla,text="Premio: "+premio, bg="white", fg="black")
    label5.place(x=320, y=5)

    label7=Label(partidaPantalla,text="Números cantados: ", bg="white", fg="black")
    label7.place(x=10,y=60)

    cantarNumero = Button(partidaPantalla,text="Cantar número", command=cantarFuncion, bg="white", fg="black")
    cantarNumero.place(x=180,y=30)

    textBox = Text(partidaPantalla,width=53, height=6, borderwidth=1, relief="solid")
    textBox.place(x=20,y=85)
    textBox.configure(state='disabled')

    label8=Label(partidaPantalla,text="Total de cartones: "+str(cantidadCartones), bg="white", fg="black")
    label8.place(x=5, y=218)

    label9=Label(partidaPantalla,text="Total de jugadores: "+str(logic.extraerCantidadJugadores()), bg="white", fg="black")
    label9.place(x=340, y=218)
    
    partidaPantalla.mainloop()