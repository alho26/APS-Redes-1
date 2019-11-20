def replace(arquivo, posicao):
    variavel = arquivo[posicao][1]  # peega o valor
    variavel = variavel.replace('"', '')  # substitui as aspas por nada
    variavel = variavel.replace(',', '')  # substitui a vitgula por nada

    return variavel

# funcao que faz a passagem dos enderecos para decimal


def decimal(endereco):
    # corto o endereco em 4 partes, com o delimitador sendo o '.'
    endereco_decimal = [int(endereco.split(".")[0]), int(endereco.split(
        ".")[1]), int(endereco.split(".")[2]), int(endereco.split(".")[3])]

    return endereco_decimal

# funcao que faz a passagem dos enderecos para binario


def binario(endereco):
    endereco_binario = [int(endereco.split(".")[0]), int(endereco.split(
        ".")[1]), int(endereco.split(".")[2]), int(endereco.split(".")[3])]
    # passo os valores para binário e verifico caso algum seja igual a vazio, se for dou o valor 0 para ele
    p0 = d2b(int(endereco_binario[0]))
    if p0 == "":
        p0 = 0

    p1 = d2b(int(endereco_binario[1]))
    if p1 == "":
        p1 = 0

    p2 = d2b(int(endereco_binario[2]))
    if p2 == "":
        p2 = 0

    p3 = d2b(int(endereco_binario[3]))
    if p3 == "":
        p3 = 0

    #print(p0, p1, p2, p3)
    # concateno todos em uma única variável
    endereco_binario = [str(p0), str(p1), str(p2), str(p3)]

    return endereco_binario

# funcao recursiva que passa um valor decimal para binario


def d2b(n):
    if n == 0:
        return ''
    else:
        return d2b(n//2) + str(n % 2)