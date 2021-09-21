'''
LIBRERIA GRÁFICAS:
Es esta librería se definen las funciones necesarias para poder graficar los distintos componentes de interés. 
'''

from matplotlib import pyplot, text
from numpy import sqrt, fabs, array, exp
from Electromagnetismo import cargaPuntual
from Algebra import norm

#-----------------------------------------------------------------------------
# Dimensiones del plano en donde se graficarán las cargas. Inicialmente se declaran en None para luego ser completadas con valores dados en la incialización del programa
XMIN, XMAX = None, None
YMIN, YMAX = None, None
ZOOM = None
XOFFSET = None

#-----------------------------------------------------------------------------
# Funciones para iniciar y ajustar el gráfico. 

def iniciarGrafico(xmin, xmax, ymin, ymax, zoom=1, xoffset=0):
    #Iniciar el gráfico 
    global XMIN, XMAX, YMIN, YMAX, ZOOM, XOFFSET
    XMIN, XMAX, YMIN, YMAX, ZOOM, XOFFSET = \
      xmin, xmax, ymin, ymax, zoom, xoffset

def ajustarGráfico():
    # Finalizar el gráfico
    ax = pyplot.gca()
    ax.set_xticks([])
    ax.set_yticks([])
    pyplot.xlim(XMIN/ZOOM+XOFFSET, XMAX/ZOOM+XOFFSET)
    pyplot.ylim(YMIN/ZOOM, YMAX/ZOOM)
    pyplot.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)

#-----------------------------------------------------------------------------
#Funciones que ingresan las formas gráficas de cada elemento en la figura. 
        
def graficarCargaPuntual(carga):
  # Genera un punto de color (donde el color indica el signo de la carga)
    color = 'b' if carga.q < 0 else 'r' if carga.q > 0 else 'k'
    # El radio del punto se calcula en base al valor de la carga, para que cargas de mayor valor se vean más grandes. 
    # La ecuación utilizada fue considerada razonable, pero el desarrollador puede modificarla para obtener el resultado que se ajuste a sus gustos. 
    r = 0.1*(sqrt(fabs(carga.q))/2 + 1)
    circle = pyplot.Circle(carga.r, r, color=color, zorder = 10)
    pyplot.gca().add_artist(circle)
    
def graficarMedidaDeCampo(listaDeCargas, medida):
  # El en el punto pedido en "medida" se obtiene por superposición.
  # Se suma el aporte de cada carga disponible (VECTORIALMENTE!) para obtener el campo resultante en el punto de interés
  campo = sum([carga.campo(medida) for carga in listaDeCargas ])
  #potencial = sum([carga.potencial(medida) for carga in listaDeCargas ])
  # El largo del vector que se dibuja es escalado para que grandes diferencias entre el módulo de distintos vectores se vean reflejadas como diferencias moderadas en los dibujos.
  # La ecuación utilizada fue considerada razonable, pero el desarrollador puede modificarla para obtener el resultado que se ajuste a sus gustos.
  escala  =(1-exp(-norm(campo)))*2
  pyplot.gca().quiver(array(medida[0]),array(medida[1]),array(campo[0]),array(campo[1]),units='xy',scale=escala,color='k')
  #pyplot.text(array(medida[0])+0.5, array(medida[1])+0.5, "Campo:"+norm(campo))
  pyplot.text(array(medida[0])+1, array(medida[1])+1, ('Campo:', norm(campo)))
  potencial = sum([carga.potencial(medida) for carga in listaDeCargas ])
  pyplot.text(array(medida[0]), array(medida[1]), ('Potencial:', norm(potencial)))

#-----------------------------------------------------------------------------
#Functiones para agregar elementos a graficar

def agregarCarga(listaDeCargas, carga = 1, x = 0, y = 0) -> cargaPuntual:
  # Esta función agrega una carga de valor q en la posición (x,y).
  # Se debe pasar como parámentro la lista de cargas obtenida de la función iniciar() así como los parámentros de la carga.  
  nuevaCarga = cargaPuntual(carga, [x, y])
  listaDeCargas.append(nuevaCarga)
  # La función retorna el elemento creado de la clase cargaPuntual
  return nuevaCarga

def agregarMedidaDeCampo(listaDeMedidas, x = 0, y = 0 ):
  # Esta función agrega una posición (x,y) a la lista de medidas a realizar.
  text  
  listaDeMedidas.append([x,y])

#-----------------------------------------------------------------------------
#Funciones para iniciar y mostrar el gráfico

def iniciar():
  # Al iniciar la la aplicación se deberá definir el tamaño del plano donde podrán ponerse las cargas y tomar las medidas. 
  XMIN, XMAX = -10, 10
  YMIN, YMAX = -10, 10
  ZOOM = 1
  XOFFSET = 0
  iniciarGrafico(XMIN, XMAX, YMIN, YMAX, ZOOM, XOFFSET)
  # Además se crean dos vectores vacíos que contendrán las cargas y medidas solicitadas.
  cargas = []
  medidas = []
  return (cargas, medidas)

def mostrar(cargas = None, medidas = None):
  # Esta función toma las cargas y medidas y se encarga de solicitar que se agreguen a la figura. 
  #El tamaño de la ventana en la que se mostrará la figura viene dado por el parámetro figsize que se pasa como argumento a la hora de iniciar la figura.  
  pyplot.figure(figsize=(2, 2))
  ajustarGráfico()
  # Se grafican las cargas y vectores de campo para cada caso agregado
  [graficarCargaPuntual(carga) for carga in cargas]
  [graficarMedidaDeCampo(cargas,medida) for medida in medidas]
  # Finalmente se muestra el gráfico obtenido
  pyplot.show()