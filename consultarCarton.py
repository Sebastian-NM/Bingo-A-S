'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''

#Importar Librerías
from tkinter import *
from PIL  import Image, ImageTk
import menuPrincipal as MP
import logica as logic


#Inicio variables globales
consultarCartonPantalla="";
identificacion=""
imagenCarton=""
frameImagen=""
label3=""
label7=""


'''
Entradas: identificacionText
Salidas: carton (img) 
Restriciones: identificacionText (str)
              identificacionText !=""
'''
#Muestra el carton solicitado
def mostrarCarton():
    global consultarCartonPantalla
    global identificacion
    global frameImagen
    global label3
    global label7
    
    identificacionText = identificacion.get()    
    
    if(identificacionText!="" and identificacionText!="Ejemplo: NCC004" ):
        if(len(identificacionText)==6):
            if(logic.existeCarpetaCartones()):
                if(logic.existeImagenEnCarpeta(identificacionText)):
                    if(logic.identificarJugadorConCarton(identificacionText)):
                        cartonJugador = logic.extraerIdentificadorJugadorConCarton(identificacionText)
                        label7.destroy()
                        label7=Label(consultarCartonPantalla,text="Dueño del carton: "+str(cartonJugador[1])+" ,cedula: "+str(cartonJugador[0])+".", bg="white", fg="black")
                        label7.place(x=40,y=350)
                    else:
                        label7.destroy()
                        label7=Label(consultarCartonPantalla,text="", bg="white", fg="black")
                        label7.place(x=40,y=350)
                    
                    label3.destroy()
                    label3=Label(consultarCartonPantalla,text="Se encontró la imagen.", bg="white", fg="black")
                    label3.place(x=50,y=60)

                    frameImagen.destroy()

                    frameImagen = Frame(consultarCartonPantalla, width = 350, height=260)
                    frameImagen.place(x="40", y="80")

                    img = Image.open('cartones/'+identificacionText+'.png')
                    img = img.resize((354, 270), Image.BICUBIC)
                    tkimage = ImageTk.PhotoImage(img)
                    labelImage= Label(frameImagen, image=tkimage, width=350, height=260).pack()
                    consultarCartonPantalla.mainloop()
                else:
                    label3.destroy()
                    label3=Label(consultarCartonPantalla,text="El cartón que desea consultar no existe.", bg="white", fg="black")
                    label3.place(x=50,y=60)
            else:
                label3.destroy()
                label3=Label(consultarCartonPantalla,text="No es posible enontrar el carton debido a que no se an creado cartones.", bg="white", fg="black")
                label3.place(x=50,y=60)
        else:
            label3.destroy()
            label3=Label(consultarCartonPantalla,text="Se ingreso una identificación que no es valida.", bg="white", fg="black")
            label3.place(x=50,y=60)
    else:
        label3.destroy()
        label3=Label(consultarCartonPantalla,text="No se digitó nada, por favor intentelo de nuevo.", bg="white", fg="black")
        label3.place(x=50,y=60)


'''
Entradas: menuPrincipal
Salidas: MP (interfaz) 
Restriciones: menuPrincipal (interfaz)
'''
#Abre la interfaz gráfica MP
def regresarFuncion():
    global consultarCartonPantalla
    consultarCartonPantalla.destroy()
    MP.inicio()


'''
Entradas: event
Salidas: se borra el contenido de identificacion (accion)
Restriciones: event debe tener una interaccion con identificación para su uso (accion)
'''
#Borra el contenido de identificación
def clickIdentificar(event):
    identificacion.config(state=NORMAL)
    identificacion.delete(0,END)


'''
Entradas: consultarCartonPantalla
Salidas: consultarCartonPantalla (interfaz) 
Restriciones: consultarCartonPantalla (interfaz)
'''
#Creación de la interfaz grafica de consultar cartón
def inicio():
    global consultarCartonPantalla
    global identificacion
    global frameImagen
    global label3
    global label7

    consultarCartonPantalla=Tk()
    consultarCartonPantalla.title("Bingo")
    consultarCartonPantalla.config(bg="white")
    consultarCartonPantalla.resizable(False, False)
    window_width  = 450
    window_height  = 405
    screen_width  = consultarCartonPantalla.winfo_screenwidth()
    screen_height  = consultarCartonPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    consultarCartonPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))

    label2=Label(consultarCartonPantalla,text="Consultar Cartones", bg="white", fg="black")
    label2.place(x=20,y=5)
  
    label4=Label(consultarCartonPantalla,text="Identificación:", bg="white", fg="black")
    label4.place(x=30,y=30)

    identificacionCartones_StringVar = StringVar()
    
    identificacion = Entry(consultarCartonPantalla, bg="white", fg="black", textvariable=identificacionCartones_StringVar, width="25")
    identificacion.insert(0,"Ejemplo: NCC004")
    identificacion.config(state=DISABLED)
    identificacion.bind("<Button-1>",clickIdentificar)
    identificacion.place(x=120,y=32)

    botonIniciarSesion = Button(consultarCartonPantalla,text="Mostrar", command=mostrarCarton, bg="white", fg="black")
    botonIniciarSesion.place(x=380,y=30)

    botonCerrarAplicacion = Button(consultarCartonPantalla,text="Regresar", command=regresarFuncion, bg="white", fg="black")
    botonCerrarAplicacion.place(x=376,y=370)
  
    frameImagen = Frame(consultarCartonPantalla, width = 370, height=260);
    frameImagen.place(x="40", y="80");
 
    label3=Label(consultarCartonPantalla,text="", bg="white", fg="black")
    label3.place(x=50,y=60)

    label7=Label(consultarCartonPantalla,text="", bg="white", fg="black")
    label7.place(x=40,y=350)

    consultarCartonPantalla.mainloop()