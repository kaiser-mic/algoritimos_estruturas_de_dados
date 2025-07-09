from Apartamento import Apartamento

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, id, numero, torre):
        nodo = Apartamento(id, numero, torre)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo        
        self.fim = nodo
        self.imprimir()
    

    def imprimir(self):
        print("lista espera ap")
        if self.inicio is None:
            print( "Fila está vazia!" )
        else:
            aux = self.inicio
            txt = ""
            while aux :
                txt +=  aux.numero + " - "
                aux = aux.prox
            print (txt)

    def remover(self, vaga):
        if self.inicio is not None:
            elemento = self.inicio
            self.inicio = self.inicio.prox
            if self.inicio is None:
                    self.fim = self.inicio
            print("O Apartamento",elemento.numero, "recebeu a vaga:",vaga)
                
        