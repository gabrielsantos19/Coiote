from geopy import distance
import time

def findices(lst):
    indices = []
    i_inicial = 0
    i_final = 0
    cont = 0
    for i, x in enumerate(lst):
        for y in x:
            if y[0] == "e":
                cont += 1
            elif y == "f" or y == "p":
                i_final = i
                cont += 1
            elif y == "i" or y == "r":
                i_inicial = i
                cont += 1

            if cont == 2:
                indices.append( (i_inicio, i_final) )
                cont = 0
    return indices
    
def encontrarValido(lst, indice):
    for i in range(indice + 1, len(lst)):
        if lst[i] != -1:
            return i
    return len(lst) - 1

def mediaPonderada(lst):
    resultado = 0
    i = 1
    while i < len(lst):
        if lst[i] != -1: 
            novoI = i
            mediaArit = (lst[i] + lst[i-1]) / 2
        else:
            novoI = encontrarValido(lst, i)
            mediaArit = (lst[i-1] + lst[novoI]) / 2
        resultado += mediaArit * (novoI - (i-1))
        i += 1
    return resultado

def Distancia(Geolocs):
    delta_space = 0.0
    i = 1
    while i != len(Geolocs):
        try:    
            delta_space += distance.distance((Geolocs[i]["latitude"], Geolocs[i]["longitude"]), (Geolocs[i-1]["latitude"], Geolocs[i-1]["longitude"])).km
        except:
            pass
        i += 1
    return delta_space

def difAltitudes(alts):
    inicio = 0
    fim = len(alts) - 1
    for altitude in alts:
        if altitude == {}:
            inicio += 1
        else:
            break
    for i in range(len(alts), inicio):
        if alts[i] == {}:
            fim = i - 1
        else:
            break
    if inicio > fim:
        return -1
    else:
        return alts[fim]["altitude"] - alts[inicio]["altitude"]

    return (regis[-1]-regis[0])/60 // distancia(Geolocs)


def Ritmos(regis, Geolocs):
    resultado = []
    for i in range(1, len(regis)):
        try:
            resultado.append({"ritmo": (float(regis[i]["timeStamp"]) - float(regis[i-1]["timeStamp"])) / 60 // Distancia(Geolocs[i-1:i+1])})
        except ZeroDivisionError:
            resultado.append({})
    return resultado


def converterTempo(tempo):
    hora = time.strftime("%H", time.gmtime(tempo))
    if tempo < 7200:
        hora += " hora"
    else:
        hora += "horas"
    minutos = time.strftime("%M", time.gmtime(tempo)) + " minutos"
    segundos = time.strftime("%S", time.gmtime(tempo)) + " segundos"
    if hora[0:2] == "00":
        hora = ""
    if minutos[0:2] == "00":
        minutos = "" 
        hora = hora
    if segundos[0:2] == "00":
        segundos = ""
    resultado = hora + minutos + segundos
    return resultado


def Afastamento(coordenadas, escx, escy, rect, origens):
    minX, maxX = escx * (min([v["x"] for v in coordenadas]) - origens[0]) + rect["width"] / 2, escx * (max([v["x"] for v in coordenadas]) - origens[0]) + rect["width"] / 2
    minY, maxY = escy * (min([v["y"] for v in coordenadas]) - origens[1]) + rect["height"] / 2, escy * (max([v["y"] for v in coordenadas]) - origens[1]) + rect["height"] / 2
    distX = (rect["width"] - maxX) - minX
    distY = (rect["height"] - maxY) - minY
    return distX, distY
