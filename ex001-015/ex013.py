# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
nome = input('Digite o nome do funcionário ')
s = float(input('Digite o salário'))
d = s + (s * 0.15)
print ('O Novo salario do funcionário {}, foi de {:.2f} reais para {:.2f} reais'.format(nome, s,d))
#ou s * 15/100