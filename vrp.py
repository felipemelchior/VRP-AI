import math # Importação da biblioteca matematica
from operator import itemgetter # Importação do itemgetter, usado para ordenar os savings

# Abaixo temos a definição da classe principal, que chamamos de Vrp
# Nela teremos os métodos que irão calcular a distancia, imprimir dados na tela, calcular economias e calcular o custo
class Vrp(): # Definição da classe principal do programa, chamada vrp

	# Construtor padrão que inicia algumas listas que serão usadas e também dois numeros inteiros
	def __init__(self): # Construtor da classe, apenas inicializa o grafo com uma lista vazia
		self.numConsumers = 0 # Inteiro que guarda o numero de consumidores
		self.vehiclesCapacity = 0  # Inteiro que guarda a capacidade dos caminhões
		self.Cost = 0 # Varivel de ponto flutuante que guarda o custo das viagens
		self.Graph = [] # Grafo inicializado com uma lista vazia
		self.Demands = [] # Lista que armazena as demandas de cada cidade e se a cidade já foi visitada
		self.Distances = [] # Lista que guarda as distancias entre cada ponto
		self.Routes = [] # Lista de Rotas que os caminhões farão
		self.Savings = [] # Lista de Economias entre as rotas

	# Leitor dos dados, recebe uma linha por vez de dados e remapeia para as variaveis da classe
	def reader(self): # Função que faz a leitura dos dados, podendo entrar pelo teclado ou redirecionando a entrada padrão
		# string = input("Enter the number of consumers and th capacity of vehicles => ") # Usado uma string auxiliar para pegar os dados digitados
		string = input("") # Mesmo código acima, porém não imprimindo nada na tela
		self.numConsumers, self.vehiclesCapacity = map(int,string.split()) # Utilizando um map, os dados são convertidos para inteiro e a string é "separada" para as outras variaveis

		# string = input("\nEnter the coords (X, Y) of deposit => ") # Utilizando o mesmo sistema de cima, é utilizado uma string para guardar os dados
		string = input("") # Mesmo código acima, porém não imprimindo nada na tela
		coord_X, coord_Y = map(int, string.split()) # E o mesmo map é usado para atribuir os dados para outras variaveis
		
		self.Graph.append([coord_X, coord_Y]) # O deposito é adicionado ao grafo, com as coordenadas que foram passadas e demanda 0
		self.Demands.append([0]) # O deposito tem demanda 0

		for i in range(self.numConsumers): # Aqui temos um bloco de repetição, que vai de 0 até a quantidade de consumidores passado para o programa
			# string = input("\nEnter the coords (X, Y) of consumer and the consumer demand => " ) # String auxiliar
			string = input("") # Mesmo código acima, porém não imprimindo nada na tela
			coord_X, coord_Y, demand = map(int, string.split()) # Novas variaveis atribuidas, da mesma forma de cima
			
			self.Graph.append([coord_X, coord_Y]) # Consumidor adicionado ao grafo, com suas coordenadas
			self.Demands.append([demand]) # Cada consumidor é adicionado à lista de demandas com a sua respectiva demanda

	# Abaixo teremos um seção de códigos que irão imprimir dados na tela, usados apenas para debug, pois algumas nem estão sendo chamadas
	def printGraph(self): # Função que imprime todo o grafo
		print() # Print apenas para saltar um linha
		for i in self.Graph: # Bloco de repetição que inicia em 0 e vai até o tamanho total do grafo
			print(i) # Imprime cada Vertice do grafo

	def printDistances(self): # Função que imprime as distancias
		print() # Print apenas para saltar um linha
		for i in self.Distances: # Bloco de repetição que inicia em 0 e vai até o tamanho total das distancias
			print(i) # Imprime cada Distancia do grafo

	def printDemands(self): # Função que imprime as demandas
		print() # Print apenas para saltar um linha
		for i in self.Demands: # Bloco que itera até o tamanho maximo das demandas
			print(i) # Imprime cada Demanda

	def printRoutes(self): # Função que imprime as rotas
		# print("\nROUTES\n") # Imprime apenas a palavra ROTAS, apenas para separação
		for i in self.Routes: # Bloco que itera até o tamanho maximo de rotas
			print(i) # Imprime cada rota

	def printSavings(self): # Função que imprime as economias
		print() # Print apenas para saltar um linha
		for i in self.Savings: # Bloco que percorre toda a lista de economias
			print(i) # Imprime cada economia

	# Aqui temos uma função que calcula a distancia euclidiana entre todos os pontos através da formula raiz( (xf-xi)² + (yf-yi)² )
	def euclidianDist(self): # Função que calcula a distancia euclidiana de cada ponto para todos os pontos
		for i in range(len(self.Graph)): # Repete ate passar por todas as cidades
			self.Distances.append([]) # Adiciona a lista que sera modificada pela funcao no momento
			for j in range(len(self.Graph)): # Outro for que passa por todas as cidades
				if i == j: # Se as cidades forem iguais
					self.Distances[i].append(0.0) # Sua distancia vai ser igual a 0
				else: # Se as cidades forem diferentes
					distX = (self.Graph[i][0] - self.Graph[j][0]) ** 2 # X final menos X inicial ao quadrado
					distY = (self.Graph[i][1] - self.Graph[j][1]) ** 2 # Y final menos Y inicial ao quadrado
					self.Distances[i].append(math.sqrt(distX + distY)) # Raiz quadrada da soma das distancias em X e distancias em Y

	# Abaixo temos a heurística do programa, usei o Algoritmo de Savings que encontrei em um artigo do professor Schepke
	# Basicamente este algoritmo encontra as melhores ligações para as rotas
	# Usando a formula Sij = Ci0 + C0j - Cij
	def savingsAlgorithm(self): # Função do algoritmo de Economias, este algoritmo leva em conta a distancia de uma cidade i ate chegar ao deposito somado à distancia do deposito ate a cidade j e tudo isso subtraido com a distancia de i para j --> Sij = Ci0 + C0j - Cij
		saving = 0 # Variavel local para o calculo
		for i in range(1, len(self.Demands)): # Inicia as Rotas inicialmente apenas com o indice, pois sabemos que cada rota começa em 0 e termina em 0
			self.Routes.append([i]) # Adiciona os indices em uma lista de Rotas

		for i in range(1, len(self.Routes)+1): # Roda o for em todas as cidades
			for j in range(1, len(self.Routes)+1): # Roda o for em todas as cidades
				if i == j: # Como na Savings nao podemos ter a distancia da cidade para ela mesma
					pass # Apenas passamos a condicional e não fazemos nada
				else: # Caso as cidades forem diferentes
					saving = (self.Distances[i][0] + self.Distances[0][j]) - self.Distances[i][j] # Faz o calculo -- Sij = Ci0 + C0j - Cij
					self.Savings.append([i, j, saving]) # Adiciona os indices das cidades e o calculo da economia

		self.Savings = sorted(self.Savings, key=itemgetter(2), reverse=True) # Ordena a lista de economias

		for i in range(len(self.Savings)): # For que percorre a lista de economias
			startRoute = [] # Reset da variavel startRoute
			endRoute = [] # Reset da variavel endRoute
			routeDemand = 0 # Reset da demanda da possivel rota
			for j in range(len(self.Routes)): # For que percorre as rotas ja existentes
				if(self.Savings[i][0] == self.Routes[j][-1]): # Se a primeira cidade da dupla de economia estiver no final de uma rota
					endRoute = self.Routes[j] # Adiciona toda a rota em uma variavel auxiliar
				elif(self.Savings[i][1] == self.Routes[j][0]): # Se a segunda cidade da dupla de economia estiver no inicio de uma rota
					startRoute = self.Routes[j] # Adiciona toda a rota em uma variavel auxiliar
				
				if((len(startRoute) != 0) and (len(endRoute) != 0)): # Se as duas rotas forem diferentes de nulo
					for k in range(len(startRoute)): # For que percorre a lista auxiliar
						routeDemand += self.Demands[startRoute[k]][0] # e adiciona o custo da cidade que está na rota auxiliar
					for k in range(len(endRoute)): # For que percorre a lista auxiliar
						routeDemand += self.Demands[endRoute[k]][0] # e adiciona o custo da cidade que está na rota auxiliar

					if(routeDemand <= self.vehiclesCapacity): # Só faz a mudança nas rotas se as demandas couberem no caminhão
						self.Routes.remove(startRoute) # Remove da lista de rotas a lista startRoute
						self.Routes.remove(endRoute) # Remove da lista de rotas a lista endRoute
						self.Routes.append(endRoute + startRoute) # Adiciona as rotas removidas, porém agora são concatenadas
					break # Quebra do For para ir para a proxima economia
				
		for i in range(len(self.Routes)): # For que percorre a lista das Rotas e normaliza as mesma, colocando o deposito no inicio e no final
			self.Routes[i].insert(0, 0) # Insere o deposito no inicio
			self.Routes[i].insert(len(self.Routes[i]), 0) # Insere o deposito no final

	# Com as rotas prontas, esta função é chamada apenas para calcular o custo total de todas as rotas
	def calcCosts(self): # Função que calcula o custo das rotas
		for i in range(len(self.Routes)): # For que percorre as rotas
			for j in range(len(self.Routes[i])-1): # For que percorre as cidades da rota acima
				self.Cost += self.Distances[self.Routes[i][j]][self.Routes[i][j+1]] # Soma das distancias
				
		print("\nTotal Cost: ", round(self.Cost,3)) # Imprime o custo

	# Função que apenas faz a chamada de outras funções, usada apenas para diminuir a quantidade de funções chamadas pelo arquivo Main.py
	def start(self): # Função mestre, que chama todas as outras
		self.reader() # Chamada da função do leitor
		self.euclidianDist() # Chamada da função que calcula a distancia euclidiana das cidades
		self.savingsAlgorithm() # Chamada da função que calcula as economias e gera as rotas
		# print("============================== RESULTS ==============================") # Print de separação
		self.printRoutes() # Chamada da função que imprime as rotas
		# self.calcCosts() # Chamada da função que calcula o custo das rotas