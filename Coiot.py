from turtle import Turtle
from Interface import *
from Mensagem import isolarMensagens, selecionarEmRegistros
from Resumo import *
from Grafico import desenharGrafico, desenharCircuito
import Calculos


def carregarArquvio(diretorio):
        global mensagens, coordenadas
        with open(diretorio) as arquivo:
                mensagens = isolarMensagens(arquivo)
                setArquivoInfo(diretorio)
                coordenadas = selecionarEmRegistros(mensagens, ["longitude", "latitude"])


def desenharGraficos():
        TEMP_Rect = CONTEUDO_ABA_Rect.copy()
        if sobreporGraficos:
                imagem = [selecionarEmRegistros(mensagens, "altitude"), selecionarEmRegistros(mensagens, "bpm"), Calculos.Ritmos(selecionarEmRegistros(mensagens, "timeStamp"), selecionarEmRegistros(mensagens, ["longitude", "latitude"]))]
                desenharGrafico(turtles["aba"], CONTEUDO_ABA_Rect, selecionarEmRegistros(mensagens, "timeStamp"), imagem, ["Altitude", "BPM", "Ritmo"])
        else:
                TEMP_Rect["width"] /= 2
                TEMP_Rect["height"] /= 2
                desenharGrafico(turtles["aba"], TEMP_Rect, selecionarEmRegistros(mensagens, "timeStamp"), [Calculos.Ritmos(selecionarEmRegistros(mensagens, "timeStamp"), selecionarEmRegistros(mensagens, ["longitude", "latitude"]))], ["Ritmo"])

                TEMP_Rect["xPos"] += CONTEUDO_ABA_Rect["width"] / 2
                desenharGrafico(turtles["aba"], TEMP_Rect, selecionarEmRegistros(mensagens, "timeStamp"), [selecionarEmRegistros(mensagens, "altitude")], ["Altitude"])

                TEMP_Rect["xPos"] = CONTEUDO_ABA_Rect["xPos"]
                TEMP_Rect["yPos"] += CONTEUDO_ABA_Rect["height"] / 2
                desenharGrafico(turtles["aba"], TEMP_Rect, selecionarEmRegistros(mensagens, "timeStamp"), [selecionarEmRegistros(mensagens, "bpm")], ["BPM"])

                TEMP_Rect["xPos"] += CONTEUDO_ABA_Rect["width"] / 2
                desenharGrafico(turtles["aba"], TEMP_Rect, selecionarEmRegistros(mensagens, "timeStamp"), [selecionarEmRegistros(mensagens, "bpm")], ["BPM"], True)


def tratarEventoSubMenu(selecao, xMouse, yMouse):
        global considerarPausa, subMenu, msgSobreporGraficos, msgConsiderarPausa, sobreporGraficos, resumoPorVolta

        if selecao[0]:
                if abaSelecionada != "Gráficos" and abaSelecionada != "Percurso":
                        considerarPausa = not considerarPausa
                        if considerarPausa:
                                msgConsiderarPausa = "Desconsiderar pausas"
                        else:
                                msgConsiderarPausa = "Considerar pausas"
                        subMenu[1] = [msgConsiderarPausa]
                        if abaSelecionada == "Resumo geral":
                                resumoGeral = gerarResumoGeral(mensagens, considerarPausa)
                        elif abaSelecionada == "Resumo por km":
                                resumoPorKm = gerarResumoPorKm(mensagens, False)
                        elif abaSelecionada == "Resumo por volta":
                                resumoPorVolta = gerarResumoPorVolta(mensagens, considerarPausa)
                elif abaSelecionada == "Gráficos":
                        sobreporGraficos = not sobreporGraficos
                        if sobreporGraficos:
                                msgSobreporGraficos = "Separar gráficos"
                        else:
                                msgSobreporGraficos = "Mesclar gráficos"
                        subMenu[1] = [msgSobreporGraficos]
        abaSelecionadaNoSubMenu = selecao[1]

        turtles["aba"].clear()
        imprimirTexto(turtles["aba"], TITULO_ABA)
        imprimirSubMenu(turtles["aba"], subMenu)
        if abaSelecionada == "Resumo geral":
                imprimirResumo(turtles["aba"], CONTEUDO_ABA_Rect, resumoGeral)
        elif abaSelecionada == "Resumo por km":
                imprimirResumo(turtles["aba"], CONTEUDO_ABA_Rect, resumoPorKm[abaSelecionadaNoSubMenu])
        elif abaSelecionada == "Resumo por volta":
                imprimirResumo(turtles["aba"], CONTEUDO_ABA_Rect, resumoPorVolta[abaSelecionadaNoSubMenu])
        elif abaSelecionada == "Gráficos":
                desenharGraficos()


def tratarEvento(xMouse, yMouse):
        global abaSelecionada, resumoGeral, resumoPorKm, resumoPorVolta, subMenu
        temp = getItemSelecionado(screen, xMouse, yMouse)
        if temp: abaSelecionada = temp

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
        elif checarSelecao(screen, MENU_Rect, xMouse, yMouse) or checarSelecao(screen, MINI_MAPA_Rect, xMouse, yMouse):
                turtles["aba"].clear()
                TITULO_ABA["texto"] = abaSelecionada
                imprimirTexto(turtles["aba"], TITULO_ABA)
                if mensagens:
                        if abaSelecionada == "Resumo geral":
                                resumoGeral = gerarResumoGeral(mensagens, considerarPausa)
                                if resumoGeral:
                                        subMenu = [[], [msgConsiderarPausa]]
                                else:
                                        subMenu = [[], []]
                                imprimirResumo(turtles["aba"], CONTEUDO_ABA_Rect, resumoGeral)
                        elif abaSelecionada == "Resumo por km":
                                resumoPorKm = gerarResumoPorKm(mensagens, considerarPausa)
                                if resumoPorKm:
                                        subMenu = [["Km " + str(x+1) for x in range(len(resumoPorKm))], [msgConsiderarPausa]]
                                else:
                                        subMenu = [[], []]
                                imprimirResumo(turtles["aba"], CONTEUDO_ABA_Rect, resumoPorKm[abaSelecionadaNoSubMenu])
                        elif abaSelecionada == "Resumo por volta":
                                resumoPorVolta = gerarResumoPorVolta(mensagens)
                                print(resumoPorVolta)
                                if resumoPorVolta:
                                        subMenu = [["Lap "+str(x+1) for x in range(len(resumoPorVolta))], [msgConsiderarPausa]]
                                else:
                                        subMenu = [[], []]
                                imprimirResumo(turtles["aba"], CONTEUDO_ABA_Rect, resumoPorVolta[abaSelecionadaNoSubMenu])
                        elif abaSelecionada == "Gráficos":
                                subMenu = [[], [msgSobreporGraficos]]
                                desenharGraficos()
                        elif abaSelecionada == "Percurso":
                                subMenu = [[], []]
                                desenharCircuito(turtles["aba"], CONTEUDO_ABA_Rect, coordenadas)

                        if subMenu:
                                imprimirSubMenu(turtles["aba"], subMenu)
        elif subMenu:
                selecao = checarSelecaoSubMenu(screen, subMenu, xMouse, yMouse)
                if selecao:
                        tratarEventoSubMenu(selecao, xMouse, yMouse)


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
                        imprimirTexto(turtles["aba"], TITULO_ABA)
                        if abaSelecionada == "Resumo geral":
                                imprimirResumo(turtles["aba"], CONTEUDO_ABA_Rect, resumoGeral)
                        elif abaSelecionada == "Resumo por km":
                                imprimirResumo(turtles["aba"], CONTEUDO_ABA_Rect, resumoPorKm[abaSelecionadaNoSubMenu])
                        elif abaSelecionada == "Resumo por volta":
                                imprimirResumo(turtles["aba"], CONTEUDO_ABA_Rect, resumoPorVolta[abaSelecionadaNoSubMenu])
                        elif abaSelecionada == "Gráficos":
                                desenharGraficos()
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
considerarPausa = True
msgConsiderarPausa = "Desconsiderar pausas"
sobreporGraficos = False
msgSobreporGraficos = "Mesclar gráficos"
abaSelecionadaNoSubMenu = 0
resumoGeral = None
resumoPorKm = None
resumoPorVolta = None
coordenadas = None

atualizar()
imprimirInterface(turtle)
imprimirArquivoInfo(turtles["arquivoInfo"])

screen.mainloop()
