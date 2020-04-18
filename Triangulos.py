#Autor: Andy (Dino) Martínez Hernández, A01376720
#Ejercicio: leer lados de un triángulo y si si existe clasificarlo por longitud de lados


#Función para determinar si es un triangulo valido
def esValido(A,B,C):
    if A+B>C:
        return True
    elif A+C>B:
        return True
    elif B+C>A:
        return True
    else:
        return False
    
#Función para categorizar que tipo de triangulo es
def categorizarTriangulo(A,B,C):
    
    if A==B and A==C:
        return "Equilátero"
    elif A==B and A!=C:
        return "Isóceles"
    elif A==C and A!=B:
        return "Isóceles"
    elif B==C and B!=A:
        return "Isóceles"
    else:
        return False
        
    

#Función main para comparar los lados a imprimir resultados
def main():
    
    ladoA= int(input( "Teclea la medida del lado A:"))
    ladoB= int(input( "Teclea la medida del lado B:"))
    ladoC=int(input("Teclea la medida del lado C:"))
    
    valido= esValido(ladoA,ladoB,ladoC)
    tipo= categorizarTriangulo (ladoA,ladoB,ladoC)
    
    if valido==True:
        if tipo!=False:
            print ("Este triángulo es un triángulo:", tipo)
        else:
            print ("Este triángulo no es isóceles ni equilátero")
    else:
        print("Estos lados no corresponden a un triángulo")
        
main()