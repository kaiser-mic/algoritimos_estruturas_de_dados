from Cidade import Cidade

class Pessoa:
    def __init__(self, nome, cpf = None, cid =Cidade("Alvorada") ):
        self.id = None
        self.nome = nome
        self.cpf = cpf
        self.cidade = cid

    def __Str__(self):
        return f"pessoa {self.nome} \n Cpf: {self.__cpf} \n Cidade: {str(self.cidade)}"
        