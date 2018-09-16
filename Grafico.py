from Interface import transladarParaCentralizado
from utm import from_latlon
import Calculos


def gridx(duracao, pos_x, pos_y, width, height):
    cont = 0
    pos = cont + pos_x
    interv = duracao / width
    while pos <= pos_x + width:
        turtle.goto(pos, pos_y - 25)
        turtle.write(int(cont * interv), align="center")
        turt.goto(pos, pos_y)
        turt.down()
        turt.goto(pos, pos_y - 3)
        turt.goto(pos, pos_y + height + 3)
        pos += width // 10
        cont += width // 10
        turt.up()


def gridy(maximo, pos_x, pos_y, width, height):
    cont = 0
    pos = cont + pos_y
    interv = maximo / 200
    while pos <= pos_y + 200:
        turtle.goto(pos_x - 12, pos - 8)
        turt.write(int(cont * interv, align="right"))
        turt.goto(pos_x, pos)
        turt.down()
        turt.goto(pos_x - 3, pos)
        turt.goto(pos_x + width + 3, pos)
        pos += height // 10
        cont += height // 10 
        turt.up()


def desenharGrid(dom, lst, rect):
    pos_x = rect["xPos"]
    pos_y = rect["yPos"]
    width = rect["width"]
    height = rect["height"]
    gridx(dom[-1] - dom[0], pos_x, pos_y, width, height)
    gridy(max(lst), rect)


def desenharEixos(rect):
    pos_x = rect["xPos"]
    pos_y = rect["yPos"]
    width = rect["width"]
    height = rect["height"]
    #eixo x
    turtle.goto(pox_x - 10, pos_y)
    turtle.down()
    turtle.goto(pos_x + width + 10, pos_y)
    turtle.up()
    #eixo y
    turtle.goto(pos_x, pos_y - 10)
    turtle.down()
    turtle.goto(pos_x, pos_y + height + 10)
    turtle.up()


def desenharLinha(lst, rect, escs):
    pos_x = rect["xPos"]
    pos_y = rect["yPos"]
    turtle.goto(pos_x, (pos_y + lst[0]) * escs[1])
    turtle.down()
    for y in lst[1:]:
        turtle.goto((pos_x + i) * escs[0], (pos_y + y) * escs[1])
        i += 1


def desenharGrafico(turtle, rect, dominio, imagem, nomeDaImagem):
    # rect é um dicionário nesse tipo {"xPos": valor, "yPos": valor, "width": valor, "height": valor}
    # ele é definido em um plano diferente, onde o ponto (0, 0) refere-se ao canto superior-esquerdo
    screen = turtle.getscreen()
    x, y = transladarParaCentralizado(screen, x=rect["xPos"], y=rect["yPos"])
    # esse código gera o ponto equivalente no plano onde (0, 0) é o centro da tela
    
    # dominio é uma lista com os timestamps dos registros
    
    # imagem é uma lista de listas, cada elemento de imagem é uma lista com todos os valores de um atributo dos registros
    # por exemplo [[todos os BPMs][todas as alturas]] que é um gráfico com duas linhas
    # ou [[todas as alturas]] que no caso seria um gráfico só com uma linha mas continua sendo uma lista de lista
    # caso algum elemento na imagem esteja faltando vai constar None [["432", "423", None, "6757"]]
    
    # nomeDaImagem é uma lista com a definição de quais dados estão na imagem
    # para imagem = [[todos os BPMs][todas as alturas]] nomeDaImagem seria ["BPMs", "Altura"]
    iMaior = 0
    for i in range(len(imagem)):
        if max(len[i]) > max(len[i_maior]):
            iMaior = i

    escalas = ((rect["width"] - 15) / (dominio[-1] - dominio[0]), rect["height"] - 15 / max(imagem[iMaior]))

    cores = ["red", "blue"]
    cores.insert("black", iMaior)
    for i in range(len(imagem)):
        turtle.color(cores[i])
        if i == iMaior:
            desenharEixos(rect)
            desenharGrid(dominio, imagem[i], rect)
        desenharLinha(imagem[i], rect, escalas)
#---------------------------------------------------------------------------------------------------------------------
    
    
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

    km = 0
    distAtual = 0
    distTotal = Calculos.Distancia(listaDeGeolocalizacoes)
    alfa = 0
    turtle.up()

    for i in range(len(coordsTemp)):
        try:
            xGo = x + (rect["width"] / 2) + (coordsTemp[i]["x"] - origem[0]) * escx
            yGo = y - (rect["height"]/ 2) + (coordsTemp[i]["y"] - origem[1]) * escy
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
