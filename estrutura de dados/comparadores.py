# testando comparadores Python 3

class Nodo:
    def __init__(self, dado, prioridade):
        self.dado = dado
        self.prioridade = int(prioridade)

    def __lt__(self, other):  # menor que
        if self.prioridade == other.prioridade:
            return self.dado < other.dado
        else:
            return self.prioridade < other.prioridade

    def __le__(self, other):  # menor igual
        if self.prioridade == other.prioridade:
            return self.dado <= other.dado
        else:
            return self.prioridade <= other.prioridade

    def __gt__(self, other):  # maior que
        if self.prioridade == other.prioridade:
            return self.dado > other.dado
        else:
            return self.prioridade > other.prioridade

    def __ge__(self, other):  # maior igual
        if self.prioridade == other.prioridade:
            return self.dado >= other.dado
        else:
            return self.prioridade >= other.prioridade

    def __eq__(self, other):  # igual
        return (self.dado == other.dado) and (self.prioridade == other.prioridade)

    def __str__(self):
        return str(self.dado)

    def __repr__(self):
        return str(self.dado) + "(" + str(self.prioridade) + ")"



nodo1 = Nodo('ABC', 1)
nodo2 = Nodo('DEF', 1)
print(nodo1 == nodo2)

nodo1 = Nodo('ABC', 1)
nodo2 = Nodo('ABC', 1)
print(nodo1 == nodo2)

nodo1 = Nodo('ABC', 1)
nodo2 = Nodo('ABC', 2)
print(nodo1 == nodo2)

nodo1 = Nodo('ABC', 1)
nodo2 = Nodo('DEF', 1)
print(nodo1 < nodo2)

# ====
print(nodo1)
print(repr(nodo1))
