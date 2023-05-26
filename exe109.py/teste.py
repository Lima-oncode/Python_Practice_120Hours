# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from moeda import moeda, metade, dobro, aumentar, diminuir

p = float(input('Digite o valor R$: '))
print(f'A metade de {moeda(p)} é {metade(p, formatado=True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, formatado=True)}')
print(f'Aumentando 10% de {moeda(p)} fica {aumentar(p, 10, formatado=False)}')
print(f'Diminuindo 10% de {moeda(p)} fica {diminuir(p, 10, formatado=False)}')

# Resolução do professor

from moeda import metade2, dobro2, aumentar2, diminuir2, moeda2

print()
p = float(input('Digite o valor R$: '))
print(f'A metade de {moeda2(p)} é {metade2(p, formatado=False)}')
print(f'O dobro de {moeda2(p)} é {dobro2(p, formatado=False)}')
print(f'Aumentando 10% de {moeda2(p)} fica {aumentar2(p, 10, formatado=True)}')
print(f'Diminuindo 10% de {moeda2(p)} fica {diminuir2(p, 10, formatado=True)}')