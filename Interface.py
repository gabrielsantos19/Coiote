from tkinter import filedialog


def selecionarArquivo():
	return filedialog.askopenfilename(filetypes = [("Text files", "*.txt")])


def setArquivoInfo(diretorio):
	ARQUIVO["texto"] = diretorio.split('/')[-1][:-4]
	DIRETORIO["texto"] = '"' + diretorio + '"'


def transladarParaCentralizado(screen, x = None, y = None):
	if x != None and y != None:
		return -screen.window_width() * 0.5 + x, screen.window_height() * 0.5 - y
	elif x != None:
		return -screen.window_width() * 0.5 + x
	elif y != None:
		return screen.window_height() * 0.5 - y


def getItemSelecionadoMenu(screen, xMouse, yMouse):
	TEMP_BOX = MENU_Rect.copy()
	TEMP_BOX["height"] = MENU_Rect["height"] / len(itensDoMenu)
	for item in itensDoMenu:
		if checarSelecao(screen, TEMP_BOX, xMouse, yMouse):
			return item
		TEMP_BOX["yPos"] += TEMP_BOX["height"]


def getItemSelecionado(screen, xMouse, yMouse):
	if checarSelecao(screen, MENU_Rect, xMouse, yMouse):
		return getItemSelecionadoMenu(screen, xMouse, yMouse)
	elif checarSelecao(screen, MINI_MAPA_Rect, xMouse, yMouse):
		return "Mini mapa"


def checarSelecao(screen, rect, xMouse, yMouse):
	xMouse += screen.window_width() * 0.5
	yMouse = screen.window_height() * 0.5 - yMouse
	return rect["xPos"] + rect["width"] >= xMouse >= rect["xPos"] and  rect["yPos"] + rect["height"] >= yMouse >= rect["yPos"]


def imprimirTexto(turtle, objTxt):
	screen = turtle.getscreen()
	turtle.up()
	turtle.pencolor(objTxt["cor"])
	turtle.goto(transladarParaCentralizado(screen, objTxt["xPos"], objTxt["yPos"]))
	turtle.write(objTxt["texto"], False, "left", (objTxt["fonte"], objTxt["size"], objTxt["tipo"]))


def imprimirMenu(turtle, listaDeItens, objTxtBase, espacamentoVertical):
	ITEM = objTxtBase.copy()
	for item in listaDeItens:
		ITEM["texto"] = item
		ITEM["yPos"] += espacamentoVertical
		imprimirTexto(turtle, ITEM)


def imprimirArquivoInfo(turtle):
	imprimirTexto(turtle, ARQUIVO)
	imprimirTexto(turtle, DIRETORIO)


def imprimirInterface(turtle):
	desenharFillRect(turtle, COIOT_Rect, "#57ff4f")
	desenharFillRect(turtle, CABECALHO_Rect, "#ffffff")
	desenharFillRect(turtle, MENU_Rect, "#ffffff")
	desenharFillRect(turtle, MINI_MAPA_Rect, "#ffffff")
	desenharFillRect(turtle, ABA_Rect, "#ffffff")
	imprimirTexto(turtle, COIOT)
	imprimirMenu(turtle, itensDoMenu, ITEM_MENU, 50)


def desenharFillRect(turtle, rect, cor):
	screen = turtle.getscreen()
	turtle.up()
	turtle.goto(transladarParaCentralizado(screen, rect["xPos"], rect["yPos"]))
	turtle.fillcolor(cor)
	turtle.pensize(1)
	turtle.begin_fill()
	turtle.setx(transladarParaCentralizado(screen, x = rect["xPos"] + rect["width"]))
	turtle.sety(transladarParaCentralizado(screen, y = rect["yPos"] + rect["height"]))
	turtle.setx(transladarParaCentralizado(screen, x = rect["xPos"]))
	turtle.end_fill()


COIOT_Rect=dict(xPos=7, yPos=7, width=250, height=100)
COIOT=dict(texto="Coiot", fonte="Arial", size=50, tipo="bold", cor="White", xPos=45, yPos=95)

CABECALHO_Rect=dict(xPos=COIOT_Rect["width"] + 14, yPos=7, width=1000, height=100)
ARQUIVO=dict(texto="Nenhum arquivo selecionado", fonte="Arial", size=20, tipo="bold", cor="#7a7a7a", xPos=CABECALHO_Rect["xPos"] + 30, yPos=57)
DIRETORIO=dict(texto="...", fonte="Arial", size=15, tipo="italic", cor="#7a7a7a", xPos=ARQUIVO["xPos"], yPos=88)

itensDoMenu=("Abrir arquivo", "Resumo geral", "Resumo por km", "Resumo por volta", "Gráficos", "Sair")
MENU_Rect=dict(xPos=7, yPos=CABECALHO_Rect["height"] + 7 + 7, width=250, height=53 * len(itensDoMenu))
ITEM_MENU=dict(texto='', fonte="Arial", size=15, tipo="bold", cor="#7a7a7a", xPos=MENU_Rect["xPos"] + 30, yPos=MENU_Rect["yPos"] - 5)

MINI_MAPA_Rect = dict(xPos=7, yPos=MENU_Rect["yPos"] + MENU_Rect["height"] + 7, width=MENU_Rect["width"], height=MENU_Rect["width"])

ABA_Rect = dict(xPos=CABECALHO_Rect["xPos"], yPos=CABECALHO_Rect["yPos"] + CABECALHO_Rect["height"] + 7, width=1000, height=700)