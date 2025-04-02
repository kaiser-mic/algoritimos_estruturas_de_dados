
class Carro:

    def __init__(self):
        self.__modelo = 'uno'
        self.__ano = 2005
        self.__km = 0


    def set_km(self, km):
        self.__km += km

    def set_ano(self, ano):
        self.__ano = ano
    
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo
    def get_ano(self):
        return self.__ano
    def get_km(self):
        return self.__km
    

    def __str__(self):
        return " o modelo do carro é " + self.get_modelo() + ", o ano do carro é " + str(self.get_ano()) + " e a kilometragem do carro é: " + str(self.get_km())

    def printkm(self):
        return ("o carro tem ", str(self.get_km)())
 

carro=Carro()

print(carro)

km=int(input("quantos km o carro andou?"))
modelo=input("qual o modelo do carro?")
ano=int(input("qual o ano do carro?"))
carro.set_km(km)
carro.set_ano(ano)
carro.set_modelo(modelo)
print(carro)
print(carro.printkm)