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
        largo = self.calcular_largo(reticulado)
        peso = secc.peso()
        peso_f = peso * largo
        return peso_f


    def obtener_rigidez(self, ret):
        
        """Implementar"""	
        
        return 0

    def obtener_vector_de_cargas(self, ret):
        
        """Implementar"""	
        
        return 0


    def obtener_fuerza(self, ret):
        
        """Implementar"""	
        
        return 0




    def chequear_diseño(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0





    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


    def rediseñar(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


