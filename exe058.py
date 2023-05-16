# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
# foram necessários para vencer

from random import randint
from time import sleep

computador = randint(0,10)
tentativas = 0
jogador = 0

while jogador != computador:
    jogador = int(input('Qual número a CPU pensou??? '))
    print('Verificando...')
    sleep(1)
    tentativas += 1
    if jogador != computador:
        print('Errado! não pensei nesse número... tente novamente!')
print('Parabéns! você deu {} palpites até a vitória'.format(tentativas))

# Resolução do professor

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez!')
        if jogador > computador:
            print('Menos... tente mais uma vez!')
print('Acertou com {} tentativas!'.format(palpites))

