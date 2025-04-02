class Produto:
    def __init__(self, nome, preco = 10.0, qtd = 0 ):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    def __str__(self):
        return f" Produto: {self.nome} \n preço: {str(self.preco)} \n"
        