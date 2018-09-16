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
	global abaSelecionada, resumoGeral, resumoPorKm, resumoPorVolta, subMenu
	abaSelecionada = getItemSelecionado(screen, xMouse, yMouse)
	subMenu = None

	if abaSelecionada == "Abrir arquivo":
		diretorio = selecionarArquivo()
		if diretorio:
			carregarArquvio(diretorio)
			for i in turtles:
				turtles[i].clear()
			imprimirArquivoInfo(turtles["arquivoInfo"])
			desenharCircuito(turtles["miniMapa"], MINI_MAPA_Rect, coordenadas)
	elif abaSelecionada == "Sair":
		screen.bye()
	else:
		turtles["aba"].clear()
		TITULO_ABA["texto"] = abaSelecionada
		imprimirTexto(turtles["aba"], TITULO_ABA)
		if abaSelecionada == "Resumo geral":
			resumoGeral = gerarResumoGeral(mensagens)
			subMenu = [[], ["Desconsiderar pausas"]]
			imprimirResumoGeral(turtles["aba"], CONTEUDO_ABA_Rect, resumoGeral)
		elif abaSelecionada == "Resumo por km":
			resumoPorKm = gerarResumoPorKm(mensagens)
			subMenu = [["Km " + str(x+1) for x in range(5)], ["Desconsiderar pausas"]]
			imprimirResumoPorKm(turtles["aba"], CONTEUDO_ABA_Rect, resumoPorKm)
		elif abaSelecionada == "Resumo por volta":
			resumoPorVolta = gerarResumoPorVolta(mensagens)
			subMenu = [["Lap " + str(x+1) for x in range(7)], ["Desconsiderar pausas"]]
			imprimirResumoPorVolta(turtles["aba"], CONTEUDO_ABA_Rect, resumoPorVolta)
		elif abaSelecionada == "Gráficos":
			subMenu = [["Ritmo", "Altitude", "BPM", "Zonas de BPM"], ["Sobrepor gráficos"]]
			pass
		elif abaSelecionada == "Mini mapa" and mensagens:
			desenharCircuito(turtles["aba"], CONTEUDO_ABA_Rect, coordenadas)

		if subMenu:
			imprimirSubMenu(turtles["aba"], subMenu)


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
		if abaSelecionada == "Abrir arquivo":
			pass
		else:
			imprimirTexto(turtles["aba"], TITULO_ABA)
			if abaSelecionada == "Resumo geral":
				imprimirResumoGeral(turtles["aba"], CONTEUDO_ABA_Rect, resumoGeral)
			elif abaSelecionada == "Resumo por km":
				imprimirResumoPorKm(turtles["aba"], CONTEUDO_ABA_Rect, resumoPorKm)
			elif abaSelecionada == "Resumo por volta":
				imprimirResumoPorVolta(turtles["aba"], CONTEUDO_ABA_Rect, resumoPorVolta)
			if subMenu:
				imprimirSubMenu(turtles["aba"], subMenu)
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
subMenu = None
resumoGeral = None
resumoPorKm = None
resumoPorVolta = None
coordenadas = None

atualizar()
imprimirInterface(turtle)
imprimirArquivoInfo(turtles["arquivoInfo"])

screen.mainloop()
