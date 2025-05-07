from Pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self,  nome, cpf, matricula):
        super().__init__( nome, cpf)
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula
    def set_matricula(self, matricula):
        self.__matricula = matricula
    def __str__(self):
        return f'Nome {str(self.nome)}, cpf : {str(self._cpf)}, matricula: {str(self.get_matricula())}  ' 
    