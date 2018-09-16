def selecionarEmRegistros(registros, atributos):
	selecionados = []
	for registro in registros:
		temp = {}
		for key in registro:
			if key in atributos:
				temp.update({key: registro[key]})
		selecionados.append(temp)
	return selecionados


def isolarCorpoEvento(arquivo):
	return {"evento": arquivo.readline()[0]}


def isolarCorpoRegistro(arquivo):
	atributos = {'n': "longitude", 'l': "latitude", 'a': "altitude", 'b': "bpm", 'p': "numeroDePassos"}
	registros = {}

	linha = arquivo.readline()
	while linha[0] != '#':
		registros.update({atributos[linha[0]]: linha.split()[1]})
		linha = arquivo.readline()

	return registros


def isolarCorpoLap(arquivo):
	return {}


def isolarCorpoMensagem(tipoDaMensagem, arquivo):
	if tipoDaMensagem == 'e':
		return isolarCorpoEvento(arquivo)
	elif tipoDaMensagem == 'r':
		return isolarCorpoRegistro(arquivo)
	elif tipoDaMensagem == 'l':
		return isolarCorpoLap(arquivo)
	else:
		return {}


def isolarMensagens(arquivo):
	mensagens = []

	for linha in arquivo:
		tipo, timeStamp = linha.split()
		mensagens.append({"tipo": tipo, "timeStamp": timeStamp})
		mensagens[-1].update(isolarCorpoMensagem(tipo, arquivo))

	return mensagens