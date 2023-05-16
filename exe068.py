# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-'*6)
print('PAR OU ÍMPAR') 
print('=-'*6)

vitoria = 0
while True:
    valor = int(input('Diga um valor: '))
    par_impar = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    pc = randint(0, 10)
    soma = valor + pc
    while par_impar not in 'PI':
        par_impar = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    if par_impar == 'P':
        if soma % 2 == 0:
            P_or_I = 'DEU PAR'
            print('Você VENCEU!')
            vitoria += 1
        else:
            P_or_I = 'DEU ÍMPAR'
            print('Você PERDEU!')
            print(f'Você jogou {valor} e o computador {pc}. Total de {soma} {P_or_I}')
            break
    if par_impar == 'I':
        if soma % 2 != 0:
            P_or_I = 'DEU ÍMPAR'
            print('Você VENCEU!')
            vitoria += 1
        else:
            P_or_I = 'DEU PAR'
            print('Você PERDEU!')
            print(f'Você jogou {valor} e o computador {pc}. Total de {soma} {P_or_I}')
            break
    print(f'Você jogou {valor} e o computador {pc}. Total de {soma} {P_or_I}')
print(f'GAME OVER! Você venceu {vitoria} vez(ez)')

# Resolução do professor

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v +=1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')

