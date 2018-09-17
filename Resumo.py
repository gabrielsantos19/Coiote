from Interface import imprimirTexto
from Mensagem import selecionarEmRegistros
import Calculos


def imprimirResumoPorVolta(turtle, rect, resumoPorVolta):
    # resumoPorVolta possui o q gerarResumoPorVolta retornar
    pass


def imprimirResumoPorKm(turtle, rect, resumoPorKm):
    # resumoPorKm possui o q gerarResumoPorKm retornar
    pass


def imprimirResumoGeral(turtle, rect, resumoGeral):
    # resumoGeral possui o q gerarResumoGeral retornar
    ITEM = dict(texto="", fonte="Arial", size=15, align="left", tipo="", cor="#7a7a7a", xPos=rect["xPos"] + 30, yPos=rect["yPos"])
    for item in resumoGeral.items():
            ITEM["xPos"] = rect["xPos"] + 40
            for i in item:
                    ITEM["texto"] = i
                    imprimirTexto(turtle, ITEM)
                    ITEM["xPos"] += rect["width"] * 0.5
            ITEM["yPos"] += 30


def gerarResumoPorVolta(mensagens):
    print(mensagens)
    # essa função recebe todas as mensagens
    # o q ela retornar será usado para chamar imprimirResumoPorVolta


def gerarResumoPorKm(mensagens, tipo="sem pausa"):
    listaDeGeolocalizacoes = selecionarEmRegistros(mensagens, ["longitude", "latitude"])
    altitudes = selecionarEmRegistros(mensagens, ["altitude"])
    i = 2
    inicio = 1
    km = 0
    distAtual = 0
    listaKM = []
    while i < len(altitudes) + 1:
        distAtual += Calculos.Distancia(listaDeGeolocalizacoes[i-1:i+1])
        if distAtual >= 1 or i == len(mensagens) - 2:
            resultadoGeral = fResumo(mensagens[inicio:i+1], tipo)
            resultadoGeral["Ganho/perda de altitude"] = Calculos.difAltitudes(altitudes)
            listaKM.append({key: value for key, value in resultadoGeral.items() if key not in ["Altitude máxima", "Altitude mínima", "BPM máxima", "BPM mínima", "Distância total"] and value != -1})
            km += 1
            distAtual = 0
            inicio = i
        i += 1
    return listaKM


def gerarResumoGeral(mensagens, tipo="sem pausa"):
    resultado = fResumo(mensagens, tipo)
    return {key: value for key, value in resultado.items() if value != -1}


def fResumo(mensagens, tipo):
    listaDeGeolocalizacoes = selecionarEmRegistros(mensagens, ["longitude", "latitude"])
    dados = selecionarEmRegistros(mensagens, ["timeStamp", "altitude", "bpm", "numeroDePassos"])
    if tipo != "sem pausa":
        indices = fIndices(tipo)
    else:
        indices = [(0, len(dados) + 1)]
    dist = 0
    duracao = 0
    somaPassos = 0
    mpBPM = 0
    bpmMAX, bpmMIN, altMAX, altMIN = (-1,) * 4 
    for i in indices:
        dist += Calculos.Distancia(listaDeGeolocalizacoes[i[0]:i[1]])
        duracao += float(dados[i[1]-2]["timeStamp"]) - float(dados[i[0]]["timeStamp"])
        dadosParte = dados[i[0]:i[1]]
        mpBPM += operarItens(dadosParte, "bpm", "media ponderada", float(dados[-1]["timeStamp"]) - float(dados[0]["timeStamp"]))
        somaPassos += operarItens(dadosParte, "numeroDePassos", "soma")
        bpmMAXtemp = operarItens(dadosParte, "bpm", "maximo")
        altMAXtemp = operarItens(dadosParte, "altitude", "maximo")
        bpmMIN = operarItens(dadosParte, "bpm", "minimo")
        altMIN = operarItens(dadosParte, "altitude", "minimo")
        if bpmMAXtemp > bpmMAX:
            bpmMAX = bpmMAXtemp
        if altMAXtemp > altMAX:
            altMAX = altMAXtemp

    if somaPassos == 0:
        cadencia = -1
    else:
        cadencia = somaPassos // (duracao / 60)

    if mpBPM < 0:
        mpBPM = -1

    ritmo = (duracao / 60) // dist
            
    return {"Distância total": "{:.2f} km".format(dist), "Tempo total": duracao / 60, "Média ponderada de BPM": "{:.0f}".format(mpBPM),"Ritmo médio": "{:.0f} mins/km".format(ritmo), "BPM máximo": "{:.0f}".format(bpmMAX), "BPM mínimo": "{:.0f}".format(bpmMIN), "Cadência": "{:.0f} passos/min".format(cadencia), "Altitude máxima": "{:.6f}".format(altMAX), "Altitude mínima": "{:.6f}".format(altMIN)}


def operarItens(lista, item, operacao, tempo=0.0):
    lst = []
    resultado = 0
    for x in lista:
        try:
            lst.append(x[item])
        except KeyError:
            if item == "numeroDePassos":
                lst.append(0)
            else:
                lst.append(-1)
    if operacao == "soma":
        return max(lst)
    elif operacao == "maximo":
        return max(lst)
    elif operacao == "minimo":
        return minimo(lst)
    else:
        return Calculos.mediaPonderada(lst, tempo)


def minimo(lst):
    minimo = max(lst)
    for x in lst:
        if x < minimo and x != -1:
            minimo = x
    return minimo
            

