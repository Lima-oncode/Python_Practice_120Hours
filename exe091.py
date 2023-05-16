# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo_do_dado = {'jogador_1':'', 'jogador_2':'', 'jogador_3':'', 'jogador_4':''}

for j in jogo_do_dado:
    lance = jogo_do_dado[j] = randint(1, 6)

for k, v in jogo_do_dado.items():
    print(f'{k} pontuou: {v}')
    sleep(0.4)
 
# É criado um dict 'ranking' para pegar os valores do primeiro dicionario 'jogo_do_dado'
# a função sorted tem o parametro 'key =' e para isso usamos a classe 'itemgetter' do módulo 'operator' 
# itemgetter deve pegar o objeto(1) do dicionário sendo este o valor. O objeto (0) é a chave. 
ranking = {}
ranking = sorted(jogo_do_dado.items(), key = itemgetter(1), reverse=True)
print(ranking)
print(f'O vencedor desta rodada foi {ranking[0]}')

# Resolução do professor

jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}

print('____ Valores Sorteados ____')

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = {}
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('____ Ranking ____')
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)