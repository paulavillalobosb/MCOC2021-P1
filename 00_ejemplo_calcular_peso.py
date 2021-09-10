from reticulado import Reticulado
from barra import Barra
from graficar2d import ver_reticulado_2d
from constantes import *
from secciones import Circular



#Inicializar modelo
ret = Reticulado()

#Nodos
ret.agregar_nodo(0,0)
ret.agregar_nodo(1,0)
ret.agregar_nodo(1,1)

#Seccion
circular_200_40 = Circular(200*mm_, 4*mm_)

#Barras
b1 = Barra(0, 1, circular_200_40)
b2 = Barra(1, 2, circular_200_40)
b3 = Barra(0, 2, circular_200_40)

ret.agregar_barra(b1)
ret.agregar_barra(b2)
ret.agregar_barra(b3)

l1 = b1.calcular_largo(ret)
l2 = b2.calcular_largo(ret)
l3 = b3.calcular_largo(ret)

p0 = b1.calcular_peso(ret)
p1 = b2.calcular_peso(ret)
p2 = b3.calcular_peso(ret)

a1 = circular_200_40.area()
a2 = circular_200_40.area()
a3 = circular_200_40.area()


print (f"largo de la barra 0 = {l1}")
print (f"largo de la barra 1 = {l2}")
print (f"largo de la barra 2 = {l3}")

print ( f"el area de la barra 0 es {a1}")
print ( f"el area de la barra 1 es {a2}")
print ( f"el area de la barra 2 es {a3}")

print (f"el peso de la barra 0 es {p0}")
print (f"el peso de la barra 1 es {p1}")
print (f"el peso de la barra 2 es {p2}")

print(ret)

peso_total = ret.calcular_peso_total()

print(f"peso_total = {peso_total}")

ver_reticulado_2d(ret)
