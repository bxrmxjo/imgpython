#
# Envoltorio para cargar imágenes como listas
#
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from typing import Union 

ImagenBW = list[list[int]]
Color = list[int]
ImagenColor = list[list[Color]]
Imagen = Union[ImagenBW,ImagenColor]


def read(ruta: str) -> Imagen:
    """Lee una imagen desde un archivo"""

    return plt.imread(ruta).tolist()


def show(img: Imagen):
    """Muestra una imagen"""

    kwargs = {}

    if not isinstance(img[0][0], list):
        kwargs = {'cmap': 'gray', 'vmin': 0, 'vmax': 255}

    plt.imshow(img, **kwargs)


def save(nombre: str, img: Imagen):
    """Guarda una imagen en un archivo"""
    if not isinstance(img[0][0], list):
        pil_image = Image.fromarray(np.asarray(img,dtype=np.uint8))
        pil_image.save(nombre)
    else:
        plt.imsave(nombre, np.asarray(img, dtype=np.uint8))

