# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

print('''======= JOKENPÔ ========
Vença a máquina neste clássico!

[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

pedra = 1
papel = 2
tesoura = 3
opcoes = [1,2,3]
cpu = choice(opcoes)
user = int(input('Selecione sua opção: '))

if user == 1:
    if cpu == 1:
        print('Você escolheu PEDRA e a CPU escolheu PEDRA portanto vocês EMPATARAM!')
    elif cpu == 2:
        print('Você escolheu PEDRA e a CPU escolheu PAPEL portanto você PERDEU!')
    elif tesoura == 3:
        print('Você escolheu PEDRA e a CPU escolheu TESOURA portanto você VENCEU!')

if user == 2:
    if cpu == 1:
        print('Você escolheu PAPEL e a CPU escolheu PEDRA portanto você VENCEU!')
    elif cpu == 2:
        print('Você escolheu PAPEL e a CPU escolheu PAPEL portanto vocês EMPATARAM!')
    elif cpu == 3:
        print('Você escolheu PAPEL e a CPU escolheu TESOURA portanto você PERDEU!')

if user == 3:
    if cpu == 1:
        print('Você escolheu TESOURA e a CPU escolheu PEDRA portanto você PERDEU!')
    elif cpu == 2:
        print('Você escolheu TESOURA e a CPU escolheu PAPEL portanto você VENCEU!')
    elif cpu == 3:
        print('Você escolheu TESOURA e a CPU escolheu TESOURA portanto você EMPATARAM!')

# Resolução do professor

from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0:
    if jogador  == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
