def selecionar(lista, tipoDaMensagem, dado = None):
	selecionados = []

	for mensagem in lista:
		if mensagem[0] == tipoDaMensagem:
			selecionados.append(mensagem)

	return selecionados