import Graficas as gr

cargas, medidas = gr.iniciar()
gr.agregarCarga(cargas, 1*10**-9, 1, 0)
#gr.agregarCarga(cargas, 1*10**-9, 5, 2)
#gr.agregarCarga(cargas, 1*10**-9, 5, 4)
gr.agregarMedidaDeCampo(medidas, 1, 2)
gr.agregarMedidaDeCampo(medidas, 7, 4)
gr.mostrar(cargas, medidas)
