#Kleber e Emerson
import heapq
from sys import exit
from random import choice

class FilaDePrioridade:
    def __init__(self):
        self._fila = []
        self._senhas =[]
        self._senhasChamadas = []
        self._indice = 0
        self._senha = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def inserir(self, prioridade):
        senha = ''
        for i in range(3):
            senha += choice(self._senha)
        print('senha:' + str(senha))

        self._senhas.append(senha)
        heapq.heappush(self._fila, (-prioridade, self._indice,senha))
        self._indice += 1


    def chamar(self):
        try:
            chamada =  heapq.heappop(self._fila)[-1]
            self._senhasChamadas.append(chamada)
            return chamada
        except IndexError:
            return 'Não existem mais senhas para serem chamadas'    

    def listar(self):
        try:
            print('Ùltimas senhas:')
            print(self._senhasChamadas[-5], self._senhasChamadas[-4], self._senhasChamadas[-3],
              self._senhasChamadas[-2], self._senhasChamadas[-1])
        except IndexError:
            print('Não foram chamadas 5 senhas')      


fila = FilaDePrioridade()

while True:
    print('Menu Principal\n1-Gerar senha comum\n2-Senha prioritária\n3-Senha urgente\n4-Chamar senha\n5-Listas as últimas 5 senhas\n6-Sair\nDigite:')
    escolha = input('')
    if escolha == '1':
        fila.inserir(0)
    elif escolha == '2':
        fila.inserir(1)
    elif escolha == '3':
        fila.inserir(2)
    elif escolha == '4':
        print('Painel:' + str(fila.chamar()))
    elif escolha == '5':
        fila.listar()
    elif escolha == '6':
        exit()
    else:
        print('Comando inválido')    

