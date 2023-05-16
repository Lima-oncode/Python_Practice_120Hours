'''Um professor quer sortear um de seus 4 alunos para pagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.'''

from random import choice
a1 = input('Primeiro aluno')
a2 = input('Segundo aluno')
a3 = input('terceiro aluno')
a4 = input('Quarto aluno')
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print('O aluno sorteado foi {}'.format(escolhido))