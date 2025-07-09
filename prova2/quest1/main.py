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
        id = input("Digite o id que será inserido na fila: ")
        numero = input("Digite o numero do apartamento que será inserido na fila: ")
        torre = input("Digite a torre do apartamento que será inserido na fila: ")

        fila.add(id, numero, torre)
    elif op ==2:
        vaga = int(input("Digite o numero da vaga que o apartamento recebeu"))

        fila.remover(vaga)
    elif op ==3:
        fila.imprimir()
    elif op != 0:
        print("Opção Invalida!")
    input("Enter para continuar...")
