import numpy as np
from scipy.linalg import solve

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        #print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        


    def agregar_nodo(self, x, y, z=0):	

        #print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos

        self.xyz[numero_de_nodo_actual,:] = [x, y, z]

        self.Nnodos += 1
        
        return 0

    def agregar_barra(self, barra):
        
        self.barras.append(barra)        
        
        return 0

    def obtener_coordenada_nodal(self, n):
                
        return self.xyz[n,:]

    def calcular_peso_total(self):
        
        peso_total = 0

        for barra in self.barras:
            peso_total += barra.calcular_peso(self)
        
        return peso_total

    def obtener_nodos(self):
        
        return self.xyz

    def obtener_barras(self):
        
        return self.barras



    
    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        
        if nodo not in self.restricciones:
            restricciones[nodo] = []

        self.restricciones[nodo].append([gdl, valor])
        
        return None

    def agregar_fuerza(self, nodo, gdl, valor):
        
        if nodo not in self.cargas:
            cargas[nodo] = []

        cargas[nodo].append([gdl, valor])   
        
        return None


    def ensamblar_sistema(self, factor_peso_propio=0.):
        
        #inicializar K y F

        K = np.zeros(3*self.Nnodos+2, 3*self.Nnodos+2)
        F = np.zeros(3*self.Nnodos+2)

        #Ensamblar rigidez y vectores de carga

        for e in self.barras:
            ni = e.ni
            nj = e.nj
            ke = e.obtener_rigidez(self)
            fe = e.obtener_vector_de_cargas(self)

            d = [3*ni, 3*ni+1, 3*ni+2, 3*nj, 3*nj+1, 3*nj+2]

            for i in range(6):
                p = d[i]
                for j in range(6):
                    q = d[j]
                    K[p, q] += ke[i,j]
                    
                if i < 3:
                    F[p] += fe[i] * factor_peso_propio[i]
                else:
                    F[p] += fe[i] * factor_peso_propio[i-3]

        #Agregar cargas puntuales
        
        for nodo in self.cargas:
            for carga in self.cargas[nodo]:
                gdl = carga[0]
                f = carga[1]

                gdl_global = 3*nodo + gdl
                F[gdl_global] += f

        return K, F




    def resolver_sistema(self):
        
        """Implementar"""	
        
        return 0

    def obtener_desplazamiento_nodal(self, n):
        
        """Implementar"""	
        
        return 0


    def obtener_fuerzas(self):
        
        """Implementar"""	
        
        return 0


    def obtener_factores_de_utilizacion(self, f):
        
        """Implementar"""	
        
        return 0

    def rediseñar(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0






    def __str__(self):

        s = "nodos:"  
        s += "\n"
        
        for i in range(self.Nnodos):

            s += str(i) + " : " + str(tuple(self.xyz[0 : self.Nnodos,:][i])) + "\n"

        s += "\n"
        s += "\n"

        s += "barras:"
        s += "\n"

        cont = 0    
        for j in (self.barras):

            s += f"{cont} : [{j.ni}, {j.nj}]\n"
            cont += 1
            
        s += "\n"

        return s
