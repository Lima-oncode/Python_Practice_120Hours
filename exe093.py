# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
# do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = {}
count_gol = 0

jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('N° de partidas: '))
for p in range(jogador['partidas']):
    partida = gols[f'partida nº {p+1}'] = int(input(f'Quantos gols na {p+1}º partida: '))
    count_gol += partida
jogador['tot_gols'] = count_gol

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas. Veja os gols por partida:')
for k, v in gols.items():
    print(f'{k} com {v} gols')
print(f'Totalizando {jogador["tot_gols"]} gols durante a temporada!')

# Resolução do professor

jog = dict()
# Quando temos mais de um valor, para uma chave podemos colocar numa lista e depois copiar [:] para o dict
partidas = list()

jog['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jog['gols'] = partidas[:]
jog['total'] = sum(partidas)

# Primeira forma:
print(jog)

# Segunda forma:
print('_' * 30)
for k, v in jog.items():
    print(f'O campo {k} tem o valor {v}')
    
# Terceira forma:
print(f'O jogador {jog["nome"]} jogou {len(jog["gols"])} partidas.')
for i, v in enumerate(jog["gols"]):
    print(f'     => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jog["total"]} gols')
    

    
    

