# Inicializa una lista vacía para almacenar los números complejos
numeros_complejos = []

continuar = True


while continuar:
    try:
        # Qy=ue ingrese la parte real del número complejo siono
        real = float(input("Ingrese la parte real: "))
        
        
        imag = float(input("Ingrese la parte imaginaria: "))
        
        # Crea un número complejo a partir de la parte real e imaginaria que usted ponga
        numero_complejo = complex(real, imag)
        
     
        numeros_complejos.append(numero_complejo)
    
    except ValueError:
        # Manager del error por si pones un caracter q nada qver vd
        print("Nonono, lo que sea menos eso.")
    
    
    respuesta = input("¿Desea ingresar otro número complejo? (N = No, S = Si): ")
    
    
    if respuesta.upper() == 'N':
        continuar = False


print("Los números complejos son:")
for numero_complejo in numeros_complejos:
    print(numero_complejo)
    
    #Por cierto, Esto es muy bobo, lo odioo nadie va a leer este mensaje de seguro muejejejeje
