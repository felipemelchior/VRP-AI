###########################################################
#           TRABALHO INTELIGENCIA ARTIFICIAL              #
#          https://github.com/homdreen/vrp-ai             #
#                                                         #
#                FELIPE HOMRICH MELCHIOR                  #
#                      161150758                          #
########################################################### 

from vrp import * # Importação da classe que está em outro arquivo

if __name__ == '__main__': # Condição que faz o arquivo funcionar como uma função "Main"
	vrp = Vrp() # Instanciação da classe Vrp
	vrp.reader() # Chamada da função do leitor
	# vrp.printGraph() # Chamada da função que imprime todo o grafo
	vrp.euclidianDist()
	vrp.printDemands()
	vrp.genRoutes()
	#vrp.printDistances()