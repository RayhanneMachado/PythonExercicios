#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 POR Km todado
d =int(input('Quantos dias alugador? '))
km =float(input('Quantos km rodados? '))
t = (d * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(t))