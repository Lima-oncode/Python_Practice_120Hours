'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.

O computador deverá escrever na tela se o usuário venceu ou perdeu'''

from random import choice
lista = [0,1,2,3,4,5]
computador_pensou = choice(lista)
escolha_usuario = int(input('Digite o número que o computador pensou: '))

if escolha_usuario == computador_pensou:
    print('Venceu!')
else:
    print('Perdeu!')
print('o número escolhido foi {}'.format(computador_pensou))

# Resolução professor

from random import randint
from time import sleep
computador = randint(0, 5)
print('=' * 50)
print('Vou pensar um número entre 0 e 5. Tente advinhar...')
print('=' * 50)
jogador = int(input('Em que número eu pensei: '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS, VOCÊ ACERTOU!')
else:
    print('GANHEI! eu pensei no número {} e não no número {}'.format(computador, jogador))



