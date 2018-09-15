from tkinter import filedialog


def selecionarArquivo():
	return filedialog.askopenfilename(filetypes = [("Text files", "*.txt")])


def setArquivoInfo(diretorio):
	ARQUIVO["texto"] = diretorio.split('/')[-1][:-4]
	DIRETORIO["texto"] = '"' + diretorio + '"'


def imprimirTexto(turtle, objTxt):
	screen = turtle.getscreen()
	turtle.up()
	turtle.goto(-screen.window_width() * 0.5 + objTxt["xPos"], screen.window_height() * 0.5 - objTxt["yPos"])
	turtle.write(objTxt["texto"], False, "left", (objTxt["fonte"], objTxt["size"], objTxt["tipo"]))


def imprimirMenu(turtle, listaDeItens, objTxtBase, espacamentoVertical):
	TEMP = objTxtBase.copy()
	for item in listaDeItens:
		TEMP["texto"] = item
		TEMP["yPos"] += espacamentoVertical
		imprimirTexto(turtle, TEMP)


def imprimirInterface(turtle):
	imprimirTexto(turtle, COIOT)
	imprimirTexto(turtle, ARQUIVO)
	imprimirTexto(turtle, DIRETORIO)
	imprimirMenu(turtle, itensDoMenu, ITEM_MENU, 50)


COIOT = dict(texto = "Coiot", fonte = "Arial", size = 50, tipo = "normal", xPos = 35, yPos = 90)
ARQUIVO = dict(texto = "Nenhum arquivo selecionado", fonte = "Arial", size = 20, tipo = "bold", xPos = 240, yPos = 50)
DIRETORIO = dict(texto = "...", fonte = "Arial", size = 15, tipo = "italic", xPos = ARQUIVO["xPos"], yPos = 80)

ITEM_MENU = dict(texto = "", fonte = "Arial", size = 15, tipo = "normal", xPos = 35, yPos = 160)
itensDoMenu = ("Resumo geral", "Resumo por km", "Resumo por volta", "Gráficos")