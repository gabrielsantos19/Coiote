from Interface import imprimirTexto


def imprimirResumoPorVolta(turtle, rect, resumoPorVolta):
	pass


def imprimirResumoPorKm(turtle, rect, resumoPorKm):
	pass


def imprimirResumoGeral(turtle, rect, resumoGeral):
	TITULO_ABA = dict(texto="Resumo geral", fonte="Aria", size=23, tipo="bold", cor="#7a7a7a", xPos=rect["xPos"] + 50, yPos=rect["yPos"] + 50)
	imprimirTexto(turtle, TITULO_ABA)

	ITEM = dict(texto="", fonte="Arial", size=15, tipo="", cor="#7a7a7a", xPos=rect["xPos"] + 50, yPos=rect["yPos"] + 80)
	for item in resumoGeral.items():
		ITEM["xPos"] = rect["xPos"] + 50
		for i in item:
			ITEM["texto"] = i
			imprimirTexto(turtle, ITEM)
			ITEM["xPos"] += rect["width"] * 0.5
		ITEM["yPos"] += 30


def gerarResumoPorVolta(mensagens):
	pass


def gerarResumoPorKm(mensagens):
	pass


def gerarResumoGeral(mensagens):
	return {"Distância total": 2534, "Tempo total": 253453, "Ritmo médio": 234, "Média ponderada de BPM": 3243, 
	"BPM Máximo": 423, "BPM Mínimo": 2312, "Cadência média de passos": 435, "Altitude máxima": 234, "Altitude mínima": 32}