# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# Apenas os 5 primeiros colocados.
# Os últimos 4 colocados da tabela.
# uma lista com os times em ordem alfabética.
# Clube na primeira colocação com campeonato
# A posição do Juventude na tabela

tabela = ('PALMEIRAS', 'INTERNACIONAL', 'FLUMINENSE', 'CORINTHIANS', 'FLAMENGO', 'ATHLETICO PARANAENSE', 'ATLETICO MINEIRO', 'FORTALEZA', 'SAO PAULO', 'AMERICA', 'BOTAFOGO', 'SANTOS', 'GOIAS', 'BRAGANTINO', 'CORITIBA', 'CUIABA', 'CEARA', 'ATLETICO GO', 'AVAI', 'JUVENTUDE')
espaco = '=-' * 60

print(f'Os 5 primeiros colocados da tabela foram {tabela[:5]}')
print(espaco)
print(f'Os 4 últimos colocados da tabela foram {tabela[-4:]}')
print(espaco)
print('CAMPEONATO BRASILEIRO 2022')
print(sorted(tabela))
print(espaco)
print(f'O líder do campeonato é o {tabela[0]}')
print('O Juventude está na {}° posição'.format(tabela.index("JUVENTUDE")+1))

# Resolução do professor

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitoria', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')





