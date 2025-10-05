#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#O dolar está na cotação do dia da aula em 2017, considere: US$1,00 = R$3,27
r =float(input('Quantos dinheiro você tem na carteira? '))
d = r / 3.27
print('Com o dinheiro que você tem na carteira {} reais, você pode comprar o equivalente a {}'.format(r,d))

