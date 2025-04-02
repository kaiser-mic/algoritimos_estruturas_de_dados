from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, ano=2025, qtdportas = 4):
        super().__init__(modelo, ano)
        self.portas = qtdportas

    def __str__(self):
        return super().__str__() + "\n portas: " + str(self.portas)