#Autor: Andy (Dino) Martínez Hernández, A01376720
#Ejercicio: leer dimensiones de 2 rectángulos, calcular perímetro y área y calcular el de mayor área


#Función para calcular el área de cada rectángulo
def calcularArea(A,B,C,D):
    area1= A*B
    area2= C*D
    
    areas= area1, area2
    return areas
    
    
    
#Función para encontar cual area es mayor
def calcularMayor(A,B,C,D):
    area1= A*B
    area2= C*D
    
    if area1>area2:
        return area1
    elif area1<area2:
        return area2
    elif area1==area2:
        return False  #<- Aquí para cuando son iguales
    
        

#Función para calcular el perimetro de cada rectángulo
def calcularPerimetro(A,B,C,D):
    perimetro1= A*2+B*2
    perimetro2= C*2+D*2
    
    perimetros= perimetro1, perimetro2
    
    return perimetros


#Función main para pedir las dimensiones y llamar a las otras funciones
def main():
    A1= int(input("Teclea Base del rectángulo 1 en cm:"))
    A2= int (input("Teclea altura del rectángulo 1 en cm:"))
    
    B1= int (input("Teclea Base del rectángulo 2 en cm:"))
    B2= int (input("Teclea altura del rectángulo 2 en cm:"))
    
    perimetros= calcularPerimetro (A1,A2,B1,B2)
    print ("Los perimetros respectivamente son:", perimetros)
    
    areas= calcularArea (A1,A2,B1,B2)
    areaMayor= calcularMayor(A1,A2,B1,B2)
    
    if areaMayor==False:
        print ("Él área de los rectángulos es el mismo:", areas)
    else:
        print ("las areas respectivamente son:", areas)
        print ("Y el área del rectángulo mayor es de:", areaMayor)
    
        
main()
   