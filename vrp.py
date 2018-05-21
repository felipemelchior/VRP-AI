class Vrp(): # Definição da classe principal do programa, chamada vrp
	def __init__(self): # Construtor da classe, apenas inicializa o grafo com uma lista vazia
		self.Graph = [] # Grafo inicializado com uma lista vazia

	def reader(self): # Função que faz a leitura dos dados, podendo entrar pelo teclado ou redirecionando a entrada padrão
		string = input("Enter the number of consumers and th capacity of vehicles => ") # Usado uma string auxiliar para pegar os dados digitados
		numConsumers, vehiclesCapacity = map(int,string.split()) # Utilizando um map, os dados são convertidos para inteiro e a string é "separada" para as outras variaveis

		string = input("Enter the coords (X, Y) of deposit => ") # Utilizando o mesmo sistema de cima, é utilizado uma string para guardar os dados
		coord_X, coord_Y = map(int, string.split()) # E o mesmo map é usado para atribuir os dados para outras variaveis

		self.Graph.append([coord_X, coord_Y, 0]) # O deposito é adicionado ao grafo, com as coordenadas que foram passadas e demanda 0
		
		for i in range(numConsumers): # Aqui temos um bloco de repetição, que vai de 0 até a quantidade de consumidores passado para o programa
			string = input("Enter the coords (X, Y) of consumer and the consumer demand => ") # String auxiliar
			coord_X, coord_Y, demand = map(int, string.split()) # Novas variaveis atribuidas, da mesma forma de cima

			self.Graph.append([coord_X, coord_Y, demand]) # Consumidor adicionado ao grafo, com suas coordenadas e demanda

	def printGraph(self): # Função que imprime todo o grafo
		for i in self.Graph: # Bloco de repetição que inicia em 0 e vai até o tamanho total do grafo
			print(i) # Imprime cada Vertice do grafo
				