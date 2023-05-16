# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes de aproveitamento de cada jogador.

# jogadores = []
# jogador = dict()
# partidas = list()

# while True:
#     jogador.clear()
#     jogador['nome'] = str(input('Nome do jogador: '))
#     ptds = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
#     partidas.clear()
#     for c in range(0, ptds):
#         partidas.append(int(input(f'Quantos gols na partida {c}? ')))
#     jogador['gols'] = partidas[:]
#     jogador['total'] = sum(partidas)
#     jogadores.append(jogador.copy())
#     while True:
#         resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
#         if resposta in 'SN':
#             break
#         print('Resposta incorreta! Digite apenas S ou N')
#     if resposta == 'N':
#         break

# print('_' * 50)
# print('Cod ', end='')
# for j in jogador.keys():
#     print(f'{j:<15}', end='')
# print()
# print('_' * 40)
# for k, v in enumerate(jogadores):
#     print(f'{k:>4} ', end='')
#     for info in v.values():
#         print(f'{str(info):<15}  ', end='')
#     print()
# print('_' * 50)

# Resolução do professor


jog = dict()
partidas = list()
time = list()

while True:
    jog.clear()
    jog['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jog['gols'] = partidas[:]
    jog['total'] = sum(partidas)
    time.append(jog.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('_' * 40)
print('cod ', end='')
for i in jog.keys():
    print(f'{i:<15}', end='')
print()    
print('_' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('_' * 40)

while True:
    busca = int(input('Mostrar os dados de qual jogador (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'--- DADOS DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
        print('_' * 40)
        