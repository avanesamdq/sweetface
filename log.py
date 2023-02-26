
import tkinter
from Reconocimiento_facial_copy import usuario, contra, usuario_entrada, contra_entrada, pantalla1

# ========== funcion que se encargara de registrar al Usuario ========

def registrar_usuario():
    usuario_info = usuario.get() #obtener la informacion almacenada en usuario
    contra_info = contra.get() # la informacion almacenada en contra

    archivo = open(usuario_info, 'w') #abrir la informacion en modo escritura
    archivo.write(usuario_info + '\n') #escribir la informacion
    archivo.write(contra_info)
    archivo.close()

    # Limpiar los text variables 
    usuario_entrada.delete(0, tkinter.END)
    contra_entrada.delete(0, tkinter.END)

    # informar al usuario que su registro fue exitoso
    tkinter.Label(pantalla1, text= "Registro Convencional Exitoso ", fg= 'green', font= ('calibri', 11 )).pack()














