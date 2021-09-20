from numpy import pi, sqrt, nan
from numpy.random import rand
from constantes import g_, ρ_acero, mm_
import pandas as pd
 
class Circular(object):
    """define una seccion Circular"""

    def __init__(self, D, Dint, color=rand(3)):
        super(Circular, self).__init__()
        self.D = D
        self.Dint = Dint
        self.color = color  #color para la seccion

    def area(self):
        return pi*(self.D**2 - self.Dint**2)/4

    def peso(self):
        return self.area()*ρ_acero*g_

    def inercia_xx(self):
        return pi*(self.D**4 - self.Dint**4)/4

    def inercia_yy(self):
        return self.inercia_xx()

    def nombre(self):
        return f"O{self.D*1e3:.0f}x{self.Dint*1e3:.0f}"

    def __str__(self):
        return f"Seccion Circular {self.nombre()}"


        
#Mas adelante, no es para P1E1

class SeccionICHA(object):
    """Lee la tabla ICHA y genera una seccion apropiada"""

    def __init__(self, denominacion, base_datos="Perfiles ICHA.xlsx", debug=False, color=rand(3)):
        super(SeccionICHA, self).__init__()
        self.denominacion = denominacion
        self.color = color  #color para la seccion
        self.base_datos=base_datos
        #datos = pd.read_excel(base_datos, engine="openpyxl", )
        
    def leer(self):
        denominacion= self.denominacion
        base_datos= self.base_datos
        if denominacion.find("HR") != -1:
            denominacion1=denominacion.replace("HR","x")
            denominacion2=denominacion1.split("x")
            denominacion2.pop(0)
            denominacion3=[]
            for n in denominacion2:
                denominacion3.append(float(n))
            tabla=pd.read_excel(base_datos,engine="openpyxl",sheet_name="HR",header=0,skiprows=11)
            df=pd.DataFrame(tabla)
            for i in range(0,len(df)+1):
                if df.loc[i,"d"]==denominacion3[0] and df.loc[i,"bf"]==denominacion3[1] and df.loc[i,"peso"]==denominacion3[2]:
                    Area = df.loc[i,"A"]/10**6
                    peso = df.loc[i,"peso"]
                    Ixx = df.loc[i,"Ix/10⁶"]*10**6
                    Iyy = df.loc[i,"Iy/10⁶"]*10**6
                    return f"Tipo de seccion {denominacion} encontrada. A={Area} Ixx={Ixx} Iyy={Iyy}\nSeccion ICHA {denominacion}\n Area : {Area}\n peso : {peso}\n Ixx  : {Ixx}\n Iyy  : {Iyy}"

                #elif df.loc[i,"d"]!=denominacion3[0] and df.loc[i,"bf"]!=denominacion3[1] and df.loc[i,"peso"]!=denominacion3[2] : 
                    #Area = df.loc[i,"A"]/10**6
                    #peso = df.loc[i,"peso"]
                    #Ixx = df.loc[i,"Ix/10⁶"]*10**6
                    #Iyy = df.loc[i,"Iy/10⁶"]*10**6
                    #return f"Tipo de seccion {denominacion} no encontrada en base de datos\nSeccion ICHA {denominacion}\n Area : {Area}\n peso : {peso}\n Ixx  : {Ixx}\n Iyy  : {Iyy}"


        elif denominacion.find("H") != -1:
            denominacion1=denominacion.replace("H","x")
            denominacion2=denominacion1.split("x")
            denominacion2.pop(0)
            denominacion3=[]
            for n in denominacion2:
                denominacion3.append(float(n))
        tabla=pd.read_excel(base_datos,engine="openpyxl",sheet_name="H",header=0,skiprows=11)
        df=pd.DataFrame(tabla)
        for i in range(0,len(df)+1):
            if df.loc[i,"d"]==denominacion3[0] and df.loc[i,"bf"]==denominacion3[1] and df.loc[i,"peso"]==denominacion3[2]:
                Area = df.loc[i,"A"]/10**6
                peso = df.loc[i,"peso"]
                Ixx = df.loc[i,"Ix/10⁶"]*10**6
                Iyy = df.loc[i,"Iy/10⁶"]*10**6
                return f"Tipo de seccion {denominacion} encontrada. A={Area} Ixx={Ixx} Iyy={Iyy}\nSeccion ICHA {denominacion}\n Area : {Area}\n peso : {peso}\n Ixx  : {Ixx}\n Iyy  : {Iyy}" 
            elif df.loc[i,"d"]!=denominacion3[0] and df.loc[i,"bf"]!=denominacion3[1] and df.loc[i,"peso"]!=denominacion3[2] and i==len(df)+1: 
                Area = df.loc[i,"A"]/10**6
                peso = df.loc[i,"peso"]
                Ixx = df.loc[i,"Ix/10⁶"]*10**6
                Iyy = df.loc[i,"Iy/10⁶"]*10**6
                return f"Tipo de seccion {denominacion} no encontrada en base de datos\nSeccion ICHA {denominacion}\n Area : {Area}\n peso : {peso}\n Ixx  : {Ixx}\n Iyy  : {Iyy}"      
 
        if denominacion.find("PH") != -1:
            denominacion1=denominacion.replace("PH","x")
            denominacion2=denominacion1.split("x")
            denominacion2.pop(0)
            denominacion3=[]
            for n in denominacion2:
                denominacion3.append(float(n))
        tabla=pd.read_excel(base_datos,engine="openpyxl",sheet_name="PH",header=0,skiprows=11)
        df=pd.DataFrame(tabla)
        for i in range(0,len(df)+1):
            if df.loc[i,"d"]==denominacion3[0] and df.loc[i,"bf"]==denominacion3[1] and df.loc[i,"peso"]==denominacion3[2]:
                Area = df.loc[i,"A"]/10**6
                peso = df.loc[i,"peso"]
                Ixx = df.loc[i,"Ix/10⁶"]*10**6
                Iyy = df.loc[i,"Iy/10⁶"]*10**6
                return f"Tipo de seccion {denominacion} encontrada. A={Area} Ixx={Ixx} Iyy={Iyy}\nSeccion ICHA {denominacion}\n Area : {Area}\n peso : {peso}\n Ixx  : {Ixx}\n Iyy  : {Iyy}" 
            #elif df.loc[i,"d"]!=denominacion3[0] and df.loc[i,"bf"]!=denominacion3[1] and df.loc[i,"peso"]!=denominacion3[2] : 
                #Area = df.loc[i,"A"]/10**6
                #peso = df.loc[i,"peso"]
                #Ixx = df.loc[i,"Ix/10⁶"]*10**6
                #Iyy = df.loc[i,"Iy/10⁶"]*10**6
                #return f"Tipo de seccion {denominacion} no encontrada en base de datos\nSeccion ICHA {denominacion}\n Area : {Area}\n peso : {peso}\n Ixx  : {Ixx}\n Iyy  : {Iyy}"  

        if denominacion.find("[]") != -1:
            denominacion1=denominacion.replace("[]","x")
            denominacion2=denominacion1.split("x")
            denominacion2.pop(0)
            denominacion3=[]
        for n in denominacion2:
            denominacion3.append(float(n))
        tabla=pd.read_excel(base_datos,engine="openpyxl",sheet_name="Cajon",header=0,skiprows=11)
        df=pd.DataFrame(tabla)
        for i in range(0,len(df)+1):
            if df.loc[i,"d"]==denominacion3[0] and df.loc[i,"bf"]==denominacion3[1] and df.loc[i,"peso"]==denominacion3[2]:
                Area = df.loc[i,"A"]/10**6
                peso = df.loc[i,"peso"]
                Ixx = df.loc[i,"Ix/10⁶"]*10**6
                Iyy = df.loc[i,"Iy/10⁶"]*10**6
                return f"Tipo de seccion {denominacion} encontrada. A={Area} Ixx={Ixx} Iyy={Iyy}\nSeccion ICHA {denominacion}\n Area : {Area}\n peso : {peso}\n Ixx  : {Ixx}\n Iyy  : {Iyy}"  
            #elif df.loc[i,"d"]!=denominacion3[0] and df.loc[i,"bf"]!=denominacion3[1] and df.loc[i,"peso"]!=denominacion3[2] : 
                #Area = df.loc[i,"A"]/10**6
                #peso = df.loc[i,"peso"]
                #Ixx = df.loc[i,"Ix/10⁶"]*10**6
                #Iyy = df.loc[i,"Iy/10⁶"]*10**6
                #return f"Tipo de seccion {denominacion} no encontrada en base de datos\nSeccion ICHA {denominacion}\n Area : {Area}\n peso : {peso}\n Ixx  : {Ixx}\n Iyy  : {Iyy}" 

        if denominacion.find("O") != -1:
            denominacion1=denominacion.replace("O","x")
            denominacion2=denominacion1.split("x")
            denominacion2.pop(0)
            denominacion3=[]
        for n in denominacion2:
            denominacion3.append(float(n))
        tabla=pd.read_excel(base_datos,engine="openpyxl",sheet_name="Circulares Mayores",header=0,skiprows=10)
        df=pd.DataFrame(tabla)
        for i in range(0,len(df)+1):
            if df.loc[i,"D"]==denominacion3[0] and df.loc[i,"Dint"]==denominacion3[1] :
                Area = df.loc[i,"A"]/10**6
                peso = df.loc[i,"peso"]
                Ixx = df.loc[i,"Ix/10⁶"]*10**6
                Iyy = df.loc[i,"Iy/10⁶"]*10**6
                return f"Tipo de seccion {denominacion} encontrada. A={Area} Ixx={Ixx} Iyy={Iyy}\nSeccion ICHA {denominacion}\n Area : {Area}\n peso : {peso}\n Ixx  : {Ixx}\n Iyy  : {Iyy}"  
            #elif df.loc[i,"d"]!=denominacion3[0] and df.loc[i,"bf"]!=denominacion3[1] : 
                #Area = df.loc[i,"A"]/10**6
                #peso = df.loc[i,"peso"]
                #Ixx = df.loc[i,"Ix/10⁶"]*10**6
                #Iyy = df.loc[i,"Iy/10⁶"]*10**6
                #return f"Tipo de seccion {denominacion} no encontrada en base de datos\nSeccion ICHA {denominacion}\n Area : {Area}\n peso : {peso}\n Ixx  : {Ixx}\n Iyy  : {Iyy}" 

        if denominacion.find("O") != -1:
            denominacion1=denominacion.replace("o","x")
            denominacion2=denominacion1.split("x")
            denominacion2.pop(0)
            denominacion3=[]
        for n in denominacion2:
            denominacion3.append(float(n))
        tabla=pd.read_excel(base_datos,engine="openpyxl",sheet_name="Circulares Menores",header=0,skiprows=10)
        df=pd.DataFrame(tabla)
        for i in range(0,len(df)+1):
            if df.loc[i,"D"]==denominacion3[0] and df.loc[i,"Dint"]==denominacion3[1] :
                Area = df.loc[i,"A"]/10**6
                peso = df.loc[i,"peso"]
                Ixx = df.loc[i,"Ix/10⁶"]*10**6
                Iyy = df.loc[i,"Iy/10⁶"]*10**6
                return f"Tipo de seccion {denominacion} encontrada. A={Area} Ixx={Ixx} Iyy={Iyy}\nSeccion ICHA {denominacion}\n Area : {Area}\n peso : {peso}\n Ixx  : {Ixx}\n Iyy  : {Iyy}" 
            #elif df.loc[i,"d"]!=denominacion3[0] and df.loc[i,"bf"]!=denominacion3[1] : 
                #Area = df.loc[i,"A"]/10**6
                #peso = df.loc[i,"peso"]
                #Ixx = df.loc[i,"Ix/10⁶"]*10**6
                #Iyy = df.loc[i,"Iy/10⁶"]*10**6
                #return f"Tipo de seccion {denominacion} no encontrada en base de datos\nSeccion ICHA {denominacion}\n Area : {Area}\n peso : {peso}\n Ixx  : {Ixx}\n Iyy  : {Iyy}" 
                
    def __str__(self):
        return f"Seccion ICHA {self.denominacion[0]} {self.leer()} "
