import math # Importação da biblioteca matematica
from operator import itemgetter


class Vrp(): # Definição da classe principal do programa, chamada vrp
	def __init__(self): # Construtor da classe, apenas inicializa o grafo com uma lista vazia
		self.numConsumers = 0 # Inteiro que guarda o numero de consumidores
		self.vehiclesCapacity = 0  # Inteiro que guarda a capacidade dos caminhões
		self.Graph = [] # Grafo inicializado com uma lista vazia
		self.Demands = [] # Lista que armazena as demandas de cada cidade e se a cidade já foi visitada
		self.Distances = [] # Lista que guarda as distancias entre cada ponto
		self.Routes = [] # Lista de Rotas que os caminhões farão
		self.Savings = [] # Lista de Economias entre as rotas

	def reader(self): # Função que faz a leitura dos dados, podendo entrar pelo teclado ou redirecionando a entrada padrão
		string = input("Enter the number of consumers and th capacity of vehicles => ") # Usado uma string auxiliar para pegar os dados digitados
		self.numConsumers, self.vehiclesCapacity = map(int,string.split()) # Utilizando um map, os dados são convertidos para inteiro e a string é "separada" para as outras variaveis

		string = input("Enter the coords (X, Y) of deposit => ") # Utilizando o mesmo sistema de cima, é utilizado uma string para guardar os dados
		coord_X, coord_Y = map(int, string.split()) # E o mesmo map é usado para atribuir os dados para outras variaveis
		print() # Print apenas para saltar um linha

		self.Graph.append([coord_X, coord_Y]) # O deposito é adicionado ao grafo, com as coordenadas que foram passadas e demanda 0
		self.Demands.append([0, True]) # O deposito tem demanda 0 e ja foi visitado, pois o problema começa no deposito

		for i in range(self.numConsumers): # Aqui temos um bloco de repetição, que vai de 0 até a quantidade de consumidores passado para o programa
			string = input("Enter the coords (X, Y) of consumer and the consumer demand => " ) # String auxiliar
			coord_X, coord_Y, demand = map(int, string.split()) # Novas variaveis atribuidas, da mesma forma de cima
			print() # Print apenas para saltar um linha

			self.Graph.append([coord_X, coord_Y]) # Consumidor adicionado ao grafo, com suas coordenadas
			self.Demands.append([demand, False]) # Cada consumidor é adicionado à lista de demandas com a sua respectiva demanda e que a cidade ainda não foi visitada

	def printGraph(self): # Função que imprime todo o grafo
		for i in self.Graph: # Bloco de repetição que inicia em 0 e vai até o tamanho total do grafo
			print(i) # Imprime cada Vertice do grafo

	def printDistances(self): # Função que imprime as distancias
		for i in self.Distances: # Bloco de repetição que inicia em 0 e vai até o tamanho total das distancias
			print(i) # Imprime cada Distancia do grafo

	def printDemands(self): # Função que imprime as demandas
		for i in self.Demands: # Bloco que itera até o tamanho maximo das demandas
			print(i) # Imprime cada Demanda

	def printRoutes(self): # Função que imprime as rotas
		for i in self.Routes: # Bloco que itera até o tamanho maximo de rotas
			print(i) # Imprime cada rota

	def printSavings(self): # Função que imprime as economias
		for i in self.Savings: # Bloco que percorre toda a lista de economias
			print(i) # Imprime cada economia

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

	def checkVisited(self): # Função que checa se existem cidades que ainda não foram visitadas
		for i in range(len(self.Demands)): # For que percorre a quantidade total das distancias
			if(self.Demands[i][1] == False): # Se existir uma cidade que ainda não foi visitada retorna False
				return False # Retorno da função caso existir uma cidade não visitada

		return True # Retorno da função caso todas as cidades já foram visitadas

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

		self.Savings = sorted(self.Savings, key=itemgetter(2)) # Ordena a lista de economias

	def start(self):
		self.reader()
		self.euclidianDist()
		# self.printDistances()
		self.savingsAlgorithm()
		self.printSavings()