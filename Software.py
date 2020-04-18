#Autor: Andy (Dino) Martínez Hernández, A01376720
#Ejercicio: calcular costo y descuento al comprar cierta cantidad de producto


#Función para el descuento
def calcularDescuento(paquetes):
    if paquetes>0 and paquetes<=9:
        descuento=0
        return descuento
    elif paquetes>=10 and paquetes<=19:
        descuento= 13
        return descuento
    elif paquetes>=20 and paquetes<=49:
        descuento= 20
        return descuento
    elif paquetes >=50 and paquetes<=99:
        descuento= 32
        return descuento
    elif paquetes >=100:
        descuento= 50
        return
    else:
        return False  #<- Aquí si es 0 o negativo
    

#Función para calcular el precio
def calcularPrecio (paquetes, descuento):
    descuento= calcularDescuento(paquetes)
    precio= paquetes*2300-(2300*descuento/100)
    
    return precio


#función main
def main():
    paquetes= int (input ("Teclea la cantidad de paquetes por adquirir:"))
    descuento= calcularDescuento(paquetes)
    precio= calcularPrecio(paquetes, descuento)
    
    if paquetes<=0:
        print("Error")
    else:
        print ("La cantidad tiene descuento de:", descuento, "%%. Y el precio total es de: $%.02f MXN" % precio)




main()