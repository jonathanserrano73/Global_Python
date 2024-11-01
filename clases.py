class Detector:
    bases_nitrogenadas=["A","T","C","G"]
    
    def __init__(self,matriz_adn):
        self.matriz_adn=matriz_adn
        self.tamaño=len(matriz_adn)
    
    def detectar_mutantes (self):
        for bases in self.matriz_adn:
            for base in bases:
                pass
                
            
    def detectar_horizontal(self):
        for bases in self.matriz_adn:
            contador=0
            base_anterior=None
            for base in bases:
                if base==base_anterior:
                    contador+=1  
                else:
                    contador=1
                base_anterior=base
                if contador >=4:
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
                
                if base in base_anterior:
                    contador_bases+=1
                else:
                    contador_bases=1
            
                if contador_bases>=4:
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
                        return True
                    else:
                        return False
                    
        for columna_inicial in reversed(len(columnas)):
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
                        return True
                    else:
                        return False                    
    
class Mutador:
    base_nitrogenada=""
    def __init__(self):
        pass
    
    def crear_mutante(self):
        pass
    
class Radiacion(Mutador):
    base_nitrogenada=""
    
    def __init__(self):
        pass
    def crear_mutante(self, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        pass

class Virus(Mutador):
    base_nitrogenada=""
    def __init__(self):
        pass
    
    def crear_mutante(self, base_nitrogenada, posicion_inicial):
        pass

class Sanador:
    
    def __init__(self):
        pass
    
    def sanar_mutantes(self):
        pass