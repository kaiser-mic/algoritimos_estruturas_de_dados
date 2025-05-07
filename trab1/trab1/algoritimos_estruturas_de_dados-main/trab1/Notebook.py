from Produto import Produto
class Notebook(Produto):
    def __init__(self, modelo, cor, preco, cat, tempo):
        super().__init__(modelo, cor, preco, cat)
        self.__tempoDeBateria = tempo
    def getinformacoes(self):
        return f'modelo {str(self.modelo)}, cor : {str(self.cor)}, preço: {str(self.preco)}, categoria: {str(self.categoria)}, duração da bateria: {str(self.__tempoDeBateria)}  '
    