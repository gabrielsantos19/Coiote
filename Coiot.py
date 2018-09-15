from turtle import Turtle
from Interface import imprimirInterface, selecionarArquivo, setArquivoInfo


def tratarEvento(xMouse, yMouse):
	diretorioDoArquivo = selecionarArquivo()
	setArquivoInfo(diretorioDoArquivo)
	turtle.clear()
	imprimirInterface(turtle)


def atualizar():
	global oldWidth, oldHeight
	if oldWidth != screen.window_width() or oldHeight != screen.window_height():
		oldWidth, oldHeight = screen.window_width(), screen.window_height()
		turtle.clear()
		imprimirInterface(turtle)
	screen.ontimer(atualizar, 300)


turtle = Turtle()
turtle.hideturtle()
turtle.speed(0)

screen = turtle.getscreen()
screen.title("Coiot")
screen.setup(910, 512)
screen.delay(0)
screen.onclick(tratarEvento)

oldWidth, oldHeight = screen.window_width(), screen.window_height()
mensagens = []

imprimirInterface(turtle)
atualizar()

screen.mainloop()
