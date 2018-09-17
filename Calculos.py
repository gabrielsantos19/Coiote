from geopy import distance

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

def mediaPonderada(lst, tempo):
    resultado = 0
    i = 1
    while i < len(lst):
        if lst[i] != -1: 
            novoI = i
            mediaArit = (lst[i] + lst[i-1]) / 2
        else:
            novoI = encontrarValido(lst, i)
            mediaArit = (lst[i-1] + lst[novoI]) / 2
        resultado += mediaArit * ((novoI - (i-1)) / tempo)
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


"""def ritmo(regis, Geolocs):
    return (regis[-1]-regis[0])/60 // distancia(Geolocs)


def Ritmos(regis, Geolocs):
    resultado = []
    for i in range(1, len(regis)):
        try:
            resultado.append((regis[i-1] - regis[i]) / 60 // Distancia(Geolocs))
    return resultado

def cadencia(tempos, passos):
    return sum(passos) // (tempos[-1]-tempos[0])/60

def resumo_corrida(dados, tempos, lat, longi, alt, pausa):
    if pausa:
        indices = findices(dados)
    else:
        indices = [(0, len(dados))]
    dist = 0
    dur = 0
    for i in indices:
        dist += distancia(lat[i[0]:i[1]], longi[i[0]:i[1]])
        dur += duracao(tempos[i[0]:i[1]])
    return [dist, dur, max(alt), min(alt)]

def percurso(lat, longi):
    coords = []
    for i in range(len(lat)):
        infos = from_latlon(lat[i], longi[i])
        if i == 0:
            dif_lat, dif_longi = infos[0], infos[1]
        coords.append(((infos[0]-dif_lat)*0.15, (infos[1]-dif_longi)*0.15))
        print(coords[-1])
    return coords


def converterTempo(tempo):
    return time.strtime("%H:%M:%S", time.gmtime(tempo))"""


