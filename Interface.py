from tkinter import filedialog


def selecionarArquivo():
	return filedialog.askopenfilename(filetypes = [("Text files", "*.txt")])


def setArquivoInfo(diretorio):
	ARQUIVO["texto"] = diretorio.split('/')[-1][:-4]
	DIRETORIO["texto"] = '"' + diretorio + '"'


def imprimirTexto(turtle, objTxt):
	screen = turtle.getscreen()
	turtle.up()
	turtle.goto(screen.window_width() * objTxt["xPos"], screen.window_height() * objTxt["yPos"])
	turtle.write(objTxt["texto"], False, "left", (objTxt["fonte"], int(screen.window_height() * objTxt["size"]), objTxt["type"]))


def iniciarInterface(turtle):
	imprimirTexto(turtle, COIOT)
	imprimirTexto(turtle, ARQUIVO)
	imprimirTexto(turtle, DIRETORIO)


# Objetos de texto
COIOT = {"texto":"Coiot", "fonte": "Arial", "size": 0.07, "type": "normal", "xPos": -0.48, "yPos": 0.38}
ARQUIVO = {"texto":"Nenhum arquivo selecionado", "fonte": "Arial", "size": 0.03, "type": "bold", "xPos": -0.32, "yPos": 0.43}
DIRETORIO = {"texto":"...", "fonte": "Arial", "size": 0.02, "type": "italic", "xPos": -0.32, "yPos": 0.395}