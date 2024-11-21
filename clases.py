import random

class Detector:
    '''
    Esta clase se encarga de detectar mutaciones en una matriz de ADN
    Un mutante se puede presentar en una secuencia horizontal, vertical,
    diagonal en la matriz que proporsiona el usuario
    '''
    def __init__(self,matriz_adn:list[str]):
        self.matriz_adn=matriz_adn #matriz de ADN mutante
        self.tamaño=len(matriz_adn)  #Tamaño de la matriz
        self.posicion_mutante=[]  # Lista que guardara la posicion de la mutacion
    
            
    def detectar_mutantes (self)-> bool: 
        if self.detectar_horizontal()==True or self.detectar_vertical()==True or self.detectar_diagonal()==True:
            return True
        else:
            return False
            
    def detectar_horizontal(self)-> bool:
        '''Metodo que detecta si hay mutacion en secuencia horizontal revisando fila por fila
        y retorna True si la encuentra'''
        for fila_inicio,bases in enumerate(self.matriz_adn):
            contador=1      #Variable que acumula la cantidad de repeticiones
            base_anterior=None
            for columna_inicio, base in enumerate(bases):
                if base==base_anterior:
                    contador+=1  
                else:
                    contador=1
                base_anterior=base
                if contador >=4:
                    self.posicion_mutante.append((fila_inicio,columna_inicio-3))
                    return True
        return False
                    
                
    def detectar_vertical(self)-> bool:
        '''Metodo que revisa si hay una mutacion en secuencia vertical que revisa por columna en la matriz
        y retorna True si encuentra la mutación'''
        filas=self.tamaño #Cantidad de elementos de la matriz
        columnas=len(self.matriz_adn[0]) #La cantidad de bases de el elemento son las columnas
        
        for columna in range(columnas):
            contador_bases=1
            base_anterior=None
            for fila in range(filas):
                base=self.matriz_adn[fila][columna]
                
                if base == base_anterior:
                    contador_bases+=1
                else:
                    contador_bases=1
            
                if contador_bases>=4:
                    self.posicion_mutante.append((fila-3,columna))
                    return True
        return False
                
        
    def detectar_diagonal(self)-> bool:
        '''Metodo que revisa si hay repeticiones diagonales de izquierda a derecha y
        retora True si encuentra una mutacion'''
        filas=self.tamaño
        columnas=len(self.matriz_adn[0])
        
        for columna_inicial in range(columnas):
            contador_bases=1
            base_anterior=None
            for i in range(filas):
                '''Recorre desde la columna inicial y va pasando a 
                la siguiente columna '''
                if columna_inicial+i < columnas: 
                    base=self.matriz_adn[i][columna_inicial+i]
                    
                    if base==base_anterior:
                        contador_bases+=1
                    else:
                        contador_bases=1
                    base_anterior=base
                    if contador_bases>=4:
                        self.posicion_mutante.append((i-3,columna_inicial))
                        return True
                    
        for columna_inicial in reversed(range(columnas)):
            '''
            Bucle que recorre la lista en reversa para detectar mutante de derecha
            a izquierda y retorna True si encuentra alguna mutación.
            '''
            contador_bases=1
            base_anterior=None
            for i in range(filas):
                if columna_inicial-i>=0:
                    base=self.matriz_adn[i][columna_inicial-i]
                    if base==base_anterior:
                        contador_bases+=1
                    else:
                        contador_bases=1
                    base_anterior=base
                    if contador_bases>=4:
                        self.posicion_mutante.append((i-3,columna_inicial))
                        return True
        return False                    
    
    def imprimir_matriz(self):
        for fila in self.matriz_adn:
            print(fila)
class Mutador:
    '''Clase que se encarga de mutar una matriz de ADN proporcionada por el usuario
    
    Recibe:
    - Matriz de ADN que sera la que va a recibir la mutación,
    - Base nitrogenada que sera la que se repita en la matriz,
    - Posicion donde se insertara la mutación'''
    def __init__(self,matriz_adn:list[str],base_nitrogenada: str,posicion_inicial:tuple[int,int]):
        self.matriz_adn=matriz_adn
        self.base_nitrogenada=base_nitrogenada
        self.posicion_inicial=posicion_inicial
    
    def crear_mutante(self)->list[str]:
        pass
    
    def imprimir_matriz(self):
        for fila in self.matriz_adn:
            print(fila)
class Radiacion(Mutador):
    '''Subclase de Mutador que genera mutaciones en forma horizontal o vertical
    Recibe la orientacion de la mutación que indica si se quiere insertar de manera "H o V" (horizontal o vertical)
    '''
    def __init__(self,matriz_adn:list[str],base_nitrogenada:str,posicion_inicial:tuple[int,int], orientacion_de_la_mutacion:str):
        super().__init__(matriz_adn,base_nitrogenada,posicion_inicial)
        
        self.tamaño=len(matriz_adn)
        self.orientacion_de_la_mutacion=orientacion_de_la_mutacion  #Orientacion en la que se quiere insertar la mutación
        
    def crear_mutante(self)->list[str]:
        
        try:
            fila_inicial,columna_inicial=self.posicion_inicial
            if not (0<=fila_inicial<self.tamaño and 0<=columna_inicial<len(self.matriz_adn[0])):
                raise ValueError("La posicion inicial esta fuera de los limites de la matriz")
            if self.orientacion_de_la_mutacion=="H":
                if fila_inicial<self.tamaño:    
                    '''Revisamos si hay espacio para la mutacion'''
                    if columna_inicial+3 <len(self.matriz_adn[fila_inicial]):
                        fila_mutada=list(self.matriz_adn[fila_inicial])  #convierte la fila en una lista
                        '''Remplaza las bases con la base indicada'''
                        fila_mutada[columna_inicial:columna_inicial+4]=[self.base_nitrogenada]*4    #Introduce la mutación
                        self.matriz_adn[fila_inicial]=''.join(fila_mutada)  #Vuelve a convertir la fila en un String 
                    else:
                        raise ValueError ("No hay suficiente espacio en la fila para añadir mutación")
            elif self.orientacion_de_la_mutacion=="V":
                if fila_inicial<self.tamaño and columna_inicial<len(self.matriz_adn[fila_inicial]):  #Revisa si hay espacio en la matriz para introducir la mutacion
                    
                    if fila_inicial+3 <self.tamaño:
                        for i in range(4):
                            fila_mutada=list(self.matriz_adn[fila_inicial+i])
                            fila_mutada[columna_inicial]=self.base_nitrogenada      #Introduce la mutacion en la columna
                            self.matriz_adn[fila_inicial+i]=''.join(fila_mutada)    #Vuelve a convertir la lista en un string
                    else:
                        raise ValueError("No hay suficiente espacio en la columna para añadir mutación")
            else:
                raise ValueError ("Error, orientacion no valida, debe ingresar 'H' o 'V'")
        
            print("\nADN despues de la mutación")
            return self.matriz_adn
        except ValueError as e:
            print(f"Error {e}")
            return None
        

class Virus(Mutador):
    '''Subclase de Mutador que genera mutantes en secuencia diagonal,
    
    '''
    def __init__(self,matriz_adn:list[str], base_nitrogenada:str, posicion_inicial:tuple[int,int]):
        super().__init__(matriz_adn, base_nitrogenada, posicion_inicial)
        self.tamaño=len(matriz_adn)

    
    def crear_mutante(self):

        try:
            fila_inicial,columna_inicial=self.posicion_inicial
            
            if fila_inicial+3>self.tamaño or columna_inicial+3>len(self.matriz_adn[0]):

                raise ValueError("No hay suficiente espacio en la fila o columna para añadir la mutación")
                

            for i in range(4):
                fila=fila_inicial+i
                columna=columna_inicial+i
                if fila<self.tamaño and columna<len(self.matriz_adn[0]):
                    fila_mutada=list(self.matriz_adn[fila])
                    fila_mutada[columna]=self.base_nitrogenada                
                    self.matriz_adn[fila]=''.join(fila_mutada)
            print("\nADN despues de la mutación")
            return self.matriz_adn        
        except ValueError as e:
            print(f"Error {e}")
            return None

class Sanador(Detector):
    '''Subclase de Detector que sanara las matrices de ADN si presentan alguna mutacion,
    Recibe una matriz mutada, genera una nueva matriz de ADN y la revisa hasta generar una sin ninguna mutación 
    '''
    def __init__(self, matriz_adn:list[str]):
        super().__init__(matriz_adn)
        self.lista_bases=['A','G','C','T']  #bases que se usaran de manera aleatoria para sanar al mutante
    
    def sanar_mutantes(self)->list[str]:
        if self.detectar_mutantes()==True:
            print("\nLa Secuencia de ADN contiene mutaciones, comienza la curación")
            print("")
            while True:
                self.matriz_adn=[''.join(random.choice(self.lista_bases) for i in range(6)) for i in range(6)]
                if self.detectar_mutantes() == False:
                    print("\nSecuencia curada con exito")
                    return self.matriz_adn
                else:
                    print("\nLa matriz sigue teniendo mutaciones, generando un nuevo ADN...")
    def imprimir_matriz(self):
        for fila in self.matriz_adn:
            print(fila)

