from tkinter import filedialog


def selecionarArquivo():
	return filedialog.askopenfilename(filetypes = [("Text files", "*.txt")])


def transladar(screen, x = None, y = None):
	if x != None and y != None:
		return -screen.window_width() * 0.5 + x, screen.window_height() * 0.5 - y
	elif x != None:
		return -screen.window_width() * 0.5 + x
	elif y != None:
		return screen.window_height() * 0.5 - y


def imprimirTexto(turtle, objTxt):
	screen = turtle.getscreen()
	turtle.up()
	turtle.goto(transladar(screen, objTxt["xPos"], objTxt["yPos"]))
	turtle.write(objTxt["texto"], False, "left", (objTxt["fonte"], objTxt["size"], objTxt["tipo"]))


def imprimirMenu(turtle, listaDeItens, objTxtBase, espacamentoVertical):
	ITEM = objTxtBase.copy()
	for item in listaDeItens:
		ITEM["texto"] = item
		ITEM["yPos"] += espacamentoVertical
		imprimirTexto(turtle, ITEM)


def desenharFillRect(turtle, rect, cor):
	screen = turtle.getscreen()
	turtle.up()
	turtle.goto(transladar(screen, rect["xPos"], rect["yPos"]))
	turtle.fillcolor(cor)
	turtle.pensize(1)
	turtle.begin_fill()
	turtle.setx(transladar(screen, x = rect["xPos"] + rect["width"]))
	turtle.sety(transladar(screen, y = rect["yPos"] + rect["height"]))
	turtle.setx(transladar(screen, x = rect["xPos"]))
	turtle.end_fill()