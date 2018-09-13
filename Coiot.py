from turtle import Turtle
from Interface import iniciarInterface, selecionarArquivo, setArquivoInfo


def tratarEvento(xMouse, yMouse):
	turtle.clear()
	setArquivoInfo(selecionarArquivo())
	iniciarInterface(turtle)


turtle = Turtle()
turtle.hideturtle()
turtle.speed(0)

screen = turtle.getscreen()
screen.title("Coiot")
screen.setup(910, 512)
screen.delay(0)
screen.onclick(tratarEvento)

iniciarInterface(turtle)

screen.mainloop()
