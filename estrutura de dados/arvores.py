### Arvore Binaria N�o Balanceada
# Estrutura Recursiva
###
class Nodo:
    """
    Nodo da arvore:
      filhos da esquerda e direita + dado (que pode ser qualquer objeto)
    """
    def __init__(self, dado):
        self.esq = None
        self.dir = None
        self.dado = dado

    def __str__(self):
        return str(self.dado)

    def __repr__(self):
        return str(self.dado)

    def numFilhos(self, alvo):
        num_filhos = 0
        if (alvo.esq is not None):
            num_filhos += 1

        if (alvo.dir is not None):
            num_filhos += 1
        
        return num_filhos

    def inserir(self, dado):
        """
        Insere um novo nodo com dados

        @param dado a ser inserido
        """
        
        ## Insere na sub-arvore da esquerda
        if dado < self.dado:
            if self.esq is None:
                # Cria um novo nodo (que sera a sub-arvore da esquerda)
                self.esq = Nodo(dado)
            else:
                self.esq.inserir(dado)

        ## Insere na sub-arvore da direita
        elif dado > self.dado:
            if self.dir is None:
                # Cria um novo nodo (que sera a sub-arvore da direita)
                self.dir = Nodo(dado)
            else:
                self.dir.inserir(dado)

    def buscar(self,alvo, pai=None):
        # retornar uma tupla contendo o nodo alvo e o pai        
        if alvo == self.dado:
            return self, pai
        else:
            if alvo > self.dado:
                if self.dir is None:
                    return None, None
                return self.dir.buscar(alvo, self)
            elif alvo < self.dado:
                if self.esq is None:
                    return None, None
                return self.esq.buscar(alvo, self)
    
    def remover(self, alvo, pai):
        pass
                    
    def imprimirEmOrdem(self):
        """
        Imprime o conteudo da arvore na tela, usando travessia em-ordem (in-order | arv_esq - raiz - arq_dir)
        """
        # Sub-arvore da Esquerda
        if self.esq:            
            self.esq.imprimirEmOrdem()

        # Raiz
        print(self.dado)

        # Sub-arvore da Esquerda
        if self.dir:            
            self.dir.imprimirEmOrdem()

    def imprimirPreOrdem(self):        
        # Raiz
        print(self.dado)

        # Sub-arvore da Esquerda
        if self.esq:            
            self.esq.imprimirPreOrdem()        

        # Sub-arvore da Direita
        if self.dir:            
            self.dir.imprimirPreOrdem()

    def imprimirPosOrdem(self):
        # Sub-arvore da Esquerda
        if self.esq:            
            self.esq.imprimirPosOrdem()

        # Sub-arvore da Direita
        if self.dir:            
            self.dir.imprimirPosOrdem()

        # Raiz
        print(self.dado)

def main():
    # 10, 4, 3, 5, 9, 12, 1, 13, 11
    
    ## Inserindo...
    raiz = Nodo(10)
    nums = [4, 3, 5, 9, 12, 1, 13, 11]
    for n in nums:
        raiz.inserir(n)
    #print('In-Ordem')
    #raiz.imprimirEmOrdem()
    #print('Pré-ordem')
    #raiz.imprimirPreOrdem()
    #print('Pós-ordem')
    #raiz.imprimirPosOrdem
    
    achou = raiz.buscar(12)
    
            
if __name__ == "__main__":
    main()
