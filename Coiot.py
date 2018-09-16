from turtle import Turtle
from Interface import *
from Mensagem import isolarMensagens, selecionarEmRegistros
from Resumo import *
from Grafico import desenharCircuito


def carregarArquvio(diretorio):
	global mensagens, coordenadas
	with open(diretorio) as arquivo:
		mensagens = isolarMensagens(arquivo)
		setArquivoInfo(diretorio)
		coordenadas = selecionarEmRegistros(mensagens, ["longitude", "latitude"])


def tratarEvento(xMouse, yMouse):
	global abaSelecionada, resumoGeral, resumoPorKm, resumoPorVolta
	abaSelecionada = getItemSelecionado(screen, xMouse, yMouse)

	if abaSelecionada == "Abrir arquivo":
		diretorio = selecionarArquivo()
		if diretorio:
			carregarArquvio(diretorio)
			for i in turtles:
				turtles[i].clear()
			imprimirArquivoInfo(turtles["arquivoInfo"])
			desenharCircuito(turtles["miniMapa"], MINI_MAPA_Rect, coordenadas)
	elif abaSelecionada == "Resumo geral":
		resumoGeral = gerarResumoGeral(mensagens)
		turtles["aba"].clear()
		imprimirResumoGeral(turtles["aba"], ABA_Rect, resumoGeral)
	elif abaSelecionada == "Resumo por km":
		resumoPorKm = gerarResumoPorKm(mensagens)
		turtles["aba"].clear()
		imprimirResumoPorKm(turtles["aba"], ABA_Rect, resumoPorKm)
	elif abaSelecionada == "Resumo por volta":
		resumoPorVolta = gerarResumoPorVolta(mensagens)
		turtles["aba"].clear()
		imprimirResumoPorVolta(turtles["aba"], ABA_Rect, resumoPorVolta)
	elif abaSelecionada == "Gráficos":
		turtles["aba"].clear()
		pass
	elif abaSelecionada == "Sair":
		screen.bye()
	elif abaSelecionada == "Mini mapa":
		turtles["aba"].clear()
		desenharCircuito(turtles["miniMapa"], ABA_Rect, coordenadas)


def atualizar():
	global oldWidth, oldHeight
	if oldWidth != screen.window_width() or oldHeight != screen.window_height():
		oldWidth, oldHeight = screen.window_width(), screen.window_height()
		turtle.clear()
		for i in turtles:
			turtles[i].clear()
		imprimirInterface(turtle)
		imprimirArquivoInfo(turtles["arquivoInfo"])
		if mensagens:
			desenharCircuito(turtles["miniMapa"], MINI_MAPA_Rect, coordenadas)
		if abaSelecionada == "Resumo geral":
			imprimirResumoGeral(turtles["aba"], ABA_Rect, resumoGeral)
		elif abaSelecionada == "Resumo por km":
			imprimirResumoPorKm(turtles["aba"], ABA_Rect, resumoPorKm)
		elif abaSelecionada == "Resumo por volta":
			imprimirResumoPorVolta(turtles["aba"], ABA_Rect, resumoPorVolta)
	screen.ontimer(atualizar, 300)



turtle = Turtle()
turtle.hideturtle()
turtle.speed(0)

turtles = dict(arquivoInfo=Turtle(), aba=Turtle(), miniMapa=Turtle())
for i in turtles:
	turtles[i].hideturtle()
	turtles[i].speed(0)

screen = turtle.getscreen()
screen.title("Coiot")
screen.setup(910, 512)
screen.bgcolor("#e8e8e8")
screen.delay(0)
screen.onclick(tratarEvento)

oldWidth, oldHeight = screen.window_width(), screen.window_height()
mensagens = []
abaSelecionada = None
resumoGeral = None
resumoPorKm = None
resumoPorVolta = None
coordenadas = None

atualizar()
imprimirInterface(turtle)
imprimirArquivoInfo(turtles["arquivoInfo"])

screen.mainloop()
