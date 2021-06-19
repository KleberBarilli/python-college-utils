import heapq
from random import randint, choice

def funcao():
    y = '0123456789'
    x = randint(0,9)
    lista = ''
    for i in range(x):
        lista += choice(y)
    print(set(list(lista)))
    print(heapq.nlargest(3, lista))


funcao()
