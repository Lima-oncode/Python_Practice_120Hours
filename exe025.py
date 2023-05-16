'''Crie um programa que leia o nome de uma pessoa e retorna se ela tem SILVA no nome'''

# Meu formato de resolução 

nome = str(input('Digite o nome de uma pessoa: ').upper())
verifica_nome = ('SILVA' in nome)

if verifica_nome is True:
    print('O nome digitado tem SILVA')
else:
    print('O nome digitado não tem SILVA')

# Formato de resolução do professor

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))