class Transicao:
	def __init__(self, valor_leitura, estado_destino, valor_escrita, movimento):
		self.valor_leitura, self.estado_destino, self.valor_escrita, self.movimento = valor_leitura, estado_destino, valor_escrita, movimento

	def transita(fita, cabeca_leitura):
		if cabeca_leitura==len(fita)-1 and self.valor_escrita!="B":
			fita+="B"

		if self.movimento=="L": cabeca_leitura-=1
		else: cabeca_leitura+=1

		return [fita, cabeca_leitura]

class Estado:
	def __init__(self, valor_estado):
		self.valor_estado, self.transicoes = valor_estado, [] #Lembre-se de transformar em um dicionário para mais fácil acesso a qual letra de leitura

	def adicionarTransicao(self, transicao):
		self.transicoes.append(transicao)

	def listarTransicoes(self):
		iterador = self.transicoes
		for x in iterador:
			print("({}, {}) -> ({}, {}, {})\n".format(self.valor_estado, x.valor_leitura, x.estado_destino, x.valor_escrita, x.movimento))

		print("\n")


def maquinaTuringUniversal():
	maquina = str(input("Insira a máquina: \n")).replace("000", "")
	#fita = str(input("Insira a fita: \n"))

	transicoes = maquina.split("00")
	
	alfabeto = {
		"1": "0",
		"11": "1",
		"111": "B",
	}

	movimentos = {
		"1" : "L",
		"11" : "R"
	}

	estados = {}
	transicoes_tratadas = []


	############## Gerando as transições para a máquina #################
	for transicao in transicoes:

		valores_transicao = transicao.split("0")

		if(estados.get(valores_transicao[0])==None):
			estados[valores_transicao[0]] = Estado(valores_transicao[0])


		estados[valores_transicao[0]].adicionarTransicao(Transicao(
			alfabeto[valores_transicao[1]], 
			valores_transicao[2], 
			alfabeto[valores_transicao[3]], 
			movimentos[valores_transicao[4]]
		))


	for x in estados:
		estados[x].listarTransicoes()


maquinaTuringUniversal()