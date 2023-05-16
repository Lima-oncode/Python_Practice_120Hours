# Listas
# Listas são mutáveis e Tuplas são imutáveis

lanche = ['hamburguer', 'suco', 'pizza', 'picole']
print(lanche)
lanche.append('cookie') # append para adicionar um objeto no fim da lista
print(lanche)
lanche.insert(0, 'cachorro quente') # insert para adicionar um objeto numa posição específica da lista
print(lanche)
del lanche[3] # del para deletar a posicao na lista
print(lanche)
lanche.pop(3) # pop para deletar uma posicao na lista (pop é um metodo portanto a posicao da lista deve 
# estar em tupla)
print(lanche)
lanche.remove('hamburguer') # remove para deletar um objeto apos passa-lo como string no metodo
print(lanche)
lanche.pop() # deleta a ultima posicao quando não é passado a posicao dentro do metodo pop
print(lanche)
if 'suco' in lanche:
    lanche.remove('suco')
    print(lanche)

valores = list(range(4,11))
print(valores)
valores = [8,2,5,4,9,3,0]
print(valores)
valores.sort() # O metodo sort coloca a lista em ordem
print(valores)
valores.sort(reverse = True) # O parametros reverse como verdadeiro ordena os objetos ao inverso
print(valores)

num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort()
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.insert(0, 10)
print(num)
num.pop(0)
print(num)
num.append(2)
print(num)
num.remove(2)
print(num)
if 1 in num:
    num.remove(1)
else:
    print('Não achei o número em questão')
print(num)
print(f'Esta lista tem {len(num)} elementos')

# Para criar uma lista vazia

valores = []
# valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'\n  na posicao {c}... eu achei {v}. ')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

# Cada vez que referenciamos uma variavel a outra em lista elas criam um vinculo onde tudo que muda em B altera
# em A também

a = [2,3,4,7]
b = a
b[2] = 6
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Para apenas criar uma cópia invés do vínculo use b = a[:] :

a = [2,3,4,7]
b = a[:]
b[2] = 6
print(f'Lista A: {a}')
print(f'Lista B: {b}')

