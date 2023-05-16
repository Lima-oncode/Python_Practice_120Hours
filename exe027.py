'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o ultimo nome separadamente.
EX:ANA MARIA DE SOUZA
PRIMEIRO: ANA
ULTIMO: SOUZA'''

nome = str(input('Digite o seu nome completo: ').strip())
name = nome.split()
ultimo = name[len(name)-1]
print('O primeiro nome é {}'.format(name[0]))
print('Seu ultimo nome é {}'.format(ultimo))

