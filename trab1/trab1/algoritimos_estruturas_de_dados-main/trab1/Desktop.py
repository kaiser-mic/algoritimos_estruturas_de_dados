from Produto import Produto
class Desktop(Produto):
    def __init__(self, modelo, cor, preco, cat, potencia):
        super().__init__(modelo, cor, preco, cat)
        self._potenciaDaFonte = potencia
    def getinformacoes(self):
        return f'modelo {str(self.modelo)}, cor : {str(self.cor)}, preço: {str(self.preco)}, categoria: {str(self.categoria)}, potencia da fonte: {str(self._potenciaDaFonte)}  '