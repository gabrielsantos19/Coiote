from tkinter import filedialog


def selecionarArquivo():
	return filedialog.askopenfilename(filetypes = [("Text files", "*.txt")])


def transladarParaCentralizado(screen, x = None, y = None):
	if x != None and y != None:
		return -screen.window_width() * 0.5 + x, screen.window_height() * 0.5 - y
	elif x != None:
		return -screen.window_width() * 0.5 + x
	elif y != None:
		return screen.window_height() * 0.5 - y


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


def desenharMenuIcone(turtle, rect):
	pass