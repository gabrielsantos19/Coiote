def isolarCorpoEvento(arquivo):
	return [arquivo.readline()[0]]


def isolarCorpoRegistro(arquivo):
	registros = []

	linha = arquivo.readline()
	while linha[0] != '#':
		registros.append(linha[:-1])
		linha = arquivo.readline()

	return registros


def isolarCorpoLap(arquivo):
	return []


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
	mensagens = []

	for linha in arquivo:
		mensagens.append(linha.split() + isolarCorpoMensagem(linha[0], arquivo))

	return mensagens
