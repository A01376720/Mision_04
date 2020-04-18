#Autor: Andy (Dino) Martínez Hernández, A01376720
#Ejercicio: preguntar que operación se hace a la imagen, hacer esa operacion y mostrar las dos imágenes


#Importar cosas de imagen
from PIL import Image, ImageOps


#Función para importar la imagen
def cargarImagen (archivo):
    imagen= Image.open (archivo)
    return imagen


#Función para sacar el negativo de la imagen
def sacarNegativo(imagen):
    negativo= ImageOps.invert (imagen)
    return negativo
    

#Función para sacar la imagen invertida
def voltearImagen(imagen):
    volteo= ImageOps.flip (imagen)
    return volteo


#función main, para preguntar al usuario
def main():
    imagen= cargarImagen ("Riker.png")
    
    pregunta= input ("La imagen es sorpresa, ¿qué desea hacer con ella? A)Invertir   B)Voltear: ")
    
    invertir= sacarNegativo(imagen)
    voltear= voltearImagen(imagen)
    
    
    if pregunta == "A":
        imagen.show()
        invertir.show()
    elif pregunta == "B":
        imagen.show()
        voltear.show()
    else:
        print ("Esa opción no está disponible. Verifique letra y que esté en mayúscula")        



main()  
