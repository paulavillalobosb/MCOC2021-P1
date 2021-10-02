from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import Circular

L = 5.46428568696429
H = 0.130102043139577
#Inicializar modelo
ret = Reticulado()

#Nodos tablero
ret.agregar_nodo(2.343634807564907163e+00      ,0,4.281724747887941618e+01)     #pto0
ret.agregar_nodo(2.343634807564907163e+00+L    ,0,4.281724747887941618e+01-H)   #pto1
ret.agregar_nodo(2.343634807564907163e+00+L*2  ,0,4.281724747887941618e+01-H*2) #pto2
ret.agregar_nodo(2.343634807564907163e+00+L*3  ,0,4.281724747887941618e+01-H*3) #pto3
ret.agregar_nodo(2.343634807564907163e+00+L*4  ,0,4.281724747887941618e+01-H*4) #pto4
ret.agregar_nodo(2.343634807564907163e+00+L*5  ,0,4.281724747887941618e+01-H*5) #pto5
ret.agregar_nodo(2.343634807564907163e+00+L*6  ,0,4.281724747887941618e+01-H*6) #pto6
ret.agregar_nodo(2.343634807564907163e+00+L*7  ,0,4.281724747887941618e+01-H*7) #pto7
ret.agregar_nodo(2.343634807564907163e+00+L*8  ,0,4.281724747887941618e+01-H*8) #pto8
ret.agregar_nodo(2.343634807564907163e+00+L*9  ,0,4.281724747887941618e+01-H*9) #pto9
ret.agregar_nodo(2.343634807564907163e+00+L*10 ,0,4.281724747887941618e+01-H*10)#pto10
ret.agregar_nodo(2.343634807564907163e+00+L*11 ,0,4.281724747887941618e+01-H*11)#pto11
ret.agregar_nodo(2.343634807564907163e+00+L*12 ,0,4.281724747887941618e+01-H*12)#pto12
ret.agregar_nodo(2.343634807564907163e+00+L*13 ,0,4.281724747887941618e+01-H*13)#pto13
ret.agregar_nodo(2.343634807564907163e+00+L*14 ,0,4.281724747887941618e+01-H*14)#pto14
ret.agregar_nodo(2.343634807564907163e+00+L*15 ,0,4.281724747887941618e+01-H*15)#pto15
ret.agregar_nodo(2.343634807564907163e+00+L*16 ,0,4.281724747887941618e+01-H*16)#pto16
ret.agregar_nodo(2.343634807564907163e+00+L*17 ,0,4.281724747887941618e+01-H*17)#pto17
ret.agregar_nodo(2.343634807564907163e+00+L*18 ,0,4.281724747887941618e+01-H*18)#pto18
ret.agregar_nodo(2.343634807564907163e+00+L*19 ,0,4.281724747887941618e+01-H*19)#pto19
ret.agregar_nodo(2.343634807564907163e+00+L*20 ,0,4.281724747887941618e+01-H*20)#pto20
ret.agregar_nodo(1.170936342338148819e+02      ,0,4.008510457294829621e+01)		#pto21

#Nodos Parte superior 
ret.agregar_nodo(2.343634807564907163e+00+L     ,0,6.281724747887941618e+01-H)   #pto22
ret.agregar_nodo(2.343634807564907163e+00+L*2   ,0,6.281724747887941618e+01-H*2) #pto23
ret.agregar_nodo(2.343634807564907163e+00+L*3   ,0,6.281724747887941618e+01-H*3) #pto24
ret.agregar_nodo(2.343634807564907163e+00+L*4   ,0,6.281724747887941618e+01-H*4) #pto25
ret.agregar_nodo(2.343634807564907163e+00+L*5   ,0,6.281724747887941618e+01-H*5) #pto26
ret.agregar_nodo(2.343634807564907163e+00+L*6   ,0,6.281724747887941618e+01-H*6) #pto27
ret.agregar_nodo(2.343634807564907163e+00+L*7   ,0,6.281724747887941618e+01-H*7) #pto28
ret.agregar_nodo(2.343634807564907163e+00+L*8   ,0,6.281724747887941618e+01-H*8) #pto29
ret.agregar_nodo(2.343634807564907163e+00+L*9   ,0,6.281724747887941618e+01-H*9) #pto30
ret.agregar_nodo(2.343634807564907163e+00+L*10  ,0,6.281724747887941618e+01-H*10)#pto31
ret.agregar_nodo(2.343634807564907163e+00+L*11  ,0,6.281724747887941618e+01-H*11)#pto32
ret.agregar_nodo(2.343634807564907163e+00+L*12  ,0,6.281724747887941618e+01-H*12)#pto33
ret.agregar_nodo(2.343634807564907163e+00+L*13  ,0,6.281724747887941618e+01-H*13)#pto34
ret.agregar_nodo(2.343634807564907163e+00+L*14  ,0,6.281724747887941618e+01-H*14)#pto35
ret.agregar_nodo(2.343634807564907163e+00+L*15  ,0,6.281724747887941618e+01-H*15)#pto36
ret.agregar_nodo(2.343634807564907163e+00+L*16  ,0,6.281724747887941618e+01-H*16)#pto37
ret.agregar_nodo(2.343634807564907163e+00+L*17  ,0,6.281724747887941618e+01-H*17)#pto38
ret.agregar_nodo(2.343634807564907163e+00+L*18  ,0,6.281724747887941618e+01-H*18)#pto39
ret.agregar_nodo(2.343634807564907163e+00+L*19  ,0,6.281724747887941618e+01-H*19)#pto40
ret.agregar_nodo(2.343634807564907163e+00+L*20  ,0,6.281724747887941618e+01-H*20)#pto41

#replica------------------------------------------------------------------------------------------
ret.agregar_nodo(2.343634807564907163e+00      ,4,4.281724747887941618e+01)	   #pto 42
ret.agregar_nodo(2.343634807564907163e+00+L    ,4,4.281724747887941618e+01-H)  #pto 43
ret.agregar_nodo(2.343634807564907163e+00+L*2  ,4,4.281724747887941618e+01-H*2)#pto 44
ret.agregar_nodo(2.343634807564907163e+00+L*3  ,4,4.281724747887941618e+01-H*3)#pto 45
ret.agregar_nodo(2.343634807564907163e+00+L*4  ,4,4.281724747887941618e+01-H*4)#pto 46
ret.agregar_nodo(2.343634807564907163e+00+L*5  ,4,4.281724747887941618e+01-H*5)#pto 47
ret.agregar_nodo(2.343634807564907163e+00+L*6  ,4,4.281724747887941618e+01-H*6)#pto 48
ret.agregar_nodo(2.343634807564907163e+00+L*7  ,4,4.281724747887941618e+01-H*7)#pto 49
ret.agregar_nodo(2.343634807564907163e+00+L*8  ,4,4.281724747887941618e+01-H*8)#pto 50
ret.agregar_nodo(2.343634807564907163e+00+L*9  ,4,4.281724747887941618e+01-H*9)#pto 51
ret.agregar_nodo(2.343634807564907163e+00+L*10 ,4,4.281724747887941618e+01-H*10)#pto52
ret.agregar_nodo(2.343634807564907163e+00+L*11 ,4,4.281724747887941618e+01-H*11)#pto53
ret.agregar_nodo(2.343634807564907163e+00+L*12 ,4,4.281724747887941618e+01-H*12)#pto54
ret.agregar_nodo(2.343634807564907163e+00+L*13 ,4,4.281724747887941618e+01-H*13)#pto55
ret.agregar_nodo(2.343634807564907163e+00+L*14 ,4,4.281724747887941618e+01-H*14)#pto56
ret.agregar_nodo(2.343634807564907163e+00+L*15 ,4,4.281724747887941618e+01-H*15)#pto57
ret.agregar_nodo(2.343634807564907163e+00+L*16 ,4,4.281724747887941618e+01-H*16)#pto58
ret.agregar_nodo(2.343634807564907163e+00+L*17 ,4,4.281724747887941618e+01-H*17)#pto59
ret.agregar_nodo(2.343634807564907163e+00+L*18 ,4,4.281724747887941618e+01-H*18)#pto60
ret.agregar_nodo(2.343634807564907163e+00+L*19 ,4,4.281724747887941618e+01-H*19)#pto61
ret.agregar_nodo(2.343634807564907163e+00+L*20 ,4,4.281724747887941618e+01-H*20)#pto62
ret.agregar_nodo(1.170936342338148819e+02      ,4,4.008510457294829621e+01)		#pto63

#Nodos Parte superior 
ret.agregar_nodo(2.343634807564907163e+00+L ,4,6.281724747887941618e+01-H)     #pto64
ret.agregar_nodo(2.343634807564907163e+00+L*2 ,4,6.281724747887941618e+01-H*2) #pto65
ret.agregar_nodo(2.343634807564907163e+00+L*3 ,4,6.281724747887941618e+01-H*3) #pto66
ret.agregar_nodo(2.343634807564907163e+00+L*4 ,4,6.281724747887941618e+01-H*4) #pto67
ret.agregar_nodo(2.343634807564907163e+00+L*5 ,4,6.281724747887941618e+01-H*5) #pto68
ret.agregar_nodo(2.343634807564907163e+00+L*6 ,4,6.281724747887941618e+01-H*6) #pto69
ret.agregar_nodo(2.343634807564907163e+00+L*7 ,4,6.281724747887941618e+01-H*7) #pto70
ret.agregar_nodo(2.343634807564907163e+00+L*8 ,4,6.281724747887941618e+01-H*8) #pto71
ret.agregar_nodo(2.343634807564907163e+00+L*9 ,4,6.281724747887941618e+01-H*9) #pto72
ret.agregar_nodo(2.343634807564907163e+00+L*10 ,4,6.281724747887941618e+01-H*10)#pto73
ret.agregar_nodo(2.343634807564907163e+00+L*11 ,4,6.281724747887941618e+01-H*11)#pto74
ret.agregar_nodo(2.343634807564907163e+00+L*12 ,4,6.281724747887941618e+01-H*12)#pto75
ret.agregar_nodo(2.343634807564907163e+00+L*13 ,4,6.281724747887941618e+01-H*13)#pto76
ret.agregar_nodo(2.343634807564907163e+00+L*14 ,4,6.281724747887941618e+01-H*14)#pto77
ret.agregar_nodo(2.343634807564907163e+00+L*15 ,4,6.281724747887941618e+01-H*15)#pto78
ret.agregar_nodo(2.343634807564907163e+00+L*16 ,4,6.281724747887941618e+01-H*16)#pto79
ret.agregar_nodo(2.343634807564907163e+00+L*17 ,4,6.281724747887941618e+01-H*17)#pto80
ret.agregar_nodo(2.343634807564907163e+00+L*18 ,4,6.281724747887941618e+01-H*18)#pto81
ret.agregar_nodo(2.343634807564907163e+00+L*19 ,4,6.281724747887941618e+01-H*19)#pto82
ret.agregar_nodo(2.343634807564907163e+00+L*20 ,4,6.281724747887941618e+01-H*20)#pto83

#Secciones de las barras
circular_200_4 = Circular(200*mm_, 4*mm_, color="#3E701D")
circular_200_8 = Circular(200*mm_, 8*mm_, color="#A3500B")

#Crear y agregar las barras
#tablero
ret.agregar_barra(Barra(0, 1, circular_200_4))   #0
ret.agregar_barra(Barra(1, 2, circular_200_4))   #1
ret.agregar_barra(Barra(2, 3, circular_200_4))   #2
ret.agregar_barra(Barra(3, 4, circular_200_4))   #3
ret.agregar_barra(Barra(4, 5, circular_200_4))   #4
ret.agregar_barra(Barra(5, 6, circular_200_4))   #5
ret.agregar_barra(Barra(6, 7, circular_200_4))   #6
ret.agregar_barra(Barra(7, 8, circular_200_4))   #7
ret.agregar_barra(Barra(8, 9, circular_200_4))   #8
ret.agregar_barra(Barra(9, 10, circular_200_4))  #9
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

#union tablero y parte superior
ret.agregar_barra(Barra(1, 22, circular_200_4))  #21
ret.agregar_barra(Barra(2, 23, circular_200_4)) #22)
ret.agregar_barra(Barra(3, 24, circular_200_4)) #23)
ret.agregar_barra(Barra(4, 25, circular_200_4))  #22
ret.agregar_barra(Barra(5, 26, circular_200_4)) #25)
ret.agregar_barra(Barra(6, 27, circular_200_4))  #23
ret.agregar_barra(Barra(7, 28, circular_200_4))  #24
ret.agregar_barra(Barra(8, 29, circular_200_4))  #25
ret.agregar_barra(Barra(9, 30, circular_200_4))  #26
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

#union barras superiores
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

#arriostramineto
ret.agregar_barra(Barra(0, 22, circular_200_4))  #57
ret.agregar_barra(Barra(1, 23, circular_200_4))  #58
ret.agregar_barra(Barra(2, 24, circular_200_4))  #58
ret.agregar_barra(Barra(3, 25, circular_200_4))  #58
ret.agregar_barra(Barra(4, 26, circular_200_4))  #59
ret.agregar_barra(Barra(5, 27, circular_200_4))  #59
ret.agregar_barra(Barra(6, 28, circular_200_4))  #60
ret.agregar_barra(Barra(7, 29, circular_200_4))  #61
ret.agregar_barra(Barra(8, 30, circular_200_4))  #62
ret.agregar_barra(Barra(9, 31, circular_200_4))  #63
ret.agregar_barra(Barra(10, 32, circular_200_4)) #64
ret.agregar_barra(Barra(11, 32, circular_200_4)) #65
ret.agregar_barra(Barra(13, 33, circular_200_4)) #66
ret.agregar_barra(Barra(14, 34, circular_200_4)) #67
ret.agregar_barra(Barra(15, 35, circular_200_4)) #78
ret.agregar_barra(Barra(16, 36, circular_200_4)) #79
ret.agregar_barra(Barra(17, 37, circular_200_4)) #70
ret.agregar_barra(Barra(18, 38, circular_200_4)) #71
ret.agregar_barra(Barra(19, 39, circular_200_4)) #72
ret.agregar_barra(Barra(20, 40, circular_200_4)) #73
ret.agregar_barra(Barra(41, 21, circular_200_4)) #74
ret.agregar_barra(Barra(11, 33, circular_200_4)) #74
ret.agregar_barra(Barra(12, 32, circular_200_4)) #74

#replica------------------------------------------------------------------------
#tablero
ret.agregar_barra(Barra(42, 43, circular_200_4))  #75
ret.agregar_barra(Barra(43, 44, circular_200_4))  #76
ret.agregar_barra(Barra(44, 45, circular_200_4))  #77
ret.agregar_barra(Barra(45, 46, circular_200_4))  #78
ret.agregar_barra(Barra(46, 47, circular_200_4))  #79
ret.agregar_barra(Barra(47, 48, circular_200_4))  #80
ret.agregar_barra(Barra(48, 49, circular_200_4))  #81
ret.agregar_barra(Barra(49, 50, circular_200_4))  #82
ret.agregar_barra(Barra(50, 51, circular_200_4))  #83
ret.agregar_barra(Barra(51, 52, circular_200_4))  #84
ret.agregar_barra(Barra(52, 53, circular_200_4))  #85
ret.agregar_barra(Barra(53, 54, circular_200_4))  #86
ret.agregar_barra(Barra(54, 55, circular_200_4))  #87
ret.agregar_barra(Barra(55, 56, circular_200_4))  #88
ret.agregar_barra(Barra(56, 57, circular_200_4))  #89
ret.agregar_barra(Barra(57, 58, circular_200_4))  #90
ret.agregar_barra(Barra(58, 59, circular_200_4))  #91
ret.agregar_barra(Barra(59, 60, circular_200_4))  #92
ret.agregar_barra(Barra(60, 61, circular_200_4))  #93
ret.agregar_barra(Barra(61, 62, circular_200_4))  #94
ret.agregar_barra(Barra(62, 63, circular_200_4))  #95


#union tablero y parte superior
ret.agregar_barra(Barra(43, 64, circular_200_4)) #96
ret.agregar_barra(Barra(44, 65, circular_200_4)) #22)
ret.agregar_barra(Barra(45, 66, circular_200_4)) #23)
ret.agregar_barra(Barra(46, 67, circular_200_4)) #97
ret.agregar_barra(Barra(47, 68, circular_200_4)) #25)
ret.agregar_barra(Barra(48, 69, circular_200_4)) #98
ret.agregar_barra(Barra(49, 70, circular_200_4)) #99
ret.agregar_barra(Barra(50, 71, circular_200_4)) #100
ret.agregar_barra(Barra(51, 72, circular_200_4)) #101
ret.agregar_barra(Barra(52, 73, circular_200_4)) #102
ret.agregar_barra(Barra(53, 74, circular_200_4)) #103
ret.agregar_barra(Barra(54, 75, circular_200_4)) #104
ret.agregar_barra(Barra(55, 76, circular_200_4)) #105
ret.agregar_barra(Barra(56, 77, circular_200_4)) #106
ret.agregar_barra(Barra(57, 78, circular_200_4)) #107
ret.agregar_barra(Barra(58, 79, circular_200_4)) #108
ret.agregar_barra(Barra(59, 80, circular_200_4)) #109
ret.agregar_barra(Barra(60, 81, circular_200_4)) #110
ret.agregar_barra(Barra(61, 82, circular_200_4)) #111
ret.agregar_barra(Barra(62, 83, circular_200_4)) #112

#union barras superiores
ret.agregar_barra(Barra(64, 65, circular_200_4)) #113
ret.agregar_barra(Barra(65, 66, circular_200_4)) #114
ret.agregar_barra(Barra(66, 67, circular_200_4)) #115
ret.agregar_barra(Barra(67, 68, circular_200_4)) #116
ret.agregar_barra(Barra(68, 69, circular_200_4)) #117
ret.agregar_barra(Barra(69, 70, circular_200_4)) #118
ret.agregar_barra(Barra(70, 71, circular_200_4)) #119
ret.agregar_barra(Barra(71, 72, circular_200_4)) #120
ret.agregar_barra(Barra(72, 73, circular_200_4)) #121
ret.agregar_barra(Barra(73, 74, circular_200_4)) #122
ret.agregar_barra(Barra(74, 75, circular_200_4)) #123
ret.agregar_barra(Barra(75, 76, circular_200_4)) #124
ret.agregar_barra(Barra(76, 77, circular_200_4)) #125
ret.agregar_barra(Barra(77, 78, circular_200_4)) #126
ret.agregar_barra(Barra(78, 79, circular_200_4)) #127
ret.agregar_barra(Barra(79, 80, circular_200_4)) #128
ret.agregar_barra(Barra(80, 81, circular_200_4)) #129
ret.agregar_barra(Barra(81, 82, circular_200_4)) #130
ret.agregar_barra(Barra(82, 83, circular_200_4)) #131

#arriostramineto
ret.agregar_barra(Barra(42, 64, circular_200_4)) #132
ret.agregar_barra(Barra(43, 65, circular_200_4)) #133
ret.agregar_barra(Barra(44, 66, circular_200_4)) #133
ret.agregar_barra(Barra(45, 67, circular_200_4)) #133
ret.agregar_barra(Barra(46, 68, circular_200_4)) #134
ret.agregar_barra(Barra(47, 69, circular_200_4)) #134
ret.agregar_barra(Barra(48, 70, circular_200_4)) #135
ret.agregar_barra(Barra(49, 71, circular_200_4)) #136
ret.agregar_barra(Barra(50, 72, circular_200_4)) #137
ret.agregar_barra(Barra(51, 73, circular_200_4)) #138
ret.agregar_barra(Barra(52, 73, circular_200_4)) #139
ret.agregar_barra(Barra(53, 74, circular_200_4)) #140
ret.agregar_barra(Barra(55, 75, circular_200_4)) #141
ret.agregar_barra(Barra(56, 76, circular_200_4)) #142
ret.agregar_barra(Barra(57, 77, circular_200_4)) #143
ret.agregar_barra(Barra(58, 78, circular_200_4)) #144
ret.agregar_barra(Barra(59, 79, circular_200_4)) #145
ret.agregar_barra(Barra(60, 80, circular_200_4)) #146
ret.agregar_barra(Barra(61, 81, circular_200_4)) #147
ret.agregar_barra(Barra(62, 82, circular_200_4)) #148
ret.agregar_barra(Barra(83, 63, circular_200_4)) #149
ret.agregar_barra(Barra(53, 75, circular_200_4)) #149
ret.agregar_barra(Barra(54, 74, circular_200_4)) #149

#uniones horizontales tablero
ret.agregar_barra(Barra(0,  42, circular_200_4))  #150
ret.agregar_barra(Barra(1,  43, circular_200_4))  #151
ret.agregar_barra(Barra(2,  44, circular_200_4))  #152
ret.agregar_barra(Barra(3,  45, circular_200_4))  #153
ret.agregar_barra(Barra(4,  46, circular_200_4))  #154
ret.agregar_barra(Barra(5,  47, circular_200_4))  #155
ret.agregar_barra(Barra(6,  48, circular_200_4))  #156
ret.agregar_barra(Barra(7,  49, circular_200_4))  #157
ret.agregar_barra(Barra(8,  50, circular_200_4))  #158
ret.agregar_barra(Barra(9,  51, circular_200_4))  #159
ret.agregar_barra(Barra(10, 52, circular_200_4))  #160
ret.agregar_barra(Barra(11, 53, circular_200_4))  #161
ret.agregar_barra(Barra(12, 54, circular_200_4))  #162
ret.agregar_barra(Barra(13, 55, circular_200_4))  #163
ret.agregar_barra(Barra(14, 56, circular_200_4))  #164
ret.agregar_barra(Barra(15, 57, circular_200_4))  #165
ret.agregar_barra(Barra(16, 58, circular_200_4))  #166
ret.agregar_barra(Barra(17, 59, circular_200_4))  #167
ret.agregar_barra(Barra(18, 60, circular_200_4))  #168
ret.agregar_barra(Barra(19, 61, circular_200_4))  #169
ret.agregar_barra(Barra(20, 62, circular_200_4))  #170
ret.agregar_barra(Barra(21, 63, circular_200_4))  #171

#uniones horizontales barras superiores
ret.agregar_barra(Barra(22, 64, circular_200_4)) #172
ret.agregar_barra(Barra(23, 65, circular_200_4)) #173
ret.agregar_barra(Barra(24, 66, circular_200_4)) #174
ret.agregar_barra(Barra(25, 67, circular_200_4)) #175
ret.agregar_barra(Barra(26, 68, circular_200_4)) #176
ret.agregar_barra(Barra(27, 69, circular_200_4)) #177
ret.agregar_barra(Barra(28, 70, circular_200_4)) #178
ret.agregar_barra(Barra(29, 71, circular_200_4)) #179
ret.agregar_barra(Barra(30, 72, circular_200_4)) #180
ret.agregar_barra(Barra(31, 73, circular_200_4)) #181
ret.agregar_barra(Barra(32, 74, circular_200_4)) #182
ret.agregar_barra(Barra(33, 75, circular_200_4)) #183
ret.agregar_barra(Barra(34, 76, circular_200_4)) #184
ret.agregar_barra(Barra(35, 77, circular_200_4)) #185
ret.agregar_barra(Barra(36, 78, circular_200_4)) #186
ret.agregar_barra(Barra(37, 79, circular_200_4)) #187
ret.agregar_barra(Barra(38, 80, circular_200_4)) #188
ret.agregar_barra(Barra(39, 81, circular_200_4)) #189
ret.agregar_barra(Barra(40, 82, circular_200_4)) #190
ret.agregar_barra(Barra(41, 83, circular_200_4)) #191



#Visualizar y comprobar las secciones
opciones_barras = {
	"ver_secciones_en_barras": True,
	"color_barras_por_seccion": True,
}
ver_reticulado_3d(ret,opciones_barras=opciones_barras)




#Resolver el problema
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,0.])
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
	"dato":f
}


ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras)
