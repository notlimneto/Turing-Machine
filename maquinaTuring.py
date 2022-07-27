class Transicao:
	def __init__(self, valor_leitura, estado_destino, valor_escrita, movimento):
		self.valor_leitura, self.estado_destino, self.valor_escrita, self.movimento = valor_leitura, estado_destino, valor_escrita, movimento

	def transita(self, fita, cabeca_leitura):
		if cabeca_leitura==len(fita)-1 and self.valor_escrita!="B":
			fita+="B"

		temp = list(fita)
		temp[cabeca_leitura] = self.valor_escrita
		fita = "".join(temp)

		if self.movimento=="L": cabeca_leitura-=1
		elif self.movimento=="R": cabeca_leitura+=1

		return [fita, self.estado_destino, cabeca_leitura]

class Estado:
	def __init__(self, valor_estado):
		self.valor_estado, self.transicoes = valor_estado, {}

	def adicionarTransicao(self, transicao):
		self.transicoes[transicao.valor_leitura] = transicao

	def listarTransicoes(self):
		iterador = self.transicoes
		for x in iterador:
			print("({}, {}) -> ({}, {}, {})\n".format(self.valor_estado, 
				iterador[x].valor_leitura, 
				iterador[x].estado_destino, 
				iterador[x].valor_escrita, 
				iterador[x].movimento
			))


	def getTransicao(self, valor_leitura):
		return self.transicoes[valor_leitura]


def maquinaTuringUniversal():
	maquina = str(input("Insira a máquina: \n")).replace("000", "")

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

	#Isso daqui mostrava os estados computados

	# for x in estados:
	# 	estados[x].listarTransicoes()

	fita = str(input("Insira a fita: \n"))

	estado_atual = estados["1"]
	existe_transicao = True
	cabeca_leitura = 0

	################### Computar a fita segundo a máquina ####################

	while existe_transicao:
		try:
			valores_transicao = estado_atual.getTransicao(fita[cabeca_leitura]).transita(fita, cabeca_leitura)
			fita = valores_transicao[0]
			estado_atual = estados[valores_transicao[1]]
			cabeca_leitura = valores_transicao[2]
		except:
			existe_transicao=False
		#print("    {}".format(fita)) #Isso daqui era pra mostrar as computações

	print("\nFita resultante: {}".format(fita))

maquinaTuringUniversal()