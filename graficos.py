'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''


# Importar Librerías
from tkinter import *
import menuPrincipal
import logica as logic


# Inicio variables globales
graficosMenu = ""


'''
Entradas: graficoNumerosCantados
Salidas: grafico (graph) 
Restriciones: graficoNumerosCantados (graph)
'''
# Genera un gráfico de los numeros cantados


def graficoTopNumerosCantados():
    logic.graficoNumerosCantados()


'''
Entradas: graficoFrecuenciaConfiguracion
Salidas: grafico (graph) 
Restriciones:
- graficoFrecuenciaConfiguracion (graph)
'''
# Genera un gráfico por frecuencia por configuracion


def graficoFrecuenciaConfiguracion():
    logic.graficoFrecuenciaConfiguracion()


'''
Entradas: enviarCartonesPantalla
Salidas: menuPrincipal (interfaz) 
Restriciones: enviarCartonesPantalla (interfaz)
'''
# Abre la interfaz gráfica menuPrincipal


def regresarMenu():
    global graficosMenu
    graficosMenu.destroy()
    menuPrincipal.inicio()


'''
Entradas: consultarCartonPantalla
Salidas: consultarCartonPantalla (interfaz) 
Restriciones: consultarCartonPantalla (interfaz)
'''
# Crea la interfaz grafica


def inicio():
    global graficosMenu
    graficosMenu = Tk()
    graficosMenu.iconbitmap("bingo.ico")
    graficosMenu.title("Estadísticas - Gráficos")
    graficosMenu.config(bg="#B0E0E6")
    graficosMenu.resizable(False, False)
    window_width = 385
    window_height = 200
    screen_width = graficosMenu.winfo_screenwidth()
    screen_height = graficosMenu.winfo_screenheight()
    position_top = (screen_width / 2) - (window_width / 2)
    position_right = (screen_height / 2) - (window_height / 2)
    graficosMenu.geometry('%dx%d+%d+%d' % (window_width,
                          window_height, position_top, position_right))

    label2 = Label(
        graficosMenu, text="Por favor selecione el tipo de grafico que desea ver:", bg="#B0E0E6", font=("Finland", 10, 'bold'))
    label2.place(x=20, y=30)

    numerosCantados = Button(graficosMenu, text="Top 10 de números cantados",
                             command=graficoTopNumerosCantados, bg="#20B2AA", font=("Finland", 10))
    numerosCantados.place(x=105, y=60)

    frecuenciaConfiguracion = Button(graficosMenu, text="Frecuencia de configuración de partidas",
                                     command=graficoFrecuenciaConfiguracion, bg="#20B2AA", font=("Finland", 10))
    frecuenciaConfiguracion.place(x=77, y=100)

    segundaOpcion = Button(graficosMenu, text="Menú principal",
                           command=regresarMenu, bg="#E00000", fg="#FFFFFF", font=("Finland", 10, 'bold'))
    segundaOpcion.place(x=135, y=150)

    graficosMenu.mainloop()
