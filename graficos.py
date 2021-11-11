'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''


#Importar Librerías
from tkinter import *
import menuPrincipal
import logica as logic


#Inicio variables globales
graficosMenu="";


'''
Entradas: graficoNumerosCantados
Salidas: grafico (graph) 
Restriciones: graficoNumerosCantados (graph)
'''
#Genera un gráfico de los numeros cantados 
def graficoTopNumerosCantados():
    logic.graficoNumerosCantados()


'''
Entradas: graficoFrecuenciaConfiguracion
Salidas: grafico (graph) 
Restriciones:
- graficoFrecuenciaConfiguracion (graph)
'''
#Genera un gráfico por frecuencia por configuracion 
def graficoFrecuenciaConfiguracion():
    logic.graficoFrecuenciaConfiguracion()


'''
Entradas: graficoFechasConMasPartidas
Salidas: grafico (graph) 
Restriciones: graficoFechasConMasPartidas (graph)
'''
#Genera un gráfico por fechas con mas partidas
def graficoFechaJugadas():
    logic.graficoFechasConMasPartidas()


'''
Entradas: graficoJugadoresGanadores
Salidas: grafico (graph) 
Restriciones: graficoJugadoresGanadores (graph)
'''
#Genera un gráfico con los jugadores con mas partidas ganadas 
def graficoJugadoresGanadores():
    logic.graficoJugadoresGanadores()


'''
Entradas: graficoClasificacionHorasPartidas
Salidas: grafico (graph) 
Restriciones: graficoClasificacionHorasPartidas (graph)
'''
#Genera un gráfico de la clasificacion de horas de las partidas
def graficoHorarios():
    logic.graficoClasificacionHorasPartidas()


'''
Entradas: graficoTopNumerosContadosPorConfiguracion
Salidas: grafico (graph) 
Restriciones: graficoTopNumerosContadosPorConfiguracion (graph)
'''
#Genera un gráfico Top de los numeros contados por configuracion
def graficoCantadosConfiguracion():
    logic.graficoTopNumerosContadosPorConfiguracion()


'''
Entradas: enviarCartonesPantalla
Salidas: menuPrincipal (interfaz) 
Restriciones: enviarCartonesPantalla (interfaz)
'''
#Abre la interfaz gráfica menuPrincipal  
def regresarMenu():
    global graficosMenu
    graficosMenu.destroy()
    menuPrincipal.inicio()


'''
Entradas: consultarCartonPantalla
Salidas: consultarCartonPantalla (interfaz) 
Restriciones: consultarCartonPantalla (interfaz)
'''
#Crea la interfaz grafica 
def inicio():
    global graficosMenu
    graficosMenu=Tk()
    graficosMenu.title("Bingo")
    graficosMenu.config(bg="white")
    graficosMenu.resizable(False, False)
    window_width  = 368
    window_height  = 340
    screen_width  = graficosMenu.winfo_screenwidth()
    screen_height  = graficosMenu.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    graficosMenu.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label1=Label(graficosMenu,text="Menú de graficos", bg="white", fg="black")
    label1.place(x=140,y=10)

    label2=Label(graficosMenu,text="Por favor selecione el tipo de grafico que desea ver:", bg="white", fg="black")
    label2.place(x=55,y=30)

    numerosCantados= Button(graficosMenu,text="Top 10 de números cantados", command=graficoTopNumerosCantados, bg="white", fg="black")
    numerosCantados.place(x=105,y=60)

    frecuenciaConfiguracion = Button(graficosMenu,text="Frecuencia de configuración de partidas", command=graficoFrecuenciaConfiguracion, bg="white", fg="black")
    frecuenciaConfiguracion.place(x=77,y=100)

    fechaJugadas = Button(graficosMenu,text="Top 3 de fecha en que se jugaron más partidas", command=graficoFechaJugadas, bg="white", fg="black")
    fechaJugadas.place(x=55,y=140)

    jugadoresGanadores = Button(graficosMenu,text="Top 5 de los jugadores que han ganado en más ocasiones", command=graficoJugadoresGanadores, bg="white", fg="black")
    jugadoresGanadores.place(x=30,y=180)

    horarios = Button(graficosMenu,text="Distribución de horarios donde se ha jugado", command=graficoHorarios, bg="white", fg="black")
    horarios.place(x=60,y=220)

    cantadosConfiguracion = Button(graficosMenu,text="Top 10 de números más cantados por configuración de partida", command=graficoCantadosConfiguracion, bg="white", fg="black")
    cantadosConfiguracion.place(x=15,y=260)

    segundaOpcion = Button(graficosMenu,text="Menú principal", command=regresarMenu, bg="white", fg="black")
    segundaOpcion.place(x=135,y=300)
    
    graficosMenu.mainloop()