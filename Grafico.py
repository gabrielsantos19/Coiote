from Interface import transladarParaCentralizado
from utm import from_latlon
import Calculos


def gridx(turtle, tam, duracao, rect, x, y):
    cont = 0
    pos = cont + x + 20
    interv = (duracao / 60) / (rect["width"] - 150)
    while pos <= x + rect["width"] - 130:
        turtle.goto(pos, y - rect["height"])
        turtle.write(int(cont * interv), align="center")
        turtle.goto(pos, y - rect["height"] + 15)
        turtle.down()
        turtle.goto(pos, y)
        pos += (rect["width"] - 150) // 10
        cont += (rect["width"] - 150) // 10
        turtle.up()


def gridy(turtle, maximo, rect, x, y):
    cont = 0
    pos = cont + y - rect["height"] + 20
    interv = maximo / (rect["height"] - 25)
    while pos <= y - 5:
        turtle.goto(x + 12, pos - 8)
        turtle.write(int(cont * interv), align="right")
        turtle.goto(x + 15, pos)
        turtle.down()
        turtle.goto(x + rect["width"] - 130, pos)
        pos += (rect["height"] - 25) // 10
        cont += (rect["height"] - 25) // 10 
        turtle.up()


def desenharGrid(turtle, tam, dom, maximo, rect, x, y, zonas):
    gridx(turtle, tam, float(dom[-1]["timeStamp"]) - float(dom[0]["timeStamp"]), rect, x, y)
    if zonas == False:
        gridy(turtle, maximo, rect, x, y)


def desenharEixos(turtle, rect, x, y):
    #eixo y
    turtle.goto(x + 20, y - 5)
    turtle.down()
    turtle.goto(x + 20, y - rect["height"] + 20)
    turtle.up()
    #eixo x
    turtle.goto(x + 15, y - rect["height"] + 20)
    turtle.down()
    turtle.goto(x + rect["width"] - 50, y - rect["height"] + 130) 
    turtle.up()


def desenharLinha(turtle, lst, x, y, escs, rect, zonas):
    if zonas:
        escy = 1
    else:
        escy = escs[1]
    try:
        turtle.goto(x + 20, (y + 20 - rect["height"]) + lst[0] * escy)
        turtle.down()
    except TypeError:
        pass
    i = 1
    for im in lst[1:]:
        try:
            turtle.goto(x + 20 + i * escs[0], (y + 20 - rect["height"]) + im * escy)
            turtle.down()
        except TypeError:
            turtle.up()
        i += 1

    if zonas == True: 
        values = [104, 114, 133, 152, 171]
        p = 0
        while p < len(values):
            turtle.up()
            turtle.goto(x + 12, (y + 10 - rect["height"]) + values[p])
            turtle.write(p+1)
            turtle.goto(x + 15, (y + 10 - rect["height"]) + values[p])
            turtle.down()
            turtle.goto(x + rect["width"] - 130, (y + 10 - rect["height"]) + values[p])
            turtle.up()
            p += 1
    turtle.up()



def desenharGrafico(turtle, rect, dominio, imagem, nomeDaImagem, zonas=False):
    screen = turtle.getscreen()
    x, y = transladarParaCentralizado(screen, x=rect["xPos"], y=rect["yPos"])

    iMaior = 0

    for i in range(len(nomeDaImagem)):
        if Maximos(imagem[i], nomeDaImagem[i].lower()) > Maximos(imagem[iMaior], nomeDaImagem[iMaior].lower()):
            iMaior = i

    escalas = [(rect["width"] - 150) / len(imagem[iMaior]), (rect["height"] - 25) / Maximos(imagem[iMaior], nomeDaImagem[iMaior].lower())]

    #if nomeDaImagem == ["Zonas"]:
    #    escalas[1] = (rect["height"] - 25) / 
    
    cores = ["red", "blue"]
    cores.insert(iMaior, "black")
    for i in range(len(imagem)):
        turtle.color(cores[i])
        if i == iMaior:
            #desenharEixos(turtle, rect, x, y)
            try:
                desenharGrid(turtle, len(imagem[i]), dominio, Maximos(imagem[i], nomeDaImagem[i].lower()), rect, x, y, zonas)
            except TypeError:
                pass
        desenharLinha(turtle, doLst(imagem[i], nomeDaImagem[i].lower()), x, y, escalas, rect, zonas)
    posT = 0

    for i in range(len(nomeDaImagem)):
        turtle.up()
        turtle.goto(x + rect["width"] - 115, y - 45 + posT)
        turtle.down()
        turtle.color(cores[i])
        turtle.goto(x + rect["width"] - 100, y - 45 + posT)
        turtle.up()
        turtle.color("black")
        turtle.goto(x + rect["width"] - 95, y - 53 + posT)
        turtle.write(nomeDaImagem[i])
        posT -= 15
    
    
def desenharCircuito(turtle, rect, listaDeGeolocalizacoes):
    cont = 0
    # Uma pra desenhar e outra pras escalas
    coordenadas = []
    coordsTemp = []
    for i in listaDeGeolocalizacoes:
        try:
            infos = from_latlon(i["latitude"], i["longitude"])
            coordenadas.append({"x": infos[0], "y": infos[1]})
            coordsTemp.append({"x": infos[0], "y": infos[1]})
            if cont == 0:
                origem = (infos[0], infos[1])
                cont = 1
        except KeyError:
            coordsTemp.append({}) 

    # A posição inicial será no meio do retângulo --> x + rect["width"] / 2, y + rect["height"] / 2
    # Escalas para fazer o circuito caber no mini-mapa, deixando uma borda de 5 pixels
    screen = turtle.getscreen()
    x, y = transladarParaCentralizado(screen, x=rect["xPos"], y=rect["yPos"])
    escx = ((rect["width"] / 2) - 5) / (max([abs(v["x"] - origem[0]) for v in coordenadas]))
    escy = ((rect["height"] / 2) - 5) / (max([abs(v["y"] - origem[1]) for v in coordenadas]))

    afastamentoX, afastamentoY = Calculos.Afastamento(coordenadas, escx, escy, rect, (origem[0], origem[1]))

    km = 0
    distAtual = 0
    distTotal = Calculos.Distancia(listaDeGeolocalizacoes)
    alfa = 0
    turtle.up()

    for i in range(len(coordsTemp)):
        try:
            xGo = (afastamentoX / 2) + (x + (rect["width"] / 2) + (coordsTemp[i]["x"] - origem[0]) * escx)
            yGo = (afastamentoY / 2) + (y - (rect["height"]/ 2) + (coordsTemp[i]["y"] - origem[1]) * escy)
            turtle.goto(xGo, yGo)
            if i > 0:
                distAtual += Calculos.Distancia(listaDeGeolocalizacoes[i-1:i+1])
            if distAtual >= 1 or alfa == 0:
                if alfa != 0:
                    km += 1
                else:
                    turtle.color("green")
                    alfa = 1
                turtle.up()
                turtle.goto(xGo, yGo + 5)
                if km == int(distTotal):
                    turtle.color("red")
                turtle.write(km)
                turtle.color("black")
                turtle.down()
                turtle.goto(xGo, yGo - 5)
                turtle.goto(xGo, yGo)
                distAtual = 0
            turtle.down()
        except KeyError:
            turtle.up()
        
        
    # esse método já está incomporado na interface, todas as alterações feitas aqui já são apresentadas lá
    
    # o rect está no mesmo padrão do desenharGrafico
    
    # listaDeGeolocalizadores é uma lista de dicionários tipo: [{"longitude": 234, "latitude": 423}, {"longitude": 43, "latitude": 123}]
    # caso algum elemento não exista o dicionário não vai ter a chave
    # se latitude n existir um um registro vai ficar somente a longitude, caso n exista nenhum, vai ficar um dicionário vazio {}

def Maximos(lst, nome):
    maximo = 0
    for x in lst:
        try:
            if x[nome] > maximo:
                maximo = x[nome]
        except KeyError:
            pass
    return maximo

def doLst(lst, nome):
    lista = []
    for x in lst:
        try:
            lista.append(x[nome])
        except KeyError:
            lista.append(" ")
    return lista


