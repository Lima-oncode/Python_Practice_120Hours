# Adapte o código do desafio 107, criando uma função adicional chamda moeda() que consiga mostrar os valores como um valor monetário formatado.

from moeda import metade, dobro, aumentar, diminuir, moeda



p = float(input('Digite o valor R$: '))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10% de {moeda(p)} fica {moeda(aumentar(p, 10))}')
print(f'Diminuindo 10% de {moeda(p)} fica {moeda(diminuir(p, 10))}')

# Resolução do professor

from moeda import metade2, dobro2, aumentar2, diminuir2, moeda2

print()
p = float(input('Digite o valor R$: '))
print(f'A metade de {moeda2(p)} é {moeda2(metade2(p))}')
print(f'O dobro de {moeda2(p)} é {moeda2(dobro2(p))}')
print(f'Aumentando 10% de {moeda2(p)} fica {moeda2(aumentar2(p, 10))}')
print(f'Diminuindo 10% de {moeda2(p)} fica {moeda2(diminuir2(p, 10))}')
