# Tuplas

# Existem 3 tipos de variáveis compostas as tuplas as listas e os dicionários   

''' Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis 
compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves 
individuais '''

# toda variável simples é uma espaço na memória por exemplo 'lanche = hamburguer', neste caso tereremos a
# string hamburguer dentro do espaco da memória. Se logo depois definissemos 'lanche = suco', a string suco
# ficaria no lugar do hamburguer na memoria
# Caso quisessemos armazenar mais de um objeto na mesma variavel podemos utilizar as tuplas para isso

#Variável simples = 'lanche = hamburguer'
#Variável composta = 'lanche = (hamburguer, suco, pizza, pudim)

# Os elementos das tuplas são identificados por índices, o índice 0 da variável composta definida logo acima
# 'print(lanche[0])' seria o hamburguer 
# 'print(lanche[0:2])' Neste caso ele mostraria o hamburguer e o suco
# 'print(lanche[1:]) Neste caso ele mostraria o suco, a pizza e o pudim
# 'print(lanche[-1]) Neste caso ele apresentaria o último elemento 'pudim'
# len(lanche) Neste caso seria 4
# for c in lanche: Neste caso ele (c) vai pegar a primeira comida (hamburguer) e depois vai percorrer todos os
# lanches na repetição

''' As tuplas são IMUTÁVEIS. Caso quiséssemos trocar o pudim por outro alimento, precisariamos mudar a tupla e 
executar o programa novamente '''

lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim', 'batata-frita')
print(sorted(lanche))
print(lanche)
print(len(lanche))
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2])
print(lanche[-2:])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
print('Comi pra caramba')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')


# somando duas tuplas ela faz a junção das duas

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
# Quantas vezes aparece 5 na tupla
print(c.count(5))
print(c.index(8))
print(c.index(5))
print(c.index(5, 1))
pessoa = ('gustavo', 39, 'M', 99.88)
print(pessoa)
# O del apaga a variavel da memoria 
del(pessoa)



