from turtle import Turtle
from Interface import *
from Mensagem import isolarMensagens


def setArquivoInfo(diretorio):
	ARQUIVO["texto"] = diretorio.split('/')[-1][:-4]
	DIRETORIO["texto"] = '"' + diretorio + '"'


def getItemSelecionadoMenu(xMouse, yMouse):
	TEMP_BOX = MENU_Rect.copy()
	TEMP_BOX["height"] = MENU_Rect["height"] / len(itensDoMenu)
	for item in itensDoMenu:
		if checarSelecao(TEMP_BOX, xMouse, yMouse):
			return item
		TEMP_BOX["yPos"] += TEMP_BOX["height"]


def getItemSelecionado(xMouse, yMouse):
	if checarSelecao(screen, MENU_Rect, xMouse, yMouse):
		return getItemSelecionadoMenu(xMouse, yMouse)


def carregarArquvio(diretorio):
	global mensagens
	with open(diretorio) as arquivo:
		arquivo.readline()
		mensagens = isolarMensagens(arquivo)
		setArquivoInfo(diretorio)


def tratarEvento(xMouse, yMouse):
	selecao = getItemSelecionado(xMouse, yMouse)
	if selecao == "Abrir arquivo":
		diretorio = selecionarArquivo()
		if diretorio: carregarArquvio(diretorio)
		turtle.clear()
		imprimirInterface()
	elif selecao == "Resumo geral":
		
		pass
	elif selecao == "Resumo por km":
		pass
	elif selecao == "Resumo por volta":
		pass
	elif selecao == "Gráficos":
		pass
	elif selecao == "Sair":
		screen.bye()


def imprimirInterface():
	desenharFillRect(turtle, COIOT_Rect, "#57ff4f")
	desenharFillRect(turtle, CABECALHO_Rect, "#ffffff")
	desenharFillRect(turtle, MENU_Rect, "#ffffff")
	imprimirTexto(turtle, COIOT)
	imprimirTexto(turtle, ARQUIVO)
	imprimirTexto(turtle, DIRETORIO)
	imprimirMenu(turtle, itensDoMenu, ITEM_MENU, 50)


def atualizar():
	global oldWidth, oldHeight
	if oldWidth != screen.window_width() or oldHeight != screen.window_height():
		oldWidth, oldHeight = screen.window_width(), screen.window_height()
		turtle.clear()
		imprimirInterface()
	screen.ontimer(atualizar, 300)



turtle = Turtle()
turtle.hideturtle()
turtle.speed(0)

screen = turtle.getscreen()
screen.title("Coiot")
screen.setup(910, 512)
screen.bgcolor("#e8e8e8")
screen.delay(0)
screen.onclick(tratarEvento)

# Interface
COIOT_Rect=dict(xPos=7, yPos=7, width=250, height=100)
COIOT=dict(texto="Coiot", fonte="Arial", size=50, tipo="bold", cor="White", xPos=45, yPos=95)
CABECALHO_Rect=dict(xPos=COIOT_Rect["width"] + 14, yPos=7, width=1000, height=100)
ARQUIVO=dict(texto="Nenhum arquivo selecionado", fonte="Arial", size=20, tipo="bold", cor="#7a7a7a", xPos=CABECALHO_Rect["xPos"] + 30, yPos=57)
DIRETORIO=dict(texto="...", fonte="Arial", size=15, tipo="italic", cor="#7a7a7a", xPos=ARQUIVO["xPos"], yPos=88)

itensDoMenu=("Abrir arquivo", "Resumo geral", "Resumo por km", "Resumo por volta", "Gráficos", "Sair")
MENU_Rect=dict(xPos=7, yPos=CABECALHO_Rect["height"] + 7 + 7, width=250, height=53 * len(itensDoMenu))
ITEM_MENU=dict(texto='', fonte="Arial", size=15, tipo="bold", cor="#7a7a7a", xPos=MENU_Rect["xPos"] + 30, yPos=MENU_Rect["yPos"] - 5)


oldWidth, oldHeight = screen.window_width(), screen.window_height()
mensagens = []
turtleResumo = turtle
turtleGrafico = turtle

imprimirInterface()
atualizar()

screen.mainloop()
