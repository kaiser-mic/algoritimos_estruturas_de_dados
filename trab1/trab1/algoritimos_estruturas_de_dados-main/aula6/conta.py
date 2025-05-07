class Conta:
    logado = True
    tarifa = 1.99

    def __init__(self):
        self.__saldo = 0.0

    def get_saldo(self):
        if self.logado:    
            return self.__saldo
        else:
            return None

    def set_saldo(self, valor):
        if valor > self.__saldo:
            self.__saldo = valor

    @property
    def saldo(self):
        if self.logado:    
            return self.__saldo
        else:
            return None
    
    @saldo.setter
    def saldo(self, valor):
        if valor > self.__saldo:
            self.__saldo = valor
        else:
            print("valor nao permitido")

    def __descontartarifa(self):
        self.__saldo -= self.tarifa
    def sacar (self, valor):
        if self.__saldo >= valor + self.tarifa:
            self.__saldo -= valor
            self.__descontartarifa()
        else:
            print("saldo insuficiente")