def desenharGrid():
    pass


def desenharEixos(turtle):
    #eixo x
    turtle.goto(pos_x - 10, pos_y)
    turtle.down()
    turtle.goto(pos_x + 310, pos_y)
    turtle.up()
    #eixo y
    turtle.goto(pos_x, pos_y - 10)
    turtle.down()
    turtle.goto(pos_x, pos_y + 210)
    turtle.up()
    pass


def desenharLinha():
    pass


def desenharGrafico(lst, turtle):
    turtle.goto(pos_x, (pos_y + lst[0]) * escy)
    turtle.down()
    for y in lst[1:]:
        turtle.goto((pos_x + i) * escx, (pos_y + y) * escy)
        i += 1
    
# Estava usando um espaçamento de 250 pixels entre um gráfico e outro
