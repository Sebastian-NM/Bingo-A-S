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
import menuPrincipal
import logica as logic
#Fin de Imports



#Inicio variables globales
#graficosMenu (str)
graficosMenu="";
#Fin variables globales



'''
Entradas:
- graficoNumerosCantados
Salidas:
- grafico (graph) 
Restriciones:
- graficoNumerosCantados (graph)
'''
#Algoritmo que genera un gráfico de los numeros cantados 
def graficoTopNumerosCantados():
    logic.graficoNumerosCantados()
#Fin del algoritmo graficoNumerosCantados()



'''
Entradas:
- graficoFrecuenciaConfiguracion
Salidas:
- grafico (graph) 
Restriciones:
- graficoFrecuenciaConfiguracion (graph)
'''
#Algoritmo que genera un gráfico por frecuencia por configuracion 
def graficoFrecuenciaConfiguracion():
    logic.graficoFrecuenciaConfiguracion()
#Fin del algoritmo graficoFrecuenciaConfiguracion()



'''
Entradas:
- graficoFechasConMasPartidas
Salidas:
- grafico (graph) 
Restriciones:
- graficoFechasConMasPartidas (graph)
'''
#Algoritmo que genera un gráfico por fechas con mas partidas
def graficoFechaJugadas():
    logic.graficoFechasConMasPartidas()
#Fin del algoritmo graficoFechasConMasPartidas()



'''
Entradas:
- graficoJugadoresGanadores
Salidas:
- grafico (graph) 
Restriciones:
- graficoJugadoresGanadores (graph)
'''
#Algoritmo que genera un gráfico con los jugadores con mas partidas ganadas 
def graficoJugadoresGanadores():
    logic.graficoJugadoresGanadores()
#Fin del algoritmo graficoJugadoresGanadores()



'''
Entradas:
- graficoClasificacionHorasPartidas
Salidas:
- grafico (graph) 
Restriciones:
- graficoClasificacionHorasPartidas (graph)
'''
#Algoritmo que genera un gráfico de la clasificacion de horas de las partidas
def graficoHorarios():
    logic.graficoClasificacionHorasPartidas()
#Fin del algoritmo graficoClasificacionHorasPartidas()



'''
Entradas:
- graficoTopNumerosContadosPorConfiguracion
Salidas:
- grafico (graph) 
Restriciones:
- graficoTopNumerosContadosPorConfiguracion (graph)
'''
#Algoritmo que genera un gráfico Top de los numeros contados por configuracion
def graficoCantadosConfiguracion():
    logic.graficoTopNumerosContadosPorConfiguracion()
#Fin del algoritmo graficoTopNumerosContadosPorConfiguracion()


'''
Entradas:
- enviarCartonesPantalla
Salidas:
- menuPrincipal (interfaz) 
Restriciones:
- enviarCartonesPantalla (interfaz)
'''
#Algoritmo que abre la interfaz gráfica menuPrincipal  
def regresarMenu():
    global graficosMenu
    #se destruye la interfaz graficosMenu 
    graficosMenu.destroy()
    #se abre la interfaz menuPrincipal
    menuPrincipal.inicio()
#Fin del algoritmo regresarFuncion()



'''
Entradas:
- consultarCartonPantalla
Salidas:
- consultarCartonPantalla (interfaz) 
Restriciones:
- consultarCartonPantalla (interfaz)
'''
#Algoritmo que crea la interfaz grafica 
def inicio():
    global graficosMenu
    #Se inicializa las caracteristicas de la gráfica
    graficosMenu=Tk()
    #Se crea el nombre del banner
    graficosMenu.title("Bingo")
    #Se integra el color del fondo
    graficosMenu.config(bg="white")
    #Se establece que el usuario no puede cambiar el tamaño de la aplicacion
    graficosMenu.resizable(False, False)
    #Se establece las caracteristicas del frame de la aplicación
    window_width  = 368
    window_height  = 340
    #Se establece los parametros para insertar el screen en el centro de la pantalla
    screen_width  = graficosMenu.winfo_screenwidth()
    screen_height  = graficosMenu.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    #Se crea el screen 
    graficosMenu.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    #Se crea una etiqueta label1
    label1=Label(graficosMenu,text="Menú de graficos", bg="white", fg="black")
    label1.place(x=140,y=10)

    #Se crea una etiqueta label2
    label2=Label(graficosMenu,text="Por favor selecione el tipo de grafico que desea ver:", bg="white", fg="black")
    label2.place(x=55,y=30)

    #Se crea el boton numerosCantados
    numerosCantados= Button(graficosMenu,text="Top 10 de números cantados", command=graficoTopNumerosCantados, bg="white", fg="black")
    numerosCantados.place(x=105,y=60)

    #Se crea el boton frecuenciaConfiguracion
    frecuenciaConfiguracion = Button(graficosMenu,text="Frecuencia de configuración de partidas", command=graficoFrecuenciaConfiguracion, bg="white", fg="black")
    frecuenciaConfiguracion.place(x=77,y=100)

    #Se crea el boton fechaJugadas
    fechaJugadas = Button(graficosMenu,text="Top 3 de fecha en que se jugaron más partidas", command=graficoFechaJugadas, bg="white", fg="black")
    fechaJugadas.place(x=55,y=140)

    #Se crea el boton jugadoresGanadores
    jugadoresGanadores = Button(graficosMenu,text="Top 5 de los jugadores que han ganado en más ocasiones", command=graficoJugadoresGanadores, bg="white", fg="black")
    jugadoresGanadores.place(x=30,y=180)

    #Se crea el boton horarios
    horarios = Button(graficosMenu,text="Distribución de horarios donde se ha jugado", command=graficoHorarios, bg="white", fg="black")
    horarios.place(x=60,y=220)

    #Se crea el boton cantadosConfiguracion
    cantadosConfiguracion = Button(graficosMenu,text="Top 10 de números más cantados por configuración de partida", command=graficoCantadosConfiguracion, bg="white", fg="black")
    cantadosConfiguracion.place(x=15,y=260)

    #Se crea el boton segundaOpcion
    segundaOpcion = Button(graficosMenu,text="Menú principal", command=regresarMenu, bg="white", fg="black")
    segundaOpcion.place(x=135,y=300)
    
    #Se crea la pantalla
    graficosMenu.mainloop()
#Fin del algoritmo inicio()


