# Neste primeiro exemplo deixa claro que todo comando que está colado a esquerda do código deve ser executado
# No caso, independente da condição, o comando print('Bom dia {}!'.format(nome)) será executado

'''nome = str(input('Digite o seu nome: '))
if nome == 'Lucas':
    print('Que nome panaca você tem!')
else: 
    print('Seu nome é tão normal')
print('Bom dia {}!'.format(nome))'''

# Exemplo 2

'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 7:
    print('Você foi aprovado!')
else: 
    print('Você foi reprovado...')
print('A sua média foi {:.1f}'.format(m))'''

# Exemplo 3 (Condição composta)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print('Parabéns!' if m >=7 else 'Estude +')
print('A sua média foi {:.1f}'.format(m))

