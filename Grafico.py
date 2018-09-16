from Interface import transladarParaCentralizado


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
    pass
    
    
def desenharCircuito(turtle, rect, listaDeGeolocalizacoes):
    for i in listaDeGeolocalizacoes:
        print(i)
    # esse método já está incomporado na interface, todas as alterações feitas aqui já são apresentadas lá
    
    # o rect está no mesmo padrão do desenharGrafico
    
    # listaDeGeolocalizadores é uma lista de dicionários tipo: [{"longitude": 234, "latitude": 423}, {"longitude": 43, "latitude": 123}]
    # caso algum elemento não exista o dicionário não vai ter a chave
    # se latitude n existir um um registro vai ficar somente a longitude, caso n exista nenhum, vai ficar um dicionário vazio {}
    pass