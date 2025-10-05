#Ler duas notas de um aluno e dar sua média
nome =input('Digite seu nome: ')
n1 =float(input('Digite a primeira nota'))
n2 =float(input('Digite a segunda nota'))
media = (n1 + n2) / 2
print('Olá, aluno(a) {}, sua média é {:.1f}'.format(nome,media))
