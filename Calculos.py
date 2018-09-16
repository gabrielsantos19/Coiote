from geopy import distance

"""def findices(lst):
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
    
def encontrar_non_zero(lst, indice):
    for i in range(indice+1, len(lst)):
        if lst[i] != 0:
            return i
    return len(lst) - 1

def media_pond(lst):
    resultado = 0
    i = 1
    while i < len(lst):
        if lst[i] != 0: 
            novo_i = i
            media_arit = (lst[i] + lst[i-1]) / 2
        else:
            novo_i = encontrar_non_zero(lst, i)
            media_arit = (lst[i-1] + lst[novo_i]) / 2
        resultado += media_arit * ( (novo_i-(i-1)) / len(lst))
    return resultado

def duracao(tempos):
    return tempos[-1] - tempos[0]"""

def Distancia(Geolocs):
    delta_space = 0
    i = 1
    while i != len(Geolocs):
        try:    
            delta_space += distance.distance((Geolocs[i]["latitude"], Geolocs[i]["longitude"]), (Geolocs[i-1]["latitude"], Geolocs[i-1]["longitude"])).km
        except:
            pass
        i += 1
    return delta_space


"""def ritmo(regis, lat, longi):
    return (regis[-1]-regis[0])/60 // distancia(lat, longi)

def ritmos(regis, lat, longi):
    resultado = []
    for i in range(1, len(regis)):
        resultado.append(ritmo(regis[i-1:i+1], lat[i-1:i+1], longi[i-1:i+1]))
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
    return coords"""
