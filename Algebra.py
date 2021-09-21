'''
LIBRERIA ÁLGEBRA:
Es esta librería encontrarán funciones útiles para operar más cómodamente con elementos en 2D, como puntos, vectores o líneas. 
'''
import functools
from numpy import arccos, sqrt, fabs, sum, array
from numpy import dot, cross
from numpy.linalg import det
from scipy.interpolate import splrep, splev



# Decoradores
def arrayargs(func):
    """Verifica que todos los argumentos son arrays."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Verifica que todos los argumentos son arrays."""
        return func(*[array(a) for a in args], **kwargs)
    return wrapper

def norm(x):
    """Devuelve la magnitud del vector x."""
    return sqrt(sum(array(x)**2, axis=-1))

@arrayargs
def distancia_punto_a_linea(x0, x1, x2):
    """Encuentra la menor distancia entre el punto x0 y la linea x1-x2.
    Ref: http://mathworld.wolfram.com/Point-LineDistance3-Dimensional.html"""
    assert x1.shape == x2.shape == (2,)
    return fabs(cross(x0-x1, x0-x2))/norm(x2-x1)

@arrayargs
def angulo(x0, x1, x2):
    """Devuelve el angulo entre tres puntos, x1 es el vertice.
    Ref: https://stackoverflow.com/questions/1211212"""
    assert x1.shape == x2.shape == (2,)
    a, b = x1 - x0, x1 - x2
    return arccos(dot(a, b)/(norm(a)*norm(b)))

@arrayargs
def esta_a_la_izquierda(x0, x1, x2):
    """Devuelve True si x0 está a la izquierda de la linea x1-x2,
    False otherwise.  Ref: https://stackoverflow.com/questions/1560492"""
    assert x1.shape == x2.shape == (2,)
    matrix = array([x1-x0, x2-x0])
    if len(x0.shape) == 2:
        matrix = matrix.transpose((1, 2, 0))
    return det(matrix) > 0

def interpolacion_lineal(x1, y1, x):
    """Interpolacion lineal en los puntos x, entre los arrays (x1, y1).
    Solo y1 puede ser de dos dimensiones.  Los valores de x1 deben estar
    ordenados de menos a mayor.  Devuelve un array de numpy de los 
    valores y correspondientes a los puntos x."""
    return splev(x, splrep(x1, y1, s=0, k=1))