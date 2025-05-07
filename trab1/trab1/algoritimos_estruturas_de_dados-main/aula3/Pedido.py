from datetime import date
from Pessoa import Pessoa
from Produto import Produto
class Pedido:
    def __init__(self, data = date.today(), cliente = Pessoa("Balcão")):
        self.id = None
        self.data = data
        self.cliente = cliente
        self.produtos = []
    
    def addproduto( self, prod ):
        if  prod  and prod.preco >= 10:
            self.produtos.append(prod)
        soma = 0.0
        for p in self.produtos:
            soma += p.preco
        return soma

    def forloop(self):
        for p in self.produtos:
            return p

    def __str__(self):
        return f"Pedido realizado em: {str(self.data)} \n cliente: {str(self.cliente)} \n Produtos: {self.forloop}"
        

        