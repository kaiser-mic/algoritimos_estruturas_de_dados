from Categoria import Categoria
class Produto(Categoria):
    def __init__(self, modelo, cor, preco, cat):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = cat
    def getinformacoes(self):
        return f'modelo {str(self.modelo)}, cor : {str(self.cor)}, preço: {str(self.preco)}, categoria: {str(self.categoria)}  '
    def cadastrar(self):
        pass