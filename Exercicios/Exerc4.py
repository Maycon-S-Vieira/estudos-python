import array as arr

x = 1
array = arr.array('f')
while x != 0 :
    num = float(input("Insira um valor: "))
    array.append(num)
    x = int(input("Deseja inserir outro valor? (1 - Sim / 0 - Não): "))

def pares(array):
    p_count = 0
    for i in array:
        if i % 2 == 0:
            p_count += 1
    print("Quantidade de números pares: ", p_count)

def impares(array):
    i_count = 0
    for i in array:
        if i % 2 != 0:
            i_count += 1
    print("Quantidade de números ímpares: ", i_count)

def maior(array):
    m = array[0]
    for i in array:
        if i > m:
            m = i
    print("Maior numero: ", m)

def menor(array):
    m = array[0]
    for i in array:
        if i < m:
            m = i
    print("Menor numero: ", m)

def media(array):
    soma = 0
    for i in array:
        soma += i
    print("Média: ", soma/len(array))

pares(array)
impares(array)
maior(array)
menor(array)
media(array)

