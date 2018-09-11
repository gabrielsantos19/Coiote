def isolarCorpoEvento(arquivo):
	return [arquivo.readline()[0]]


def isolarCorpoRegistro(arquivo):
	registro = []

	linha = arquivo.readline()
	while linha[0] != '#':
		registro.append(linha[:-1])
		linha = arquivo.readline()

	return registro


def isolarCorpoLap(arquivo):
	pass


def isolarCorpoMensagem(tipo, arquivo):
	if tipo == 'e':
		return isolarCorpoEvento(arquivo)
	elif tipo == 'r':
		return isolarCorpoRegistro(arquivo)
	elif tipo == 'l':
		return isolarCorpoLap(arquivo)
	else:
		return []


def isolarMensagens(arquivo):
	mensagem = []

	for linha in arquivo:
		mensagem.append(linha.split() + isolarCorpoMensagem(linha[0], arquivo))

	return mensagem
