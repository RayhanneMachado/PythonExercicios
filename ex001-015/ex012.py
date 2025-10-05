#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
valor = float(input('Digite o valor da peça R$'))
d = valor-(valor * 0.05)
print('A peça com 5% de desconto ficou por {:.2f} reais'.format(d))
# valor - (valor * 5/100)