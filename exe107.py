# Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from exe107moeda import metade, dobro, aumentar, diminuir

p = float(input('Digite o valor R$: '))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10% de {p} fica {aumentar(p, 10)}')
print(f'Diminuindo 10% de {p} fica {diminuir(p, 10)}')