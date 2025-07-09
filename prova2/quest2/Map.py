
def gasto_Familiar ( valores):
    soma = 0
    for x in valores:
        soma += x
    return soma

gastos = [100, 815, 200, 150, 50], [1000, 2000, 300] , [900, 100, 500, 200], [10, 100, 20, 40, 50]

total = map( gasto_Familiar , gastos )
print("gasto total familiar:", list(total) )
total_somado = sum(map( gasto_Familiar , gastos ))
print("gasto total somado:", total_somado)


def ganho_familiar ( salario):
    soma = 0
    for x in salario:
        soma += x
    return soma

salarios = [1700, 3000] , [5000]

ganho_total = map( ganho_familiar , salarios )
print("ganho total familiar:", list(ganho_total) )
ganho_total_somado = sum(map( ganho_familiar , salarios ))
print("ganho total somado:", ganho_total_somado)


print("Considerando o balanço realizado a familia tem um ganho de:", ganho_total_somado - total_somado)
