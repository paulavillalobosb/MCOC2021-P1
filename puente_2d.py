from reticulado import Reticulado
from barra import Barra
from graficar2d import ver_reticulado_2d
from constantes import *
from math import sqrt
from secciones import Circular

L = 2.*m_

#Inicializar modelo
ret = Reticulado()

#Nodos tablero
ret.agregar_nodo(2.343634807564907163e+00 ,4.281724747887941618e+01)#pto 0
ret.agregar_nodo(5.075777986710320100e+00 ,4.281724747887941618e+01-0.130102043139577)#pto 1
ret.agregar_nodo(7.261492147526644736e+00 ,4.281724747887941618e+01-0.130102043139577*2)#pto 2
ret.agregar_nodo(9.447206472271542310e+00 ,4.281724747887941618e+01-0.130102043139577*3)#pto 3
ret.agregar_nodo(1.203126941841552444e+01 ,4.281724747887941618e+01-0.130102043139577*4)#pto 4
ret.agregar_nodo(1.557551065670554635e+01 ,4.281724747887941618e+01-0.130102043139577*5)#pto 5
ret.agregar_nodo(1.987061142983234419e+01 ,4.281724747887941618e+01-0.130102043139577*6)#pto 6
ret.agregar_nodo(2.477708327459076898e+01 ,4.281724747887941618e+01-0.130102043139577*7)#pto 7
ret.agregar_nodo(3.111720940566445037e+01 ,4.281724747887941618e+01-0.130102043139577*8)#pto 8
ret.agregar_nodo(3.873145234877593168e+01 ,4.281724747887941618e+01-0.130102043139577*9)#pto 9
ret.agregar_nodo(4.682869826836961380e+01 ,4.281724747887941618e+01-0.130102043139577*10)#pto10
ret.agregar_nodo(5.443343663273993371e+01 ,4.281724747887941618e+01-0.130102043139577*11)#pto11
ret.agregar_nodo(6.256338958148909768e+01 ,4.281724747887941618e+01-0.130102043139577*12)#pto12
ret.agregar_nodo(6.804476221508502931e+01 ,4.281724747887941618e+01-0.130102043139577*13)#pto13
ret.agregar_nodo(7.403904003641143561e+01 ,4.281724747887941618e+01-0.130102043139577*14)#pto14
ret.agregar_nodo(7.939304016773286321e+01 ,4.281724747887941618e+01-0.130102043139577*15)#pto15
ret.agregar_nodo(8.338472827472728000e+01 ,4.281724747887941618e+01-0.130102043139577*16)#pto16
ret.agregar_nodo(8.840793693585601432e+01 ,4.281724747887941618e+01-0.130102043139577*17)#pto17
ret.agregar_nodo(9.359720524280722032e+01 ,4.281724747887941618e+01-0.130102043139577*18)#pto18
ret.agregar_nodo(1.001543482170419139e+02 ,4.281724747887941618e+01-0.130102043139577*19)#pto19
ret.agregar_nodo(1.078043483536490612e+02 ,4.281724747887941618e+01-0.130102043139577*20)#pto20
ret.agregar_nodo(1.170936342338148819e+02 ,4.008510457294829621e+01)#pto 21

#Nodos Parte superior 
ret.agregar_nodo(5.075777986710320100e+00 ,6.281724747887941618e+01-0.130102043139577)#pto   22
ret.agregar_nodo(7.261492147526644736e+00 ,6.281724747887941618e+01-0.130102043139577*2)#pto 23
ret.agregar_nodo(9.447206472271542310e+00 ,6.281724747887941618e+01-0.130102043139577*3)#pto 24
ret.agregar_nodo(1.203126941841552444e+01 ,6.281724747887941618e+01-0.130102043139577*4)#pto 25
ret.agregar_nodo(1.557551065670554635e+01 ,6.281724747887941618e+01-0.130102043139577*5)#pto 26
ret.agregar_nodo(1.987061142983234419e+01 ,6.281724747887941618e+01-0.130102043139577*6)#pto 27
ret.agregar_nodo(2.477708327459076898e+01 ,6.281724747887941618e+01-0.130102043139577*7)#pto 28
ret.agregar_nodo(3.111720940566445037e+01 ,6.281724747887941618e+01-0.130102043139577*8)#pto 29
ret.agregar_nodo(3.873145234877593168e+01 ,6.281724747887941618e+01-0.130102043139577*9)#pto 30
ret.agregar_nodo(4.682869826836961380e+01 ,6.281724747887941618e+01-0.130102043139577*10)#pto31
ret.agregar_nodo(5.443343663273993371e+01 ,6.281724747887941618e+01-0.130102043139577*11)#pto32
ret.agregar_nodo(6.256338958148909768e+01 ,6.281724747887941618e+01-0.130102043139577*12)#pto33
ret.agregar_nodo(6.804476221508502931e+01 ,6.281724747887941618e+01-0.130102043139577*13)#pto34
ret.agregar_nodo(7.403904003641143561e+01 ,6.281724747887941618e+01-0.130102043139577*14)#pto35
ret.agregar_nodo(7.939304016773286321e+01 ,6.281724747887941618e+01-0.130102043139577*15)#pto36
ret.agregar_nodo(8.338472827472728000e+01 ,6.281724747887941618e+01-0.130102043139577*16)#pto37
ret.agregar_nodo(8.840793693585601432e+01 ,6.281724747887941618e+01-0.130102043139577*17)#pto38
ret.agregar_nodo(9.359720524280722032e+01 ,6.281724747887941618e+01-0.130102043139577*18)#pto39
ret.agregar_nodo(1.001543482170419139e+02 ,6.281724747887941618e+01-0.130102043139577*19)#pto40
ret.agregar_nodo(1.078043483536490612e+02 ,6.281724747887941618e+01-0.130102043139577*20)#pto41

#Secciones de las barras
circular_200_4 = Circular(200*mm_, 4*mm_)
circular_200_8 = Circular(200*mm_, 8*mm_)

#Crear y agregar las barras
ret.agregar_barra(Barra(0, 1, circular_200_4)) #0
ret.agregar_barra(Barra(1, 2, circular_200_4)) #1
ret.agregar_barra(Barra(2, 3, circular_200_4)) #2
ret.agregar_barra(Barra(3, 4, circular_200_4)) #3
ret.agregar_barra(Barra(4, 5, circular_200_4)) #4
ret.agregar_barra(Barra(5, 6, circular_200_4)) #5
ret.agregar_barra(Barra(6, 7, circular_200_4)) #6
ret.agregar_barra(Barra(7, 8, circular_200_4)) #7
ret.agregar_barra(Barra(8, 9, circular_200_4)) #8
ret.agregar_barra(Barra(9, 10, circular_200_4)) #9
ret.agregar_barra(Barra(10, 11, circular_200_4)) #10
ret.agregar_barra(Barra(11, 12, circular_200_4)) #11
ret.agregar_barra(Barra(12, 13, circular_200_4)) #12
ret.agregar_barra(Barra(13, 14, circular_200_4)) #13
ret.agregar_barra(Barra(14, 15, circular_200_4)) #14
ret.agregar_barra(Barra(15, 16, circular_200_4)) #15
ret.agregar_barra(Barra(16, 17, circular_200_4)) #16
ret.agregar_barra(Barra(17, 18, circular_200_4)) #17
ret.agregar_barra(Barra(18, 19, circular_200_4)) #18
ret.agregar_barra(Barra(19, 20, circular_200_4)) #19
ret.agregar_barra(Barra(20, 21, circular_200_4)) #20

ret.agregar_barra(Barra(1, 22, circular_200_4)) #21
#ret.agregar_barra(Barra(2, 23, circular_200_4)) (#22)
#ret.agregar_barra(Barra(3, 24, circular_200_4)) (#23)
ret.agregar_barra(Barra(4, 25, circular_200_4)) #22
#ret.agregar_barra(Barra(5, 26, circular_200_4)) (#25)
ret.agregar_barra(Barra(6, 27, circular_200_4)) #23
ret.agregar_barra(Barra(7, 28, circular_200_4)) #24
ret.agregar_barra(Barra(8, 29, circular_200_4)) #25
ret.agregar_barra(Barra(9, 30, circular_200_4)) #26
ret.agregar_barra(Barra(10, 31, circular_200_4)) #27
ret.agregar_barra(Barra(11, 32, circular_200_4)) #28
ret.agregar_barra(Barra(12, 33, circular_200_4)) #29
ret.agregar_barra(Barra(13, 34, circular_200_4)) #30
ret.agregar_barra(Barra(14, 35, circular_200_4)) #31
ret.agregar_barra(Barra(15, 36, circular_200_4)) #32
ret.agregar_barra(Barra(16, 37, circular_200_4)) #33
ret.agregar_barra(Barra(17, 38, circular_200_4)) #34
ret.agregar_barra(Barra(18, 39, circular_200_4)) #35
ret.agregar_barra(Barra(19, 40, circular_200_4)) #36
ret.agregar_barra(Barra(20, 41, circular_200_4)) #37

ret.agregar_barra(Barra(22, 23, circular_200_4)) #38
ret.agregar_barra(Barra(23, 24, circular_200_4)) #39
ret.agregar_barra(Barra(24, 25, circular_200_4)) #40
ret.agregar_barra(Barra(25, 26, circular_200_4)) #41
ret.agregar_barra(Barra(26, 27, circular_200_4)) #42
ret.agregar_barra(Barra(27, 28, circular_200_4)) #43
ret.agregar_barra(Barra(28, 29, circular_200_4)) #44
ret.agregar_barra(Barra(29, 30, circular_200_4)) #45
ret.agregar_barra(Barra(30, 31, circular_200_4)) #46
ret.agregar_barra(Barra(31, 32, circular_200_4)) #47
ret.agregar_barra(Barra(32, 33, circular_200_4)) #48
ret.agregar_barra(Barra(33, 34, circular_200_4)) #49
ret.agregar_barra(Barra(34, 35, circular_200_4)) #50
ret.agregar_barra(Barra(35, 36, circular_200_4)) #51
ret.agregar_barra(Barra(36, 37, circular_200_4)) #52
ret.agregar_barra(Barra(37, 38, circular_200_4)) #53
ret.agregar_barra(Barra(38, 39, circular_200_4)) #54
ret.agregar_barra(Barra(39, 40, circular_200_4)) #55
ret.agregar_barra(Barra(40, 41, circular_200_4)) #56

ret.agregar_barra(Barra(0, 22, circular_200_4)) #57
ret.agregar_barra(Barra(1, 25, circular_200_4)) #58
ret.agregar_barra(Barra(4, 27, circular_200_4)) #59
ret.agregar_barra(Barra(6, 28, circular_200_4)) #60
ret.agregar_barra(Barra(7, 29, circular_200_4)) #61
ret.agregar_barra(Barra(8, 30, circular_200_4)) #62
ret.agregar_barra(Barra(9, 31, circular_200_4)) #63
ret.agregar_barra(Barra(10, 32, circular_200_4)) #64
ret.agregar_barra(Barra(11, 33, circular_200_4)) #65
ret.agregar_barra(Barra(13, 33, circular_200_4)) #66
ret.agregar_barra(Barra(14, 34, circular_200_4)) #67
ret.agregar_barra(Barra(15, 35, circular_200_4)) #78
ret.agregar_barra(Barra(16, 36, circular_200_4)) #79
ret.agregar_barra(Barra(17, 37, circular_200_4)) #70
ret.agregar_barra(Barra(18, 38, circular_200_4)) #71
ret.agregar_barra(Barra(19, 39, circular_200_4)) #72
ret.agregar_barra(Barra(20, 40, circular_200_4)) #73
ret.agregar_barra(Barra(41, 21, circular_200_4)) #74







#Crear restricciones

#Visualizar y comprobar las secciones
opciones_barras = {
	"ver_secciones_en_barras": True,
}
ver_reticulado_2d(ret,opciones_barras=opciones_barras)

#Resolver el problema
ret.ensamblar_sistema(factor_peso_propio=[0., 0., 0.])
ret.resolver_sistema()
f = ret.obtener_fuerzas()

#Ver todo el reticulado en texto
print(ret)

#Visualizar resultados de fuerzas y nodos 
opciones_nodos = {
	"usar_posicion_deformada": True,
	"factor_amplificacion_deformada": 2e3,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato": f,
	"ver_fuerza_en_barras" : True
}
ver_reticulado_2d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras)