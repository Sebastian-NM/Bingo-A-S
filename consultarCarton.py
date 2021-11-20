'''
Proyecto Programado 02
Tema: Gestor de Bingos
Estudiantes: Angela González Solano, 2021445876
             Sebastián Navarro Martinez, 2021579550
'''

#Importar Librerías
from tkinter import *
from PIL import Image, ImageTk
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
                        label7=Label(consultarCartonPantalla,text="Dueño del cartón: "+str(cartonJugador[1])+" , cédula: "+str(cartonJugador[0])+".", bg="#B0E0E6", fg="black", font=("Finland", 10))
                        label7.place(x=40,y=350)
                    else:
                        label7.destroy()
                        label7=Label(consultarCartonPantalla,text="", bg="#B0E0E6", fg="black", font=("Finland", 10))
                        label7.place(x=40,y=350)
                    
                    label3.destroy()
                    label3=Label(consultarCartonPantalla,text="Se encontró la imagen.", bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
                    label3.place(x=150,y=50)

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
                    label3=Label(consultarCartonPantalla,text="El número de cartón es incorrecto.", bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
                    label3.place(x=120,y=50)
            else:
                label3.destroy()
                label3=Label(consultarCartonPantalla,text="No existen cartones creados en el sistema.", bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
                label3.place(x=65,y=50)
        else:
            label3.destroy()
            label3=Label(consultarCartonPantalla,text="Ingrese un número de cartón válido.", bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
            label3.place(x=105,y=50)
    else:
        label3.destroy()
        label3=Label(consultarCartonPantalla,text="Por favor ingrese el número de cartón a consultar.", bg="#B0E0E6", fg="black", font=("Finland", 10, 'bold'))
        label3.place(x=65,y=50)


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
    consultarCartonPantalla.iconbitmap("bingo.ico")
    consultarCartonPantalla.title("Consultar Cartones")
    consultarCartonPantalla.config(bg="#B0E0E6")
    consultarCartonPantalla.resizable(False, False)
    window_width  = 450
    window_height  = 405
    screen_width  = consultarCartonPantalla.winfo_screenwidth()
    screen_height  = consultarCartonPantalla.winfo_screenheight()
    position_top  = (screen_width /2) - (window_width /2)
    position_right  = (screen_height /2) - (window_height /2)
    consultarCartonPantalla.geometry('%dx%d+%d+%d' % (window_width, window_height, position_top, position_right))
  
    label4=Label(consultarCartonPantalla,text="Ingrese el número de cartón:", fg="black", bg="#B0E0E6", font=("Finland", 10))
    label4.place(x=30,y=20)

    identificacionCartones_StringVar = StringVar()
    
    identificacion = Entry(consultarCartonPantalla, bg="white", fg="black", textvariable=identificacionCartones_StringVar, width="25")
    identificacion.insert(0,"Ejemplo: NCC004")
    identificacion.config(state=DISABLED)
    identificacion.bind("<Button-1>",clickIdentificar)
    identificacion.place(x=205,y=22)

    botonIniciarSesion = Button(consultarCartonPantalla,text="Buscar", command=mostrarCarton, bg="#20B2AA", fg="black", font=("Finland", 10, 'bold'))
    botonIniciarSesion.place(x=380,y=17)

    botonCerrarAplicacion = Button(consultarCartonPantalla,text="Menú Principal", command=regresarFuncion, bg="#E00000", fg="#FFFFFF", font=("Finland", 10,'bold'))
    botonCerrarAplicacion.place(x=176,y=370)
  
    frameImagen = Frame(consultarCartonPantalla, width = 370, height=260);
    frameImagen.place(x="40", y="80");
 
    label3=Label(consultarCartonPantalla,text="", bg="#B0E0E6", fg="black", font=("Finland", 10))
    label3.place(x=40,y=45) 

    label7=Label(consultarCartonPantalla,text="", bg="#B0E0E6", fg="black", font=("Finland", 10))
    label7.place(x=40,y=350)

    consultarCartonPantalla.mainloop()