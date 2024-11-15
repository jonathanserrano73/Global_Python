import random

class Detector:
    
    def __init__(self,matriz_adn):
        self.matriz_adn=matriz_adn
        self.tamaño=len(matriz_adn)
        self.posicion_mutante=[]
    
    def detectar_mutantes (self):
        if self.detectar_horizontal()==True or self.detectar_vertical()==True or self.detectar_diagonal()==True:
            return True
        else:
            return False
            
    def detectar_horizontal(self):
        for fila_inicio,bases in enumerate(self.matriz_adn):
            contador=0
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
                    
                
    def detectar_vertical(self):
        filas=self.tamaño #son la cantidad de elementos de la matriz
        columnas=len(self.matriz_adn[0]) #La cantidad de bases de el elemento son las columnas
        
        for columna in range(columnas):
            contador_bases=0
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
                
        
    def detectar_diagonal(self):
        filas=self.tamaño
        columnas=len(self.matriz_adn[0])
        '''Revisa si hay repeticiones diagonales de izquierda a derecha'''
        for columna_inicial in range(columnas):
            contador_bases=0
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
            contador_bases=0
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
    
class Mutador:
    
    def __init__(self,matriz_adn,base_nitrogenada,posicion_inicial):
        self.matriz_adn=matriz_adn
        self.base_nitrogenada=base_nitrogenada
        self.posicion_inicial=posicion_inicial
        self.tamaño=len(self.matriz_adn)
    
    def crear_mutante(self):
        pass
    
class Radiacion(Mutador):
    
    def __init__(self,matriz_adn,base_nitrogenada,posicion_inicial,tamaño, orientacion_de_la_mutacion):
        super().__init__(matriz_adn,base_nitrogenada,posicion_inicial, tamaño)
        self.orientacion_de_la_mutacion=orientacion_de_la_mutacion
        
    def crear_mutante(self):
        
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
                        fila_mutada[columna_inicial:columna_inicial+4]=[self.base_nitrogenada]*4
                        self.matriz_adn[fila_inicial]=''.join(fila_mutada)
                    else:
                        raise ValueError ("No hay suficiente espacio en la fila para añadir mutación")
            elif self.orientacion_de_la_mutacion=="V":
                if fila_inicial<self.tamaño and columna_inicial<len(self.matriz_adn[fila_inicial]):
                    
                    if fila_inicial+3 <self.tamaño:
                        for i in range(4):
                            fila_mutada=list(self.matriz_adn[fila_inicial+i])
                            fila_mutada[columna_inicial]=self.base_nitrogenada
                            self.matriz_adn[fila_inicial+i]=''.join(fila_mutada)
                    else:
                        raise ValueError("No hay suficiente espacio en la columna para añadir mutación")
            else:
                raise ValueError ("Error, orientacion no valida, debe ingresar 'H' o 'V'")
            
            return self.matriz_adn
        except ValueError as e:
            print(f"Error {e}")
            return None
        

class Virus(Mutador):
    base_nitrogenada=""
    def __init__(self,matriz_adn, posicion_inicial, base_nitrogenada,tamaño):
        super().__init__(matriz_adn, posicion_inicial, base_nitrogenada, tamaño)
    
    def crear_mutante(self, base_nitrogenada, posicion_inicial):

        try:
            fila_inicial,columna_inicial=posicion_inicial
            
            if not (0<=fila_inicial<self.tamaño and 0<=columna_inicial<len(self.matriz_adn[0])):                        
                raise ValueError("La posicion inicial esta fuera de los limites de la matriz")

            for i in range(self.tamaño):
                fila=fila_inicial+i
                columna=columna_inicial+i
                if fila<self.tamaño or columna<len(self.matriz_adn[0]):
                    raise ValueError("No hay suficiente espacio en la fila o columna para añadir la mutación")
                
                self.matriz_adn[fila][columna]=base_nitrogenada
            return self.matriz_adn        
        except ValueError as e:
            print(f"Error {e}")
            return None

class Sanador(Detector):
   
    def __init__(self, matriz_adn):
        super().__init__(matriz_adn)
        self.lista_bases=['A','G','C','T']
    
    def sanar_mutantes(self):
        if self.detectar_mutantes()==True:
            print("La Secuencia de ADN contiene mutaciones, comienza la curación")
            print("")
            while True:
                self.matriz_adn=[[random.choice(self.lista_bases) for i in range(6)] for i in range(6)]
                if self.detectar_mutantes() == False:
                    print("Secuencia curada con exito")
                    return self.matriz_adn
                else:
                    print("La matriz sigue teniendo mutaciones, generando un nuevo ADN...")
 

