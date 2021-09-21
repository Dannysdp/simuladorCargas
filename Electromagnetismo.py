'''
LIBRERIA ELECTROMAGNETISMO:
Es esta librería se define la clase Carga Puntual. La clase tiene como métodos el campo y potencial generado por ella en un punto dado. 
Pueden implementarse otros métodos o clases que se consideren de interés. 
'''

from numpy import array
from Algebra import norm
import numpy as np

class cargaPuntual:
    radio = 0.1  # Radio de la carga
    k = 9*(10**9)
    def __init__(self, q, r):
        # Inicializa el valor de la carga q y la posición r=(x,y).
        self.q, self.r = q, array(r)
        
    def campo(self, r):  
        if self.q == 0:
            return 0
        #vectorq = sum(r, -self.r)
        vectorq = (r - self.r)
        return ((self.q/(norm(vectorq)**3)*cargaPuntual.k*vectorq))

    def potencial(self, r):
        vectorq = (r - self.r)
        return (cargaPuntual.k*self.q)/norm(vectorq)

