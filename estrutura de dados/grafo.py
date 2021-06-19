import networkx as nx
import matplotlib.pyplot as plt
import pylab
class RedeSocial:
    def __init__(self):
        self.g = nx.Graph()
        self.matriz = []

    def adicionar_amigo(self, pessoa1, pessoa2):


        self.g.add_edge(pessoa1, pessoa2, egdes=2)
        h = nx.Graph(self.g)
        list(h.edges())
        pos=nx.spring_layout(self.g)
        nx.draw(self.g,pos)
        edge_labels=dict([((fe,se,),e['egdes'])
        for fe,se,e in self.g.edges(data=True)])

        nx.draw_networkx_edge_labels(self.g,pos,edge_labels)

        pylab.show()

        #print(h.degree())
        #print(self.g.nodes())
        #print(h.edges())





        #print(self.g.number_of_edges())
        #print(self.g.degree())


rede = RedeSocial()


rede.adicionar_amigo('Kleber', 'Joana')
rede.adicionar_amigo('Kleber', 'Carlos')
rede.adicionar_amigo('Marcos', 'Anna')
