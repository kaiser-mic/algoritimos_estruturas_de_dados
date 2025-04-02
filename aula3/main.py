from Pessoa import Pessoa
from Produto import Produto
from Cidade import Cidade
from Pedido import Pedido

c1 = Cidade()
c2= Cidade("Porto Alegre")
p1= Pessoa("João")
p2 = Pessoa("Maria", cid= c1)

prod01 = Produto("Coca-Cola", 9.99)
prod02 = Produto("Pepsi", qtd= 50)
prod03 = Produto("Fanta", preco=7.85,  qtd= 50)

ped = Pedido(cliente= p2)
ped.addproduto(prod02)
ped.addproduto(prod03)
print(ped)