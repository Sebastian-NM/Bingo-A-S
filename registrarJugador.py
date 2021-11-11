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
registrarJugadorPantalla=""
nombre=""
cedula=""
correo=""
label6=""


'''
Entradas: pCorreo
Salidas: correo es valido (bool) 
Restriciones: pCorreo (str)
              pCorreo != ""
'''
#Genera un juegador en el sistema
def identificarCorreo(pCorreo):
    if(pCorreo.rfind("@")!=-1):
        return True
    else:
        return False


def generarFuncion():
    global registrarJugadorPantalla
    global nombre
    global cedula
    global correo
    global label6

    nombreText = nombre.get()
    cedulaText = cedula.get()
    correoText = correo.get() 

    if(nombreText!="" and cedulaText!="" and correoText!="" and nombreText!="Ejemplo: Luis Soto" and correoText!="Ejemplo: luis@gmail.com"  and cedulaText!="Ejemplo: 103250410"):
        if(len(cedulaText)==9 and cedulaText.isnumeric()):
            if(identificarCorreo(correoText)):
                if(logic.existeJugador(cedulaText)==False):
                    logic.crearJugador(nombreText,cedulaText,correoText)
                    label6.destroy()
                    label6=Label(registrarJugadorPantalla,text="Se registro un nuevo jugador.", bg="white", fg="black")
                    label6.place(x=100,y=120)
                    
                else:
                    label6.destroy()
                    label6=Label(registrarJugadorPantalla,text="El jugador que se desea guardar ya existe.", bg="white", fg="black")
                    label6.place(x=100,y=120)
            else:
                label6.destroy()
                label6=Label(registrarJugadorPantalla,text="Se digitó un correo que no es valido.", bg="white", fg="black")
                label6.place(x=100,y=120)
        else:
            label6.destroy()
            label6=Label(registrarJugadorPantalla,text="Se digitó una cedula que no es valida.", bg="white", fg="black")
            label6.place(x=100,y=120)
    else:
        label6.destroy()
        label6=Label(registrarJugadorPantalla,text="Falta información por completar.", bg="white", fg="black")
        label6.place(x=100,y=120)


'''
Entradas: enviarCartonesPantalla
Salidas: MP (interfaz) 
Restriciones: enviarCartonesPantalla (interfaz)
'''
#Abre la interfaz gráfica MP  
def regresarFuncion():
    global registrarJugadorPantalla
    registrarJugadorPantalla.destroy()
    MP.inicio()


'''
Entradas: event
Salidas: se borra el contenido de nombre (accion)
Restriciones: event debe tener una interaccion con nombre para su uso (accion)
'''
#Borra el contenido de nombre 
def clickNombre(event):
    nombre.config(state=NORMAL)
    nombre.delete(0,END)


'''
Entradas: event
Salidas: se borra el contenido de cedula (accion)
Restriciones: event debe tener una interaccion con cedula para su uso (accion)
'''
#Borra el contenido de correo 
def clickCedula(event):
    cedula.config(state=NORMAL)
    cedula.delete(0,END)


'''
Entradas: event
Salidas: se borra el contenido de correo (accion)
Restriciones: event debe tener una interaccion con correo para su uso (accion)
'''
#Borra el contenido de correo 
def clickCorreo(event):
    correo.config(state=NORMAL)
    correo.delete(0,END)


'''
Entradas: consultarCartonPantalla
Salidas: consultarCartonPantalla (interfaz) 
Restriciones: consultarCartonPantalla (interfaz)
'''
#Crea la interfaz grafica 
def inicio():
    global registrarJugadorPantalla
    global nombre
    global cedula
    global correo
    global label6

    registrarJugadorPantalla=Tk()
    registrarJugadorPantalla.title("Bingo")
    registrarJugadorPantalla.config(bg="white")
    registrarJugadorPantalla.resizable(False, False)
    window_width  = 366
    window_height  = 180
    screen_width  = registrarJugadorPantalla.winfo_screenwidth()
    screen_height  = registrarJugadorPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    registrarJugadorPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label2=Label(registrarJugadorPantalla,text="Registrar jugador", bg="white", fg="black")
    label2.place(x=130,y=10)

    label3=Label(registrarJugadorPantalla,text="Nombre:", bg="white", fg="black")
    label3.place(x=30,y=30)

    nombre_StringVar = StringVar()
    nombre = Entry(registrarJugadorPantalla, bg="white", fg="black", textvariable=nombre_StringVar, width="38")
    nombre.insert(0,"Ejemplo: Luis Soto")
    nombre.config(state=DISABLED)
    nombre.bind("<Button-1>",clickNombre)
    nombre.place(x=100,y=32)

    label4=Label(registrarJugadorPantalla,text="Cédula:", bg="white", fg="black")
    label4.place(x=30,y=60)

    cedula_StringVar = StringVar()
    cedula = Entry(registrarJugadorPantalla, bg="white", fg="black", textvariable=cedula_StringVar, width="38")
    cedula.insert(0,"Ejemplo: 103250410")
    cedula.config(state=DISABLED)
    cedula.bind("<Button-1>",clickCedula)
    cedula.place(x=100,y=62)
 
    label5=Label(registrarJugadorPantalla,text="Correo:", bg="white", fg="black")
    label5.place(x=30,y=90)

    correo_StringVar = StringVar()
    correo = Entry(registrarJugadorPantalla, bg="white", fg="black", textvariable=correo_StringVar, width="38")
    correo.insert(0,"Ejemplo: luis@gmail.com")
    correo.config(state=DISABLED)
    correo.bind("<Button-1>",clickCorreo)
    correo.place(x=100,y=92)

    botonIniciarSesion = Button(registrarJugadorPantalla,text="Guardar", command=generarFuncion, bg="white", fg="black")
    botonIniciarSesion.place(x=100,y=150)
    
    botonCerrarAplicacion = Button(registrarJugadorPantalla,text="Menu Principal", command=regresarFuncion, bg="white", fg="black")
    botonCerrarAplicacion.place(x=180,y=150)

    label6=Label(registrarJugadorPantalla,text="", bg="white", fg="black")
    label6.place(x=100,y=120)
    
    registrarJugadorPantalla.mainloop()