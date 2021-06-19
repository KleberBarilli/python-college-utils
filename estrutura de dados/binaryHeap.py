import heapq

class FilaDePrioridade:

	def __init__(self):
		self._fila = []
		self._indice = 0

	def inserir(self, item, prioridade):
		heapq.heappush(self._fila, (-prioridade, self._indice, item))
		self._indice += 1

	def remover(self):
		return heapq.heappop(self._fila)[-1]


class Pessoa:
	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		return self.nome


fila = FilaDePrioridade()
fila.inserir(Pessoa('Maria'), 1)
fila.inserir(Pessoa('Pedro'), 5)
fila.inserir(Pessoa('Felipe'), 3)
fila.inserir(Pessoa('Carol'), 4)

print(fila.remover())