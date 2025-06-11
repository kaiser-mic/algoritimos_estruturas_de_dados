from carro import Carro

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, modelo, ano, placa):
        nodo = Carro(modelo, ano, placa)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo        
        self.fim = nodo
        self.imprimir()
    
    def imprimir(self):
        print("---------------FILA - FIFO------------------")
        if self.inicio is None:
            print( "Fila está vazia!" )
        else:
            aux = self.inicio
            txt = ""
            while aux :
                txt +=  aux.modelo + " - "
                aux = aux.prox
    
            print (txt)
    def remover(self):
        if self.inicio is not None:
            elemento = self.inicio
            self.inicio = self.inicio.prox
            
            if self.inicio is None:
                self.fim = self.inicio
            
            print( "Elemento", elemento.modelo,  "Removido" )
        self.imprimir()