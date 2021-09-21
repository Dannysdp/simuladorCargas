import Graficas as gr

cargas, medidas, medidasp = gr.iniciar()
gr.agregarCarga(cargas, 1*10**-9, 1, 1)
gr.agregarCarga(cargas, 1*10**-9, 2, 1)
gr.agregarCarga(cargas, 1*10**-9, 4, 1)
gr.agregarMedidaDeCampo(medidas, 0, 0)
gr.agregarMedidaDeCampo(medidas, 2, 2)
gr.agregarMedidaDePotencial(medidasp, 3,5)
gr.agregarMedidaDePotencial(medidasp,1,-1)
gr.mostrar(cargas, medidas, medidasp)