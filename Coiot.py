from turtle import Screen


def tratarEvento(xMouse, yMouse):
	pass


screen = Screen()
screen.title("Coiot")
screen.setup(910, 512)
screen.delay(0)

screen.onclick(tratarEvento)
screen.listen()

screen.mainloop()
