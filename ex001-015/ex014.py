#1 - Crie um programa que receba uma temperatura em graus Celsius e a converta para Fahrenheit.Formula:
#F=(C×9/5)+32
c =float(input('Informe a temperatura em °C'))
f = c * 9 / 5 + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(c,f))
