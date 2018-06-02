#!/usr/bin/python3
# -*- coding: utf-8 -*-

###################################################################
#               TRABALHO INTELIGENCIA ARTIFICIAL                  #
#              https://github.com/homdreen/vrp-ai                 #
#                                                                 #   
#     		 ARTIGO DE REFERENCIA (PROFESSOR SCHEPKE)             # 
#   http://www.sirc.unifra.br/arquivos/edicoes/2004/Artigo24.pdf  #
#                                                                 #
#                  FELIPE HOMRICH MELCHIOR                        #
#                        161150758                                #
################################################################### 

from vrp import * # Importação da classe que está em outro arquivo

if __name__ == '__main__': # Condição que faz o arquivo funcionar como uma função "Main"
	vrp = Vrp() # Instanciação da classe Vrp
	vrp.start() # Chamada da função de todas as operações
	