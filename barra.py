from secciones import Circular
import numpy as np

from constantes import g_, ρ_acero, E_acero
from math import sqrt

class Barra(object):

    """Constructor para una barra"""
    def __init__(self, ni, nj, seccion, color=np.random.rand(3)):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.seccion = seccion
        self.color = color


    def obtener_conectividad(self):
        return [self.ni, self.nj]

    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        ni = self.ni
        nj = self.nj
        xi = reticulado.xyz[ni,:]
        xj = reticulado.xyz[nj,:]

        res = sqrt((xj[0]**2 - xi[0]**2) + (xj[1]**2 - xi[1]**2) + (xj[2]**2 - xi[2]**2))
        return res

    def calcular_peso(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        secc = self.seccion
        l = self.calcular_largo(reticulado)
        peso = secc.peso()
        peso_f = peso * l
        return peso_f


    def T(self, reticulado):
        ni = self.ni
        nj = self.nj
        l = self.calcular_largo(reticulado)
        xi = reticulado.xyz[ni,:]
        xj = reticulado.xyz[nj,:]
        Lx = xj[0] - xi[0]
        Ly = xj[1] - xi[1]
        Lz = xj[2] - xi[2]
        cosΘx = Lx/l
        cosΘy = Ly/l
        cosΘz = Lz/l

        return np.array([-cosΘx, -cosΘy, cosΘz, -cosΘx, -cosΘy, cosΘz])


    def obtener_rigidez(self, reticulado):
        
        """Implementar"""
        ni = self.ni
        nj = self.nj
        l = self.calcular_largo(reticulado)
        T = self.T(reticulado)
        
        Ke = self.seccion.area()* E_acero/l * T.T @ T
        return Ke

    def obtener_vector_de_cargas(self, reticulado):
        
        """Implementar"""	
        w = self.calcular_peso(reticulado)
        v = np.array([0,0,1,0,0,1]).T

        return -w/2*v


    def obtener_fuerza(self, reticulado):
        
        """Implementar"""	
        l = self.calcular_largo(reticulado)
        T = self.T(reticulado)
        ni = self.ni
        nj = self.nj

        d = [3*ni, 3*ni+1, 3*ni+2, 3*nj, 3*nj+1, 3*nj+2]
        u_e = np.zeros(6)
        u = reticulado.resolver_sistema()

        for i in range(6):
            p = d[i]
            u_e[i] += u[p]


        se = self.seccion.area()* E_acero/l * T @ u_e.T

        return se




    def chequear_diseño(self, Fu, reticulado, ϕ=0.9):
        
        area = self.seccion.area()
        peso = self.seccion.peso()
        inercia_xx = self.seccion.inercia_xx()
        inercia_yy = self.seccion.inercia_yy()
        nombre = self.seccion.nombre()
        
        #Resistencia nominal
        Fn = area * σy_acero

        #Revisar resistencia nominal
        if abs(Fu) > ϕ*Fn:
            print(f"Resistencia nominal Fu = {Fu} ϕ*Fn = {ϕ*Fn}")
            return False

        L = self.calcular_largo(ret)

        #Inercia es la minima
        I = min(inercia_xx, inercia_yy)
        i = np.sqrt(I/area)

        #Revisar radio de giro
        if Fu >= 0 and L/i > 300:
            print(f"Esbeltez Fu = {Fu} L/i = {L/i}")
            return False

        #Revisar carga critica de pandeo
        if Fu < 0:  #solo en traccion
            Pcr = np.pi**2*E_acero*I / L**2
            if abs(Fu) > Pcr:
                print(f"Pandeo Fu = {Fu} Pcr = {Pcr}")
                return False
        
        #Si pasa todas las pruebas, estamos bien
        return True
        


    def rediseñar(self, Fu, reticulado, ϕ=0.9):
        
        """Implementar"""	
        




    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        A = self.seccion.area()
        Fn = A * σy_acero

        return abs(Fu) / (ϕ*Fn)


