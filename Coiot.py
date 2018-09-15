from turtle import Turtle
from Interface import imprimirInterface, selecionarArquivo, setArquivoInfo


def tratarEvento(xMouse, yMouse):
    # O problema é o tamanho da fonte
    escx = screen.window_width() / 1366
    escy = screen.window_height() / 768
    coords = [(-647*escx, -547*escx, 174*escy, 189*escy)]
    i = 0
    pull = 0
    while i < len(coords) and pull == 0:
        if coords[i][0] <= xMouse <= coords[i][1] and coords[i][2] <= yMouse <= coords[i][3]:
            print("foi")
            pull += 1
        i += 1
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
