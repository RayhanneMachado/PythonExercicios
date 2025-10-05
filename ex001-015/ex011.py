#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la Sabendo que cada litro de tinta, pinta uma área de 2m²
a = float(input('Digite a altura da parede em metros'))
l = float(input('Digite a largura da parede em metros'))
area = a * l
tinta = area / 2
print('A altura da parede é {} metros, e a largura {} metros, sua área {} m², cada litro de tinta pinta 2m²'
      'então para pintar essa parede sera necessário {} litros'.format(a,l,area,tinta))