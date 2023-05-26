# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from moeda import resumo

p = float(input('Digite o valor R$: '))
resumo(p)

# Resolução do professor

from moeda import resumo2

print()
p = float(input('Digite o valor R$: '))
resumo2(p)