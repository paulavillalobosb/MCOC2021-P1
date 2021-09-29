from h5py._hl import dataset
from matplotlib.pyplot import cla
import numpy as np
import h5py
from scipy.linalg import solve
from secciones import SeccionICHA
from barra import Barra


class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.Nrestricciones = 0
        self.Ncargas = 0
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
            self.restricciones[nodo] = []

        self.restricciones[nodo].append([gdl, valor])
        self.Nrestricciones += 1
        
        return None

    def agregar_fuerza(self, nodo, gdl, valor):
        
        if nodo not in self.cargas:
            self.cargas[nodo] = []

        self.cargas[nodo].append([gdl, valor])
        self.Ncargas += 1   
        
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
        
        fuerzas = np.zeros((len(self.barras)), dtype=np.double)
        for i,b in enumerate(self.barras):
            fuerzas[i] = b.obtener_fuerza(self)

        return fuerzas


    def obtener_factores_de_utilizacion(self, f, ϕ=0.9):
        
        FU = np.zeros((len(self.barras)), dtype=np.double)
        for i,b in enumerate(self.barras):
            FU[i] = b.obtener_factor_utilizacion(f[i], ϕ)

        return FU


    def rediseñar(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        cumple = True
        for i,b in enumerate(self.barras):
            if not b.chequear_diseño(Fu[i], self, ϕ):
                print(f"----> Barra {i} no cumple algun criterio. ")
                cumple = False
        return cumple	
        

    def guardar(self, nombre):

        dataset = h5py.File(nombre, "w")   
        dataset["xyz"] = self.xyz
        barras = np.zeros((len(self.barras),2), dtype= np.int32)
        secciones = np.zeros((len(self.barras),), dtype= h5py.string_dtype())
        restricciones = np.zeros((self.Nrestricciones,2), dtype= np.int32)
        restricciones_val = np.zeros((self.Nrestricciones,1), dtype= np.double)
        cargas = np.zeros((self.Ncargas, 2), dtype=np.int32)
        cargass_val = np.zeros((self.Ncargas,1), dtype= np.double)

        i=0
        for clave in (self.restricciones):
            for valor in (self.restricciones[clave]):
                print(clave)
                restricciones[i,0] = clave
                restricciones[i,1] = valor[0]
                restricciones_val[i,0] = valor[1]
                i+=1
        
        for i,b in enumerate(self.barras):
            barras[i,0] = b.ni
            barras[i,1] = b.nj
            secciones[i] = b.seccion.nombre()

        i=0
        for clave in (self.cargas):
            for valor in (self.cargas[clave]):
                print(clave)
                cargas[i,0] = clave
                cargas[i,1] = valor[0]
                cargass_val[i,0] = valor[1]
                i+=1

        dataset["restricciones"] = restricciones
        dataset["restricciones_val"] = restricciones_val
        dataset["barras"] = barras
        dataset["secciones"] = secciones
        dataset["cargas"] = cargas
        dataset["cargass_val"] = cargass_val
        return 0


    def abrir(self, nombre):

        dataset = h5py.File(nombre, "r")

        xyz = dataset["xyz"]
        barras = dataset["barras"]
        secciones = dataset["secciones"]
        restricciones = dataset["restricciones"]
        restricciones_val = dataset["restricciones_val"]
        cargas = dataset["cargas"]
        cargas_val = dataset["cargas_val"]

        for i in xyz:
            self.agregar_nodo(i[0], i[1], i[2])

        for i in barras:
            B = Barra(i[0],i[1],SeccionICHA(str(secciones[i])))
            self.agregar_barra(B)

        for i in cargas:
            self.agregar_fuerza(int(i[0]),int(i[1]),double(cargas_val[i]))
        
        for i in restricciones:
            self.agregar_restriccion(int(i[0]),int(i[1]),double(restricciones_val[i]))

        dataset.close()




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
