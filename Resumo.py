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
    ITEM = dict(texto="", fonte="Arial", size=15, tipo="", cor="#7a7a7a", xPos=rect["xPos"] + 30, yPos=rect["yPos"])
    for item in resumoGeral.items():
            ITEM["xPos"] = rect["xPos"] + 40
            for i in item:
                    ITEM["texto"] = i
                    imprimirTexto(turtle, ITEM)
                    ITEM["xPos"] += rect["width"] * 0.5
            ITEM["yPos"] += 30


def gerarResumoPorVolta(mensagens):
    # essa função recebe todas as mensagens
    # o q ela retornar será usado para chamar imprimirResumoPorVolta
    pass


def gerarResumoPorKm(mensagens):
    # essa função recebe todas as mensagens
    # o q ela retornar será usado para chamar imprimirResumoPorKm
    pass


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
    bpmMAX, bpmMIN, altMAX, altMIN = (-1,) * 4 
    for i in indices:
        dist += Calculos.Distancia(listaDeGeolocalizacoes[i[0]:i[1]])
        duracao += float(dados[i[1]-2]["timeStamp"]) - float(dados[i[0]]["timeStamp"])
        dadosParte = dados[i[0]:i[1]]
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

    ritmo = (duracao / 60) // dist
            
    return {"Distância total": dist, "Tempo total": duracao / 60, "Ritmo médio": ritmo, "BPM máximo": bpmMAX, "BPM mínimo": bpmMIN, "Cadência": cadencia, "Altitude máxima": altMAX, "Altitude mínima": altMIN}


def operarItens(lista, item, operacao):
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
    else:
        return minimo(lst)


def minimo(lst):
    minimo = max(lst)
    for x in lst:
        if x < minimo and x != -1:
            minimo = x
    return minimo
            

