from tkinter import filedialog
from Mensagem import isolarMensagens


def abrirArquivo():
	with open(filedialog.askopenfilename(filetypes = [("Text files", "*.txt")])) as arquivo:
		return isolarMensagens(arquivo)


def tratarEvento(xMouse, yMouse):
	if True:
		return abrirArquivo()


def imprimirInterface():
	pass
