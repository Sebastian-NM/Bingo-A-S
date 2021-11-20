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
import partida as game


#Inicio variables globales
iniciarJuegoPantalla="";
premio=""
label6=""
juegoSelecionado=""


'''
Entradas: premioText, juegoSeleccionadoText
Salidas: game (interfaz) 
Restriciones: premioText (str)
              premioText != ""
              juegoSeleccionadoText (str)
              juegoSeleccionadoText != ""
'''
#Genera solicitud de los requerimientos necesarios para iniciar una partida
def generarFuncion():
    global iniciarJuegoPantalla
    global premio
    global label6
    global juegoSelecionado

    premioText = premio.get()
    juegoSeleccionadoText = juegoSelecionado.get()
    
    if(premioText!="50.000 colones" and premioText!=""):
        if(logic.enviarTotalCartones()!=0):
            logic.guardarDatosJuego(juegoSeleccionadoText,premioText)
            label6.destroy()
            label6=Label(iniciarJuegoPantalla,text=juegoSeleccionadoText, bg="white", fg="black")
            label6.place(x=150,y=56)
            iniciarJuegoPantalla.destroy()
            game.inicio()
        else:
            label6.destroy()
            label6=Label(iniciarJuegoPantalla,text="No se puede iniciar el juego debido a que no existen cartones", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
            label6.place(x=40,y=56)
    else:
        label6.destroy()
        label6=Label(iniciarJuegoPantalla,text="Complete la información solicitada", fg="black", bg="#B0E0E6", font=("Finland", 10, 'bold'))
        label6.place(x=120,y=56)
        

'''
Entradas: iniciarJuegoPantalla
Salidas: MP (interfaz) 
Restriciones: iniciarJuegoPantalla (interfaz)
'''
#Abre la interfaz gráfica MP         
def regresarFuncion():
    global iniciarJuegoPantalla
    iniciarJuegoPantalla.destroy()
    MP.inicio()


'''
Entradas: event
Salidas: se borra el contenido de premio (accion)
Restriciones: event debe tener una interaccion con premio para su uso (accion)
'''
#Eliminación del contenido de cantidadCartones
def clickpremio(event):
    premio.config(state=NORMAL)
    premio.delete(0,END)
  
    
'''
Entradas: iniciarJuegoPantalla
Salidas: iniciarJuegoPantalla (interfaz) 
Restriciones: iniciarJuegoPantalla (interfaz)
'''
#Crea la interfaz grafica 
def inicio():
    global iniciarJuegoPantalla
    global premio
    global label6
    global juegoSelecionado

    logic.limpiarVariables()
    iniciarJuegoPantalla=Tk()
    iniciarJuegoPantalla.iconbitmap("bingo.ico")
    iniciarJuegoPantalla.title("Iniciar Juego")
    iniciarJuegoPantalla.config(bg="#B0E0E6")
    iniciarJuegoPantalla.resizable(False, False)
    window_width  = 470
    window_height  = 120
    screen_width  = iniciarJuegoPantalla.winfo_screenwidth()
    screen_height  = iniciarJuegoPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    iniciarJuegoPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label2=Label(iniciarJuegoPantalla,text="¡Juguemos!", bg="#B0E0E6", fg="black", font=("Finland", 12, 'bold'))
    label2.place(x=200,y=5)

    label4=Label(iniciarJuegoPantalla,text="Configuración:", bg="#B0E0E6", fg="black", font=("Finland", 10))
    label4.place(x=15,y=30)

    choices = ['Jugar en X', 'Cuatro esquinas', 'Cartón lleno','Jugar en Z']
    juegoSelecionado = ttk.Combobox(iniciarJuegoPantalla, values = choices)
    juegoSelecionado.current(0)
    juegoSelecionado.place(x=100,y=30)

    label5=Label(iniciarJuegoPantalla,text="Premio:", bg="#B0E0E6", fg="black")
    label5.place(x=250, y=30)

    premio_StringVar = StringVar()
    premio = Entry(iniciarJuegoPantalla, bg="white", fg="black", textvariable=premio_StringVar, width="25")
    premio.insert(0,"50.000 colones")
    premio.config(state=DISABLED)
    premio.bind("<Button-1>",clickpremio)
    premio.place(x=300,y=30)

    botonIniciarSesion = Button(iniciarJuegoPantalla,text="Iniciar", command=generarFuncion, bg="#20B2AA", fg="black", font=("Finland", 10, 'bold'))
    botonIniciarSesion.place(x=275,y=80)

    botonCerrarAplicacion = Button(iniciarJuegoPantalla,text="Menú Principal", command=regresarFuncion, bg="#E00000", fg="#FFFFFF", font=("Finland", 10,'bold'))
    botonCerrarAplicacion.place(x=130,y=80)

    label6=Label(iniciarJuegoPantalla,text="", bg="#B0E0E6", fg="black")
    label6.place(x=150,y=56)  

    iniciarJuegoPantalla.mainloop()