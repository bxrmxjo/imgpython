from imagen import *
from typing import Callable,Union
import random


ColorDistance = Callable[[Color,Color],int]




img = read("beach.jpg")
color_list = [[49,165,189],[148,128,114],[240,240,240],[118,159,22]]
"""
distance: Callable[[Color,Color],int]
"""

def img_aprox(img:ImagenColor, color_list:list[Color],distance: ColorDistance)-> ImagenColor:
    """
    Le cambia el color a cada pixel en función de su proximidad a los colores de "color_list".
    Para ello, guarda en una lista "lista_distancias" la distancia entre cada pixel y cada color de la lista
    antes mencionada. Posteriormente se guarda en "menor" la menor distancia (con el color a la que va asociada)
    para cambiárselo al pixel correspondiente. 
    """

    for col in range(len(img)):
        for fil in range(len(img[0])):
            lista_distancias = []
            for t in range(len(color_list)):
                lista_distancias.append([distance(img[col][fil],color_list[t]),color_list[t]])
            menor = min(lista_distancias)
            img[col][fil] = menor[1]
    show(img)


def dist1(color1:Color,color2:Color):
    result = 0
    for i in range(len(color1)):
        result = result + (color1[i]-color2[i])**2
    return result

def dist2(color1:Color,color2:Color)->int:
    result = 0
    for i in range(len(color1)):
        result = max(result, abs(color1[i]-color2[i]))
    return result

def dist3(color1:Color,color2:Color)->int:
    result = 0
    cofs = [2, 4, 3]
    for i in range(len(color1)):
        result = result + cofs[i]*(color1[i]-color2[i])**2
    return result


def muestra(img:ImagenColor,k:int,l:int)->list[Color]:

    width ,heigth = len(img[0]), len(img)
    result = []
    for y in range(0,heigth,heigth//k):
        for x in range(0,width,width//l):
            result.append(img[y][x])
    return result



def random_color_list(N:int)->list:
    """
    Devuelve una lista de "N" colores aleatorios.
    """
    colores = []
    for i in range(N):
        colores.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    return colores

pruebacolores = muestra(img,5,3)

def new_list(img:ImagenColor, color_list:list[Color], distance:ColorDistance)->list[Color]:
    l = []
    for col in range(len(img)):
        for fil in range(len(img[0])):
            dist = distance(color_list[0], )
            for t in range(1,len(color_list)):
                if distance(img[col][fil],color_list[t]):
                img[col][fil] 
