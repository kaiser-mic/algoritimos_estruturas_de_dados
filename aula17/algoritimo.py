vetor = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
iteracoes = 0

key=input("digite o numero que deseja usar")
tamanho_vetor = len(vetor)

for i in vetor:
    pass

inicio = 0
fim = tamanho_vetor - 1
while inicio <= fim:
    centro = (inicio + fim) // 2  
    iteracoes += 1
    if vetor[centro] == int(key):
        print("o numero digitado foi encontrado:", key, "numero total de iterações:", iteracoes)
        break 
    elif int(key) > vetor[centro]:
        inicio = centro + 1
    else:
        fim = centro - 1