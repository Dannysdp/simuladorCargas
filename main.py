import Graficas as gr

cargas, medidas, medidasp = gr.iniciar()
gr.agregarCarga(cargas, 1*10**-9, 0, 0)
gr.agregarCarga(cargas, 1*10**-9, 0, 2)
#gr.agregarCarga(cargas, 1*10**-9, 0, 4)
#gr.agregarMedidaDeCampo(medidas, 1, 0)
#gr.agregarMedidaDeCampo(medidas, 7, 4)
#gr.agregarMedidaDePotencial(medidasp,4,2)
#gr.agregarMedidaDePotencial(medidasp,6,4)
gr.mostrar(cargas, medidas, medidasp)