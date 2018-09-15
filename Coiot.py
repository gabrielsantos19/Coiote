from turtle import Turtle
from Interface import imprimirTexto, imprimirMenu, selecionarArquivo, desenharFillRect


def setArquivoInfo(diretorio):
	ARQUIVO["texto"] = diretorio.split('/')[-1][:-4]
	DIRETORIO["texto"] = '"' + diretorio + '"'


def tratarEvento(xMouse, yMouse):
	diretorioDoArquivo = selecionarArquivo()
	setArquivoInfo(diretorioDoArquivo)
	turtle.clear()
	imprimirInterface()


def imprimirInterface():
	desenharFillRect(turtle, CABECALHO_Rect, "#80ff77")
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
CABECALHO_Rect = dict(xPos = 0, yPos = 0, width = 800, height = 100)
COIOT = dict(texto = "Coiot", fonte = "Arial", size = 50, tipo = "normal", xPos = 35, yPos = 90)
ARQUIVO = dict(texto = "Nenhum arquivo selecionado", fonte = "Arial", size = 20, tipo = "bold", xPos = 240, yPos = 50)
DIRETORIO = dict(texto = "...", fonte = "Arial", size = 15, tipo = "italic", xPos = ARQUIVO["xPos"], yPos = 80)

itensDoMenu = ("Resumo geral", "Resumo por km", "Resumo por volta", "Gráficos")
MENU_Rect = dict(xPos = 10, yPos = CABECALHO_Rect["height"] + 10, width = 250, height = 55 * len(itensDoMenu))
ITEM_MENU = dict(texto = "", fonte = "Arial", size = 15, tipo = "normal", xPos = 35, yPos = MENU_Rect["yPos"])


oldWidth, oldHeight = screen.window_width(), screen.window_height()
mensagens = []

imprimirInterface()
atualizar()

screen.mainloop()
