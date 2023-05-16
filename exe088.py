# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
# lista composta

# Gostei mais de minha solução para essa tarefa

from random import randint
from time import sleep
main = []
list_aux = []
qtd_jogos = int(input('Digite quantos jogos você quer que eu sorteie: '))
for j in range(0, qtd_jogos):
    for x in range(0,6):
        num = randint(1,60)
        if num not in list_aux:
            list_aux.append(num)
    main.append(list_aux[:])
    print(f'{j+1}º jogo {list_aux}')
    sleep(0.5)
    list_aux.clear()
print('__________ Boa Sorte __________!')

# Resolução do professor

from random import randint
from time import sleep
lista = []
jogos = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear
    tot += 1
    
for i, l in enumerate(jogos):
    print(f' jogo{i+1}: {l}')
    sleep(1)    
print('-=' * 5, 'BOA SORTE', '-=' * 5)
    
        