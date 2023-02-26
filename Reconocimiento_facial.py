
import tkinter 
import os
import cv2
from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot
import numpy as np 

#================== FUNCION PARA ALMACENAR EL REGISTRO FACIAL ============================

def registro_facial():
    #capturar el rostro
    cap = cv2.VideoCapture(0)  # se elige la camara con la q va hacer la deteccion
    while (True):
        ret,frame = cap.read() # lee el video
        cv2.imshow('registro facial: ', frame) # mostramos el video en pantalla
        if cv2.waitKey(1) == 27:    # cuando oprimamos el boton de 'Escape' rompe el video
            break
    usuario_img = usuario.get()
    cv2.imwrite(usuario_img + '.jpg', frame) #guardar la ultima captura del video como imagen y asignamos el nombre del usuario
    cap.release()               # cerramos 
    cv2.destroyAllWindows()

    usuario_entrada.delete(0, tkinter.END) # Limpiar los text variables
    contra_entrada.delete(0, tkinter.END) 
    tkinter.Label(pantalla1, text= 'Registro Facial Exitoso', fg='green', font=('calibri,11')).pack()

#=================== DETECTAR EL ROSTRO Y EXPORTAR LOS PIXELES ============================

    def reg_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1,y1,ancho, alto = lista_resultados[i] ['box']
            x2,y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i + 1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg, (150,200), interpolation= cv2.INTER_CUBIC) #Guardar la imagen con un tama;o de 150x200
            cv2.imwrite(usuario_img + '.jpg', cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    img = usuario_img + '.jpg'
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    reg_rostro = (img, caras)

#===================== FUNCION PARA ASIGNAR AL BOTON REGISTRO =================================

def registro():
    global usuario #Globalizar las variables para usarlas en otras funciones
    global contra
    global usuario_entrada
    global contra_entrada
    global pantalla1
    pantalla1 = tkinter.Toplevel(pantalla) #esta pantalla es de un nivel superiror a la principal
    pantalla1.title('Registro')
    pantalla1.geometry('300x250') #Asignar el tama;o de la ventana

#================= CREAR LAS ENTRADAS =====================================
    usuario = tkinter.StringVar()
    contra = tkinter.StringVar()

    tkinter.Label(pantalla1, text= 'Registro Facial: Debe de asignar un usuario: ' ).pack()
    tkinter.Label(pantalla1, text= '').pack() # dejamos un poco de espacio
    tkinter.Label(pantalla1, text= 'Usuario *  ').pack() #mostrar en la pantalla 1 el usuario
    usuario_entrada = tkinter.Entry(pantalla1, textvariable= usuario) #crear un texto variable para q el usuario ingrese la informacion
    usuario_entrada.pack()
    tkinter.Label(pantalla1, text= 'Password').pack() # mostrar en la pantalla 1 la password
    contra_entrada = tkinter.Entry(pantalla1, textvariable= contra) #crear un texto variable para que el usuario ingrese la password
    contra_entrada.pack()
    tkinter.Label(pantalla1, text= '').pack() #dejamos un espacio
    tkinter.Button(pantalla1, text= 'Registro Facial', width= 15 , height= 1, command= registro_facial).pack() 


#========================= FUNCION PARA VERIFICAR LOS DATOS INGRESADOS AL LOGIN ===============================================

def verificacion_login():
    log_usuario = verificacion_usuario.get()
    log_contra = verificacion_contra.get()

    usuario_entrada2.delete(0, tkinter.END)
    contra_entrada2.delete(0, tkinter.END)

    lista_archivos = os.listdir() # importar la lista de archivos con la libreria os

    if log_usuario in lista_archivos: # compararemos los archivos con el que nos interesa
        archivo2 = open(log_usuario, 'r') #abrir el archivo en modo lectura 
        verificacion = archivo2.read().splitlines()# leer las lineas dentro dentro del archivo ignirando el resto
        if log_contra in verificacion:
            print('Inicio de sesion Exitosa! ')
            tkinter.Label(pantalla2, text= 'Inicio de sesion Exitosa!! ', fg= 'green', font= ('calibri', 11) ).pack()
        else:
            print('Contrase;a incorrecta, Ingrese de nuevo: ')
            tkinter.Label(pantalla2, text= 'Contrasena incorrecta', fg= 'red', font= ('calibri', 11)).pack()
    else:
        print('Usuario no encontrado')
        tkinter.Label(pantalla2, text= 'Contrasena incorrecto', fg= 'red', font=('calibri', 11) ).pack()

#=========================== FUNCION PARA EL LOGIN FACIAL ===================================================
def login_facial():
#============================ CAPTURAS EL ROSTRO ====================================
    cap = cv2.VideoCapture(0)   #elegir la camara con la que vamos hacer la deteccion
    while (True):
        ret,frame = cap.read()  # leemos el video
        cv2.imshow('login facial', frame) # mostrar el video en pantalla
        if cv2.waitKey(1) == 27: # cuando oprimamos 'escape' rompa el video
            break
    usuario_login = verificacion_usuario.get() # con esta variaable vamos a guardar la foto pero con otro nombre para no sobreescribir
    cv2.imwrite(usuario_login + 'LOG.jpg',frame) #guardar la ultima captura del video como imagen y asignar el nombre del usuario
    cap.release() # cerramos
    cv2.destroyAllWindows()

    usuario_entrada2.delete(0, tkinter.END) # limpiamos los text variables 
    contra_entrada2.delete(0, tkinter.END)

#=========================== FUNCION PARA GUARDAR EL ROSTRO ==============================================

    def log_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1, y1, ancho, alto = lista_resultados[i]['box']
            x2, y2 = x1 + ancho, y1 + alto 
            pyplot.subplot(1, len(lista_resultados), i + 1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg, (150,200), interpolation= cv2.INTER_CUBIC) #guardamos la imagen 150x200
            cv2.imwrite(usuario_login + 'LOG.jpg', cara_reg)
            return pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

#======================= DETECTAMOS EL ROSTRO ===================================================

    img = usuario_login + 'LOG.jpg'
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    log_rostro(img, caras)

#============================ FUNCION PARA COMPARAR LOS ROSTROS ===============================

    def orb_sim(img1, img2):
        orb = cv2.ORB_create()  # Crear el objeto de comparacion 

        kpa, descr_a = orb.detectAndCompute(img1, None) # crear descriptor 1 y extraemos puntos claves 
        kpa, descr_b = orb.detectAndCompute(img2, None) # crear descriptor 2 y extraemos puntos claves

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)  #creamos comparador de fuerza

        matches = comp.match(descr_a, descr_b) # aplicamos el comparador a los descriptores 

        regiones_similares = [i for i in matches if i.distance < 70 ] # extraemos los registros similares en base a los puntos claves
        if len(matches) == 0:
            return 0
        return len(regiones_similares)/len(matches) # exportamos el porcentaje de similitud

#===================== IMPORTAMOS LAS IMAGENES Y LLAMAMOS A LA FUNCION DE COMPARACION =================================

    im_archivos = os.listdir() # importar la lista de archivos con la libreria os
    if usuario_login + '.jpg' in im_archivos: #comparar los archivos con l que nos interesa
        rostro_reg = cv2.imread(usuario_login + '.jpg', 0) # importar el rostro del registro  # el 0 significa en escalas de grises
        rostro_log = cv2.imread(usuario_login + 'LOG.jpg', 0) # importar el rostro del inicio de sesion
        similitud = orb_sim(rostro_reg, rostro_log) 
        if similitud >= 0.9:
            tkinter.Label(pantalla2, text= 'Inicio de sesion Exitoso! ', fg= 'green', font= ('calibri', 11)).pack()
            print('Bienvenido al Sistema Usuario: ', usuario_login)
            print('Compatibilidad con la foto del registro: ', similitud)
        else:
            print('Rostro Incorrecto, Certifique su Usuario.')
            print('Compatibilidad con la foto del registro: ', similitud)
            tkinter.Label(pantalla2, text= 'Incompatibilidad de Rostros', fg= 'red', font= ('calibri', 11)).pack()

    else:
        print('Usuario no encontrado')
        tkinter.Label(pantalla2, text= 'Usuario no encontrado', fg= 'red', font= ('calibri', 11)).pack()

#======================= FUNCION QUE ASIGNAREMOS AL BOTON LOGIN ==========================
def login():
    global pantalla2
    global verificacion_usuario
    global verificacion_contra
    global usuario_entrada2
    global contra_entrada2

    pantalla2 = tkinter.Toplevel(pantalla)
    pantalla2.title('Login')
    pantalla2.geometry('300x250') # crear la ventana
    tkinter.Label(pantalla2, text= 'Login Facial: debe de asignar un usuario.').pack()
    tkinter.Label(pantalla2, text= 'Login Tradicional: debe de asignar un usuario y contrasena.').pack()
    tkinter.Label(pantalla2, text= '') # dejamos un pococ de espacio

    verificacion_usuario = tkinter.StringVar()
    verificacion_contra = tkinter.StringVar()

#========================== INGRESAMOS LOS DATOS ==========================================

    tkinter.Label(pantalla2, text= 'Usuario * ').pack()
    usuario_entrada2 = tkinter.Entry(pantalla2, textvariable= verificacion_usuario)
    usuario_entrada2.pack()
    tkinter.Label(pantalla2, text= 'Contrasena * ').pack()
    contra_entrada2 = tkinter.Entry(pantalla2, textvariable= verificacion_contra)
    contra_entrada2.pack()
    tkinter.Label(pantalla2, text= '').pack()
    tkinter.Button(pantalla2, text= 'Inicio de sesion tradicional', width= 20, height= 1, command= verificacion_login).pack()

#======================== CREAR EL BOTON PARA HACER EL LOGIN FACIAL ===============================================
    tkinter.Label(pantalla2, text= '').pack()
    tkinter.Button(pantalla2, text= 'Inicio de sesion Facial', width= 20, height=1, command= login_facial).pack()

#========================== FUNCION DE NUESTRA PANTALLA PRINCIPAL ==================================================

def pantalla_principal():
    global pantalla   # globalizamos la variable para usarla en otras funcionaes
    pantalla = tkinter.Tk()
    pantalla.geometry('300x250') # asignar el tamano de la ventana
    pantalla.title('Login con reconocimiento facial') # asignar el titulo de la pantalla
    tkinter.Label(text= 'Login Inteligente', bg= 'gray', width= '300', height= '2', font= ('verdana', 13)).pack() # asignamos caracteristicas a la ventana

#==================== CREAR LOS BOTONES ==========================================

    tkinter.Label(text= '').pack() # crear un espacio entre el titulo y el boton
    tkinter.Button(text= 'Inicio sesion', height= '2', width= '30', command= login).pack() 
    tkinter.Label(text= '').pack() #crear un espacio entre el primer botton y el segundo
    tkinter.Button(text= 'Registro', height= '2', width= '30', command= registro).pack()

    pantalla.mainloop()

pantalla_principal()

# la foto [ '.jpg' ] = es la foto original. y [ 'LOG.JPG' ] es la foto con la q el usuario va a iniciar sesion. 
# necesitamos dos fotos para comparar.

# tamb: para hacer la comparacion de las dos fotos tienen que ser del mismo tamano, en este caso de 150,200.