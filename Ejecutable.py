from clases import Detector, Radiacion, Virus, Sanador


def menu_opciones():
    print("\n Bienvenido, ¿Qué acción desea realizar?")
    print("1: Detectar mutantes \n2: Mutar ADN \n3: Sanar ADN \n4: Salir ")

def matriz_adn_usuario():
    print("Ingrese una secuencia de ADN ")
    print("\nDebe ser de 6 bases (A, C, T, G) \nPor ejemplo: ACGGTA") 
    matriz_adn=[]
    
    for i in range(6):
        while True:
            fila= input(f"Ingrese la fila {i+1}: ")
            if (fila=='A' or 'C' or 'G' or 'T')and len(fila)==6:
                matriz_adn.append(fila)
                break
            else:
                print("Error, la fila debe tener 6 bases y deben ser las bases 'A', 'C', 'G' o 'T' ")
         
    return matriz_adn

def detectar_mutacion(matriz_adn):
    
    detector=Detector(matriz_adn)
    if detector.detectar_mutantes():
        print("\nSe detectaron mutaciones en el ADN")
    else:
        print("\nNo se ha detectado ninguna mutación")
    detector.imprimir_matriz()
    
def mutar_adn(matriz_adn):
    
    print("\nSeleccione una opcion para mutar el ADN")
    print("1: Mutacion Horizontal \n2: Mutacion Vertical \n3: Mutación Diagonal" )
    opcion= int(input("Ingresa tu opción: "))
    base_nitrogenada =input ("Ingresa la base que deseas que se repita (A, T, C, G)").upper()
    fila= int(input("Ingresa la fila inicial donde insertar la mutación (0-5)"))
    col=int(input("Ingresa la columna inicial donde insertar la mutación (0-5)"))
    
    mutador=None
    if opcion==1:
        mutador=Radiacion(matriz_adn, base_nitrogenada, (fila,col), "H")
    elif opcion==2:
        mutador=Radiacion(matriz_adn,base_nitrogenada, (fila,col), "V")
    elif opcion==3:
        mutador=Virus(matriz_adn,base_nitrogenada,(fila,col))
    else:
        print("Opcion no valida. Por favor ingreese (1, 2 o 3)")
        return matriz_adn 
    if mutador:
        matriz_mutada=mutador.crear_mutante()
        
        mutador.imprimir_matriz()
        return matriz_mutada

def sanar_adn(matriz_adn):
    sanador=Sanador(matriz_adn)
    matriz_sanada=sanador.sanar_mutantes()
    if matriz_sanada:
        print("\nADN sanado:")
        sanador.imprimir_matriz()
    return matriz_sanada

def main():
    matriz_adn=matriz_adn_usuario()
    
    while True:
        menu_opciones()
        opcion=int(input("\nSelecccione una opción: "))
        
        if opcion==1:
            detectar_mutacion(matriz_adn)
        elif opcion==2:
            matriz_adn=mutar_adn(matriz_adn)
        elif opcion==3:
            matriz_adn=sanar_adn(matriz_adn)
        elif opcion==4:
            break
        else:
            print("\nSeleccione una opción valida")
        
        continuar= input("\n¿Desea realizar otra acción: (S/N)").strip().upper()
        if continuar == 'N':
            break

if __name__=='__main__':
    main()
        