def gridx(duracao, pos_x, pos_y, width, height)
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
    pos_x = rect[0]
    pos_y = rect[1]
    width = rect[2]
    height = rect[3]
    gridx(dom[-1] - dom[0], pos_x, pos_y, width, height)
    gridy(max(lst), rect)


def desenharEixos(rect):
    pos_x = rect[0]
    pos_y = rect[1]
    width = rect[2]
    height = rect[3]
    #eixo x
    turtle.goto(pos_x - 10, pos_y)
    turtle.down()
    turtle.goto(pos_x + width + 10, pos_y)
    turtle.up()
    #eixo y
    turtle.goto(pos_x, pos_y - 10)
    turtle.down()
    turtle.goto(pos_x, pos_y + height + 10)
    turtle.up()


def desenharLinha(lst, pos_x, pos_y):
    turtle.goto(pos_x, (pos_y + lst[0]) * escy)
    turtle.down()
    for y in lst[1:]:
        turtle.goto((pos_x + i) * escx, (pos_y + y) * escy)
        i += 1
    

def desenharGrafico(rect, dominio, imagem):
    i_maior = 0
    for i in range(len(imagem)):
        if max(len[i]) > max(len[i_maior]):
            i_maior = i

    escalas = (rect[2]/(dominio[-1] - dominio[0]), rect[3]/max(imagem[i_maior]) #--> A imagem do maior

    cores = ["red", "blue"]
    cores.insert("black", i_maior)
    for i in range(len(imagem)):
        turtle.color(cores[i])
        if i == i_maior:
            desenharEixos(rect)
            desenharGrid(dominio, imagem[i], rect)
        desenharLinha(imagem[i], rect)

# Estava usando um espaçamento de 250 pixels entre um gráfico e outro
