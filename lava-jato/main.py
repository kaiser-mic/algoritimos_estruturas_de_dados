import os
from Fila import Fila

fila = Fila()

op = -1


while op != 0:
    os.system('cls')
    print("-----------------")
    print("-1 Adicionar na fila")
    print("-2 remover da fila")
    print("-3 imprimir a fila")
    print("-0 sair")
    op = int(input("digite sua opção: "))
    if op ==1:
        modelo = input("Digite o modelo do carro que será inserido na fila: ")
        ano = int(input("Digite o ano do carro que será inserido na fila: "))
        placa = input("Digite a placa do carro que será inserido na fila: ")
        #carro1 = Carro(modelo, ano, placa)
        #fila.add(carro1)

        fila.add(modelo, ano, placa)
    elif op ==2:
        fila.remover()
    elif op ==3:
        fila.imprimir()
    elif op != 0:
        print("Opção Invalida!")
    input("Enter para continuar...")
