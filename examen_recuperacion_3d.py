"""
Examen 3D Recuperacion
Alexis Saúl Castillo Gonzalez
"""
import matplotlib.pyplot as plt 
import numpy as np
from math import sqrt 
import sys
import keyboard

#Declaracion del arrgelo
x=[30,40,80,10,40]
y=[10,60,60,10,75]
z=[-10,10,10,0,0]

#funcion del ploteo de la figura
def plotPlaneLine(xg,yg,zg,bandera,areaBase,area1,area2):
    #Tamaño del grid
    plt.title('Alexis Saúl Castillo Gonzales')
    plt.axis([0,150,100,0])
    plt.axis('on')
    plt.grid(True)
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')

    #Triangulo base
    plt.plot([x[0],x[1]],[y[0],y[1]],color='k')
    plt.plot([x[1],x[2]],[y[1],y[2]],color='k')
    plt.plot([x[2],x[0]],[y[2],y[0]],color='k')

    #Triangulos lados
    plt.plot([x[0],x[3]],[y[0],y[3]],linestyle=':',color='r')
    plt.plot([x[3],x[1]],[y[3],y[1]],linestyle=':',color='g')
    plt.plot([x[3],x[2]],[y[3],y[2]],linestyle=':',color='y')

    #Linea de interseccion
    plt.plot([x[3],x[4]],[y[3],y[4]],color='b')

    if(bandera==True):
        plt.text(100,60,'Hitpoint dentro del plano')
    else:
        plt.text(100,60,'Hitpoint fuera del plano')

    areaBase = int(areaBase)
    area1 = int(area1)
    area2 = int(area2)

    plt.text(100,25,'Area base=')
    plt.text(125,25,areaBase)
    plt.text(100,35,'Area1=')
    plt.text(120,35,area1)
    plt.text(100,40,'Area2=')
    plt.text(120,40,area2)
    plt.text(100,50,'Area1+Area2=')
    plt.text(135,50,area1+area2)
    plt.show()

def hitpoint(x,y,z):
    #Triangulo base
    #Distancia de 0 a 1
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    D01=sqrt(a*a+b*b+c*c) 
    #Distancia de 1 a 2
    a=x[2]-x[1]
    b=y[2]-y[1]
    c=z[2]-z[1]
    D12=sqrt(a*a+b*b+c*c) 
    #Distancia de 0 a 2
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    D02=sqrt(a*a+b*b+c*c)
    #Calcular area con formula de Heron
    s=(D01+D12+D02)/2
    areaBase=sqrt(s*(s-D01)*(s-D12)*(s-D02))
        
    #Triangulo 1
    #Distancia de 0 a 1
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    D01=sqrt(a*a+b*b+c*c) 
    #Distancia de 1 a 3
    a=x[3]-x[1]
    b=y[3]-y[1]
    c=z[3]-z[1]
    D13=sqrt(a*a+b*b+c*c) 
    #Distancia de 0 a 3
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    D03=sqrt(a*a+b*b+c*c)
    #Calcular area con formula de Heron
    s=(D01+D13+D03)/2
    area1=sqrt(s*(s-D01)*(s-D13)*(s-D03))

    #Triangulo 2
    #Distancia de o a 2
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    D02=sqrt(a*a+b*b+c*c) 
    #Distancia de 2 a 3
    a=x[3]-x[2]
    b=y[3]-y[2]
    c=z[3]-z[2]
    D23=sqrt(a*a+b*b+c*c) 
    #Distancia de 0 a 3
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    D03=sqrt(a*a+b*b+c*c)
    #Calcular area con formula de Heron
    s=(D02+D23+D03)/2
    area2=sqrt(s*(s-D02)*(s-D23)*(s-D03))

    #Verificacion del hitpoint
    sumaAreas = area1+area2
    bandera = True
    if(areaBase>sumaAreas):
        bandera = True
    else:
        bandera = False
    
    #Manda a plotear la figura y etiquetas
    plotPlaneLine(x,y,z,bandera,areaBase,area1,area2)

#inserccion de datos y hitpoint
print("pulsa Enter para continuar o ESC para salir")
while True:
    
    if keyboard.is_pressed('Esc'):
        sys.exit(0)
    if keyboard.is_pressed('ENTER'):
        tecla=input('-----')
        hx=input("Hitpoint x:")
        hy=input("Hitpoint y:")
        #Asignacion de los arreglos
        x[3]=int(hx)
        y[3]=int(hy)
        hitpoint(x,y,z)
        print("pulsa Enter para continuar o ESC para salir")

plt.show()