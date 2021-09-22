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


    def obtener_rigidez(self, reticulado):
        
        """Implementar"""
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

        T = np.array([-cosΘx, -cosΘy, cosΘz, -cosΘx, -cosΘy, cosΘz])
        Ke = self.seccion.area()* E_acero/l * T.T @ T
        return Ke

    def obtener_vector_de_cargas(self, reticulado):
        
        """Implementar"""	
        w = self.calcular_peso(reticulado)
        v = np.array([0,0,1,0,0,1]).T

        return -w/2*v


    def obtener_fuerza(self, reticulado):
        
        """Implementar"""	
        
        return 0




    def chequear_diseño(self, Fu, reticulado, ϕ=0.9):
        
        """Implementar"""	
        
        return 0





    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


    def rediseñar(self, Fu, reticulado, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


