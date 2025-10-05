#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros a milimetros
#conversor de medidas
n =float(input('Digite um valor em metros'))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm= n * 100
mm = n * 1000
print('A medida de {} corresponde a:'.format(n))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}cm'.format(cm))
print('{}mm'.format(mm))

