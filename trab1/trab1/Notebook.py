from Produto import Produto
class Notebook(Produto):
    def __init__(self, modelo, cor, preco, cat, tempo):
        super().__init__(modelo, cor, preco, cat)
        self.__tempoDeBateria = tempo
    def getinformacoes(self):
        return super().getinformacoes() + f', duração da bateria: {str(self.__tempoDeBateria)}  '
        #return f'modelo {str(self.modelo)}, cor : {str(self.cor)}, preço: {str(self.preco)}, categoria: {str(self.categoria)}, duração da bateria: {str(self.__tempoDeBateria)}  '
    def get_tempo(self):
        return self.__tempoDeBateria
    def set_tempo(self, tempo):
        self.__tempoDeBateria = tempo
